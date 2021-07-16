# -*- coding: utf-8 -*-
# --[scrape v1.0]--|--[From JewBMX]--
# Lazy Module to make life a little easier.

"""
from resources.lib.modules import scrape
session = scrape.Session()
url = 'https://fbi.gov'
page = scrape.Request(url, self.session)
testit = page.content
"""


import requests
from six import ensure_text
from six.moves.urllib_parse import urlparse
from resources.lib.modules import log_utils

UserAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'


def Session(customHeaders={}):
    try:
        session = requests.Session()
        session.headers.update(
            {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'User-Agent': customHeaders['User-Agent'] if 'User-Agent' in customHeaders else UserAgent,
                'Accept-Language': 'en-US,en;q=0.5',
                'Referer': customHeaders['Referer'] if 'Referer' in customHeaders else 'https://fbi.gov',
                'DNT': '1'
            }
        )
        if 'cookies' in customHeaders:
            session.cookies.update(customHeaders['cookies'])
        return session
    except:
        log_utils.log('Scrape - Exception', 1)
        return None


def Request(url, session, referer=None, post=None, ajax=None):
    try:
        if referer:
            session.headers.update({'Referer': referer})
        else:
            elements = urlparse(url)
            base = '%s://%s' % (elements.scheme, (elements.netloc or elements.path))
            session.headers.update({'Referer': base})
        if ajax: # Updates the session headers.
            oldAccept = session.headers['Accept']
            session.headers.update({'Accept': 'application/json, text/javascript, */*; q=0.01', 'X-Requested-With': 'XMLHttpRequest'})
        if post:
            r = session.post(url, data=post, timeout=8)
        else:
            r = session.get(url, timeout=8)
        if ajax: # Restores the session headers.
            session.headers['Accept'] = oldAccept
            del session.headers['X-Requested-With']
        return r
    except:
        log_utils.log('Scrape - Exception', 1)
        return type('FailedResponse', (object,), {'ok': False})


def Data(url, session):
    try:
        r = Request(url, session, ajax=True)
        if r.ok:
            return {'url': r.url, 'User-Agent': session.headers['User-Agent'], 'Referer': session.headers['Referer'], 'cookies': session.cookies.get_dict()}
        else: # No results found.
            return None
    except:
        log_utils.log('Scrape - Exception', 1)
        return None


################################################################################
################################################################################
################################################################################


## Random Code Idea Saved Here But Not Actually Part Of The Module.


def scrapePage(url, referer=None, ensure=False, post=None):
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
            if post:
                page = session.post(url, data=post)
            else:
                page = session.get(url)
            if ensure:
                page = ensure_text(page, errors='replace')
        return page
    except Exception:
        log_utils.log('Testing Exception', 1)
        return []


################################################################################
################################################################################
################################################################################


## Random Code Use Examples Saved Here But Not Actually Part Of The Module.


def ExampleBasic(url):
    try: # Basic Use Example.
        session = Session()
        r = Request(url, session)
        log_utils.log('Scrape - ExampleBasic - Request: \n' + repr(r))
        if not r.ok:
            log_utils.log('Scrape - ExampleBasic - Failed:  %s' % url)
            return None
        log_utils.log('Scrape - ExampleBasic - Worked:  ' + repr(r.url))
        return r 
    except:
        log_utils.log('Scrape - Exception', 1)
        return None


def ExampleData(url):
    try: # Basic Use Example Using Data.
        data = Data(url, Session())
        log_utils.log('Scrape - ExampleData - Data: \n' + repr(data))
        session = Session(data)
        r = Request(data['url'], session)
        log_utils.log('Scrape - ExampleData - Request: \n' + repr(r))
        if not r.ok:
            log_utils.log('Scrape - ExampleData - Failed:  %s' % url)
            return None
        log_utils.log('Scrape - ExampleData - Worked:  ' + repr(data['url']))
        return r 
    except:
        log_utils.log('Scrape - Exception', 1)
        return None


def ExampleData2(url):
    try: # Another Basic Use Example Using Data.
        session = Session()
        data = Data(url, session)
        log_utils.log('Scrape - ExampleData2 - Data: \n' + repr(data))
        r = Request(data['url'], session)
        log_utils.log('Scrape - ExampleData2 - Request: \n' + repr(r))
        if not r.ok:
            log_utils.log('Scrape - ExampleData2 - Failed:  %s' % url)
            return None
        log_utils.log('Scrape - ExampleData2 - Worked:  ' + repr(data['url']))
        return r 
    except:
        log_utils.log('Scrape - Exception', 1)
        return None


"""


# More Random Examples :

        #r = Request(url, session, post=None, referer=None, ajax=None)
        #r = Request(data['url'], session, post=None, referer=None, ajax=None)

        session = Session(data)
        r = Request(data['url'], session)
        if not r.ok:
            return None

        #htmlContent = r.json().get('src', None)
        htmlContent = r.content
        dataIndex = htmlContent.rfind(b'var movie =')

        session.cookies['view-' + str(id)] = 'true'
        session.headers['Referer'] = data['url'].replace('.html', '/watching.html')

        data = Data(url, Session())
        r = Request(data['url'], session, post=None, ajax=True)
        if not r.ok:
            return None

        User-Agent = data['User-Agent']
        referer = session.headers['Referer']
        cookies = session.cookies.get_dict()

        directHeaders = '|User-Agent=' + quote_plus(User-Agent) + '&Referer=' + quote_plus(referer)

        r = Request(url, session, post=None, ajax=True)
        for result in r.json()['playlist'][0]['sources']:
            yield {'quality': result['label'], 'url': result['file']}



"""

