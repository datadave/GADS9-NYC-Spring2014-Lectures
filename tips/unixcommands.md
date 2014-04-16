# Common Unix Commands

**Note**: Tab completion is your friend.

### Where am I?
    pwd

### What's in here?
    ls

### Navigation
    cd <directory>

#### Go home
    cd ~/

#### Go up one directory
    cd ..

#### Go up two directories
    cd ../../

### Create a directory
    mkdir <directory>

### Scroll through a file
    less <filename>
    
#### Show the top few lines of a file
    head <filename>
* This is a great way to show you the header of a .csv    
    
#### Show the bottom few lines of a file
    tail <filename>    
    
#### Count the number of lines in a file
    wc -l <filename>   

### Common file editors
    vi
    vim
    nano
    emacs
    gedit

### Delete a file
    rm <filename>

### Find a file (recursively)
    find . -type f -name "<name>"

#### Find all Python files (recursively)
    find . -type f -name "*.py"

### Getting help on a command
    man <command>       