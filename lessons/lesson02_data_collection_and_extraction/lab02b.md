## Writing a NYTimes Article Collector Script

In lessons/lesson02 you'll find a lab02b.py file. Copy it into your own lab_submissions/lab02/name folder, and then open it in your favorite text editor (if you're unsure about this, we recommend using <a href="http://www.sublimetext.com/2">Sublime Text</a>).

### Directions

* Like the earlier section of lab, go through each line of code and write a comment explaining what it does.
* Read through the <a href="http://developer.nytimes.com/docs/read/article_search_api_v2">NYTimes Article Search Documentation</a>.
* Edit the scraper class so that it can also do some of the following:
	* Use the fq filter query fields
	* easily able to return back multiple pages of data (right now it only can return back 1 page at a time)
    * instead of returning ALL of the data, just return back the 'docs'.
* Edit the script so instead of just printing out all of docs, store all of the results into a csv file.
* Think of creative ways to do the following:

1. What was the range of dates for articles written about the Malaysia incident? Are they still being written?
2. Who contributed the most source material for the Malaysia incident?
3. Create a dictionary that uses dates as keys, and then stores a count of articles written for that subject you were searching for. You can do this for as many different subjects you're interested in!

```python
list_of_dicts = [{
    'date': '2014-01-01',
    'malaysia': 10,
    'coffee': 2,
    },
    {
    'date': '2014-01-02',
    'malaysia': 2,
    'coffee': 37,
    },
]
```


### Next Steps
1. We'll want to curate as much data as possible. Many APIs limit you to how many calls you can make per day. Think about how you can get around this to collect more and more data that does not duplicate.
2. Research another API you are interested in using for your first data project. Figure out if you need to make a scraper yourself (like we did above) or if there's a library that already does the <a href='https://pypi.python.org/pypi/nytimesarticle/0.1.0'> code work for you</a>.
3. Include a brief summary of the data you'd like to collect and work on over the next week or so for your first data project.