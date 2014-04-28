# Git Workflow for Linux

[xkcd git commit fun](http://xkcd.com/1296/)

This workflow assumes you are starting in your **home directory in Linux** and that you will only use the command line for git interaction.

This means /home/*username*

	joe@ubuntu$ pwd
	/home/joe
	joe@ubuntu$
	
## Lectures Repository

You do not need to fork the [Lectures](https://github.com/datadave/GADS9-NYC-Spring2014-Lectures) repository because **you will never be pushing to the Lectures repository**.

### Clone the datadave Lectures Repository

	git clone https://github.com/datadave/GADS9-NYC-Spring2014-Lectures.git
	
**Example:**

	joe@ubuntu:~$ git clone https://github.com/datadave/GADS9-NYC-Spring2014-	Lectures.git
	Cloning into 'GADS9-NYC-Spring2014-Lectures'...
	remote: Counting objects: 824, done.
	remote: Compressing objects: 100% (432/432), done.
	remote: Total 824 (delta 360), reused 716 (delta 298)
	Receiving objects: 100% (824/824), 19.42 MiB | 659 KiB/s, done.
	Resolving deltas: 100% (360/360), done.
	Checking out files: 100% (72/72), done.
	joe@ubuntu:~$

### Update For Every Class

	cd GADS9-NYC-Spring2014-Lectures
	git pull origin master

**Example:**

	joe@ubuntu:~$ cd GADS9-NYC-Spring2014-Lectures/
	joe@ubuntu:~/GADS9-NYC-Spring2014-Lectures$ git pull origin master
	From https://github.com/datadave/GADS9-NYC-Spring2014-Lectures
	 * branch            master     -> FETCH_HEAD
	Already up-to-date.
	joe@ubuntu:~/GADS9-NYC-Spring2014-Lectures$
	
### Change Directory to the Current Lesson

	cd lessons
	cd lesson0x_abc
	
**Example:**
	
	joe@ubuntu:~/GADS9-NYC-Spring2014-Lectures$ cd lessons/
	joe@ubuntu:~/GADS9-NYC-Spring2014-Lectures/lessons$ ls
	lesson01_intro_to_data_science           lesson03a_numpy   	lesson04_matplotlib_and_EDA
	lesson02_data_collection_and_extraction  lesson03b_pandas  README.md
	joe@ubuntu:~/GADS9-NYC-Spring2014-Lectures/lessons$ cd lesson04_matplotlib_and_EDA/
	joe@ubuntu:~/GADS9-NYC-Spring2014-Lectures/lessons/lesson04_matplotlib_and_EDA$ ls
	data  DataVizLecture_v2.pdf  readme.md  Visualization_Instructional_Set.ipynb
	joe@ubuntu:~/GADS9-NYC-Spring2014-Lectures/lessons/lesson04_matplotlib_and_EDA$

### Do the Lesson

But don't push any changes.

	ipython notebook
	
## Students Repository

You will fork the [Students](https://github.com/datadave/GADS9-NYC-Spring2014-Students) repository so that you have access rights to push changes. This is a standard model used by many git-controlled projects.

### Fork the datadave Students Repository

Log into [GitHub](https://github.com). Browse to the [datadave Students repository](https://github.com/datadave/GADS9-NYC-Spring2014-Students). Click the ``Fork`` button near the top right of the page.

### Clone Your Forked Repository
Replace *username* with your GitHub username

	git clone https://github.com/username/GADS9-NYC-Spring2014-Students.git

**Example:**
	
	joe@ubuntu:~$ git clone https://github.com/jrcarli/GADS9-NYC-Spring2014-Students.git
	Cloning into 'GADS9-NYC-Spring2014-Students'...
	remote: Counting objects: 784, done.
	remote: Compressing objects: 100% (392/392), done.
	remote: Total 784 (delta 269), reused 784 (delta 269)
	Receiving objects: 100% (784/784), 13.27 MiB | 236 KiB/s, done.
	Resolving deltas: 100% (269/269), done.
	joe@ubuntu:~$		
	
### Add an Upstream Link to datadave
This step is critical to getting the latest *lab_submissions/lab0x* directories.

	cd GADS9-NYC-Spring2014-Students	
	git remote -v
	git remote add upstream https://github.com/datadave/GADS9-NYC-Spring2014-Students.git
	git remote -v	
Note: *git remote -v* will show you where git knows to look for different items. You will notice that git is unaware of *upstream* before running the *git remote add upstream ...* command.	

**Example:**

	joe@ubuntu:~$ cd GADS9-NYC-Spring2014-Students
	joe@ubuntu:~/GADS9-NYC-Spring2014-Students$ git remote -v
	origin	https://github.com/jrcarli/GADS9-NYC-Spring2014-Students.git (fetch)
	origin	https://github.com/jrcarli/GADS9-NYC-Spring2014-Students.git (push)
	joe@ubuntu:~/GADS9-NYC-Spring2014-Students$ git remote add upstream https://github.com/datadave/GADS9-NYC-Spring2014-Students.git
	joe@ubuntu:~/GADS9-NYC-Spring2014-Students$ git remote -v
	origin	https://github.com/jrcarli/GADS9-NYC-Spring2014-Students.git (fetch)
	origin	https://github.com/jrcarli/GADS9-NYC-Spring2014-Students.git (push)
	upstream	https://github.com/datadave/GADS9-NYC-Spring2014-Students.git (fetch)
	upstream	https://github.com/datadave/GADS9-NYC-Spring2014-Students.git (push)
	joe@ubuntu:~/GADS9-NYC-Spring2014-Students$
	
### Merge the Official datadave Updates
We are going to fetch datadave (*upstream*), which puts the updates in a local branch called *upstream/master*. We'll make sure we are in our master branch, then perform the merge.

	git fetch upstream
	git checkout master
	git merge upstream/master

**Example:**

	joe@ubuntu:~/GADS9-NYC-Spring2014-Students$ git fetch upstream
	remote: Counting objects: 187, done.
	remote: Compressing objects: 100% (148/148), done.
	remote: Total 187 (delta 67), reused 77 (delta 22)
	Receiving objects: 100% (187/187), 60.51 KiB, done.
	Resolving deltas: 100% (67/67), done.
	From https://github.com/datadave/GADS9-NYC-Spring2014-Students
	 * [new branch]      dir_struct_for_repo -> upstream/dir_struct_for_repo
	 * [new branch]      lesson03   -> upstream/lesson03
	 * [new branch]      lesson1    -> upstream/lesson1
	 * [new branch]      lesson2    -> upstream/lesson2
	 * [new branch]      master     -> upstream/master
	 * [new branch]      python_and_data_lesson -> upstream/python_and_data_lesson
	joe@ubuntu:~/GADS9-NYC-Spring2014-Students$ git checkout master
	Already on 'master'
	joe@ubuntu:~/GADS9-NYC-Spring2014-Students$ git merge upstream/master
	Updating 0804e21..358897f
	...
	joe@ubuntu:~/GADS9-NYC-Spring2014-Students$
	
### Do Your Work!
Always remember to create an *flastname* directory beneath *lab_submissions/lab0x*, where you will save your work!

	cd lab_submissions
	cd lab0x_...
	mkdir flastname
	cd flastname
	[do work here]

**Example** (assuming the work we want to do is in lab02):

	joe@ubuntu:~/GADS9-NYC-Spring2014-Students$ cd lab_submissions/
	joe@ubuntu:~/GADS9-NYC-Spring2014-Students/lab_submissions$ cd lab02
	joe@ubuntu:~/GADS9-NYC-Spring2014-Students/lab_submissions/lab02$ mkdir jrcarli
	joe@ubuntu:~/GADS9-NYC-Spring2014-Students/lab_submissions/lab02$ cd jrcarli
	joe@ubuntu:~/GADS9-NYC-Spring2014-Students/lab_submissions/lab02/jrcarli$ vi lab02_linux.py 
	joe@ubuntu:~/GADS9-NYC-Spring2014-Students/lab_submissions/lab02/jrcarli$ vi mydata_linux.csv
	joe@ubuntu:~/GADS9-NYC-Spring2014-Students/lab_submissions/lab02/jrcarli$
	
### Add Your Work
We need to tell git that we want to begin tracking the work you've just done.

	git add fileA fileB ... fileN
	-- Or --
	git add .

**Example** (assuming two files are to be added, *lab02_linux.py* and *mydata_linux.csv*):

	joe@ubuntu:~/GADS9-NYC-Spring2014-Students/lab_submissions/lab02/jrcarli$ git add lab02_linux.py mydata_linux.csv
	joe@ubuntu:~/GADS9-NYC-Spring2014-Students/lab_submissions/lab02/jrcarli$

### Commit Your Work
Pro tip: Leaving off *-m &lt;msg&gt;* will bring up your default text editor. The comments in the editor will show you which files are being added, removed, or modified. *-m &lt;msg&gt;* is a convenience feature.

	git commit -m "Your commit message here"

**Example:**
	
	joe@ubuntu:~/GADS9-NYC-Spring2014-Students/lab_submissions/lab02/jrcarli$ git commit -m "Committing lab02 files for GitHub linux workflow documentation"
	[master edc76d9] Committing lab02 files for GitHub linux workflow documentation
	 2 files changed, 12 insertions(+)
	 create mode 100644 lab_submissions/lab02/jrcarli/lab02_linux.py
	 create mode 100644 lab_submissions/lab02/jrcarli/mydata_linux.csv
	joe@ubuntu:~/GADS9-NYC-Spring2014-Students/lab_submissions/lab02/jrcarli$
	
### Push Your Work
Remember *git remote -v* and how it showed that *origin* referred to your personal fork of the Students repository? That's where you want to push your changes changes. *master* refers to the branch name you are pushing--since you didn't change branches, your changes should be in your (local) master branch.

	git push origin master

**Exmple:**

	joe@ubuntu:~/GADS9-NYC-Spring2014-Students/lab_submissions/lab02/jrcarli$ git push origin master
	Username for 'https://github.com': jrcarli
	Password for 'https://jrcarli@github.com': 
	Counting objects: 19, done.
	Compressing objects: 100% (11/11), done.
	Writing objects: 100% (12/12), 1.25 KiB, done.
	Total 12 (delta 4), reused 0 (delta 0)
	To https://github.com/jrcarli/GADS9-NYC-Spring2014-Students.git
	   58206fc..8c406f3  master -> master
	joe@ubuntu:~/GADS9-NYC-Spring2014-Students/lab_submissions/lab02/jrcarli$

### Issue a Pull Request From Your Repository

Find and click the ```Pull Request``` link above your repository's file listing. Click the green ```Create Pull Request``` on the resulting page, add a title and comments as appropriate, and finally click ```Send pull request```.