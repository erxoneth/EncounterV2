# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 00:56:30 2023

@author: mathagra
"""

import tkinter as tk
from tkinter import *
from tkinter import IntVar
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk
import time
import random
import os
import sys

from tkinter.filedialog import askopenfilename, asksaveasfilename

#Getting directory
directory = os.getcwd()
# os.environ["TCL_LIBRARY"] = "<PathToPython>\\Python\\Python36-32\\tcl\\tcl8.6"
# os.environ["TK_LIBRARY"] = "<PathToPython>\\Python\\Python36-32\\tcl\\tk8.6"

#Time Var
date = 1
ToDh = "12"
ToDm = "00"
timeString = f"{ToDh}"+":"+f"{ToDm}"
dayString = "Date: "+f"{date}"
#Journal Entries
entries = ["There is no entry as of yet"]
entriesStr =""
entryQ = 0
pageIndex = 1

#Weather Types        
def onWeather():
    availW = []
    weatherTypes = ['Clear','Rain','Snow','Windy','Wind and Rain','Acid Rain','Ashfall','Firestorm','Ghostlight','Hail','Thunderstorm','Blizzard','Heatwave','Monsoon','Coldfront']
    colorList = ['skyblue','cornflowerblue','snow','lightcyan','lightslategray','yellowgreen','lightslategray','orangered','palegreen','lightyellow','yellow','dodgerblue','tomato','mediumturquoise','cyan']
    textColor = ['white','darkblue','grey','black','white','darkolivegreen','white','yellow','blue','black','dimgrey','white','yellow','black','black']
    if wClear.get() == 1:
        availW.append("Clear")
    if wRain.get() ==1:
        availW.append("Rain")
    if wSnow.get() ==1:
        availW.append("Snow")
    if wWindy.get() ==1:
        availW.append("Windy")
    if wWindAndRain.get() ==1:
        availW.append("Wind and Rain")
    if wAcidRain.get() ==1:
        availW.append("Acid Rain")
    if wAshfall.get() ==1:
        availW.append("Ashfall")
    if wFirestorm.get() ==1:
        availW.append("Firestorm")
    if wGhostlight.get() ==1:
        availW.append("Ghostlight")
    if wHail.get() ==1:
        availW.append("Hail")
    if wThunderstorm.get() ==1:
        availW.append("Thunderstorm")
    if wBlizzard.get() ==1:
        availW.append("Blizzard")
    if wHeatwave.get() ==1:
        availW.append("Heatwave")
    if wMonsoon.get() ==1:
        availW.append("Monsoon")
    if wColdfront.get() ==1:
        availW.append("Coldfront")
    if len(availW)==0:
        disp_weather["text"] = "No Weather Selected"
    if disp_weather != "No Weather Selected":
        items = len(availW)
        choice = random.randint(0,items-1)
        index = f"{availW[choice]}"
        disp_weather["text"] = f"{availW[choice]}"
        for i in range(0,len(weatherTypes)):
            if weatherTypes[i] == index:
                disp_weather['bg'] = f"{colorList[i]}"
                disp_weather['fg'] = f"{textColor[i]}"
                break
        
    
    
    
    
#Adventure Var
currentAdv = ""

#Setting window
def openSettings():
    settingWindow = tk.Toplevel(window)
    settingWindow.title("Weather Settings")
    settingWindow.geometry("300x500")
    settingWindow.resizable(False,False)
    
    settingFrame = tk.Frame(settingWindow)
    settingFrame.grid(row=0,column=0)
    
    settingSplash = tk.Label(settingFrame,text="Weather Options",relief=tk.GROOVE,padx=10,pady=10)
    settingSplash.grid(row=0,column=0)
    
    #Weather Checks
    tk.Label(settingFrame,text="Default Weather",bg='blue',fg='white').grid(row=1,column=0,sticky="nesw")
    tk.Checkbutton(settingFrame,text="Clear",variable=wClear,onvalue=1,offvalue=0).grid(row=2,column=0,sticky="w")
    tk.Checkbutton(settingFrame,text="Rain",variable=wRain,onvalue=1,offvalue=0).grid(row=3,column=0,sticky="w")
    tk.Checkbutton(settingFrame,text="Snow",variable=wSnow,onvalue=1,offvalue=0).grid(row=4,column=0,sticky="w")
    tk.Checkbutton(settingFrame,text="Windy",variable=wWindy,onvalue=1,offvalue=0).grid(row=5,column=0,sticky="w")
    tk.Label(settingFrame,text="Extreme Weather",bg='red',fg='white').grid(row=6,column=0,sticky="nesw")
    tk.Checkbutton(settingFrame,text="Wind and Rain",variable=wWindAndRain,onvalue=1,offvalue=0).grid(row=7,column=0,sticky="w")
    tk.Checkbutton(settingFrame,text="Hail",variable=wHail,onvalue=1,offvalue=0).grid(row=8,column=0,sticky="w")
    tk.Checkbutton(settingFrame,text="Thunderstorm",variable=wThunderstorm,onvalue=1,offvalue=0).grid(row=9,column=0,sticky="w")
    tk.Checkbutton(settingFrame,text="Blizzard",variable=wBlizzard,onvalue=1,offvalue=0).grid(row=10,column=0,sticky="w")
    tk.Checkbutton(settingFrame,text="Heatwave",variable=wHeatwave,onvalue=1,offvalue=0).grid(row=11,column=0,sticky="w")
    tk.Checkbutton(settingFrame,text="Coldfront",variable=wColdfront,onvalue=1,offvalue=0).grid(row=12,column=0,sticky="w")
    tk.Checkbutton(settingFrame,text="Monsoon",variable=wMonsoon,onvalue=1,offvalue=0).grid(row=13,column=0,sticky="w")
    tk.Label(settingFrame,text="Unusual Weather",bg='orange',fg='white').grid(row=14,column=0,sticky="w")
    tk.Checkbutton(settingFrame,text="Firestorm",variable=wFirestorm,onvalue=1,offvalue=0).grid(row=15,column=0,sticky="w")
    tk.Checkbutton(settingFrame,text="Ashfall",variable=wAshfall,onvalue=1,offvalue=0).grid(row=16,column=0,sticky="w")
    tk.Checkbutton(settingFrame,text="Ghostlight",variable=wGhostlight,onvalue=1,offvalue=0).grid(row=17,column=0,sticky="w")
    tk.Checkbutton(settingFrame,text="Acid Rain",variable=wAcidRain,onvalue=1,offvalue=0).grid(row=18,column=0,sticky="w")      


#Compile Events
def compEvents():
    global entriesStr
    global entries
    global pageIndex
    totalPages = countPages()
    #calculate page quantity
    if len(entries) > 20*(totalPages):
        page_max_print = 20*(totalPages)
    else:
        page_max_print = len(entries)
    
    if pageIndex > 1:
        pageMulti = ((pageIndex-1)*20)
    # if entries[0] == "There is no entry as of yet":
    #     entriesStr = entries[0]
    #     return entriesStr
    else: 
        pageMulti = 0
    entriesStr = ""
    tempList = entries
    lessHolder = []
    moreHolder = []
    for i in range(pageMulti,len(entries)-1):
        j = str(entries[i])
        j1 = j.split(':')[0]
        k = j1.replace("Day ","")
        l = str(entries[i+1])
        l1 = l.split(':')[0]
        m = l1.replace("Day ","")
        kE = int(k)
        mE = int(m)
        if i==0:
            tempList[0]=j
     
        if kE > mE:
            moreHolder = entries[i]
            lessHolder = entries[i+1]
            tempList[i]=lessHolder
            tempList[i+1]=moreHolder
            
        #entries = tempList
            
    for i in range(pageMulti,page_max_print):
    #    # if i == 0:
    #    #     firstFix = str(entries[i])[2:-2]
    #     #    entriesStr = "{}\n".format(firstFix)
    #     #else:
         entriesStr += "{}\n".format(str(entries[i]))
    return entriesStr

def countPages():
    maxPage = 1
    count = len(entries)
    while count >= 19:
        tempCount = count-20
        count = tempCount
        maxPage += 1
    return maxPage

def pageUp():
    global pageIndex
    maxPage = countPages()
    if pageIndex < maxPage:
        pageIndex +=1


def pageDown():
    global pageIndex
    maxPage = countPages()
    if pageIndex <= maxPage and pageIndex > 1:
        pageIndex -=1
        

#Journal Window


def openJournal():

    def deleteEntries():
            
        global checkboxes
        global pageIndex
        global entries
        global Dindex
        global chkIndex
        chkIndex = len(entries)-1
        checkboxes = []
        
        def deleteSelected():
            global entries
            global Dindex
            global entryQ
            global chkIndex
            global checkboxes
            
            # print(checkboxes)
            # for i in reversed(range(len(entries),Dindex)):
            #### run a list of boxes
            if Dindex == 0:
                for i in reversed(range(0,len(checkboxes))):
                    if checkboxes[i].get() == 1:
                        del entries[i]
                        del checkboxes[i]
                        entryQ -= 1
                dWindow.destroy()
            else:
                for i in reversed(range(0,len(checkboxes))):
                    if checkboxes[i].get() == 1:
                        del entries[i+Dindex]
                        del checkboxes[i]
                        entryQ -= 1
                dWindow.destroy()
                    
        
        # 
        dateStr = dateHeader['text']
                    
        for i in range(0,len(entries)):
            #get the date
            print("date is {}".format(dateStr))
            j = dateStr
            j1 = j.split(':')[1]
            k = j1.replace(" ","")
            kE = int(k)
            q = str(entries[i])
            q1 = q.split(':')[0]
            q2 = q1.split('Day ')[1]
            qE = int(q2)
            if kE <= qE:
                Dindex = i
                break
        print("Dindex = : {}".format(Dindex))  
      
        dWindow = tk.Toplevel(jWindow)
        dWindow.title("Delete Journal Entries")
        dWindow.geometry("629x366")
        dWindow.configure(bg='salmon')
        dWindow.resizable(False,False)
        
        topFrame = tk.Frame(dWindow)
        topFrame.grid(row=0,column=0)
        topFrame.columnconfigure([0],minsize=450,weight=1)
        #topFrame sub frames
        # labelFrm = tk.Frame(topFrame,bg='green')
        # labelFrm.grid(row=0,column=0)
        # btnFrm = tk.Frame(topFrame,bg='red')
        # btnFrm.grid(row=0,column=1)
        #topFrame widgets
        title = tk.Label(topFrame,text="Journal Entries")
        title.grid(row=0,column=0,sticky='w',columnspan=2)
        dBtn = tk.Button(topFrame,text="Delete Selected",command=deleteSelected)
        dBtn.grid(row=0,column=1,sticky='w',columnspan=2)
        textFrame = tk.Frame(dWindow,bg='yellow')
        textFrame.grid(row=2,column=0,sticky='w')
        textFrame.rowconfigure([0],minsize=10,weight=1)
        #textFrame sub frames
        eventFrm = tk.Frame(textFrame)
        eventFrm.grid(row=0,column=0,columnspan=2)
        eventFrm.columnconfigure([0],minsize=600,weight=1)
        # topFrame.columnconfigure([0],minsize=800,weight=1)
        
       
        
        for i in range(Dindex,len(entries)):
                var = tk.IntVar()
                checkbox = tk.Checkbutton(eventFrm,variable=var, text = entries[i])
                checkbox.grid(row=i,column=0,sticky='w')
                checkboxes.append(var)
                print("checkbox {} label is {}".format(i,entries[i]))
        print("final checkbox length is {}".format(len(checkboxes)))
        #populate checklist
        # for i in range(0,5):
        #     checkbox = tk.Checkbutton(eventFrm,text=entries[i],onvalue=1,offvalue=0, variable=var).grid(row=i,column=0,sticky="w")
        
        # def confirmDelete():
        #     global pageIndex
        #     global entries
            
        #     dEntries = []
        #     for i in range(0,5):
        #         vChk = tk.Checkbutton(eventFrm,)
        
        
    
    global pageIndex
    jWindow = tk.Toplevel(window)
    jWindow.title("Journal")
    jWindow.geometry("629x350")
    jWindow.resizable(False,False)
    
    jFrame = tk.Frame(jWindow,bg='saddlebrown')
    jFrame.grid(row=0,column=0)
    jBtnFrame = tk.Frame(jFrame)
    jBtnFrame.grid(row=0,column=1)
    
    libraryBtns = tk.Frame(jBtnFrame)
    libraryBtns.grid(row=1,column=0)
    
    jSplash = tk.Label(jFrame,text="Journal Entries")
    jSplash.grid(row=0,column=0,sticky='w')
    jPage = tk.Label(jFrame,text="{}/{}".format(pageIndex,countPages()))
    jPage.grid(row=0,column=0,sticky='e')
    jSplash.columnconfigure([0],minsize=450,weight=1)
    
    libraryPre = tk.Button(libraryBtns,text="<",command=pageDown)
    libraryPre.grid(row=0,column=0,sticky='e')
    libraryPost = tk.Button(libraryBtns,text=">",command=pageUp)
    libraryPost.grid(row=0,column=1,sticky='e')
    
    jEntries = tk.Label(jFrame,text=compEvents(),width=75,height=20,padx=5,pady=5,relief=tk.GROOVE, anchor='nw',justify='left',wraplength=500)
    jEntries.grid(row=1,column=0,sticky="nw",rowspan=2)
    
    
    tk.Button(jFrame,text="New Event",command=newEntries).grid(row=1,column=1,sticky='n',padx=5,pady=20) 
    tk.Button(jFrame,text="Delete Entries",command=deleteEntries).grid(row=2,column=1)
    
    def updateEntries():
        global pageIndex
        newEntry = compEvents()
        newPage = countPages()
        jEntries.configure(text=newEntry)
        jPage.configure(text="{}/{}".format(pageIndex,newPage))
        jEntries.after(400, updateEntries)
    updateEntries()
    

        
         
def newEntries():
    
    def validate(*args):
        if request_var.get() and execution_var.get() and execution_var.get().isnumeric():
            submitButton.config(state='normal')
        else:
            submitButton.config(state = 'disabled')
    
    def clearEvent():
        eNameText.delete(0,tk.END)
        eDateText.delete(0,tk.END)
        
    def newEvent():
        global entries
        global entryQ
        
        # RaddEvent = eNameText.get("1.0",tk.END)
        RaddEvent = eNameText.get()
        addEvent = RaddEvent.replace("\n","")
        # RaddDate = eDateText.get("1.0",tk.END)
        RaddDate = eDateText.get()
        addDate = RaddDate.replace("\n","")
        # entryQ = len(entries)-1
        if entryQ == 0:
            entries[0] = "Day {}: {}".format(addDate, addEvent)
            entryQ += 1
        else:
            entries.append("Day {}: {}".format(addDate, addEvent))
            entryQ += 1
        eNameText.delete(0,tk.END)
        eDateText.delete(0,tk.END)
        

    eWindow = tk.Toplevel(window)
    eWindow.title("New Event")
    eWindow.geometry("600x100")
    eWindow.resizable(False,False)
    eWindow.grab_set()
    
    eFrameL = tk.Frame(eWindow)
    eFrameL.grid(row=0,column=0,sticky="nw")
    eFrameB = tk.Frame(eWindow)
    eFrameB.grid(row=0,column=1,sticky="nw")
    
    #Labels for event
    eName = tk.Label(eFrameL,text="Event Description: ")
    eDate = tk.Label(eFrameL, text="Day: ")
    
    eName.grid(row=0,column=0,sticky="nw")
    eDate.grid(row=1,column=0,sticky="nw")
    
    #Buttons
    
    tk.Button(eFrameB,text="Clear",command=clearEvent).grid(row=2,column=1,sticky="w")
    submitButton = tk.Button(eFrameB,text="Submit",command=newEvent, state='disabled')
    submitButton.grid(row=2,column=1,sticky="e")
    
    request_var = tk.StringVar()
    execution_var = tk.StringVar()
    eNameText = tk.Entry(eFrameB,width=80, textvariable = request_var,)
    eNameText.grid(row=0,column=1,sticky="nw")
    eDateText = tk.Entry(eFrameB,width=20, textvariable = execution_var)
    eDateText.grid(row=1,column=1,sticky="nw")
    request_var.trace('w',validate)
    execution_var.trace('w',validate)

#File creation
def open_file():
    gameData = ""
    filepath = askopenfilename(
        filetypes=[("Text Files",".txt"),("All Files","*.*")])

    if not filepath:
        return
    
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        gameData = text
        loadGame(gameData)
    
def save_file():
    gameData = saveGame()
    filepath = asksaveasfilename(
        defaultextension = ".txt",
        filetypes=[("Text Files","*.txt"),("All FIles", "*.*")],
        )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = gameData
        output_file.write(text)

def newGame():
    
    def yPress():
        global entries
        global DMnotes
        global date
        global entryQ
        global wClear,wRain,wSnow,wWindy,wWindAndRain,wAcidRain,wAshfall,wFirestorm,wHail,wThunderstorm,wBlizzard,wHeatwave,wMonsoon,wColdfront,wGhostlight
        entries = []
        DMnotes = ""
        wClear = IntVar(value=1)
        wRain = IntVar(value=1)
        wSnow =IntVar(value=1)
        wWindy = IntVar(value=0)
        wWindAndRain = IntVar(value=0)
        wAcidRain = IntVar(value=0)
        wAshfall = IntVar(value=0)
        wFirestorm = IntVar(value=0)
        wHail = IntVar(value=0)
        wThunderstorm = IntVar(value=0)
        wBlizzard = IntVar(value=0)
        wHeatwave = IntVar(value=0)
        wMonsoon = IntVar(value=0)
        wColdfront = IntVar(value=0)
        wGhostlight = IntVar(value=0)
        disp_weather['text'] = 'Clear'
        disp_weather['bg'] = 'skyblue'
        disp_weather['fg'] = 'white'
        disp_time['text'] = '12:00'
        dateHeader['text'] = 'Date: 1'
        entryQ = 0
        nGame.destroy()
        
    def nPress():
        nGame.destroy()
        
    nGame = tk.Toplevel(window)
    nGame.geometry=("200x100")
    wLabel = tk.Label(nGame,text="Warning, any unsaved changes will be lost. Continue?")
    wLabel.grid(row=0,column=0,sticky='nesw',columnspan=2)
    yBtn = tk.Button(nGame,text="Yes",padx=5,pady=5,command=yPress)
    yBtn.grid(row=1,column=0,sticky='ew')
    nBtn = tk.Button(nGame,text="No",padx=5,pady=5,command=nPress)
    nBtn.grid(row=1,column=1,sticky='ew')
    
#Build Weather Settings List for Savegeme
#clear,rain,snow,windy,windandrain,acidrain,ashfall,firestorm,hail,thunderstorm,blizzard,heatwave,monsoon,coldfront,ghostlight
def buildWeather():
    availW = []
    wList = ""
    if wClear.get() == 1:
        availW.append("1")
    else:
        availW.append("0")
    if wRain.get() ==1:
        availW.append("1")
    else:
        availW.append("0")
    if wSnow.get() ==1:
        availW.append("1")
    else:
        availW.append("0")
    if wWindy.get() ==1:
        availW.append("1")
    else:
        availW.append("0")
    if wWindAndRain.get() ==1:
        availW.append("1")
    else:
        availW.append("0")
    if wAcidRain.get() ==1:
        availW.append("1")
    else:
        availW.append("0")
    if wAshfall.get() ==1:
        availW.append("1")
    else:
        availW.append("0")
    if wFirestorm.get() ==1:
        availW.append("1")
    else:
        availW.append("0")
    if wGhostlight.get() ==1:
        availW.append("1")
    else:
        availW.append("0")
    if wHail.get() ==1:
        availW.append("1")
    else:
        availW.append("0")
    if wThunderstorm.get() ==1:
        availW.append("1")
    else:
        availW.append("0")
    if wBlizzard.get() ==1:
        availW.append("1")
    else:
        availW.append("0")
    if wHeatwave.get() ==1:
        availW.append("1")
    else:
        availW.append("0")
    if wMonsoon.get() ==1:
        availW.append("1")
    else:
        availW.append("0")
    if wColdfront.get() ==1:
        availW.append("1")
    else:
        availW.append("0")
    for i in range(0,len(availW)):
        wList += "{}".format(availW[i])
    return wList


def buildEntries():
    bEntries = ""
    for i in range(0,len(entries)):
        if i==len(entries)-1:
            bEntries += "{}@".format(entries[i])
        else:
            bEntries += "{}#".format(entries[i])
        
    return bEntries

def rebuildEntries(bEnt):
    global entries
    char = 0
    entryA = []
    entryIndex = 0
    slave = ""
    while bEnt[char] != '@':
        if bEnt[char] == '@':
            break
        if bEnt[char] == '#':
            entryA.append(slave)
            entryIndex += 1
            char +=1
            slave = ""
        else:
            slave += bEnt[char]
            char += 1
            print(slave)
    entryA.append(slave)
    
    print(entryA)
    
    entries = entryA
            
        
#Write Adeventure Details
def saveGame():
    gameData = ""
    wSettings = buildWeather()
    bEnt = buildEntries()
    #Day$Time$Weather$Weathersettings$EventList
    gameData += "{}${}${}${}${}${}".format(dateHeader["text"],disp_time["text"],disp_weather["text"],DMnotes,wSettings,bEnt)
    print(gameData)
    return gameData
    
def loadGame(gameData):
    global entries
    global DMnotes
    ##get game data
    test = gameData
    i = test.index('$')
    t1 = test[:i]
    dateHeader["text"]=t1
    nTest = test.replace("{}$".format(t1),"")
    test = nTest
    j = test.index('$')
    t2 = test[:j]
    disp_time["text"]=t2
    nTest = test.replace("{}$".format(t2),"")
    test = nTest
    k = test.index('$')
    t3 = test[:k]
    disp_weather["text"]=t3
    nTest = test.replace("{}$".format(t3),"")
    test = nTest
    #retrieving DM notes
    notes = test.index('$')
    notesTxt = test[:notes]
    nNotesTxt = test.replace("{}$".format(notesTxt),"")
    test = nNotesTxt
    DMnotes = notesTxt
    #returning weather varaibles
    l = test.index('$')
    wValues = test[:l]
    nTest = test.replace("{}$".format(wValues),"") 
    test = nTest
    updateWeather(wValues)
    m = test.index('@')
    bEnt = test[:m]
    bEnt += '@'
    print(bEnt)
    rebuildEntries(bEnt)

def updateWeather(wValues):
    global wClear
    global wRain
    global wSnow
    global wWindy
    global wWindAndRain
    global wAcidRain
    global wAshfall
    global wFirestorm
    global wHail
    global wThunderstorm
    global wBlizzard
    global wHeatwave
    global wMonsoon
    global wColdfront
    global wGhostlight
    
    wClear = IntVar(value= wValues[0])
    wRain = IntVar(value = wValues[1])
    wSnow = IntVar(value = wValues[2])
    wWindy = IntVar(value = wValues[3])
    wWindAndRain =IntVar(value = wValues[4])
    wAcidRain=IntVar(value = wValues[5])
    wAshfall=IntVar(value = wValues[6])
    wFirestorm=IntVar(value = wValues[7])
    wHail=IntVar(value = wValues[8])
    wThunderstorm=IntVar(value = wValues[9])
    wBlizzard=IntVar(value = wValues[10])
    wHeatwave=IntVar(value = wValues[11])
    wMonsoon=IntVar(value = wValues[12])
    wColdfront=IntVar(value = wValues[13])
    wGhostlight=IntVar(value = wValues[14])

def increaseTime1m():
    #Split String
    hValue = int(disp_time["text"].split(":")[0])
    mValue = int(disp_time["text"].split(":")[1])
    day = int(dateHeader["text"].split(":")[1])
    disp_events["text"] = isHappening()
    disp_Fevents["text"]=isFuture()
    
    if mValue+1 == 60:
            mValue = "00"
            if hValue+1 == 24:
                hValue = "0"
                day = day+1
                disp_events["text"] = isHappening()
                disp_Fevents["text"]=isFuture()
                dateHeader["text"]= "Date: "+f"{day}"
                onWeather()
            else:    
                hValue = hValue+1
            
    else:
        mValue = mValue+1
        if mValue < 10:
            mValue = "0{}".format(mValue)
            
    dayColor()
    disp_time["text"] = f"{hValue}"+":"+f"{mValue}"

def decreaseTime1m():
    #Split String
    hValue = int(disp_time["text"].split(":")[0])
    mValue = int(disp_time["text"].split(":")[1])
    day = int(dateHeader["text"].split(":")[1])
    disp_events["text"] = isHappening()
    disp_Fevents["text"]=isFuture()
  
    if mValue-1 == -1:
            mValue = "59"
            if hValue-1 == -1:
                hValue = "23"
                day = day-1
                disp_events["text"] = isHappening()
                disp_Fevents["text"]=isFuture()
                dateHeader["text"]= "Date: "+f"{day}"
                
            else:    
                hValue = hValue-1
            
    else:
        mValue = mValue-1
        # if mValue-1 == 0:
        #     mValue = "00"
        if mValue == 0:
            mValue = "00"
        elif mValue > 0 and mValue < 10:
            mValue = "0{}".format(mValue)
    
    dayColor()              
    disp_time["text"] = f"{hValue}"+":"+f"{mValue}"
    
def increaseTime15():
    #Split String
    hValue = int(disp_time["text"].split(":")[0])
    mValue = int(disp_time["text"].split(":")[1])
    day = int(dateHeader["text"].split(":")[1])
    disp_events["text"] = isHappening()
    disp_Fevents["text"]=isFuture()
    
    if mValue+15 >= 60:
            mCalc = (mValue+15)-60
            if mCalc == 0:
                mValue = "00"
            else:
                if mCalc <10:
                    mValue = "0{}".format(str(mCalc))
                else:
                    mValue = str(mCalc)
            if hValue+1 == 24:
                hValue = "0"
                day = day+1
                disp_events["text"] = isHappening()
                disp_Fevents["text"]=isFuture()
                dateHeader["text"]= "Date: "+f"{day}"
                onWeather()
            else:    
                hValue = hValue+1
            
    else:
        mValue = mValue+15
    
    dayColor()
    disp_time["text"] = f"{hValue}"+":"+f"{mValue}"

def decreaseTime15():
    #Split String
    hValue = int(disp_time["text"].split(":")[0])
    mValue = int(disp_time["text"].split(":")[1])
    day = int(dateHeader["text"].split(":")[1])
    disp_events["text"] = isHappening()
    disp_Fevents["text"]=isFuture()
    if mValue-15 <= 0:
        mCalc = (mValue-15)+60
        if mCalc-60 == 0:
            mValue = "00"
            hValue += 1
        else:
            mValue = str(mCalc)            
            
        if hValue-1 == -1:
            hValue = "23"
            day = day-1
            disp_events["text"] = isHappening()
            disp_Fevents["text"]=isFuture()
            dateHeader["text"]= "Date: "+f"{day}"
                
        else:    
            hValue = hValue-1
            
    else:
        if mValue-15 < 10:
            mValue = "0{}".format(str(mValue-15))
        elif mValue == 0:
            mValue = "00"
        else:
            mValue -= 15
    if mValue == 60:
        mValue = '00'
        
    dayColor()               
    disp_time["text"] = f"{hValue}"+":"+f"{mValue}"

def decreaseTime1h():
    #Split String
    hValue = int(disp_time["text"].split(":")[0])
    mValue = int(disp_time["text"].split(":")[1])
    day = int(dateHeader["text"].split(":")[1])
    disp_events["text"] = isHappening()
    disp_Fevents["text"]=isFuture()
    
    if hValue-1 == -1:
            hValue = "23"
            day = day-1
            disp_events["text"] = isHappening()
            disp_Fevents["text"]=isFuture()
            dateHeader["text"]= "Date: "+f"{day}"
            
    else:
        hValue = hValue-1
        
    if mValue == 0:
        mValue = "00"
    elif mValue < 10:
        mValue = f"0{mValue}"
    
    dayColor()               
    disp_time["text"] = f"{hValue}"+":"+f"{mValue}"
    
def increaseTime1h():
    #Split String
    hValue = int(disp_time["text"].split(":")[0])
    mValue = int(disp_time["text"].split(":")[1])
    day = int(dateHeader["text"].split(":")[1])
    disp_events["text"] = isHappening()
    disp_Fevents["text"]=isFuture()
    
    if hValue+1 == 24:
            hValue = "0"
            day = day+1
            dateHeader["text"]= "Date: "+f"{day}"
            disp_events["text"] = isHappening()
            disp_Fevents["text"]=isFuture()
            onWeather()
            
    else:
        hValue = hValue+1
        
    if mValue == 0:
        mValue = "00"
    elif mValue < 10:
        mValue = f"0{mValue}"
    
    dayColor()
    disp_time["text"] = f"{hValue}"+":"+f"{mValue}"    

#Change the color of time widget to fit the time of day
def dayColor():
    hValue = int(disp_time["text"].split(":")[0])
    if hValue >= 0 and hValue < 4:
        disp_time['bg'] = 'midnightblue'
        disp_time['fg'] = 'white'
    if hValue >=4 and hValue < 6:
        disp_time['bg'] = 'darkblue'
        disp_time['fg'] = 'white'
    if hValue >=6 and hValue < 8:
        disp_time['bg'] = 'mediumblue'
        disp_time['fg'] = 'white'
    if hValue >=8 and hValue < 10:
        disp_time['bg'] = 'royalblue'
        disp_time['fg'] = 'white'
    if hValue >=10 and hValue < 17:
        disp_time['bg'] = 'cornflowerblue'
        disp_time['fg'] = 'white'
    if hValue >=17 and hValue < 19:
        disp_time['bg'] = 'royalblue'
        disp_time['fg'] = 'white'
    if hValue >=19 and hValue < 21:
        disp_time['bg'] = 'mediumblue'
        disp_time['fg'] = 'white'
    if hValue >=21 and hValue <23:
        disp_time['bg'] = 'darkblue'
        disp_time['fg'] = 'white'
        
def addDay():
    day = int(dateHeader["text"].split(":")[1])
    disp_events["text"] = isHappening()
    disp_Fevents["text"]=isFuture()
    
    day = day+1
    dateHeader["text"]= "Date: "+f"{day}"
    disp_events["text"] = isHappening()
    disp_Fevents["text"]=isFuture()
    onWeather()

def subDay():
    day = int(dateHeader["text"].split(":")[1])
    disp_events["text"] = isHappening()
    disp_Fevents["text"]=isFuture()
    
    if day >= 2:
        day = day-1
        dateHeader["text"]= "Date: "+f"{day}"
        disp_events["text"] = isHappening()
        disp_Fevents["text"]=isFuture()
        onWeather()


def openDice():
    dice_window = tk.Toplevel(window)
    dice_window.title("Dice Roller")
    # dice_window.configure(bg='mediumaquamarine')
    dice_window.geometry("700x350")
    dice_window.resizable=(False,False)
    dice_window.configure(bg='saddlebrown')
    path = f"{directory}"+r"\leather.jpg"
    loadBg = Image.open(path)
    mainBg = ImageTk.PhotoImage(loadBg)
    lbl = tk.Label(dice_window, image=mainBg)
    lbl.image=mainBg
    lbl.place(relx=0.5,rely=0.5, anchor ='center')
    btn_main = tk.Frame(dice_window, relief=tk.RAISED)
    btn_main.grid(row=0,column=0,sticky="ns",padx=5,pady=5)
    
    def increase_qty(dType,cQty):
        qty = int(cQty)
        if dType == 'coin': coin_qty['text'] = str(qty+1)
        if dType == 'd4': d4_qty['text'] = str(qty+1)
        if dType == 'd6': d6_qty['text'] = str(qty+1)
        if dType == 'd8': d8_qty['text'] = str(qty+1)
        if dType == 'd10': d10_qty['text'] = str(qty+1)
        if dType == 'd12': d12_qty['text'] = str(qty+1)
        if dType == 'd20': d20_qty['text'] = str(qty+1)
        if dType == 'd100': d100_qty['text'] = str(qty+1)
        
    def decrease_qty(dType,cQty):
        qty = int(cQty)
        if dType == 'coin' and qty>=1: coin_qty['text'] = str(qty-1)
        if dType == 'd4' and qty >=1: d4_qty['text'] = str(qty-1)
        if dType == 'd6' and qty >=1: d6_qty['text'] = str(qty-1)
        if dType == 'd8' and qty >=1: d8_qty['text'] = str(qty-1)
        if dType == 'd10' and qty >=1: d10_qty['text'] = str(qty-1)
        if dType == 'd12' and qty >=1: d12_qty['text'] = str(qty-1)
        if dType == 'd20' and qty >=1: d20_qty['text'] = str(qty-1)
        if dType == 'd100' and qty >=1: d100_qty['text'] = str(qty-1)
        
        
    def compileDice():
        rollStr = ''
        if int(coin_qty['text']) > 0:
            total = 0
            for i in range(int(coin_qty['text'])):
                roll = random.randint(1,2)
                if roll == 1:
                    rollStr += "( h ) "
                    total += 1
                else:
                    rollStr += "( t ) "
                    total += 2
                # total += roll
                # rollStr += "({}) ".format(str(roll))
            coinRoll['text'] = rollStr
            coinTotal['text'] = str(total)
            rollStr = ''
        else:
            coinRoll['text'] = ''
            coinTotal['text'] = ''
        if int(d4_qty['text']) > 0:
            total = 0
            for i in range(int(d4_qty['text'])):
                roll = random.randint(1,4)
                total += roll
                rollStr += "({}) ".format(str(roll))
            d4Roll['text'] = rollStr
            d4Total['text'] = str(total)
            rollStr = ''
        else:
            d4Roll['text'] = ''
            d4Total['text'] = ''
        if int(d6_qty['text']) > 0:
            total = 0
            for i in range(int(d6_qty['text'])):
                roll = random.randint(1,6)
                total += roll
                rollStr += "({}) ".format(str(roll))
            d6Roll['text'] = rollStr
            d6Total['text'] = str(total)
            rollStr = ''
        else:
            d6Roll['text'] = ''
            d6Total['text']= ''
        if int(d8_qty['text']) > 0:
            total = 0
            for i in range(int(d8_qty['text'])):
                roll = random.randint(1,8)
                total += roll
                rollStr += "({}) ".format(str(roll))
            d8Roll['text'] = rollStr
            d8Total['text'] = str(total)
            rollStr = ''
        else:
            d8Roll['text'] = ''
            d8Total['text'] = ''
        if int(d10_qty['text']) > 0:
            total = 0
            for i in range(int(d10_qty['text'])):
                roll = random.randint(1,10)
                total += roll
                rollStr += "({}) ".format(str(roll))
            d10Roll['text'] = rollStr
            d10Total['text'] = str(total)
            rollStr = ''
        else:
            d10Roll['text'] = ''
            d10Total['text'] = ''
        if int(d12_qty['text']) > 0:
            total = 0
            for i in range(int(d12_qty['text'])):
                roll = random.randint(1,12)
                total += roll
                rollStr += "({}) ".format(str(roll))
            d12Roll['text'] = rollStr
            d12Total['text'] = str(total)
            rollStr = ''
        else:
            d12Roll['text'] = ''
            d12Total['text'] = ''
        if int(d20_qty['text']) > 0:
            total = 0
            for i in range(int(d20_qty['text'])):
                roll = random.randint(1,20)
                total += roll
                rollStr += "({}) ".format(str(roll))
            d20Roll['text'] = rollStr
            d20Total['text'] = str(total)
            rollStr = ''
        else:
            d20Roll['text'] = ''
            d20Total['text'] = ''
        if int(d100_qty['text']) > 0:
            for i in range(int(d100_qty['text'])):
                roll = random.randint(1,100)
                rollStr += "({}) ".format(str(roll))
            d100Roll['text'] = rollStr
            rollStr = ''
        else:
            d100Roll['text'] = ''
            
    def clearDice():
        coin_qty['text'] = '0'
        d4_qty['text'] = '0'
        d6_qty['text'] = '0'
        d8_qty['text'] = '0'
        d10_qty['text'] = '0'
        d12_qty['text'] = '0'
        d20_qty['text'] = '0'
        d100_qty['text'] = '0'
        
        compileDice()
    
    coin_qty = tk.Label(dice_window,text='0',relief=tk.GROOVE)
    coin_qty.grid(row=0,column=3,padx=10,pady=5)
    coin_lBtn = tk.Button(dice_window,text="<",command=lambda: decrease_qty('coin',coin_qty['text']),bg='gold')
    coin_lBtn.grid(row=0,column=0,pady=5)
    coinIcon = tk.Label(dice_window,text="coin")
    coinIcon.grid(row=0,column=1,pady=5)
    coin_mBtn = tk.Button(dice_window,text=">",command=lambda: increase_qty('coin',coin_qty['text']),bg='gold')
    coin_mBtn.grid(row=0,column=2,pady=5)
    coinRoll = tk.Label(dice_window,text="",anchor = 'w',relief = tk.SUNKEN,width=70)
    coinRoll.grid(row=0,column=4,pady=5)
    coinTotal = tk.Label(dice_window,text="",anchor = 'w',relief = tk.SUNKEN,width=5)
    coinTotal.grid(row=0,column=5,pady=5)
    d4_qty = tk.Label(dice_window,text='0',relief=tk.GROOVE)
    d4_qty.grid(row=1,column=3,padx=10,pady=5)
    d4_lBtn = tk.Button(dice_window,text="<",command=lambda: decrease_qty('d4',d4_qty['text']),bg='gold')
    d4_lBtn.grid(row=1,column=0,pady=5)
    d4_Icon = tk.Label(dice_window,text="d4")
    d4_Icon.grid(row=1,column=1,pady=5)
    d4_mBtn = tk.Button(dice_window,text='>',command=lambda: increase_qty('d4',d4_qty['text']),bg='gold')
    d4_mBtn.grid(row=1,column=2,pady=5)
    d4Roll = tk.Label(dice_window,text="",anchor = 'w',relief = tk.SUNKEN,width=70)
    d4Roll.grid(row=1,column=4,pady=5)
    d4Total = tk.Label(dice_window,text="",anchor = 'w',relief = tk.SUNKEN,width=5)
    d4Total.grid(row=1,column=5,pady=5)
    d6_qty = tk.Label(dice_window,text='0',relief=tk.GROOVE)
    d6_qty.grid(row=2,column=3,padx=10,pady=5)
    d6_lBtn = tk.Button(dice_window,text="<",command=lambda: decrease_qty('d6',d6_qty['text']),bg='gold')
    d6_lBtn.grid(row=2,column=0,pady=5)
    d6_Icon = tk.Label(dice_window,text="d6")
    d6_Icon.grid(row=2,column=1,pady=5)
    d6_mBtn = tk.Button(dice_window,text='>',command=lambda: increase_qty('d6',d6_qty['text']),bg='gold')
    d6_mBtn.grid(row=2,column=2,pady=5)
    d6Roll = tk.Label(dice_window,text="",anchor = 'w',relief = tk.SUNKEN,width=70)
    d6Roll.grid(row=2,column=4,pady=5)
    d6Total = tk.Label(dice_window,text="",anchor = 'w',relief = tk.SUNKEN,width=5)
    d6Total.grid(row=2,column=5,pady=5)
    d8_qty = tk.Label(dice_window,text='0',relief=tk.GROOVE)
    d8_qty.grid(row=3,column=3,padx=10,pady=5)
    d8_lBtn = tk.Button(dice_window,text="<",command=lambda: decrease_qty('d8',d8_qty['text']),bg='gold')
    d8_lBtn.grid(row=3,column=0,pady=5)
    d8_Icon = tk.Label(dice_window,text="d8")
    d8_Icon.grid(row=3,column=1,pady=5)
    d8_mBtn = tk.Button(dice_window,text='>',command=lambda: increase_qty('d8',d8_qty['text']),bg='gold')
    d8_mBtn.grid(row=3,column=2,pady=5)
    d8Roll = tk.Label(dice_window,text="",anchor = 'w',relief = tk.SUNKEN,width=70)
    d8Roll.grid(row=3,column=4,pady=5)
    d8Total = tk.Label(dice_window,text="",anchor = 'w',relief = tk.SUNKEN,width=5)
    d8Total.grid(row=3,column=5,pady=5)
    d10_qty = tk.Label(dice_window,text='0',relief=tk.GROOVE)
    d10_qty.grid(row=4,column=3,padx=10,pady=5)
    d10_lBtn = tk.Button(dice_window,text="<",command=lambda: decrease_qty('d10',d10_qty['text']),bg='gold')
    d10_lBtn.grid(row=4,column=0,pady=5)
    d10_Icon = tk.Label(dice_window,text="d10")
    d10_Icon.grid(row=4,column=1,pady=5)
    d10_mBtn = tk.Button(dice_window,text='>',command=lambda: increase_qty('d10',d10_qty['text']),bg='gold')
    d10_mBtn.grid(row=4,column=2,pady=5)
    d10Roll = tk.Label(dice_window,text="",anchor = 'w',relief = tk.SUNKEN,width=70)
    d10Roll.grid(row=4,column=4,pady=5)
    d10Total = tk.Label(dice_window,text="",anchor = 'w',relief = tk.SUNKEN,width=5)
    d10Total.grid(row=4,column=5,pady=5)
    d12_qty = tk.Label(dice_window,text='0',relief=tk.GROOVE)
    d12_qty.grid(row=5,column=3,padx=10,pady=5)
    d12_lBtn = tk.Button(dice_window,text="<",command=lambda: decrease_qty('d12',d12_qty['text']),bg='gold')
    d12_lBtn.grid(row=5,column=0,pady=5)
    d12_Icon = tk.Label(dice_window,text="d12")
    d12_Icon.grid(row=5,column=1,pady=5)
    d12_mBtn = tk.Button(dice_window,text='>',command=lambda: increase_qty('d12',d12_qty['text']),bg='gold')
    d12_mBtn.grid(row=5,column=2,pady=5)
    d12Roll = tk.Label(dice_window,text="",anchor = 'w',relief = tk.SUNKEN,width=70)
    d12Roll.grid(row=5,column=4,pady=5)
    d12Total = tk.Label(dice_window,text="",anchor = 'w',relief = tk.SUNKEN,width=5)
    d12Total.grid(row=5,column=5,pady=5)
    d20_qty = tk.Label(dice_window,text='0',relief=tk.GROOVE)
    d20_qty.grid(row=6,column=3,padx=10,pady=5)
    d20_lBtn = tk.Button(dice_window,text="<",command=lambda: decrease_qty('d20',d20_qty['text']),bg='gold')
    d20_lBtn.grid(row=6,column=0,pady=5)
    d20_Icon = tk.Label(dice_window,text="d20")
    d20_Icon.grid(row=6,column=1,pady=5)
    d20_mBtn = tk.Button(dice_window,text='>',command=lambda: increase_qty('d20',d20_qty['text']),bg='gold')
    d20_mBtn.grid(row=6,column=2,pady=5)
    d20Roll = tk.Label(dice_window,text="",anchor = 'w',relief = tk.SUNKEN,width=70)
    d20Roll.grid(row=6,column=4,pady=5)
    d20Total = tk.Label(dice_window,text="",anchor = 'w',relief = tk.SUNKEN,width=5)
    d20Total.grid(row=6,column=5,pady=5)
    d100_qty = tk.Label(dice_window,text='0',relief=tk.GROOVE)
    d100_qty.grid(row=7,column=3,padx=10,pady=5)
    d100_lBtn = tk.Button(dice_window,text="<",command=lambda: decrease_qty('d100',d100_qty['text']),bg='gold')
    d100_lBtn.grid(row=7,column=0,pady=5)
    d100_Icon = tk.Label(dice_window,text="d100")
    d100_Icon.grid(row=7,column=1,pady=5)
    d100_mBtn = tk.Button(dice_window,text='>',command=lambda: increase_qty('d100',d100_qty['text']),bg='gold')
    d100_mBtn.grid(row=7,column=2,pady=5)
    d100Roll = tk.Label(dice_window,text="",anchor = 'w',relief = tk.SUNKEN,width=70)
    d100Roll.grid(row=7,column=4,pady=5)
    
    dRoll = tk.Button(dice_window,text='Roll Dice',command=compileDice)
    dRoll.grid(row=8,column=1,columnspan=5,padx=5,pady=12)
    
    clearRolls = tk.Button(dice_window,text='Clear Dice',command=clearDice)
    clearRolls.grid(row=8,column=5,columnspan=5,padx=5,pady=12)
    
def openNotes():
    
    def closeNotes():
        global DMnotes
        DMnotes = notebook.get('1.0',tk.END)
        noteWindow.destroy()
        
    noteWindow = tk.Toplevel(window)
    noteWindow.title("Notes")
    noteWindow.geometry("800x800")
    
    v = tk.Scrollbar(noteWindow,orient='vertical')
    v.pack(side=tk.RIGHT, fill='y')
    notebook = tk.Text(noteWindow,width=90,height=44,wrap=tk.WORD)
    notebook.insert("1.0", DMnotes)
    v.config(command=notebook.yview)
    notebook.pack()
    noteWindow.protocol("WM_DELETE_WINDOW",closeNotes)

    
def openHelp():
    helpWindow = tk.Toplevel(window)
    helpWindow.title("Help!")
    hFrame = tk.Frame(helpWindow)
    hFrame.pack(side=tk.LEFT)
    
    pathH = f"{directory}"+r"\HelpWindow.png"
    hWindow = ImageTk.PhotoImage(Image.open(pathH))
    hLbl = tk.Label(hFrame,image=hWindow)
    hLbl.image = hWindow
    hLbl.pack()

def saveYoShit():
    def closeGame():
        window.destroy()
    
    shitWin = tk.Toplevel(window)
    shitWin.title("Attention")
    sLbl = tk.Label(shitWin,text="Any unsaved changes will be lost, save?",bg='khaki',fg='black',padx=10,pady=10)
    sLbl.pack(side=tk.TOP)
    yBtn = tk.Button(shitWin,text='Yes',command=save_file,padx=5,pady=5)
    yBtn.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
    nBtn = tk.Button(shitWin,text='No',command=closeGame,padx=5,pady=5)
    nBtn.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True)
    
#Popup Splash
window = tk.Tk()
window.title("Encounter v2")
window.geometry("1150x500")
# window.rowconfigure([0, 1], minsize =100)
window.columnconfigure(1,minsize=100,weight=1)
window.configure(bg='darkgreen')
window.resizable(False,False)
window.protocol("WM_DELETE_WINDOW",saveYoShit)


#######DEBUG###########

#Weather Variables
wClear = IntVar(value=1)
wRain = IntVar(value=1)
wSnow =IntVar(value=0)
wWindy = IntVar(value=1)
wWindAndRain = IntVar(value=0)
wAcidRain = IntVar(value=0)
wAshfall = IntVar(value=0)
wFirestorm = IntVar(value=0)
wHail = IntVar(value=0)
wThunderstorm = IntVar(value=0)
wBlizzard = IntVar(value=0)
wHeatwave = IntVar(value=0)
wMonsoon = IntVar(value=0)
wColdfront = IntVar(value=0)
wGhostlight = IntVar(value=0)


mainSplash = tk.Toplevel(window)
mainSplash.title("Welcome!")
mainSplash.geometry("450x800")
path = f"{directory}"+r"\parchment.jpg"
loadIcon = Image.open(path)
splashImgL = Image.open(path)
splashImg = ImageTk.PhotoImage(splashImgL)
disp_splashImg = tk.Label(mainSplash,image=splashImg)
disp_splashImg.pack()
mainSplash.lift()
mainSplash.focus_force()
mainSplash.grab_set()
mainSplash.grab_release()

# window.wm_attributes('-transparentcolor', '#ab23ff')
#Save DM notes
DMnotes = ''


#Left Buttons
path = f"{directory}"+r"\leather.jpg"
loadBg = Image.open(path)
mainBg = ImageTk.PhotoImage(loadBg)
lbl = tk.Label(window, image=mainBg)
lbl.place(relx=0.5,rely=0.5, anchor ='center')
btn_main = tk.Frame(window, relief=tk.RAISED,bg='darkgreen')
btn_main.grid(row=0,column=0,sticky="ns",padx=5,pady=5)

#WeatherWindow
# weather_main = tk.Frame(window,height=200, relief=tk.RAISED)
# weather_main.grid(row=0,column=1,sticky="ne")
#####################################
#image1 = Image.open("D:/Documents/Blends/textures/cloudysky.jpg")
#test = ImageTk.PhotoImage(image1)

#imgLabel = tk.Label(weather_main,image=test,bg="blue")
#imgLabel.grid(row=0,column=0,sticky='nsew')

###Weather Text, time of day, events

infoDisplay = tk.Frame(window,bg='darkgreen')
infoDisplay.grid(row=0,column=1,sticky="nw",padx=5,pady=5)
pathM = f"{directory}"+r"\darkmetal.jpg"
metal = ImageTk.PhotoImage(Image.open(pathM))
hLbl = tk.Label(infoDisplay,image=metal)
hLbl.image = metal
hLbl.place(relx=0.5,rely=0.5, anchor ='center')
#infoDisplay.columnconfigure(0, minsize=50,weight=1)

disp_weather = tk.Label(infoDisplay, text ="Clear",relief=tk.GROOVE,bg='skyblue',fg="white",width=30,height=2)
disp_weather.grid(row=0,column=0,sticky="w",rowspan=2)

#EventHeaders  #ORDER:window\eLabels(eventHeader,dateHeader),eLabelFuture
eLabels = tk.Frame(infoDisplay,bg='blue')
eLabels.grid(row=1,column=0,sticky="nw")
# eLabelFuture = tk.Frame(infoDisplay,bg='orange')
# eLabelFuture.grid(row=2,column=1,sticky='nw')

#Display Time
disp_time = tk.Label(infoDisplay, text = timeString,relief=tk.GROOVE,bg='cornflowerblue',fg='white',width=10,height=2, font=('Arial',18))
disp_time.grid(row=1,column=8,sticky="e",padx=5,pady=5,rowspan=2)


dateHeader = tk.Label(infoDisplay,text=dayString, relief = tk.GROOVE,width=10,bg='green',fg='white')
dateHeader.grid(row=0,column=2,padx=5,pady=5,sticky='w',rowspan=2)

#change day buttons
dayForward = tk.Button(infoDisplay,text="+",command=addDay,bg='gold')
dayForward.grid(row=0,column=3,padx=5,pady=5,sticky='w',rowspan=2)

dayBack = tk.Button(infoDisplay, text="-",command=subDay,bg='gold')
dayBack.grid(row=0,column=1,padx=5,pady=5,sticky='w',rowspan=2)

#EventDisplay
# eventFrame = tk.Frame(window,bg='orange')
# eventFrame.grid(row=1,column=1,sticky="nsew")
# eventFrame.columnconfigure([0],minsize=200,weight=1)

eventHeader = tk.Label(infoDisplay,text="Today's Events", relief = tk.GROOVE)
eventHeader.grid(row=2,column=0,sticky="w")

#Check if anything is happening today
def isHappening():
    global entries  
    todayE = ""
    day = int(dateHeader["text"].split(":")[1])
    nothing = 'Nothing is Happening Today'
    indexOffset = 0
    lastEntry = ""
    if len(entries) == 0:
        entries.append("There is no entry as of yet")
    if str(entries[0]) == "There is no entry as of yet":
        return entries[0]
    else:
        for i in range(0,len(entries)):
            dupDay = 0
            j = str(entries[i])
            u = j.split(':')[0]
            k = int(u.replace("Day ",""))
            #print("checking day {} against day {}".format(day,k))
            
            if day == k:
                # print("day matches")
                #todayE = "{}\n".format(j.split(':')[1])
                for p in range(i,len(entries)):
                    # print("first duplicate is: {}".format(entries[p]))
                    # print ("index offset is {}".format(indexOffset))
                    # print("running iteration {}/{}".format(p,len(entries)))
                    y = str(entries[p])
                    w = y.split(':')[0]
                    z = int(w.replace("Day ",""))
                    chkDate1 = str(entries[i])
                    chkDate2 = chkDate1.split(':')[0]
                    chkDate3 = int(chkDate2.replace("Day ",""))
                    # print("checking if there is another entry after {}".format(k))
                    # print("chkDate is {}, day of next index is {}".format(chkDate3,z))
                    if z > chkDate3:
                        # print("end of index")
                        return todayE
                    if chkDate3 == z:
                        indexOffset += 1
                        # print("indexOffset set to {}".format(indexOffset))
                        # print("same day found entry is {}".format(entries[p]))
                        q = y.split(':')[1]
                        # print("new entry: {}, last entry: {}".format(q,lastEntry))
                        if q == lastEntry:
                            # print("new entry is a dupilicate, terminating.")
                            # print('end of index')
                            return todayE
                        else:
                            lastEntry = q
                            todayE += "{}\n".format(q)
                            # print("result is {}".format(todayE))
                    
                    elif chkDate3 > z:
                        # print("end of index")
                        return todayE
                  
        return todayE  
            
            # if dupDay == 1:
            #     return "\n{}".format(todayE)
                
           
            
               
            # if i+1 == len(entries):
            #   return nothing
                
            
def isFuture():
    global entries
    fEntries = ""
    day = int(dateHeader["text"].split(":")[1])
    nothing = 'Nothing is Happening Today'
    if str(entries[0]) == "There is no entry as of yet":
        return entries[0]
    else:
        for i in range(0,len(entries)):
            j = str(entries[i])
            u = j.split(':')[0]
            k = int(u.replace("Day ",""))
            if day < k:
                #q = j.split(':')[1]
                fEntries += "{}\n".format(j)
                disp_Fevents["text"] = fEntries
                continue
            if i+1 == len(entries):
                return nothing
        
def updateMainEntries():
     newEntry = isHappening()
     fEntry = isFuture()
     disp_events.configure(text=newEntry)
     disp_Fevents.configure(text=fEntry)
     disp_events.after(400, updateMainEntries)

# #FutureEventDisplay
# FeventFrame = tk.Frame(window,bg='darkgreen')
# FeventFrame.grid(row=3,column=1,sticky="nsew")

#background for events
pathM = f"{directory}"+r"\paper.jpg"
paper = ImageTk.PhotoImage(Image.open(pathM))
           
FeventHeader = tk.Label(infoDisplay,text="Upcoming Events", relief = tk.GROOVE)
FeventHeader.grid(row=4,column=0,sticky="w")
#Text Labels
disp_events = tk.Label(infoDisplay,text="Add an event to get started",anchor='nw',justify='left',height=10,width=131,wraplength=700)
disp_events.grid(row=3,column=0,sticky="ew",padx=5,pady=5,columnspan=50)



#Update Main Journal
#def updateEntries():
#    disp_events.after(2000, updateEntries)
#    disp_events["text"] = isHappening()
    
#updateEntries()


disp_Fevents = tk.Label(infoDisplay,text="It's a grand day for an adventure, \nStart by adding some events, or select 'Open' to resume a saved adventure.",anchor='nw',justify='left',height=12,width=131,wraplength=700)
disp_Fevents.grid(row=5,column=0,sticky="ew",padx=5,pady=5,columnspan=50)


#Right Side Buttons
frm_rightEdge = tk.Frame(window,bg="green")
frm_rightEdge.grid(row=0,column=3,sticky="ne",padx=5,pady=5)

#time control buttons
btn_newGame = tk.Button(btn_main,text="New Adventure",fg="white",bg="green",command=newGame)
btn_newGame.grid(row=0,column=0,sticky="ew")

btn_load = tk.Button(btn_main, text="Load Adventure",fg="white",bg="green",command=open_file)
btn_load.grid(row=1,column=0,sticky="ew")

btn_save = tk.Button(btn_main,text="Save Adventure",fg="white",bg="green",command=save_file)
btn_save.grid(row=2,column=0,sticky="ew")

# btn_dummy1 = tk.Button(btn_main,text="Dummy Save",fg="white",bg="green",command=saveGame)
# btn_dummy1.grid(row=3,column=0,sticky="ew")

# btn_dummy2 = tk.Button(btn_main,text="Dummy Load",fg="white",bg="green",command=loadGame)
# btn_dummy2.grid(row=4,column=0,sticky="ew")

btn_timeUp1m = tk.Button(infoDisplay, text=">",command=increaseTime1m,bg='gold')
btn_timeUp1m.grid(row=1,column=9,sticky="e",padx=5,pady=5,rowspan=2)

btn_timeDown1m = tk.Button(infoDisplay, text="<",command=decreaseTime1m,bg='gold')
btn_timeDown1m.grid(row=1,column=7,sticky="e",padx=5,pady=5,rowspan=2)

btn_timeUp15 = tk.Button(infoDisplay, text="->",command=increaseTime15,bg='gold')
btn_timeUp15.grid(row=1,column=10,sticky="w",padx=5,pady=5,rowspan=2)

btn_timeUp1h = tk.Button(infoDisplay, text="--->",command=increaseTime1h,bg='gold')
btn_timeUp1h.grid(row=1,column=11,sticky="e",padx=5,pady=5,rowspan=2)

btn_timeDown15 = tk.Button(infoDisplay,text="<-",command=decreaseTime15,bg='gold')
btn_timeDown15.grid(row=1,column=6,sticky="e",padx=5,pady=5,rowspan=2)

btn_timeDown1h = tk.Button(infoDisplay,text="<---",command=decreaseTime1h,bg='gold')
btn_timeDown1h.grid(row=1,column=5,sticky="e",padx=5,pady=5,rowspan=2)

###reserving column 4
# fillLabel = tk.Label(infoDisplay, width=30,bg='darkgreen')
# fillLabel.grid(row=1,column=4)

#right side buttons
#Loading icons
path = f"{directory}"+r"\weather.png"
loadIcon = Image.open(path)
wIco = ImageTk.PhotoImage(loadIcon)
btn_settings = tk.Button(frm_rightEdge, image=wIco, command=openSettings)
btn_settings.grid(row=0,column=0,sticky="ne",padx=5,pady=5)

path2 = f"{directory}"+r"\agenda.png"
loadIcon = Image.open(path2)
jIco = ImageTk.PhotoImage(loadIcon)
btn_settings = tk.Button(frm_rightEdge, image=jIco,command=openJournal)
btn_settings.grid(row=2,column=0,sticky="ne",padx=5,pady=5)

path3 = f"{directory}"+r"\die.png"
loadIcon = Image.open(path3)
diceIco = ImageTk.PhotoImage(loadIcon)
btn_dice = tk.Button(frm_rightEdge, image=diceIco,command=openDice)
btn_dice.grid(row=3,column=0,sticky='ne',padx=5,pady=5)

path4 = f"{directory}"+r"\journal.png"
loadIcon = Image.open(path4)
noteIcon = ImageTk.PhotoImage(loadIcon)
btn_Notes = tk.Button(frm_rightEdge, image=noteIcon, command=openNotes)
btn_Notes.grid(row=4,column=0,sticky='ne',padx=5,pady=5)

path = f"{directory}"+r"\help.png"
lHelp = Image.open(path)
helpIcon = ImageTk.PhotoImage(lHelp)
btn_help = tk.Button(frm_rightEdge, image=helpIcon, command=openHelp)
btn_help.grid(row=5,column=0,sticky='new',padx=5,pady=5)


updateMainEntries() 

window.mainloop()
