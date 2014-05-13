# BeautifulSoup Web Scraping Example

[Mashable.py](mashable.py) is a simple python script to parse [Mashable's Must Reads](http://mashable.com/category/must-reads).

## Initial Steps to Web Scraping

1. Figure out what page you want to scrape (obviously!)
2. Identify what parts of the page you are interested in (links, values, comments, etc.)
3. View the web page source (right-click, View Page Source)
4. Find a sample of what you want to scrape within the source
5. Identify a common container for your data (i.e., a table, a common div class, etc.)

### Example with Mashable's Must Reads

Let's say we want to grab article titles and links. What can we see in the source code?
	
	<header>
	<a class='article-category' data-crackerjax href='#'>Tech</a>
	<h1 class='article-title'>
	<a href='http://mashable.com/2014/05/08/what-is-3d-printing/'>
	3D Printing: Everything You Need to Know in 2 Minutes</a>
	</h1>
	</header>
	...
	<header>
	<a class='article-category' data-crackerjax href='#'>Lifestyle</a>
	<h1 class='article-title'>
	<a href='http://mashable.com/2014/05/08/inspiring-moms/'>
	21 Inspirational Stories That Prove Moms Are Superheroes</a>
	</h1>
	</header>

## Next Steps for Web Scraping

1. Instantiate a BeautifulSoup object, given the downloaded data
2. Use the *find()* or *find_all()* methods to locate the parent container(s)
3. Walk through the container(s) and dig in deeper (if necessary) to get the data of interest (using *find()* or *find_all()* successively until you are at tthe data)

### Code for Mashable's Must Reads
	

We have a few options here--you might look for &lt;header&gt;, but we can also see that each article title and link combination is further encapsulated within an &lt;h1&gt; tag. And, what's more, those &lt;h1&gt; tags have a class identifier! To get tags with those classes, we can do the following:

	from bs4 import BeautifulSoup
	# Assume the downloaded page contents are in a variable called document
	soup = BeautifulSoup(document)
	sectionsOfInterest = soup.findAll('h1', {'class':'article-title'}
	
Now we have a list of the &lt;h1 class='article-title'&gt; tags. The elements of the list are BeautifulSoup objects. Let's take this further to extract the links and titles that we are interested in.

	title_link_dict = {}
	for h1 in sectionsOfInterest:
        anchor = h1.find('a')
        # note: find returns the first match
        # we know only one <a href=...> exists per <h1 class=...>

		# find will return None if an element can't be found
      	if anchor == None:
      		continue
      	      
      	# make two simple safety checks to ensure 
      	# this anchor tag is formatted as expected
		if len(anchor.contents)>0 and anchor.has_attr('href'):
			link = anchor['href']
			title = anchor.contents[0]
			title_link_dict[title] = link
      	
Now we've got a dictionary with article titles as keys and URLs as values. Let's print them out!

	for title,link in title_link_dict.items():
		print "%s\n\t%s\n"%(title,link)
		
That's it! We've just scraped and printed the titles and links. Note: you could have printed in the earlier for loop, but now you have a dictionary with all of the data you found.      	
      	
	$ python mashable.py
	
	...
	
	3D Printing: Everything You Need to Know in 2 Minutes
		http://mashable.com/2014/05/08/what-is-3d-printing/

	21 Inspirational Stories That Prove Moms Are Superheroes
		http://mashable.com/2014/05/08/inspiring-moms/      	
    ...    
       
