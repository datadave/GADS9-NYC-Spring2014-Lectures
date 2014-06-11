import json
import urllib2

class NYTimesScraper():
    def __init__(self, apikey):
        # Creates a new NYTimesScraper Object using the apikey that was included.
        self.key = apikey
        self.url = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?'
    def _build_params(self, params):
        if not params:
            raise Exception('no search parameters!')
        else:
            return '&'.join([k + '=' + v for k,v in params.iteritems()])
    def search(self, params={}):
        url = self.url + self._build_params(params)
        url = url + '&api-key=%s' % self.key
        req = urllib2.Request(url)
        data = urllib2.urlopen(req).read()
        return json.loads(data)

nytimes = NYTimesScraper(apikey='')
articles = api.search({'q':'malaysia', 'begin_date': '20140101'})

for article in articles['response']['docs']:
    print '"' + '","'.join([article['byline']['person'][0]['lastname'],
        article['pub_date'],
        article['section_name'],
        article['subsection_name'],
        article['word_count'],
        article['web_url']]) + '"'

filename = 'nytimesdata.csv'
writer = open(filename, 'w')

# Fill in the column names here as one string
writer.write('')
for article in articles['response']['docs']:
    # Write the article data you want to collect here
