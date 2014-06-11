# Data Mining Workflow and Unix Commands for a Data Scientist

### Getting NYTimes Data

Use <a href="http://developer.nytimes.com/">http://developer.nytimes.com/</a> as our resource for signing up to get a nytimes API key. We'll be using the articles API key for the first few weeks of class.

```sh
mkdir nytimes_data
cd nytimes_data
curl -s 'http://api.nytimes.com/svc/search/v2/articlesearch.json?q=malaysia&page=0&api-key=$KEYVALUE' > malaysia_articles.json
```

### Observing and getting around the data
First we'll notice that the data we collected was in a JSON file format. Most APIs will end up using this format or similar
(xml). We can view the data quickly using `less`, but something tells us immediately it won't be very useful!
```sh
less malaysia_articles.json
```

Fortunately, python has a built in pretty-printer that we can use to make this file a bit more human readable. We can use `cat` as a form of printing the article out, and the pipe `|` to take whatever we printed and use in the next command.

```sh
cat malaysia_articles.json | python -mjson.tool >> malaysia_pretty_printed.json
```

`ls` Let's us examine what files we're working with. Since we're only interested in checking to see that we have both of our json, we can append '.json' to the ls. Then, we can use `head` to view the top part of the new file, or use `less` again to skim through a much easier file to read.

```sh
ls .json
head -n 20 malaysia_pretty_printed.json
less malaysia_pretty_printed.json
```

From here, we're now interested in organizing our data a bit. A quick scan shows a few data points we might be interested in:

* contributor: authors of the article
* pub_date: the publication date of the article
* section_name: which section it was included in
* subsection_name: the subsection
* word_count: length of article
* web_url: in case you want to read it later

First, we could use `grep` with our pretty-printed file to check out what a value looked like across all 10 articles:

```sh
cat malaysia_pretty_printed.json | grep 'pub_date'
cat malaysia_pretty_printed.json | grep 'word_count'
```

Likewise, we can use `sort` to provide a little bit of organization, and `uniq -c` to see our article distribution:

```sh
cat malaysia_pretty_printed.json | grep 'pub_date' | sort | uniq -c
```

Let's write a short python script to handle collecting data together into one neat file:

```python
#! /usr/bin/env python
import json

nytimes = json.load(open('malaysia_pretty_printed.json', 'r'))
print ','.join(['contributor', 'pub_date', 'section', 'subsection', 'word_count', 'url'])
for article in nytimes['response']['docs']:
    print '"' + '","'.join([article['byline']['contributor'],
        article['pub_date'],
        article['section_name'],
        article['subsection_name'],
        article['word_count'],
        article['web_url']]) + '"'
```

Now we can get this data into some usable format--

```sh
chmod +x ./nytimes_parser.py
./nytimes_parser.py > nytimes.csv
less nytimes.csv
```

###In Class

1. Explore the NYTimes Gallery for visualization ideas: http://developer.nytimes.com/gallery
2. What could be good next steps in this data exploration?
3. Try collecting more data about a particular topic from the NYTimes. You have 10000 calls per day!
    a. Think about scaleability here. You can't just append seperate api requests so easily.

Other data processing tools available on Unix
- awk
- sed
- perl