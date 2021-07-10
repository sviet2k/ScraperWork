# -*- coding: UTF-8 -*-

import re
import requests

import simplejson as json
from six import ensure_text
from oathscrapers import parse_qs, urlencode, urljoin, urlparse, quote_plus, unquote

from oathscrapers.modules import client
from oathscrapers.modules import cleantitle
from oathscrapers.modules import source_utils
from oathscrapers.modules import log_utils
from oathscrapers.modules import directstream


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
        self.domains = ['todaytvseries.bid']
        self.base_link = 'https://todaytvseries.bid'
        self.search_link = '/search/%s/feed/'


    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'title': title, 'localtitle': localtitle, 'aliases': aliases, 'year': year}
            url = urlencode(url)
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
            data = parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])
            title = data['title']
            hdlr = data['year']
            query = '%s %s' % (data['title'], data['year'])
            url = self.base_link + self.search_link % cleantitle.geturl(query)
            html = scrapePage(url)
            posts = client.parseDOM(html, 'item')
            if not posts:
                url = self.base_link + self.search_link % cleantitle.geturl(title)
                html = scrapePage(url)
                posts = client.parseDOM(html, 'item')
            for post in posts:
                name = client.parseDOM(post, 'title')[0]
                t = re.sub('(\.|\(|\[|\s)(\d{4}|S\d*E\d*|S\d*|3D)(\.|\)|\]|\s|)(.+|)', '', name, flags=re.I)
                if not cleantitle.get(t) == cleantitle.get(title):
                    raise Exception()
                y = re.findall('[\.|\(|\[|\s](\d{4}|S\d*E\d*|S\d*)[\.|\)|\]|\s]', name)[-1].upper()
                if not y == hdlr:
                    raise Exception()
                links = client.parseDOM(post, 'a', ret='href')
                for link in links:
                    if self.base_link in link:
                        continue
                    if 'multiup.org' in link:
                        html = scrapePage(link)
                        mirror = re.compile('<form action="(.+?)" method', re.DOTALL).findall(html)[0]
                        mirror = mirror.replace('/fr/mirror/', '/en/mirror/')
                        mirrorlink = 'https://multiup.org' + mirror
                        html2 = scrapePage(mirrorlink)
                        mirrors = re.compile('<input type="hidden" name="link" value="(.+?)">', re.DOTALL).findall(html2)
                        for url in mirrors:
                            valid, host = source_utils.is_host_valid(url, hostDict)
                            qual, info = source_utils.get_release_quality(url, url)
                            sources.append({'source': host, 'quality': qual, 'language': 'en', 'url': url, 'info': info, 'direct': False, 'debridonly': False})
                    if 'zippyshare.com' in link:
                        html = scrapePage(link)
                        mirrors = re.compile('<source src="(.+?)"', re.DOTALL).findall(html)
                        for url in mirrors:
                            url =  "https:" + url if not url.startswith('http') else url
                            valid, host = source_utils.is_host_valid(url, hostDict)
                            qual, info = source_utils.get_release_quality(url, url)
                            sources.append({'source': host, 'quality': qual, 'language': 'en', 'url': url, 'info': info, 'direct': False, 'debridonly': False})
                    valid, host = source_utils.is_host_valid(link, hostDict)
                    qual, info = source_utils.get_release_quality(link, link)
                    sources.append({'source': host, 'quality': qual, 'language': 'en', 'url': link, 'info': info, 'direct': False, 'debridonly': False})
            return sources
        except Exception:
            log_utils.log('Testing Exception', 1)
            return sources


    def resolve(self, url):
        return url


