"""
A quick and dirty Mashable link scraper.
This pulls links from the "Must Reads" page.

This is to demo the awesome power of BeautifulSoup!

Joe Carli
joe.carli@gmail.com
May 2014
"""

import sys
import urllib2
from socket import timeout as SocketTimeout 
from bs4 import BeautifulSoup

class MyLink(object):
    def __init__(self,url,title):
        self.url = url.strip()
        self.title = title.strip()
    def __str__(self):
        return ("%s\n\t%s"%(self.title,self.url))
# end of RedditLink class

def getPage(url):
    """
    Downloads and returns the page contents at url.
    Returns an empty string if an error is encountered.
    """
    # Build a Request object
    req = urllib2.Request(url=url)
    try:
        page = urllib2.urlopen(url=req,data=None,timeout=10)
    except urllib2.URLError, e:
        if hasattr(e, 'reason'):
            sys.stderr.write('Failed to open %s (%s)\n'%(url,e.reason))
            return ''
        elif hasattr(e, 'code'):
            sys.stderr.write('Failed to open %s (server returned code %s)\n' \
                %(url,e.code))
            return ''
    except Exception, e:
        sys.stderr.write('Failed to open %s (unexpected error: %s)\n'\
            %(url,e))
        return ''
    else:
        # Try reading the page - prepare to handle socket timeout on read()
        try:
            contents = page.read()
        except SocketTimeout as e:
            sys.stderr.write('Socket timeout reading page in getPage()\n')
            return ''
        except:
            sys.stderr.write('Unexpected error reading page in getPage()\n')
            return ''

        # Try decoding the page contents (a raw string) as utf8
        # Return the raw string if unsuccessful
        try:
            decoded = contents.decode('utf-8')
        except:
            sys.stderr.write('getPage() returning raw string from %s\n'%(url))
            return contents
        else:
            return decoded
# end of getPage()

def findLinks(document):
    """
    Given a document, returns a list of links.
    The returned item is a list, where each element is a RedditLink object.
    """
    # Create an empty list that we will populate
    links = []

    # Instantiate a BeautifulSoup object from the document
    soup = BeautifulSoup(document)
    sectionsOfInterest = soup.findAll('h1', {'class':'article-title'})
    if sectionsOfInterest == None:
        print "Unable to find the expected headers."
        return links

    print "Found %d likely links"%(len(sectionsOfInterest))
    for h1 in sectionsOfInterest:
        anchor = h1.find('a')
        if anchor == None:
            sys.stderr.write('Encountered a bad anchor tag.\n')
            continue
           
        if len(anchor.contents) > 0 and anchor.has_attr('href'):
            newLink = MyLink(url=anchor['href'],title=anchor.contents[0])
            links.append(newLink)

    print "Returning %d links"%len(links)
    return links
# end of findLinks()

if __name__=="__main__":
    url = 'http://mashable.com/category/must-reads'
    page = getPage(url)
    print "Read %d bytes from %s"%(len(page),url)
    links = findLinks(page)
    print ""
    for l in links:
        print l
    print ""
