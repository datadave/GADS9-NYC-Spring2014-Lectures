# Common Git Commands

### Clone a (GitHub) repository
    git clone https://github.com/username/repository.git
* For class, you will generally clone your forked version of a repository

### Pull the latest repository updates
    git pull origin master
    
* Note: *master* is a branch name and can be replaced, though you will almost always pull from *master* in class

### Create a branch
    git checkout -b <branch name>
    
### Add files to a branch

#### Add all new/changed files
    git add .

#### Add a specific file
    git add <filename>
    
### Remove files from a branch
    git rm <filename>
* Note: this will also delete the local copy of &lt;*filename*&gt; so use with caution!

### Committing changes
    git commit
* This will open your default text editor, where you should enter a commit message. Saving the file will complete the local commit (you still need to push it to the repository on GitHub).
* This will show, in your text editor, what changes will be made.

#### Pro tip for committing changes
    git commit -m <commit message>

### Push a branch
    git push origin <branch name>
     
