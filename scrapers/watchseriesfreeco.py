# -*- coding: utf-8 -*-

import re
import simplejson as json
from six import ensure_text
from oathscrapers import parse_qs, urlencode

from oathscrapers.modules import client
from oathscrapers.modules import cleantitle
from oathscrapers.modules import source_utils
from oathscrapers.modules import log_utils


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['watchseriesfree.co']
        self.base_link = 'https://watchseriesfree.co'
        self.search_link = '/search.html?keyword=%s'


    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            movieTitle = cleantitle.geturl(title)
            check = cleantitle.get(title)
            query = self.base_link + self.search_link % (movieTitle.replace('-', '%20'))
            r = ensure_text(client.request(query), errors='replace')
            r = client.parseDOM(r, 'li', attrs={'class': 'video-block'})
            r = [(client.parseDOM(i, 'a', ret='href'), client.parseDOM(i, 'div', attrs={'class': 'home_video_title'})) for i in r]
            r = [(i[0][0], re.compile('<div>(.+?)</div>', re.DOTALL).findall(i[1][0])[0]) for i in r if len(i[0]) > 0 and len(i[1]) > 0]
            url = [i[0] for i in r if check == cleantitle.get(i[1])][0]
            return url
        except Exception:
            log_utils.log('Testing Exception', 1)
            return


    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'tvdb': tvdb, 'tvshowtitle': tvshowtitle, 'year': year}
            url = urlencode(url)
            return url
        except Exception:
            log_utils.log('Testing Exception', 1)
            return


    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            data = parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])
            tvshowTitle = cleantitle.geturl(data['tvshowtitle'])
            check = cleantitle.get(data['tvshowtitle'])
            query = self.base_link + self.search_link % (tvshowTitle.replace('-', '%20'))
            r = ensure_text(client.request(query), errors='replace')
            r = client.parseDOM(r, 'li', attrs={'class': 'video-block'})
            r = [(client.parseDOM(i, 'a', ret='href'), client.parseDOM(i, 'div', attrs={'class': 'home_video_title'})) for i in r]
            r = [(i[0][0], re.compile('<div>(.+?)</div>', re.DOTALL).findall(i[1][0])[0]) for i in r if len(i[0]) > 0 and len(i[1]) > 0]
            url = [i[0] for i in r if check in cleantitle.get(i[1]) and ('Season %s' % season) in i[1]][0]
            url += '?episode=%01d' % int(episode)
            return url
        except Exception:
            log_utils.log('Testing Exception', 1)
            return


    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []
            if url == None:
                return sources
            url = [i for i in url.strip('/').split('/')][-1]
            if '?episode=' in url:
                url, episode = re.findall('(.+?)\?episode=(\d*)$', url)[0]
                url = self.base_link + '/watch/%s/0' % url
                result = ensure_text(client.request(url), errors='replace')
                r = [i for i in client.parseDOM(result, 'li', attrs={'class': 'nav-item'})]
                r = [(client.parseDOM(i, 'a', ret='onclick'), client.parseDOM(i, 'a', attrs={'class': 'nav-link btn btn-sm btn-secondary link-item sv-14'})) for i in r]
                r = [(i[0][0], re.compile('Episode ([A-Za-z0-9]+)', re.DOTALL).findall(i[1][0])) for i in r]
                log_utils.log('Addon Testing sources r2: \n' + repr(r))
                urls = [i[0] for i in r if episode in i[1]]
            else:
                url = self.base_link + '/watch/%s/0' % url
                result = ensure_text(client.request(url), errors='replace')
                r = [i for i in client.parseDOM(result, 'li', attrs={'class': 'nav-item'})]
                urls = [i for i in client.parseDOM(r, 'a', ret='onclick')]
            for url in urls:
                link = re.compile('''load_episode_video\(\'(.+?)'\)''', re.DOTALL).findall(url)[0]
                link = "https:" + link if not link.startswith('http') else link
                if 'vidcloud9' in link:
                    for source in self.vidcloud9(link, hostDict):
                        sources.append(source)
                else:
                    log_utils.log('Addon Testing sources link: \n' + repr(link))
                    valid, host = source_utils.is_host_valid(link, hostDict)
                    sources.append({'source': host, 'quality': 'HD', 'language': 'en', 'url': link, 'direct': False, 'debridonly': False})
            return sources
        except Exception:
            log_utils.log('Testing Exception', 1)
            return sources


    def resolve(self, url):
        return url


    def vidcloud9(self, link, hostDict):
        sources = []
        try:
            html = ensure_text(client.request(link, headers={'User-Agent': client.agent(), 'Referer': link}), errors='replace')
            urls = re.compile('data-video="(.+?)">').findall(html)
            for url in urls:
                url = "https:" + url if not url.startswith('http') else url
                if 'vidnext.net' in url:
                    if '&typesub' in url:
                        html = ensure_text(client.request(link, headers={'User-Agent': client.agent(), 'Referer': link}), errors='replace')
                        url = re.findall("file: '(.+?)'", html)[0]
                        log_utils.log('Addon Testing sources url: \n' + repr(url))
                        sources.append({'source': 'HLS', 'quality': 'SD', 'language': 'en', 'url': url, 'direct': False, 'debridonly': False})
                    else:
                        html = ensure_text(client.request(url, headers={'User-Agent': client.agent(), 'Referer': link}), errors='replace')
                        url = re.compile('data-video="(.+?)">').findall(html)
                        for url in url:
                            url = "https:" + url if not url.startswith('http') else url
                            if 'vidnext.net' in url:
                                url = ensure_text(client.request(url, headers={'User-Agent': client.agent(), 'Referer': url}), errors='replace')
                                r = re.findall('(ep.+?.m3u8)', url)
                                for r in r:
                                    url = url.split('ep')[0]
                                    url = url + r
                                    if '.720.m3u8' in url:
                                        quality = '720p'
                                    else:
                                        quality = 'SD'
                                    log_utils.log('Addon Testing sources url: \n' + repr(url))
                                    sources.append({'source': 'HLS3X', 'quality': quality, 'language': 'en', 'url': url, 'direct': False, 'debridonly': False})
                            else:
                                log_utils.log('Addon Testing sources url: \n' + repr(url))
                                valid, host = source_utils.is_host_valid(url, hostDict)
                                quality, info = source_utils.get_release_quality(url, url)
                                sources.append({'source': host, 'quality': quality, 'language': 'en', 'info': info, 'url': url, 'direct': False, 'debridonly': False})
                elif 'movcloud' in url:
                    url = url.replace('https://movcloud.net/embed/', 'https://api.movcloud.net/stream/')
                    url = ensure_text(client.request(url, headers={'User-Agent': client.agent(), 'Referer': 'https://movcloud.net'}), errors='replace')
                    url = json.loads(url)
                    url = url['data']
                    url = url['sources']
                    for url in url:
                        label = url['label']
                        url = url['file']
                        log_utils.log('Addon Testing sources url: \n' + repr(url))
                        quality, info = source_utils.get_release_quality(label, label)
                        sources.append({'source': 'movcloud', 'quality': quality, 'language': 'en', 'info': info, 'url': url, 'direct': False, 'debridonly': False})
                else:
                    log_utils.log('Addon Testing sources url: \n' + repr(url))
                    valid, host = source_utils.is_host_valid(url, hostDict)
                    quality, info = source_utils.get_release_quality(url, url)
                    sources.append({'source': host, 'quality': quality, 'language': 'en', 'info': info, 'url': url, 'direct': False, 'debridonly': False})
            return sources
        except Exception:
            log_utils.log('Testing Exception', 1)
            return sources





"""


# 'voxzer.org'  -  'https://player.voxzer.org/view/91c3c1e7c333d79ff15b05e0'
# uses jwplayer crap
# 'vidcloud9.com'  -  'https://vidcloud9.com/streaming.php?id=ODc5Mg=='
# scrapes proper url with rescrape def.


'https://player.voxzer.org/view/91c3c1e7c333d79ff15b05e0'
'https://vidembed.net/loadserver.php?id=ODc5Mg=='
'https://sbplay.org/embed-f9ybau1c0q82.html'
'https://dood.la/e/gbehlqjpzmch'
'https://mixdrop.co/e/qlek8mejcxlqo39'
'https://mixdrop.co/e/qlek8mejcxlqo39'
'https://hydrax.net/watch?v=f4vNjqfmuP'


"""



