import datetime
import csv
import os.path
import tkinter as tk
from tkinter import ttk

class Session:
    def __init__(self, name, profileName):

        self.name = name
        self.timeStarted = datetime.datetime.now()
        self.timeEnded = None

        self.beingProductive = False
        self.secondsProductive = 0
        self.secondsLazy = 0

        #A DICTIONARY variable that receives the website and whether it is productive or not
        #Key - website, value - productive/unproductive (boolean, T/F)
        self.newWebsites = {}

        # The name of the profile associated with this session
        self.profileName = profileName

    def end(self):
        self.timeEnded = datetime.datetime.now()
        self.save()

    def checkProductivity(self, isProductive):
        # called with whether current active tab is productive or not
        # called every time active tab switches
        if isProductive:
            self.beingProductive = True
        else:
            self.beingProductive = False

    def tick(self):
        # called every second
        if self.beingProductive:
            self.secondsProductive = self.secondsProductive + 1
        else:
            self.secondsLazy = self.secondsLazy + 1

    def save(self):
        file_to_open = os.path.join("RUHACKS-2020-PROJECT", "Profiles", (self.profileName + ".csv"))
        with open(file_to_open, 'w') as csv_file:
            csv_writer = csv.writer()
            csv_writer.writerow(self.name, self.timeStarted, self.timeEnded, self.secondsProductive, self.secondsLazy, len(self.newWebsites))

    def addNewWebsite(self, website):
        #stub


















