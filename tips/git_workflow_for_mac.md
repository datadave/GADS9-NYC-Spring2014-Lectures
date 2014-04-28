# Git Workflow for Mac

[xkcd git commit fun](http://xkcd.com/1296/)

This workflow assumes you are starting in your **home directory on OS X** and that you will only use the command line (no GitHub GUI here!).

This means /Users/*username*
	
	mymac:~ joe$ pwd 
	/Users/joe
	mymac:~ joe$
	
## Lectures Repository

You do not need to fork the [Lectures](https://github.com/datadave/GADS9-NYC-Spring2014-Lectures) repository because **you will never be pushing to the Lectures repository**.

### Clone the datadave Lectures Repository

	git clone https://github.com/datadave/GADS9-NYC-Spring2014-Lectures.git

**Example**:

	mymac:~ joe$ git clone https://github.com/datadave/GADS9-NYC-Spring2014-	Lectures.git
	Cloning into 'GADS9-NYC-Spring2014-Lectures'...
	remote: Counting objects: 824, done.
	remote: Compressing objects: 100% (432/432), done.
	remote: Total 824 (delta 360), reused 716 (delta 298)
	Receiving objects: 100% (824/824), 19.42 MiB | 1.48 MiB/s, done.
	Resolving deltas: 100% (360/360), done.
	mymac:~ joe$
	
### Update For Every Class

	cd GADS9-NYC-Spring2014-Lectures
	git pull origin master

**Example:**

	mymac:~ joe$ cd GADS9-NYC-Spring2014-Lectures/
	mymac:GADS9-NYC-Spring2014-Lectures joe$ git pull origin master
	From https://github.com/datadave/GADS9-NYC-Spring2014-Lectures
	 * branch            master     -> FETCH_HEAD
	Already up-to-date.
	mymac:GADS9-NYC-Spring2014-Lectures joe$
	
### Change Directory to the Current Lesson

	cd lessons
	cd lesson0x_abc
	
**Example:**
	
	mymac:GADS9-NYC-Spring2014-Lectures joe$ cd lessons/
	mymac:lessons joe$ ls
	README.md                               lesson02_data_collection_and_extraction 	lesson03b_pandas
	lesson01_intro_to_data_science          lesson03a_numpy                         	lesson04_matplotlib_and_EDA
	mymac:lessons joe$ cd lesson04_matplotlib_and_EDA/
	mymac:lesson04_matplotlib_and_EDA joe$ ls
	DataVizLecture_v2.pdf                 Visualization_Instructional_Set.ipynb 	data                                  readme.md
	mymac:lesson04_matplotlib_and_EDA joe$
	
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

	mymac:~ joe$ git clone https://github.com/jrcarli/GADS9-NYC-Spring2014-Students.git
	Cloning into 'GADS9-NYC-Spring2014-Students'...
	remote: Counting objects: 784, done.
	remote: Compressing objects: 100% (392/392), done.
	remote: Total 784 (delta 269), reused 784 (delta 269)
	Receiving objects: 100% (784/784), 13.27 MiB | 243 KiB/s, done.
	Resolving deltas: 100% (269/269), done.
	mymac:~ joe$ 

### Add an Upstream Link to datadave
This step is critical to getting the latest *lab_submissions/lab0x* directories.

	cd GADS9-NYC-Spring2014-Students	
	git remote -v
	git remote add upstream https://github.com/datadave/GADS9-NYC-Spring2014-Students.git
	git remote -v	
Note: *git remote -v* will show you where git knows to look for different items. You will notice that git is unaware of *upstream* before running the *git remote add upstream ...* command.	

**Example:**
	
	mymac:~ joe$ cd GADS9-NYC-Spring2014-Students
	mymac:GADS9-NYC-Spring2014-Students joe$ git remote -v
	origin	https://github.com/jrcarli/GADS9-NYC-Spring2014-Students.git (fetch)
	origin	https://github.com/jrcarli/GADS9-NYC-Spring2014-Students.git (push)
	mymac:GADS9-NYC-Spring2014-Students joe$ git remote add upstream https://github.com/datadave/GADS9-NYC-Spring2014-Students.git
	mymac:GADS9-NYC-Spring2014-Students joe$ git remote -v
	origin	https://github.com/jrcarli/GADS9-NYC-Spring2014-Students.git (fetch)
	origin	https://github.com/jrcarli/GADS9-NYC-Spring2014-Students.git (push)
	upstream	https://github.com/datadave/GADS9-NYC-Spring2014-Students.git (fetch)
	upstream	https://github.com/datadave/GADS9-NYC-Spring2014-Students.git (push)
	mymac:GADS9-NYC-Spring2014-Students joe$

### Merge the Official datadave Updates
We are going to fetch datadave (*upstream*), which puts the updates in a local branch called *upstream/master*. We'll make sure we are in our master branch, then perform the merge.

	git fetch upstream
	git checkout master
	git merge upstream/master
	
**Example:**

	mymac:GADS9-NYC-Spring2014-Students joe$ git fetch upstream
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
	mymac:GADS9-NYC-Spring2014-Students joe$ git checkout master
	Already on 'master'
	mymac:GADS9-NYC-Spring2014-Students joe$ git merge upstream/master
	Updating 0804e21..358897f
	...
	mymac:GADS9-NYC-Spring2014-Students joe$

### Do Your Work!
Always remember to create an *flastname* directory beneath *lab_submissions/lab0x*, where you will save your work!

	cd lab_submissions
	cd lab0x_...
	mkdir flastname
	cd flastname
	[do work here]
	
**Example** (assuming the work we want to do is in lab02):

	mymac:GADS9-NYC-Spring2014-Students joe$ cd lab_submissions/
	mymac:lab_submissions joe$ cd lab02
	mymac:lab02 joe$ mkdir jrcarli
	mymac:lab02 joe$ cd jrcarli
	mymac:jrcarli joe$ vi lab02.py
	mymac:jrcarli joe$ vi mydata.csv
	mymac:jrcarli joe$
	
### Add Your Work
We need to tell git that we want to begin tracking the work you've just done.

	git add fileA fileB ... fileN
	-- Or --
	git add .
	
**Example** (assuming two files are to be added, *lab02.py* and *mydata.csv*):

	mymac:jrcarli joe$ git add lab02.py mydata.csv 
	mymac:jrcarli joe$

### Commit Your Work
Pro tip: Leaving off *-m &lt;msg&gt;* will bring up your default text editor. The comments in the editor will show you which files are being added, removed, or modified. *-m &lt;msg&gt;* is a convenience feature.

	git commit -m "Your commit message here"
	
**Example:**

	mymac:jrcarli joe$ git commit -m "Committing Mac lab02 GitHub workflow sample files"
	[master 58206fc] Committing Mac lab02 GitHub workflow sample files
	 2 files changed, 11 insertions(+)
	 create mode 100644 lab_submissions/lab02/jrcarli/lab02.py
	 create mode 100644 lab_submissions/lab02/jrcarli/mydata.csv
	mymac:jrcarli joe$
	
### Push Your Work
Remember *git remote -v* and how it showed that *origin* referred to your personal fork of the Students repository? That's where you want to push your changes changes. *master* refers to the branch name you are pushing--since you didn't change branches, your changes should be in your (local) master branch.

	git push origin master
	
**Example:**

	mymac:jrcarli joe$ git push origin master
	Username for 'https://github.com': jrcarli
	Password for 'https://jrcarli@github.com': 
	To https://github.com/jrcarli/GADS9-NYC-Spring2014-Students.git
	   0804e21..58206fc  master -> master
	mymac:jrcarli joe$

### Issue a Pull Request From Your Repository

Find and click the ```Pull Request``` link above your repository's file listing. Click the green ```Create Pull Request``` on the resulting page, add a title and comments as appropriate, and finally click ```Send pull request```.
