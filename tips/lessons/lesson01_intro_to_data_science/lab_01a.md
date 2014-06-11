# Computer Setup and Data Handling
## Macs: installing `homebrew`

`Homebrew` is a mac installer for packages/libraries/etc that works alongside Apple's installers. We need it for git. Install oneliner:

```sh
ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"
```

If you recieve an SSL certificate error:

```sh
ruby -e "$(curl --insecure -fsSL https://raw.github.com/mxcl/homebrew/go)"
```

## Installing `git`

* Macs: `brew install git`
* Windows: Install git bash http://openhatch.org/missions/windows-setup/install-git-bash
    * The default options will probably work well for you
* Linux: If you're on linux you should already know how to do this with your package manager. On Ubuntu you can use `apt-get install git`, otherwise find your <a href="http://git-scm.com/download/linux">distribution</a>

**Note:** If you have issues with `brew install` because of an XCode error, try using this Heroku Toolbelt installation that will include git, or choose an OS based installation from this guide: http://git-scm.com/book/en/Getting-Started-Installing-Git

Once you've setup git and github, clone your fork of the class repository. We'll be using the <a href="https://help.github.com/articles/using-pull-requests#fork--pull">Fork and Pull git model</a>. You will be pushing changes to your forked repository, and submitting pull requests to the class repository.

From the github help page:
> The Fork & Pull Model lets anyone fork an existing repository and push changes to their personal fork without requiring access be granted to the source repository. The changes must then be pulled into the source repository by the project maintainer.

```sh
cd ~/; git clone git@github.com:<your github username>/GADS9-NYC-Spring2014.git
```

For example:
```sh
cd ~/; git clone git@github.com:datadave/GADS9-NYC-Spring2014.git
```

## `python`

The easiest install is Anaconda's Python. <a href="https://store.continuum.io/cshop/anaconda/">Download and install here</a> for your computer.

**Note to Engineers:** If you prefer to not have anaconda's distribution as your primary python, comment out the `PATH` line for anaconda in `~/.bash_profile` and add an alias for anaconda's python, ipython and conda package handler:

```sh
alias apython="~/anaconda/bin/python"
alias ipython="~/anaconda/bin/ipython"
alias conda="~/anaconda/bin/conda"
```

For visualizations we'll primarily use matplotlib and yhat's version of ggplot for python:

```sh
conda install -c https://conda.binstar.org/public ggplot
```

Users experiencing ggplot package errors should try pip (this problem was observed on Ubuntu and Windows):

```sh
pip install ggplot
```

## Lab Submissions

in `GADS9-NYC-Spring2014/lab_submissions/lab01`, make a directory with your first initial/full last name.

```sh
DIR='flastname'; cd ~/GADS9-NYC-Spring2014/lab_submissions/lab01; mkdir $DIR; open $DIR
```

With a text or markdown editor, create and save a markdown file with the following content:

* Your name and what you do
* One liner about your coding and math background
* Any social web you use and don't mind sharing (twitter link, for example)
* A data blog post you read recently for sharing with the class

create a branch of the repository with a unique name, and then commit to that repo

```sh
git checkout -b my_name_class_1
git add .
git commit -m 'my first git commit!'
git push origin my_name_class_1
```

Add a pull request. This is the actual submission of your work. You can do this on github by finding your branch and clicking "Create pull request." Developers, feel free to use some command line tool for this if you prefer it.

Again, a link to github documentation on the <a href="https://help.github.com/articles/using-pull-requests#fork--pull">Fork and Pull git model</a>.

## Next Steps

We will always recommend 4 or 5 readings or other support materials for every class, either to supplement the current material, prep for the next class, or covering previous material that students still have questions on.

**Reading and other Materials**

* <a href="http://www.quora.com/Data-Science/What-is-it-like-to-be-a-data-scientist">Quora: What is it like to be a data scientist?</a>
* <a href="http://www.youtube.com/watch?v=h9vQIPfe2uU"> Josh Wills: The Life of a Data Scientist</a>
* <a href="http://www.p-value.info/"> P-Value.info, Carl Anderson's blog (Director of Data at Warby Parker)</a>
* <a href="http://blog.okcupid.com/"> A look at OKCupid and their detailed work in trends</a>
* <a href="http://radar.oreilly.com/2011/09/building-data-science-teams.html">DJ Patil, Building Data Science Teams</a>
* <a href="http://benfry.com/phd/">Ben Fry's Dissertation: Computational Information Design </a>
