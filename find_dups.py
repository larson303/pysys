import os
import shutil
import argparse

def find_duplicate_files(directory, file_types):
    file_attributes = {}
    duplicate_files = []

    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if not file.lower().endswith(file_types):
                    continue

                file_path = os.path.join(root, file)
                try:
                    file_size = os.path.getsize(file_path)
                except OSError as e:
                    print(f"Error accessing {file_path}: {e}")
                    continue

                file_key = (os.path.basename(file), file_size)
                if file_key in file_attributes:
                    duplicate_files.append((file_path, file_attributes[file_key]))
                else:
                    file_attributes[file_key] = file_path
    except Exception as e:
        print(f"Error walking through {directory}: {e}")

    return duplicate_files

def move_base_directory_duplicates(duplicate_files, duplicates_folder, base_directory):
    """
    Moves duplicates found in the base directory to a specified duplicates folder.
    """
    if not os.path.exists(duplicates_folder):
        os.makedirs(duplicates_folder)

    for original, duplicate in duplicate_files:
        # Check if the duplicate is in the base directory
        duplicate_file_path = None
        if os.path.dirname(duplicate) == base_directory:
            duplicate_file_path = duplicate
        elif os.path.dirname(original) == base_directory:
            duplicate_file_path = original

        if duplicate_file_path:
            # Generate the new path for the duplicate in the duplicates folder
            file_name = os.path.basename(duplicate_file_path)
            new_file_path = os.path.join(duplicates_folder, file_name)
            
            # Move the duplicate file
            try:
                shutil.move(duplicate_file_path, new_file_path)
                print(f"Moved duplicate from base directory: {duplicate_file_path} to {new_file_path}")
            except OSError as e:
                print(f"Error moving duplicate from base directory {duplicate_file_path} to {new_file_path}: {e}")

def generate_html_file(duplicate_files, html_file):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Duplicate Files</title>
    </head>
    <body>
        <h1>Duplicate Files</h1>
        <form action="process_duplicates.php" method="post">
    """

    for i, duplicate in enumerate(duplicate_files):
        html_content += f"""
        <h3>Duplicate Set {i+1}</h3>
        <p>
            <input type="radio" name="duplicate_set_{i}" value="keep_original"> Keep Original: {duplicate[1]}<br>
            <input type="radio" name="duplicate_set_{i}" value="keep_duplicate"> Keep Duplicate: {duplicate[0]}<br>
            Original Location: {os.path.dirname(duplicate[1])}<br>
            Duplicate Location: {os.path.dirname(duplicate[0])}
        </p>
        """

    html_content += """
        <input type="submit" value="Remove Selected Duplicates">
        </form>
    </body>
    </html>
    """

    try:
        with open(html_file, 'w', encoding='utf-8') as file:
            file.write(html_content)
    except OSError as e:
        print(f"Error writing to {html_file}: {e}")

# Main script execution
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scan a specified directory for duplicate files and move duplicates from the base directory to a designated folder.')
    parser.add_argument('directory', type=str, help='The full path of the directory to scan for duplicates. Example: /path/to/directory')
    parser.add_argument('-t', '--types', nargs='+', default=['.jpg', '.mp4'],
                        help='Optional. File types to check for duplicates, specified with a dot. Default is .jpg and .mp4. Example: -t .jpg .png .gif')

    args = parser.parse_args()

    duplicates_folder = os.path.join(args.directory, 'duplicates')
    html_file = 'duplicates.html'

    duplicate_files = find_duplicate_files(args.directory, tuple(args.types))
    move_base_directory_duplicates(duplicate_files, duplicates_folder, args.directory)
    generate_html_file(duplicate_files, html_file)

    print(f"Duplicate files found: {len(duplicate_files)}")
    print(f"Report on potential duplicates generated in {duplicates_folder}")
    print(f"HTML file generated: {html_file}")
