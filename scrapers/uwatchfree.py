# -*- coding: UTF-8 -*-


import requests
from six import ensure_text
from oathscrapers import urlparse

from oathscrapers.modules import client
from oathscrapers.modules import source_utils
from oathscrapers.modules import log_utils


def scrapePage(url, referer=None):
    try:
        if not url:
            return []
        url =  "https:" + url if not url.startswith('http') else url
        with requests.Session() as session:
            if referer:
                session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0', 'Referer': referer})
            else:
                elements = urlparse(url)
                base = '%s://%s' % (elements.scheme, (elements.netloc or elements.path))
                session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0', 'Referer': base})
            page = ensure_text(session.get(url, headers=session.headers).content, errors='replace')
        return page
    except Exception:
        log_utils.log('Testing Exception', 1)
        return []


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['uwatchfree.as']
        self.base_link = 'https://www.uwatchfree.as'
        self.search_link = '/search/%s/feed/rss2/'


    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            url = self.base_link + self.search_link % imdb
            html = scrapePage(url)
            posts = client.parseDOM(html, 'item')
            for post in posts:
                if not imdb in post:
                    raise Exception()
                url = client.parseDOM(post, 'a', ret='href')[0]
            return url
        except Exception:
            log_utils.log('Testing Exception', 1)
            return


    def sources(self, url, hostDict, hostprDict):
        try:
            hostDict = hostprDict + hostDict
            sources = []
            if url == None:
                return sources
            html = scrapePage(url)
            body = client.parseDOM(html, 'tbody')[0]
            links = client.parseDOM(body, 'a', ret='href')
            for link in links:
                html = scrapePage(link)
                links = client.parseDOM(html, 'iframe', ret='src')
                for link in links:
                    log_utils.log('Addon Testing link: \n' + repr(link))
                    valid, host = source_utils.is_host_valid(link, hostDict)
                    qual, info = source_utils.get_release_quality(link, link)
                    sources.append({'source': host, 'quality': qual, 'language': 'en', 'url': link, 'info': info, 'direct': False, 'debridonly': False})
            return sources
        except Exception:
            log_utils.log('Testing Exception', 1)
            return sources


    def resolve(self, url):
        return url


