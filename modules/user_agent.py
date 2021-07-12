# -*- coding: utf-8 -*-
# --[user_agent v1.0]--|--[From JewBMX]--
# Lazy Module to make life a little easier.

"""
from resources.lib.modules import user_agent
testit = user_agent.myAgent()
"""


import random


###########################################################################################
###########################################################################################
###########################################################################################


def VLC():
    return 'VLC/2.2.0 LibVLC/2.2.0'


def PY_Requests():
    return 'python-requests/2.22.0'


def PY_URLLIB_2():
    return 'Python-urllib/2.7'


def PY_URLLIB_3():
    return 'Python-urllib/3.6'


def myAgent(): # My Dev LapTops User-Agent.
    return 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'


def myMobileAgent(): # My Dev Cell Phones User-Agent.
    return 'Mozilla/5.0 (Android 10; Mobile; rv:83.0) Gecko/83.0 Firefox/83.0'


def agent():
    return 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0'


def mobile_agent():
    return 'Mozilla/5.0 (Android 4.4.4; Mobile; rv:64.0) Gecko/64.0 Firefox/64.0'


def ios_agent():
    return 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'


def randomagent():
    _agents = [
       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063',
       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
       'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991',
       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7',
       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0',
       'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
       'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    ]
    return random.choice(_agents)


def randommobileagent(mobile):
    _mobagents = [
        'Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; F5121 Build/34.0.A.1.247) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.1.944 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-N920C Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.2 Chrome/56.0.2924.87 Mobile Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (iPad; CPU OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1'
    ]
    if mobile == 'android':
        return random.choice(_mobagents[:3])
    else:
        return random.choice(_mobagents[3:5])


###########################################################################################
###########################################################################################
###########################################################################################


# Windows User Agents
def Windows_10_Firefox():
    return 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'

def Windows_Firefox():
    return 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'

def Windows_10_Chrome():
    return 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3835.0 Safari/537.36'

def Windows_7_Chrome():
    return 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'

def Windows_10_Edge():
    return 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'

def Windows_Edge():
    return 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'

def Windows_IE_6():
    return 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)'

def Windows_IE_7():
    return 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; Trident/4.0; SLCC1)'

def Windows_IE_8():
    return 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; WOW64; Trident/4.0; SLCC1)'

def Windows_IE_9():
    return 'Mozilla/5.0 (MSIE 9.0; Windows NT 6.1; Trident/5.0)'

def Windows_IE_11():
    return 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'


###########################################################################################
###########################################################################################
###########################################################################################


# Chrome OS User Agents
def Chrome_OS():
    return 'Mozilla/5.0 (X11; CrOS x86_64 12239.19.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.38 Safari/537.36'

def Chrome_OS_Chrome():
    return 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'


###########################################################################################
###########################################################################################
###########################################################################################


# Mac User Agents
def Mac_Firefox():
    return 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0'

def Mac_OS_Firefox():
    return 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0'

def Mac_Safari():
    return 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15'

def Mac_OS_Safari():
    return 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'


###########################################################################################
###########################################################################################
###########################################################################################


# Linux User Agents
def Linux_Firefox():
    return 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'

def Linux_Chrome():
    return 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'

def Linux_Opera():
    return 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41'

def Linux_Vivaldi():
    return 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.99 Safari/537.36 Vivaldi/2.9.1705.41'


###########################################################################################
###########################################################################################
###########################################################################################


# Android WebView User Agents
def WebView_Old():
    return 'Mozilla/5.0 (Linux; U; Android 4.1.1; en-gb; Build/KLP) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30'

def WebView_KitKat2LolliPop():
    return 'Mozilla/5.0 (Linux; Android 4.4; Nexus 5 Build/_BuildID_) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36'

def WebView_LollipopAndAbove():
    return 'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36'


###########################################################################################
###########################################################################################
###########################################################################################


# Android Mobile User Agents
def Android():
    return 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36'

def Galaxy_S9():
    return 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'

def Galaxy_S8():
    return 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36'

def Galaxy_S7():
    return 'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36'

def Galaxy_S7_Edge():
    return 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36'

def Galaxy_S6():
    return 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36'

def Galaxy_S6_Edge_Plus():
    return 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36'

def Galaxy_Nexus_Chrome():
    return 'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19'

def Nexus_6P():
    return 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36'

def Sony_Xperia_XZ():
    return 'Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36'

def Sony_Xperia_Z5():
    return 'Mozilla/5.0 (Linux; Android 6.0.1; E6653 Build/32.2.A.0.253) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36'

def HTC_One_X10():
    return 'Mozilla/5.0 (Linux; Android 6.0; HTC One X10 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36'

def HTC_One_M9():
    return 'Mozilla/5.0 (Linux; Android 6.0; HTC One M9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.3'


###########################################################################################
###########################################################################################
###########################################################################################


# iPhone User Agents
def iPhone():
    return 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'

def iPhone_Safari():
    return 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1'

def iPhone_XR_Safari():
    return 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'

def iPhone_XS_Chrome():
    return 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1'

def iPhone_XS_Max_Firefox():
    return 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/13.2b11866 Mobile/16A366 Safari/605.1.15'

def iPhone_X():
    return 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'

def iPhone_6():
    return 'Mozilla/5.0 (Apple-iPhone7C2/1202.466; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543 Safari/419.3'

def iPhone_7():
    return 'Mozilla/5.0 (iPhone9,3; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1'

def iPhone_7_Plus():
    return 'Mozilla/5.0 (iPhone9,4; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1'

def iPhone_8():
    return 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'

def iPhone_8_Plus():
    return 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A5370a Safari/604.1'

def iPhone_Chrome_iOS_10_3():
    return 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'

def iPhone_Chrome_2Desktop_View_macOS():
    return 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/85 Version/11.1.1 Safari/605.1.15'

def iPhone_Safari_iOS_10_3():
    return 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'

def iPhone_Safari_2Desktop_View_Mac_OS_X():
    return 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12'


###########################################################################################
###########################################################################################
###########################################################################################


# MS Windows Phone User Agents
def Microsoft_Lumia_650():
    return 'Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254'

def Microsoft_Lumia_550():
    return 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536'

def Microsoft_Lumia_950():
    return 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058'

def Windows_Phone_Internet_Explorer():
    return 'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)'


###########################################################################################
###########################################################################################
###########################################################################################


# Tablet User Agents
def Amazon_Kindle_Fire_HDX_7():
    return 'Mozilla/5.0 (Linux; Android 4.4.3; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/47.1.79 like Chrome/47.0.2526.80 Safari/537.36'

def Google_Pixel_C_Tablet():
    return 'Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36'

def Ipad():
    return 'Mozilla/5.0 (iPad; CPU OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Tablet/15E148 Safari/604.1'

def LG_G_Pad_7():
    return 'Mozilla/5.0 (Linux; Android 5.0.2; LG-V410/V41020c Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/34.0.1847.118 Safari/537.36'

def Nvidia_Shield_Tablet_K1():
    return 'Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36'

def Samsung_Galaxy_Tab_S3():
    return 'Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36'

def Samsung_Galaxy_Tab_A():
    return 'Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36'

def Sony_Xperia_Z4_Tablet():
    return 'Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36'


###########################################################################################
###########################################################################################
###########################################################################################


# Some Popular Box User Agents
def Amazon_4K_Fire_TV():
    return 'Mozilla/5.0 (Linux; Android 5.1; AFTS Build/LMY47O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.99900.2250.0242 Safari/537.36'

def Apple_TV_5th_Gen_4K():
    return 'AppleTV6,2/11.1'

def Apple_TV_4th_Gen():
    return 'AppleTV5,3/9.1.1'

def Chromecast():
    return 'Mozilla/5.0 (CrKey armv7l 1.5.16041) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.0 Safari/537.36'

def Google_Nexus_Player():
    return 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)'

def Minix_NEO_X5():
    return 'Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30'

def Roku_Ultra():
    return 'Roku4640X/DVP-7.70 (297.70E04154A)'


###########################################################################################
###########################################################################################
###########################################################################################


# Xbox One User Agents
def XboxOneAgent():
    return 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586'


def XboxOneSAgent():
    return 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; XBOX_ONE_ED) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'


def randomXboxOneAgent():
    _agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17133',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19041'
    ]
    return random.choice(_agents)



####################################################################################
####################################################################################
####################################################################################


# Playstation 3 User Agents
def Playstation3Agent():
    return 'Mozilla/5.0 (PLAYSTATION 3; 4.50) AppleWebKit/531.22.8 (KHTML, like Gecko)'


def randomPlayStation3Agent():
    _agents = [
        'Mozilla/5.0 (PLAYSTATION 3 4.81) AppleWebKit/531.22.8 (KHTML, like Gecko)',
        'Mozilla/5.0 (PLAYSTATION 3 4.82) AppleWebKit/531.22.8 (KHTML, like Gecko)',
        'Mozilla/5.0 (PLAYSTATION 3; 4.55) AppleWebKit/531.22.8 (KHTML, like Gecko)',
        'Mozilla/5.0 (PLAYSTATION 3; 4.60) AppleWebKit/531.22.8 (KHTML, like Gecko)',
        'Mozilla/5.0 (PLAYSTATION 3; 4.66) AppleWebKit/531.22.8 (KHTML, like Gecko)'
    ]
    return random.choice(_agents)



####################################################################################
####################################################################################
####################################################################################


# Playstation 4 User Agents
def Playstation4Agent():
    return 'Mozilla/5.0 (PlayStation 4 3.11) AppleWebKit/537.73 (KHTML, like Gecko)'


def randomPlayStation4Agent():
    _agents = [
        'Mozilla/5.0 (PlayStation 4 2.00) AppleWebKit/537.73 (KHTML, like Gecko)',
        'Mozilla/5.0 (PlayStation 4 2.02) AppleWebKit/537.73 (KHTML, like Gecko)',
        'Mozilla/5.0 (PlayStation 4 2.04) AppleWebKit/537.73 (KHTML, like Gecko)',
        'Mozilla/5.0 (PlayStation 4 2.50) AppleWebKit/537.73 (KHTML, like Gecko)',
        'Mozilla/5.0 (PlayStation 4 3.15) AppleWebKit/537.73 (KHTML, like Gecko)',
        'Mozilla/5.0 (PlayStation 4 3.50) AppleWebKit/537.78 (KHTML, like Gecko)',
        'Mozilla/5.0 (PlayStation 4 3.55) AppleWebKit/537.78 (KHTML, like Gecko)',
        'Mozilla/5.0 (PlayStation 4 4.71) AppleWebKit/601.2 (KHTML, like Gecko)',
        'Mozilla/5.0 (PlayStation 4 4.73) AppleWebKit/601.2 (KHTML, like Gecko)',
        'Mozilla/5.0 (PlayStation 4 4.74) AppleWebKit/601.2 (KHTML, like Gecko)',
        'Mozilla/5.0 (PlayStation 4 5.00) AppleWebKit/601.2 (KHTML, like Gecko)',
        'Mozilla/5.0 (PlayStation 4 5.01) AppleWebKit/601.2 (KHTML, like Gecko)',
        'Mozilla/5.0 (PlayStation 4 5.03) AppleWebKit/601.2 (KHTML, like Gecko)',
        'Mozilla/5.0 (PlayStation 4 5.05) AppleWebKit/601.2 (KHTML, like Gecko)',
        'Mozilla/5.0 (PlayStation 4 5.50) AppleWebKit/601.2 (KHTML, like Gecko)',
        'Mozilla/5.0 (PlayStation 4 5.55) AppleWebKit/601.2 (KHTML, like Gecko)',
        'Mozilla/5.0 (PlayStation 4 6.00) AppleWebKit/605.1.15 (KHTML, like Gecko)',
        'Mozilla/5.0 (PlayStation 4 6.72) AppleWebKit/605.1.15 (KHTML, like Gecko)',
        'Mozilla/5.0 (PlayStation 4 7.00) AppleWebKit/605.1.15 (KHTML, like Gecko)',
        'Mozilla/5.0 (PlayStation 4 7.02) AppleWebKit/605.1.15 (KHTML, like Gecko)',
        'Mozilla/5.0 (PlayStation 4 7.50) AppleWebKit/605.1.15 (KHTML, like Gecko)',
        'Mozilla/5.0 (PlayStation 4 7.51) AppleWebKit/605.1.15 (KHTML, like Gecko)'
    ]
    return random.choice(_agents)


####################################################################################
####################################################################################
####################################################################################


