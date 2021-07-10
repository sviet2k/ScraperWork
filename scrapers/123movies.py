# -*- coding: utf-8 -*-

import re
import random
import base64

import simplejson as json
from six import ensure_text
from oathscrapers import parse_qs, urlencode, quote_plus, unquote

from oathscrapers.modules import client
from oathscrapers.modules import cleantitle
from oathscrapers.modules import directstream
from oathscrapers.modules import source_utils
from oathscrapers.modules import log_utils


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['123movies.sc']
        self.base_link = 'https://123movies.sc'
        self.search_link = '/search/%s.html'


    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            query = self.base_link + self.search_link % quote_plus(title)
            check = cleantitle.get(title)
            r = ensure_text(client.request(query), errors='replace')
            r = client.parseDOM(r, 'div', attrs={'class': 'ml-item'})
            r = [(client.parseDOM(i, 'a', ret='href'), client.parseDOM(i, 'a', ret='title'), re.findall('(\d{4})', i)) for i in r]
            r = [(i[0][0], i[1][0], i[2][0]) for i in r if len(i[0]) > 0 and len(i[1]) > 0 and len(i[2]) > 0]
            url = [i[0] for i in r if check == cleantitle.get(i[1]) and year == i[2]][0]
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
            query = self.base_link + self.search_link % quote_plus(data['tvshowtitle'])
            check = cleantitle.get(data['tvshowtitle'])
            r = ensure_text(client.request(query), errors='replace')
            r = client.parseDOM(r, 'div', attrs={'class': 'ml-item'})
            r = [(client.parseDOM(i, 'a', ret='href'), client.parseDOM(i, 'a', ret='title'), re.findall('(\d{4})', i)) for i in r]
            r = [(i[0][0], i[1][0], i[2][0]) for i in r if len(i[0]) > 0 and len(i[1]) > 0 and len(i[2]) > 0]
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
            try:
                url, episode = re.findall('(.+?)\?episode=(\d*)$', url)[0]
            except:
                episode = None
            ref = url
            log_utils.log('Addon Testing sources starting url: \n' + repr(url))
            result = ensure_text(client.request(url), errors='replace')
            if not episode == None:
                result = client.parseDOM(result, 'div', attrs={'id': 'ip_episode'})[0]
                ep_url = client.parseDOM(result, 'a', attrs={'data-name': str(episode)}, ret='href')[0]
                result = ensure_text(client.request(ep_url), errors='replace')
            r = client.parseDOM(result, 'div', attrs={'class': '[^"]*server_[^"]*'})
            for u in r:
                try:
                    url = self.base_link + '/ip.file/swf/plugins/ipplugins.php'
                    p1 = client.parseDOM(u, 'a', ret='data-film')[0]
                    p2 = client.parseDOM(u, 'a', ret='data-server')[0]
                    p3 = client.parseDOM(u, 'a', ret='data-name')[0]
                    post = {'ipplugins': 1, 'ip_film': p1, 'ip_server': p2, 'ip_name': p3, 'fix': "0"}
                    post = urlencode(post)
                    for i in range(3):
                        result = ensure_text(client.request(url, post=post, XHR=True, referer=ref, timeout='10'), errors='replace')
                        if not result == None:
                            break
                    result = json.loads(result)
                    u = result['s']
                    try:
                        s = result['v']
                    except:
                        s = result['c']
                    url = self.base_link + '/ip.file/swf/ipplayer/ipplayer.php'
                    for n in range(3):
                        try:
                            post = {'u': u, 'w': '100%', 'h': '420', 's': s, 'n': n}
                            post = urlencode(post)
                            result = ensure_text(client.request(url, post=post, XHR=True, referer=ref), errors='replace')
                            src = json.loads(result)['data']
                            if not src:
                                continue
                            if type(src) is list:
                                src = [i['files'] for i in src]
                                for i in src:
                                    try:
                                        sources.append({'source': 'gvideo', 'quality': directstream.googletag(i)[0]['quality'], 'language': 'en', 'url': i, 'direct': True, 'debridonly': False})
                                    except:
                                        log_utils.log('Testing Exception', 1)
                                        pass
                            else:
                                link = "https:" + src if not src.startswith('http') else src
                                if 'tunestream.net' in link:
                                    for source in self.tunestream(link, hostDict):
                                        sources.append(source)
                                else:
                                    log_utils.log('Addon Testing sources src link: \n' + repr(link))
                                    valid, host = source_utils.is_host_valid(link, hostDict)
                                    sources.append({'source': host, 'quality': 'HD', 'language': 'en', 'url': link, 'direct': False, 'debridonly': False})
                        except:
                            log_utils.log('Testing Exception', 1)
                            pass
                except:
                    log_utils.log('Testing Exception', 1)
                    pass
            return sources
        except Exception:
            log_utils.log('Testing Exception', 1)
            return sources


# UnUsed Result, Needs Coded.
# 'https://waaw.tv/watch_video.php?v=e78cLgr5c392'


    def resolve(self, url):
        if 'google' in url:
            url = directstream.googlepass(url)
        return url


    def tunestream(self, url, hostDict):
        sources = [] # 'https://tunestream.net/embed-f1m4uqrfm987.html'
        try:
            header = {'User-Agent': client.agent(), 'Referer': 'https://tunestream.net'}
            page = ensure_text(client.request(url, headers=header), errors='replace')
            results = re.compile('sources\s*:\s*\[(.+?)\]').findall(page)[0]
            items = re.findall(r'''{(.+?)}''', results)
            for item in items:
                try:
                    link = re.findall(r'''file:"(.+?)"''', item)[0]
                    label = re.findall(r'''label:"(.+?)"''', item)[0]
                except:
                    link = re.findall(r'''file:"(.+?)"''', item)[0]
                    label = 'SD'
                valid, host = source_utils.is_host_valid(link, hostDict)
                quality, info = source_utils.get_release_quality(label, link)
                log_utils.log('Addon Testing tunestream src link: \n' + repr(link))
                link += '|%s' % urlencode(header)
                sources.append({'source': host, 'quality': quality, 'language': 'en', 'info': info, 'url': link, 'direct': True, 'debridonly': False})
            return sources
        except Exception:
            log_utils.log('Testing Exception', 1)
            return sources



"""



https://123movies.sc/watch-the-tomorrow-war-2021-123movies.html

<div class="server_plugins">
    <a class="btn-server">Playing on <span class="playing-on"></span></a>
    <div id="servers-list" data-id="1">
        <ul id="ip_server">
            <li>
            <a class="server_6" data-film="28064" data-name="1" data-server="6" href="https://123movies.sc/watch-the-tomorrow-war-2021-123movies.html?p=1&s=6">Server VIP</a>
            </li>
            <li>
            <a class="server_15" data-film="28064" data-name="1" data-server="15" href="https://123movies.sc/watch-the-tomorrow-war-2021-123movies.html?p=1&s=15">Netu.TV</a>
            </li>
            <li>
            <a class="server_25" data-film="28064" data-name="1" data-server="25" href="https://123movies.sc/watch-the-tomorrow-war-2021-123movies.html?p=1&s=25">Fembed</a>
            </li>
        </ul>
    </div>
</div>


"""





