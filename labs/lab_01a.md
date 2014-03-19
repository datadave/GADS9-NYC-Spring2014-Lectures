# Computer Setup and Data Handling
## Macs: installing `homebrew`

`Homebrew` is a mac installer for packages/libraries/etc that works alongside Apple's installers. We need it for git. Install oneliner:

    ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"

## Installing `git`

* Macs: `brew install git`
* Windows: Install git bash http://openhatch.org/missions/windows-setup/install-git-bash
* Linux: If you're on linux you should already know how to do this with your package manager. On Ubuntu you can use `apt-get install git`, otherwise find your <a href="http://git-scm.com/download/linux">distribution</a>

**Note:** If you have issues with `brew install` because of an XCode error, try using this Heroku Toolbelt installation that will include git, or choose an OS based installation from this guide: http://git-scm.com/book/en/Getting-Started-Installing-Git

Once you've setup git and github, clone the class repository. We're using it for lab assignments and project collection.

    cd ~/; git clone git@github.com:datadave/GADS9-NYC-Spring2014.git

## `python`

The easiest install is Anaconda's Python. <a href="https://store.continuum.io/cshop/anaconda/">Download and install here</a> for your computer.

**Note to Engineers:** If you prefer to not have anaconda's distribution as your primary python, comment out the `PATH` line for anaconda in `~/.bash_profile` and add an alias for anaconda's python, ipython and conda package handler:

    alias apython="/Users/edjoy/anaconda/bin/python"
    alias ipython="/Users/edjoy/anaconda/bin/ipython"
    alias conda="/Users/edjoy/anaconda/bin/conda"

For visualizations we'll primarily use matplotlib and yhat's version of ggplot for python:

    conda install -c https://conda.binstar.org/public ggplot

## Lab Submissions (1)

in `GADS9-NYC-Spring2014/lab_submissions/lab01`, make a directory with your first initial/full last name.

    DIR='flastname'; cd ~/GADS9-NYC-Spring2014/lab_submissions/lab01; mkdir $DIR; open $DIR

With a text editor, create and save a markdown file with the following content:

* Your name and job
* One liner about your coding and math background
* Any social web you use and don't mind sharing (twitter link, for example)
* A data blog post you read recently for sharing with the class

create a branch of the repository with a unique name, and then commit to that repo

    git checkout -b some_unique_name
    git add .
    git commit -m 'my first git commit!

Add a pull request. This is the actual submission of your work. You can do this on github by finding your branch and clicking "Create pull request." Developers, feel free to use some command line tool for this if you prefer it.

## Next Steps

We (Dave and Ed) will always recommend 4 or 5 readings or other support materials for every class, either to supplement the current material, prep for the next class, or covering previous material that students still have questions on.

**Reading and other Materials**

* <a href="http://www.quora.com/Data-Science/What-is-it-like-to-be-a-data-scientist">Quora: What is it like to be a data scientist?</a>
* <a href="http://www.youtube.com/watch?v=h9vQIPfe2uU"> Josh Wills: The Life of a Data Scientist</a>
* <a href="http://www.p-value.info/"> P-Value.info, Carl Anderson's blog (Director of Data at Warby Parker)</a>
* <a href="http://blog.okcupid.com/"> A look at OKCupid and their detailed work in trends</a>
* <a href="http://radar.oreilly.com/2011/09/building-data-science-teams.html">DJ Patil, Building Data Science Teams</a>
* <a href="http://benfry.com/phd/">Ben Fry's Dissertation: Computational Information Design </a>
