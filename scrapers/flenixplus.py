# -*- coding: UTF-8 -*-
# Needs sources scraped further.

import re
from six import ensure_text

from oathscrapers.modules import client
from oathscrapers.modules import source_utils
from oathscrapers.modules import log_utils


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['flenix.plus']
        self.base_link = 'https://flenix.plus'
        self.search_link = '/index.php?do=search&filter=true'


    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            search_url = self.base_link + self.search_link
            post = ('do=search&subaction=search&search_start=0&full_search=0&result_from=1&story=%s' % (imdb))
            page = ensure_text(client.request(search_url, post=post), errors='replace')
            item = client.parseDOM(page, 'div', attrs={'class': 'post'})[0]
            path = re.compile('<a href="https://flenix.plus(.+?)"', re.DOTALL).findall(item)[0]
            url = self.base_link + path
            return url
        except Exception:
            log_utils.log('Testing Exception', 1)
            return


    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []
            if url == None:
                return sources
            log_utils.log('Addon Testing sources starting url: \n' + repr(url))
            html = ensure_text(client.request(url), errors='replace')
            links = client.parseDOM(html, 'iframe', ret='src')
            for link in links:
                link = link.replace(' ', '')
                link = "https:" + link if not link.startswith('http') else link
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



"""



https://dbgo.fun/ads.php?id=tt3758814
https://dbgo.fun/ads.php?id=tt5562070

https://api.hdv.fun/embed/tt3758814
https://api.hdv.fun/embed/tt5562070

https://123files.club/imdb/play/?id=tt3758814
https://123files.club/imdb/play/?id=tt5562070

https://database.gdriveplayer.us/player.php?imdb=tt3758814
https://database.gdriveplayer.us/player.php?imdb=tt5562070

https://gomostream.com/movie/tt3758814
https://gomostream.com/movie/tt5562070

https://consistent.stream/view/CMnX6EvG91HeSBPwrWUG/tt3758814/
https://consistent.stream/view/CMnX6EvG91HeSBPwrWUG/tt5562070/



"""


