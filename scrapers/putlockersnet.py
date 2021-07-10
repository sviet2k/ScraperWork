# -*- coding: UTF-8 -*-

import re
import requests

import simplejson as json
from six import ensure_text

from oathscrapers.modules import client
from oathscrapers.modules import cleantitle
from oathscrapers.modules import source_utils
from oathscrapers.modules import log_utils
from oathscrapers.modules import jsunpack


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['putlockers.net']
        self.base_link = 'https://wwv.putlockers.net'
        self.search_link = '/search/?s=%s'
        self.userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        self.headers = {'User-Agent': self.userAgent, 'Referer': self.base_link}
        self.gomo_link = 'https://gomo.to/decoding_v3.php'


    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            movieTitle = cleantitle.clean_search_query(title)
            link = self.base_link + self.search_link % (movieTitle + '+' + year)
            searchPage = ensure_text(requests.get(link, headers=self.headers).content, errors='replace')
            pages = client.parseDOM(searchPage, 'div', attrs={'class': 'featuredItems singleVideo'})
            results = [(client.parseDOM(i, 'a', ret='href'), client.parseDOM(i, 'a', ret='title')) for i in pages]
            result = [(i[0][0], i[1][0]) for i in results if i[0] and i[1]]
            link2 = [i[0] for i in result if cleantitle.get(title) == cleantitle.get(i[1])][0]
            moviePage = ensure_text(requests.get(link2, headers=self.headers).content, errors='replace')
            videoArea = client.parseDOM(moviePage, 'div', attrs={'class': 'videoArea'})
            url = client.parseDOM(videoArea, 'a', ret='href')[0]
            return url
        except Exception:
            log_utils.log('Testing Exception', 1)
            return


    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            tvshowTitle = cleantitle.clean_search_query(tvshowtitle)
            link = self.base_link + self.search_link % (tvshowTitle)
            searchPage = ensure_text(requests.get(link, headers=self.headers).content, errors='replace')
            pages = client.parseDOM(searchPage, 'div', attrs={'class': 'featuredItems singleVideo'})
            results = [(client.parseDOM(i, 'a', ret='href'), client.parseDOM(i, 'a', ret='title')) for i in pages]
            result = [(i[0][0], i[1][0]) for i in results if i[0] and i[1]]
            link2 = [i[0] for i in result if cleantitle.get(tvshowtitle) == cleantitle.get(i[1])][0]
            url = re.findall('(?://.+?|)(/.+)', link2)[0]
            return url
        except Exception:
            log_utils.log('Testing Exception', 1)
            return


    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            if url == None:
                return
            tvshowtitle = re.findall('/series/(.+?)/', url)[0]
            link = self.base_link + '/episode/%s-%sx%s/' % (tvshowtitle, season, episode)
            episodePage = ensure_text(requests.get(link, headers=self.headers).content, errors='replace')
            videoArea = client.parseDOM(episodePage, 'div', attrs={'class': 'videoArea'})
            url = client.parseDOM(videoArea, 'a', ret='href')[0]
            return url
        except Exception:
            log_utils.log('Testing Exception', 1)
            return


    def sources(self, url, hostDict, hostprDict):
        hostDict = hostDict + hostprDict
        sources = []
        try:
            if url == None:
                return sources
            sourcePage = ensure_text(requests.get(url, headers=self.headers).content, errors='replace')
            link = client.parseDOM(sourcePage, 'iframe', ret='src')[0]
            if 'gomo.to' in link:
                for source in self.scrapeGomo(link, hostDict):
                    log_utils.log('Addon Testing gomo source: \n' + repr(source))
                    sources.append(source)
            else:
                valid, host = source_utils.is_host_valid(link, hostDict)
                if valid:
                    quality, info = source_utils.get_release_quality(link, link)
                    log_utils.log('Addon Testing normal source: \n' + repr(source))
                    sources.append({'source': host, 'quality': quality, 'language': 'en', 'url': link, 'info': info, 'direct': False, 'debridonly': False})
            return sources
        except Exception:
            log_utils.log('Testing Exception', 1)
            return sources


    def scrapeGomo(self, url, hostDict):
        sources = []
        try:
            result = ensure_text(client.request(url), errors='replace')
            tc = re.compile('tc = \'(.+?)\';').findall(result)[0]
            if (tc):
                token = re.compile('"_token": "(.+?)",').findall(result)[0]
                post = {'tokenCode': tc, '_token': token}
                def tsd(tokenCode):
                    _13x48X = tokenCode
                    _71Wxx199 = _13x48X[4:18][::-1]
                    return _71Wxx199 + "18" + "432782"
                headers = {'Host': 'gomo.to', 'Referer': url, 'User-Agent': self.userAgent, 'x-token': tsd(tc)}
                result = ensure_text(client.request(self.gomo_link, XHR=True, post=post, headers=headers), errors='replace')
                links = json.loads(result)
                for link in links:
                    link = "https:" + link if not link.startswith('http') else link
                    if 'gomo.to' in link:
                        link = ensure_text(requests.get(link, headers=self.headers).url, errors='replace')
                        if 'gomoplayer.com' in link:
                            sourcePage = ensure_text(requests.get(link, headers=self.headers).content, errors='ignore')
                            if jsunpack.detect(sourcePage):
                                unpacked = jsunpack.unpack(sourcePage)
                                urls = re.compile('file:"(.+?)"').findall(unpacked)
                                for url in urls:
                                    if '/srt/' in url: continue
                                    info = 'MP4' if url.endswith('.mp4') else 'm3u8'
                                    sources.append({'source': 'CDN', 'quality': 'SD', 'language': 'en', 'url': url, 'info': info, 'direct': False, 'debridonly': False})
                        # https://database.gdriveplayer.us/player.php?imdb=tt1825683
                    else:
                        valid, host = source_utils.is_host_valid(link, hostDict)
                        if valid:
                            quality, info = source_utils.get_release_quality(link, link)
                            sources.append({'source': host, 'quality': quality, 'language': 'en', 'url': link, 'info': info, 'direct': False, 'debridonly': False})
            return sources
        except Exception:
            log_utils.log('Testing Exception', 1)
            return sources


    def resolve(self, url):
        return url


