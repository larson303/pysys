import os
import sys

def is_excluded(root, exclude_dirs, base_path):
    """Check if the current directory or any of its parents is in the exclude list."""
    root_abs = os.path.abspath(root)
    for exclude_dir in exclude_dirs:
        exclude_abs = os.path.abspath(os.path.join(base_path, exclude_dir))
        if root_abs.startswith(exclude_abs):
            return True
    return False

def display_tree(startpath, show_files=False, exclude_dirs=None):
    base_path = os.path.abspath(startpath)
    exclude_dirs = exclude_dirs if exclude_dirs else []

    for root, dirs, files in os.walk(startpath, topdown=True):
        if is_excluded(root, exclude_dirs, base_path):
            dirs[:] = []  # Prevent descending into excluded dirs
            continue

        level = root.replace(base_path, '').count(os.sep)
        indent = '|   ' * level + '|-- '
        subindent = '|   ' * (level + 1) + '|-- '
        print('{}{}'.format(indent if level > 0 else '', os.path.basename(root) if level > 0 else '.'))
        
        if show_files:
            for f in files:
                print('{}{}'.format(subindent, f))

def main():
    args = sys.argv[1:]
    start_path = "."
    show_files = False
    exclude_dirs = []

    i = 0
    while i < len(args):
        if args[i] == "-f":
            show_files = True
        elif args[i] == "-i" and i + 1 < len(args):
            exclude_dirs.append(args[i + 1])
            i += 1  # Skip next argument since it's part of -i
        elif os.path.isdir(args[i]):
            start_path = args[i]
        i += 1

    display_tree(start_path, show_files, exclude_dirs)

if __name__ == "__main__":
    main()
