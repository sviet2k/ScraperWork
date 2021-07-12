# -*- coding: UTF-8 -*-

import re
import requests

from six import ensure_text
from oathscrapers import urlparse

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
        self.domains = ['imdbbox.com']
        self.base_link = 'https://imdbbox.com'
        self.search_link = '/e/movie/%s'
        self.search2_link = '/d/movie/%s'


    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            url = imdb
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
            imdb = url

            url = self.base_link + self.search_link % imdb
            html = scrapePage(url)
            regex = r'''\{\s*file:\s*"(.+?)",\s*label:\s*"(.+?)"\s*\}'''
            urls = re.compile(regex).findall(html)
            if urls:
                for link, qual in urls:
                    link =  "https:" + link if not link.startswith('http') else link
                    log_utils.log('Addon Testing search_link link: \n' + repr(link))
                    valid, host = source_utils.is_host_valid(link, hostDict)
                    qual, info = source_utils.get_release_quality(qual, link)
                    sources.append({'source': host, 'quality': qual, 'language': 'en', 'url': link, 'info': info, 'direct': True, 'debridonly': False})

            url = self.base_link + self.search2_link % imdb
            html = scrapePage(url)
            regex = r'<a class="btn btn-success" href="(.+?)">(.+?)</a>'
            urls = re.compile(regex).findall(html)
            if urls:
                for link, qual in urls:
                    try:
                        link = re.findall('&url=(.+?)&format=', link)[0]
                    except:
                        link = link.split('&url=')[1]
                    link =  "https:" + link if not link.startswith('http') else link
                    log_utils.log('Addon Testing search_link2 link: \n' + repr(link))
                    valid, host = source_utils.is_host_valid(link, hostDict)
                    qual, info = source_utils.get_release_quality(qual, link)
                    sources.append({'source': host, 'quality': qual, 'language': 'en', 'url': link, 'info': info, 'direct': True, 'debridonly': False})

            return sources
        except Exception:
            log_utils.log('Testing Exception', 1)
            return sources


    def resolve(self, url):
        return url


