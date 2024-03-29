# Pysys Python System Utilities

As a long time BASH/SHELL user, I frequently would create shell scripts and add them to my repo of tools.
I early on grew weary of noticing that I *should* switch to Perl or Python (no mocking please) because
both tools allow the developer/system developer to use actual code and create a framework. One of my 
earliest code commits after my .bashrc was a script for logging.  As I moved from Operations to
Development (but was also the Dev Server Admin) I wanted to move to more mature solutions to problems, 
but time and deadlines seemed to make jumping in with the familiar tool easier.  

As time went on, most of my scripts weren't as necessary due to the corporate environment, package.json
that could house any node scripts for applications, and most of the work either done in the cloud rather
than on a dev Linux server or on a local MacOS.  

Now that I am spending more time developing on my own time and desires, I started to create my own tools
for managing my Windows systems, and thought other people may appreciate some of the utilities I am 
developing.  Maybe it's just my ADHD, but it doesn't seem uncommon for developers to have a 1-2TB HD
as well as a couple of external 2TB+ drives for back up.  For me, I copied files to my backups over
time - despite the fact I may have switched laptops or 're-organized` so ended up with duplicate files
along the way.  Dealing with multiple versions of folders with pictures and videos, I made my move (finally)
to switch to using Python for sys admin tasks - even if it is just for my local system.



# Utilities:

## pytree.py
### Usage
```sh
> pytree.py -i node_modules -i .git -i .next  -f
```

### Use-Case:  Getting a list of directories and files, while ignoring some directories.
- This tool is helpful for developers who are doing AI-assisted coding.  I ran into
instances early on where I figured out that the version of instructions they are trained on did not 
align with the version of code that I was using, making some of the answers inaccurate.  The ability
to pass the file structure to the AI in order to validate project structure was helpful, so I developed
a version of the Windows Tree utility that gives me the ability to ignore directories - which the native
version does not have.  (dos `tree /F`)

- NOTE: In case you aren't familiar with the `tree` command, it creates an ascii display of your file
  system from where you run it.  the `/F` option lists the files, so if you fail to put that flag on the
  end, you will only get the directories.

### Sample
```sh
> pytree.py -i node_modules -i .git -i .next  -f
.
|   |-- .eslintrc.json
|   |-- .gitignore
|   |-- next.config.js
|   |-- package-lock.json
|   |-- package.json
|   |-- postcss.config.js
|   |-- README.md
|   |-- tailwind.config.js
|   |-- yarn.lock
|   |-- components
|   |   |-- Modal.js
|   |   |-- Navbar.js
|   |   |-- ProfileCard.js
|   |   |-- WorkExperience.js
|   |-- pages
|   |   |-- about.js
|   |   |-- contact.js
|   |   |-- index.js
|   |   |-- services.js
|   |   |-- _app.js
|   |   |-- api
|   |   |   |-- contact.js
|   |   |   |-- hello.js
|   |-- public
|   |   |-- favicon.ico
|   |   |-- vercel.svg
|   |-- styles
|   |   |-- globals.scss
|   |   |-- Home.module.css
```

## find_dups.py
