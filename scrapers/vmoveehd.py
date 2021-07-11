# -*- coding: UTF-8 -*-

import re
import requests
from six import ensure_text
from oathscrapers import urljoin

from oathscrapers.modules import client
from oathscrapers.modules import cleantitle
from oathscrapers.modules import source_utils
from oathscrapers.modules import log_utils


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['vmoveehd.com']
        self.base_link = 'https://vmoveehd.com'
        self.search_link = '/?s=%s'
        self.ajax_link = '/wp-admin/admin-ajax.php'
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0', 'Referer': self.base_link})


    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            movieTitle = cleantitle.geturl(title)
            link = self.base_link + self.search_link % (movieTitle.replace('-', '+'))
            html = ensure_text(self.session.get(link, headers=self.session.headers).content, errors='replace')
            movie_scrape = re.compile('<div class="title".+?href="(.+?)">(.+?)</a>.+?class="year">(.+?)</span>', re.DOTALL).findall(html)
            for movie_url, movie_title, movie_year in movie_scrape:
                if cleantitle.get(title) == cleantitle.get(movie_title):
                    if year in str(movie_year):
                        return movie_url
            return
        except Exception:
            log_utils.log('Testing Exception', 1)
            return


    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            tvshowTitle = cleantitle.geturl(tvshowtitle)
            link = self.base_link + self.search_link % (tvshowTitle.replace('-', '+'))
            html = ensure_text(self.session.get(link, headers=self.session.headers).content, errors='replace')
            tv_scrape = re.compile('<div class="title".+?href="(.+?)">(.+?)</a>.+?class="year">(.+?)</span>', re.DOTALL).findall(html)
            for tv_url, tv_title, tv_year in tv_scrape:
                if cleantitle.get(tvshowtitle) == cleantitle.get(tv_title):
                    if year in str(tv_year):
                        return tv_url
            return
        except Exception:
            log_utils.log('Testing Exception', 1)
            return


    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            if not url:
                return
            url = url[:-1]
            url = url.replace('/series/', '/episodes/')
            url = url + '-%sx%s/' % (season, episode)
            return url
        except Exception:
            log_utils.log('Testing Exception', 1)
            return


    def sources(self, url, hostDict, hostprDict):
        try:
            hostDict = hostprDict + hostDict
            sources = []
            if url is None:
                return sources
            log_utils.log('Addon Testing sources starting url: \n' + repr(url))
            html = ensure_text(self.session.get(url, headers=self.session.headers).content, errors='replace')
            results = re.compile("data-type='(.+?)' data-post='(.+?)' data-nume='(\d+)'>", re.DOTALL).findall(html)
            for data_type, data_post, data_nume in results:
                customheaders = {
                    'Host': self.domains[0],
                    'Accept': '*/*',
                    'Origin': self.base_link,
                    'X-Requested-With': 'XMLHttpRequest',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
                    'Referer': url,
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'en-US,en;q=0.9'
                }
                post_link = self.base_link + self.ajax_link
                payload = {'action': 'doo_player_ajax', 'post': data_post, 'nume': data_nume, 'type': data_type}
                r = self.session.post(post_link, headers=customheaders, data=payload)
                i = ensure_text(r.content, errors='replace')
                p = re.compile('<iframe.+?src="(.+?)"', re.DOTALL).findall(i.replace('\\', ''))
                for url in p:
                    url =  "https:" + url if not url.startswith('http') else url
                    log_utils.log('Addon Testing sources url: \n' + repr(url))
                    quality, info = source_utils.get_release_quality(url, url)
                    valid, host = source_utils.is_host_valid(url, hostDict)
                    sources.append({'source': host, 'quality': quality, 'language': 'en', 'url': url, 'info': info, 'direct': False, 'debridonly': False})
            return sources
        except Exception:
            log_utils.log('Testing Exception', 1)
            return sources


    def resolve(self, url):
        return url



"""

'https://hlspanel2.xyz/player/index.php?data=10c91cbec1b70835824b898ef16a0de7&p=1'
# needs work still to resolve. think its hls from a jwplayer

"""






