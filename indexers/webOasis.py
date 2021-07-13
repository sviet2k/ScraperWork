# -*- coding: utf-8 -*-
# -Created By Tempest, Modified By JewBMX-

"""

elif action == 'radioNavigator':
    from resources.lib.indexers import webOasis
    webOasis.radio().root()

elif action == 'iptvNavigator':
    from resources.lib.indexers import webOasis
    webOasis.iptv().root()

elif action == 'webOasisPlay':
    from resources.lib.indexers import webOasis
    webOasis.play(url)

"""

import re
import sys
import requests

from six import ensure_text
from six.moves.urllib_parse import urlparse, quote_plus

from resources.lib.modules import control
from resources.lib.modules import log_utils


class radio:
    def __init__(self):
        self.list = []
        self.base_link = 'http://streamwat.ch/radio'


    def root(self):
        try:
            page = scrapePage(self.base_link, referer=self.base_link)
            channels = re.findall('<li data-title="(.+?)" data-type="(.+?)" data-url="(.+?)"></li>', page)
            for title, type, url in channels:
                label = '[COLOR magenta][B]%s[/B][/COLOR] | [I]%s[/I]' % (title, type)
                #url =  "https:" + url if not url.startswith('http') else url
                self.list.append({'title': label, 'url': url, 'image': 'DefaultAudio.png', 'action': 'webOasisPlay'})
            addDirectory(self.list)
            return self.list
        except:
            log_utils.log('WebOasis Exception', 1)
            return


class iptv:
    def __init__(self):
        self.list = []
        self.base_link = 'http://streamwat.ch/'


    def root(self):
        try:
            page = scrapePage(self.base_link, referer=self.base_link)
            channels = re.findall('<a href="(.+?)">.+?<img src="(.+?)" alt="(.+?)"></picture></div></a>', page)
            for link, jpg, title in channels:
                if any(x in link for x in ['radio', 'custom']):
                    continue
                label = '[COLOR magenta][B]%s[/B][/COLOR]' % title
                url =  self.base_link + link
                image = self.base_link + jpg
                self.list.append({'title': label, 'url': url, 'image': image, 'action': 'webOasisPlay'})
            addDirectory(self.list)
            return self.list
        except:
            log_utils.log('WebOasis Exception', 1)
            return


    def resolve(self, url):
        try:
            link =  url + 'player.min.js' if url.endswith('/') else url + '/player.min.js'
            page = scrapePage(link, referer=self.base_link)
            link = re.findall('playM3u8\("(.+?)"\)', page)[0]
            return link
        except:
            log_utils.log('WebOasis Exception', 1)
            return


def play(url):
    try:
        if 'http://streamwat.ch/' in url:
            link = iptv().resolve(url)
        else:
            link = url
        control.execute('PlayMedia(%s)' % link)
    except:
        log_utils.log('WebOasis Exception', 1)
        return


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
        log_utils.log('WebOasis Exception', 1)
        return []


def addDirectory(items, queue=False, isFolder=True):
    if items == None or len(items) == 0:
        control.idle()
        sys.exit()
    sysaddon = sys.argv[0]
    syshandle = int(sys.argv[1])
    addonFanart = control.addonFanart()
    for i in items:
        try:
            url = '%s?action=%s&url=%s' % (sysaddon, i['action'], i['url'])
            title = i['title']
            thumb = i['image'] or 'DefaultAudio.png'
            item = control.item(label=title)
            item.setProperty('IsPlayable', 'true')
            item.setInfo("mediatype", "video")
            item.setInfo("audio", '')
            item.setArt({'icon': thumb, 'thumb': thumb, 'fanart': addonFanart})
            control.addItem(handle=syshandle, url=url, listitem=item, isFolder=isFolder)
        except Exception:
            log_utils.log('WebOasis Exception', 1)
            pass
    control.content(syshandle, 'addons')
    control.directory(syshandle, cacheToDisc=True)


