from appscript import *
import appscript
from datetime import datetime
import Session
import popup
from Session import Session
import csv
import os

def tab_finder(user):
    browsed = [] #used to debug
    if appscript.app("Google Chrome").isrunning():
        visits = 0
        previous = ''
        while appscript.app("Google Chrome").isrunning():
            try:
                active = (appscript.app("Google Chrome").windows[1].active_tab()).URL()
                url = active.split("/")[2]
                if visits == 0:
                    previous = url
                else:
                    #checks if tab changed
                    if previous != url:
                        browsed.append(url)
                        previous = url
                        print(previous)
                        #check if url is new
                        if ("Profiles" not in os.getcwd()):
                            os.chdir('Profiles')
                        print(popup.exists(url,"{}-web.csv".format(user.profileName)))
                        if popup.exists(url,"{}-web.csv".format(user.profileName)) == False:
                            popup.pop(url,"{}-web.csv".format(user.profileName))
                        #check if productive or not
                        with open("{}-web.csv".format(user.profileName)) as c:
                            reader = csv.reader(c,delimiter=',')
                            for row in reader:
                                print(row)
                                if len(row) != 0:
                                    if url in row[0]:
                                        if row[1] == 'F':
                                            user.checkProductivity(False)
                                        else:
                                            user.checkProductivity(True)
                                            
                        

                visits += 1
                test.tick()
            except:
                break


tab_finder(test)
