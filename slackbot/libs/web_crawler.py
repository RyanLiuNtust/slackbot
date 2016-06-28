import urllib
import str
from google import google
from bs4 import BeautifulSoup

class web(object):
    def get_soup(self, link):
        r = urllib.urlopen(link).read()
        soup = BeautifulSoup(r, 'html.parser')
        return soup

    def get_all_property(self, link):
        soup = self.get_soup(link)
        properties = {'title':soup.find(property='og:title')['content'],
                      'desc':soup.find(property='og:description')['content'],
                      'img':soup.find(property='og:image')['content']}
        return properties

    def google_search(self, keyword, n_results=1):
        n_pages = 1
        lang = 'en'
        search_results = google.search(keyword, n_pages, lang)
        properties = [] 
        for result in search_results[:n_results]:
            p = {'title':str.str_encode(result.name),
                 'link':result.link,
                 'desc':str.str_encode(result.description),
                 'img':result.thumb}
            properties.append(p)
        return properties 
