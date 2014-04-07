import json
import urllib2

class NYTimesScraper():
    def __init__(self, apikey):
        self.key = apikey
        self.url = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?'

    def search(self, params={}):
        if not params:
            raise Exception('no search term!')
        else:
            build_params = '&'.join([k + '=' + v for k,v in params.iteritems()])
            build_params = build_params + '&api-key=%s' % self.key
            built_url = self.url + build_params
        req = urllib2.Request(built_url)
        return json.loads(urllib2.urlopen(req).read())

nytimes = NYTimesScraper(apikey='')
articles = nytimes.search({'q':'coffee', 'begin_date': '20140101'})

for article in articles['response']['docs']:
    print '"' + '","'.join([article['byline']['person'][0]['lastname'],
        article['pub_date'],
        article['section_name'],
        article['subsection_name'],
        article['word_count'],
        article['web_url']]) + '"'
