# Common Python Commands 

### Run the interpreter
    python
    
#### Quit the iPython interpreter
    >>> quit()
    
### Run the iPython interpreter
    ipython
    
#### Quit the Python interpreter
    >>> quit()    

### Run iPython Notebook
    ipython notebook
* Note: Your notebooks and other generated files will be saved in the directory where you launch *ipython* from (i.e., your present working directory).
* Second note: Any paths you reference in your notebook like *pandas.read_csv('file.csv')* will be relative to your present working directory.

#### Open an iPython Notebook file
    ipython notebook <notebook.ipynb>
    
### Stop iPython Notebook
    ctrl+c    
    
### Bookmark for Opening *.ipynb files on the web
Copy code below and paste it in as the address of a new bookmark.

Then, when viewing any *.ipynb file from github (or elsewhere) click on the bookmark to view the file in nbviewer.

``` 
javascript:date = new Date();url_root = 'http://nbviewer.ipython.org/';url = null;gist_re = /^https?:\/\/gist\.github\.com\/(?:\w+\/)?([a-f0-9]+)$/;github_re = /^https:\/\/(github\.com\/.*\/)blob\/(.*\.ipynb)$/;https_re = /^https:\/\/(.*\.ipynb)$/;http_re = /^http:\/\/(.*\.ipynb)$/;loc = location.href;if (gist_re.test(loc)) {    gist = gist_re.exec(loc);    url = url_root + gist[1];} else if (github_re.test(loc)) {    path = github_re.exec(loc);    url = url_root + 'urls/raw.' + path[1] + path[2];} else if (https_re.test(loc)) {    path = https_re.exec(loc);    url = url_root + 'urls/' + path[1];} else if (http_re.test(loc)) {    path = http_re.exec(loc);    url = url_root + 'url/' + path[1];}if (url) {void(window.open(url, 'nbviewer' + date.getTime()));}
```
    
           
