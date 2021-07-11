# -*- coding: utf-8 -*-

import re
import requests
from six import ensure_text
from oathscrapers import parse_qs, urlparse, urlencode, quote_plus

from oathscrapers.modules import client
from oathscrapers.modules import cleantitle
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
        self.domains = ['losmovies.life']
        self.base_link = 'https://losmovies.life'
        self.search_link = '/movies-search?type=movies&q=%s'


    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'title': title, 'year': year}
            url = urlencode(url)
            return url
        except:
            return


    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'tvdb': tvdb, 'tvshowtitle': tvshowtitle, 'year': year}
            url = urlencode(url)
            return url
        except:
            return


    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            if url == None: return
            url = parse_qs(url)
            url = dict([(i, url[i][0]) if url[i] else (i, '') for i in url])
            url['title'], url['premiered'], url['season'], url['episode'] = title, premiered, season, episode
            url = urlencode(url)
            return url
        except:
            return


# Needs all the sources logged and double checked then most likely scraped further besides a couple.
# Seen a few results in the site code that cock block the true url ending with some odd encode bit. think they were all imdb for the true ending.


    def sources(self, url, hostDict, hostprDict):
        
        try:
            sources = []
            if url == None:
                return sources
            data = parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])
            title = data['tvshowtitle'] if 'tvshowtitle' in data else data['title']
            check = '%s_%s' % (quote_plus(title).replace('+', '_').lower(), data['year'])
            link = self.base_link + self.search_link % quote_plus(title)
            html = scrapePage(link)
            results = client.parseDOM(html, 'div', attrs={'class': 'showRow showRowImage showRowImage'})
            results = [(client.parseDOM(i, 'a', ret='href'), client.parseDOM(i, 'img', ret='src')) for i in results]
            results = [(i[0][0], i[1][0]) for i in results if len(i[0]) > 0 and len(i[1]) > 0]
            result = [i[0] for i in results if check in i[1]][0]
            link = self.base_link + result
            html = scrapePage(link)
            if 'tvshowtitle' in data:
                season = data['season']
                episode = data['episode']
                regex = '<td class="linkHidden linkHiddenUrl" data-width="700" data-height="460" data-season="%s" data-serie="%s">(.+?)</td>' % (season, episode)
            else:
                regex = '<td class="linkHidden linkHiddenUrl" data-width="700" data-height="460" data-season=".+?" data-serie=".+?">(.+?)</td>'
            links = re.compile(regex, re.DOTALL).findall(html)
            for link in links:
                link = "https:" + link if not link.startswith('http') else link
                log_utils.log('Addon Testing link: \n' + repr(link))
                valid, host = source_utils.is_host_valid(link, hostDict)
                qual, info = source_utils.get_release_quality(link, link)
                sources.append({'source': host, 'quality': qual, 'language': 'en', 'url': link, 'info': info, 'direct': False, 'debridonly': False})
            return sources
        except:
            log_utils.log('Testing Exception', 1)
            return sources


    def resolve(self, url):
        return url


