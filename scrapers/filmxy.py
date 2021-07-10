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
        self.domains = ['filmxy.tv']
        self.base_link = 'https://www.filmxy.tv'
        self.search_link = 'https://www.google.com/search?q=%s+%s+filmxy.tv'


    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            check = cleantitle.geturl('%s-%s' % (title, year))
            searchurl = self.search_link % (quote_plus(title), year)
            html = scrapePage(searchurl)
            results = re.compile('<a href="https://www.filmxy.tv(.+?)"', re.DOTALL).findall(html)
            for result in results:
                if check in result:
                    url = self.base_link + result
            if url == None:
                url = self.base_link + check
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
            results = client.parseDOM(html, 'div', attrs={'id': 'tab-stream'})
            for result in results:
                urls = re.compile('src=&quot;(.+?)&quot;', re.DOTALL).findall(result)
                for url in urls:
                    log_utils.log('Addon Testing sources url: \n' + repr(url))
                    url =  "https:" + url if not url.startswith('http') else url
                    valid, host = source_utils.is_host_valid(url, hostDict)
                    qual, info = source_utils.get_release_quality(url, url)
                    sources.append({'source': host, 'quality': qual, 'language': 'en', 'url': url, 'info': info, 'direct': False, 'debridonly': False})
            downloads = client.parseDOM(html, 'div', attrs={'id': 'tab-download'})
            for download in downloads:
                downloadurl = re.compile('<a href=(.+?) target=_blank>Download</a>', re.DOTALL).findall(download)[0]
                downloadhtml = scrapePage(downloadurl)
                downloadposts = client.parseDOM(downloadhtml, 'div', attrs={'class': 'custom-links'})
                for downloadpost in downloadposts:
                    links = client.parseDOM(downloadpost, 'a', ret='href')
                    for link in links:
                        log_utils.log('Addon Testing sources link: \n' + repr(link))
                        link =  "https:" + link if not link.startswith('http') else link
                        valid, host = source_utils.is_host_valid(link, hostDict)
                        qual, info = source_utils.get_release_quality(link, link)
                        sources.append({'source': host, 'quality': qual, 'language': 'en', 'url': link, 'info': info, 'direct': False, 'debridonly': False})
            return sources
        except Exception:
            log_utils.log('Testing Exception', 1)
            return sources


    def resolve(self, url):
        return url


"""


'https://clicknupload.co/0yhz9pasu2t4'
'https://clicknupload.co/i0jcumammn6j'
'https://dood.watch/d/1a5pwgz6q1kr'
'https://dood.watch/d/kpzyly4k3woi'
'https://dood.watch/e/1a5pwgz6q1kr'
'https://dood.watch/e/kpzyly4k3woi'
'https://mediashore.org/f/q272waee3l1g86x'
'https://mediashore.org/v/q272waee3l1g86x'
'https://mediashore.org/v/q272waee60lg2jw'
'https://mediashore.org/v/w7m74annrelmjpz'
'https://mirrorace.com/m/3EGU6'
'https://mirrorace.com/m/4kEmw'
'https://racaty.net/ls5rwd9s4n5j'
'https://racaty.net/vz6ac6refd38'
'https://uptobox.com/5qyxwjg2co1n'
'https://uptobox.com/ib2j1m9pmag0'
'https://uptobox.com/nzl75sw82u4y'
'https://uptobox.com/v5ljccns4h2q'
'https://uptostream.com/iframe/5qyxwjg2co1n'
'https://uptostream.com/iframe/ib2j1m9pmag0'
'https://uptostream.com/iframe/nzl75sw82u4y'
'https://uptostream.com/iframe/v5ljccns4h2q'
'https://www.filefactory.com/file/2ka9lkx4fuwp'
'https://www.filefactory.com/file/4iehrydrke17'


"""


