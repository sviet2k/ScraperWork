
### This is a quick tool to make cleaning the addon "on the fly" easier lol.
## Got the idea from host505's Clear Providers quick option (cm).
## Then simply took the trakt manager def and ripped it down.
## Then tossed together a little of that with a bit of the code in the addDirectoryItem def,
## And my cleantools def to end up with this simple and quick "widget" to be lazy :D


## Simple code to toss into places like def addDirectoryItem in navigator.py
#cm.append(('[B]Clean Tools Widget[/B]', 'RunPlugin(%s?action=cleanToolsWidget)' % sysaddon))
### Heres A Bonus Idea for your navigator.py too :)
### Lazy way to clear up a little space when ya dont wanna see the changeLog option as a normal menu item.
##cm.append(('[B]View Change Log[/B]', 'RunPlugin(%s?action=changeLog)' % sysaddon))


## Simple code to toss into your main.py
#elif action == 'cleanToolsWidget': navigator.navigator().cleantools_widget()


## Simple code to toss into your navigator.py
# Recode it to match your clean tools def and your done.
"""

    def cleantools_widget(self):
        try:
            items = [('[B]Clear All Cache[/B]', 'clearAllCache')] # Item 0 (aka 1st).
            items += [('[B]Clear Providers[/B]', 'clearSources')] # Item 1 (aka 2nd).
            items += [('[B]Clear Meta Cache[/B]', 'clearMetaCache')] # Item 2 (aka 3rd).
            items += [('[B]Clear Cache[/B]', 'clearCache')] # Item 3 (aka 4th).
            items += [('[B]Clear ResolveURL Cache[/B]', 'clearResolveURLcache')] # Item 4 (aka 5th).
            items += [('[B]Clear Search History[/B]', 'clearCacheSearch')] # Item 5 (aka 6th).
            items += [('[B]Clean Old Settings[/B]', 'cleanSettings')] # Item 6 (aka 7th).
            select = control.selectDialog([i[0] for i in items], 'Cleaning Tools') # Item names and "widget" title.
            if select == -1: # Backing out or hitting cancel (aka X).
                return # Does nothing but closes "widget".
            else: # Meaning any option besides a cancel.
                control.execute('RunPlugin(%s?action=%s)' % (sysaddon, items[select][1])) # Runs whatever option you picked.
        except:
            return

"""


