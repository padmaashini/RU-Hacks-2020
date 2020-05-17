from appscript import *
import appscript
from datetime import datetime

#browsed = [] used to debug
if appscript.app("Google Chrome").isrunning():
    visits = 0
    previous = ''
    while appscript.app("Google Chrome").isrunning():
        try:
            active = (appscript.app("Google Chrome").windows[1].active_tab()).URL()
            url = active.split("/")[2]
##            if browsed == []:
##                browsed = [url]
##            if browsed[-1] != url:
##                browsed.append(url)
##                print(url)
            if visits == 0:
                previous = url
                print(previous)
            else:
                if previous != url:
                    #addNewWebsite(url)
                    previous = url
                    print(previous)
            visits += 1
        except:
            break

#test
#browsed = ['discord.com', 'stackoverflow.com', 'discord.com', 'stackoverflow.com', 'discord.com', 'stackoverflow.com', 'discord.com', 'stackoverflow.com', 'discord.com', 'stackoverflow.com', 'newtab', 'www.reddit.com', 'www.facebook.com', 'www.youtube.com', 'motorsport.com', 'www.motorsport.com', 'us.motorsport.com']
#debug
##if len(browsed) > 0:
##    print("browsed: ")
##    for x in browsed:
##        print(x,end='\n')

