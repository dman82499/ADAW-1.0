from tkinter import *
import random
import sys
import os
from pygame import mixer
import time
import subprocess


def updatetext(inputs):
    inputs = str(inputes)
    progresstext.config(text = "   "+inputs)

class generateMIDI():
    
    @staticmethod
    def generateMIDIc(track, note, notelength, startingpos):
        updatetext(notelength)
        startingposa = startingpos#formula goes here
        newnote = midi.NoteOnEvent(tick = startingpos, velocity = 50, pitch = note)
        track.append (newnote)
        newpos = startingpos + notelength
        noteend = midi.NoteOffEvent(tick = newpos, velocity = 50, pitch = note)
        track.append (noteend)
        return ("MIDI note generated on", "for", note)

    @staticmethod
    def generateMIDIchordc(track, note1, note2, note3, note4, notelength, startingpos):
            generateMIDI.generateMIDIc(track, note1, notelength, startingpos)
            generateMIDI.generateMIDIc(track, note2, notelength, startingpos)
            generateMIDI.generateMIDIc(track, note3, notelength, startingpos)
            generateMIDI.generateMIDIc(track, note4, notelength, startingpos)


def generatemidis():
    print("hello!")
def ok():
    y.destroy()
file_path = None
    
def createmusic():
    global progresstext
    if file_path == None:
        global y
        y = Tk()
        y.title("Error")
        w = Label(y, text="You need to specify a file path ")
        w.grid()
        o = Label(y, text = "for the MIDI file to be saved in first!")
        o.grid(row=2)
        i=Button(y, text= "Ok", command = ok)
        i.grid(row=3)
    
    else:
        root.destroy()
        loading = Tk()
        loading.title("Creating Music...")
        w = 200 # width for the Tk root
        h = 100 # height for the Tk root

# get screen width and height
        ws = loading.winfo_screenwidth() # width of the screen
        hs = loading.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
        loading.geometry('%dx%d+%d+%d' % (w, h, x, y))
        configuretext = Label(loading, text = "Configuing song...")
        space = Label(loading, text = "")
        space.grid(row=2)
        configuretext.grid (row = 1)
        progresstext = Label(loading, text = "")
        progresstext.grid(row=3, column = 2, columnspan=2)
        generatemidis()
        subprocess.call([str(file_path)])
        loading.mainloop()

            

firsttime = 0
p = 0
def resizescreen():
    global firsttime
    global p 
    if not firsttime:
        p = 0
        firstime = 1
     
    if p == 1:
        root.attributes("-fullscreen", True)
        p = 0
        adjustwindow.config(text = "Escape")
    else:
        root.attributes("-fullscreen", False)
        firsttime = 1
        p = 1
        adjustwindow.config(text = "Fullsize")
    print ("what")    
    print (p)
    #a temporary fix for now:


def filename():
    global file_path
    from tkinter import filedialog
    file_path = filedialog.askopenfilename()
    ju.config(text = "Current Directory:    "+ str(file_path))

def mainscreen():
    global root
    global adjustwindow
    global ju
    root = Tk()
    root.title ("Autonomous Digital Audio Workstation (ADAW)")
    root.attributes("-fullscreen", True)
    root.configure(bg = "lightblue")
    frame = Frame(root)
    frame.configure(width = root.winfo_screenwidth(), height = root.winfo_screenheight())
    frame.configure(bg = "lightblue")
    frame.grid()
    Welcome = Label(frame, text = "        Autonomous MIDI Workstation (ADAW)         ",bg = "lightblue")
    Welcome.config(font=("Caligraphy", 44))
    Welcome.grid(row = 1)
    spacer2 = Label (frame, text = " ", bg = "lightblue")
    spacer2.grid(row = 2)
    key = BooleanVar()
    title = Entry (frame)
    title.grid(row= 5)
    selectentrylabel = Label (frame, text= "Enter Title of MIDI piece:")
    selectentrylabel.config(font = 14)
    selectentrylabel.grid(row = 3, rowspan =2)
    spacer1 = Label (frame, text = " ", bg = "lightblue")
    spacer1.grid(row = 7)
#Create that dank music boi!
    createsong = Button (frame, text = "Generate MIDI into DAW", command = createmusic)
    createsong.grid(row = 9)
    adjustwindow = Button (frame, text = "Escape", command = resizescreen)
    adjustwindow.grid(row = 0, column = 2, sticky = E)
    spacer2 = Label (frame, text = " ", bg = "lightblue")
    spacer2.grid(row = 10)
    spacer3 = Label (frame, text = " ", bg = "lightblue")
    spacer3.grid(row = 11)
    genretext = Label(frame, text = "Choose Genre:", bg="lightblue")
    genretext.grid(row = 15)
    genre = IntVar()
    normal = Radiobutton(frame, text = "Classical", variable = genre, value = "1", bg = "lightblue")
    normal.grid(row = 16)
    jazz = Radiobutton(frame, text = "Jazz       ", variable = genre, value = "2", bg = "lightblue")
    jazz.grid(row = 17)
    jazz.deselect()
    spacer4 = Label (frame, text = " ", bg = "lightblue")
    spacer4.grid(row = 18)
    spacer5 = Label (frame, text = " ", bg = "lightblue")
    spacer5.grid(row = 19)
    spacer6 = Label (frame, text = " ", bg = "lightblue")
    spacer6.grid(row = 20)
    spacer7 = Label (frame, text = " ", bg = "lightblue")
    spacer7.grid(row = 21)
    spacer4 = Label (frame, text = " ", bg = "lightblue")
    spacer4.grid(row = 22)
    spacer5 = Label (frame, text = " ", bg = "lightblue")
    spacer5.grid(row = 23)
    spacer6 = Label (frame, text = " ", bg = "lightblue")
    spacer6.grid(row = 24)
    spacer7 = Label (frame, text = " ", bg = "lightblue")
    spacer7.grid(row = 25)
    options = Button(frame, text = "Choose DAW integrated loction", command = filename)
    options.grid(row = 28)
    ju= Label(frame, text = "Current Directory:    "+ str(file_path), bg = "lightblue")
    ju.grid(row= 29)
    spacer4 = Label (frame, text = " ", bg = "lightblue")
    spacer4.grid(row = 30)
    spacer5 = Label (frame, text = " ", bg = "lightblue")
    spacer5.grid(row = 31)
    spacer6 = Label (frame, text = " ", bg = "lightblue")
    spacer6.grid(row = 32)
    spacer7 = Label (frame, text = " ", bg = "lightblue")
    spacer7.grid(row = 33)
    spacer8 = Label (frame, text = " ", bg = "lightblue")
    spacer8.grid(row = 34)
    spacer9 = Label (frame, text = " ", bg = "lightblue")
    spacer9.grid(row = 35)
    spacer10 = Label (frame, text = " ", bg = "lightblue")
    spacer10.grid(row = 36)
    spacer11= Label (frame, text = " ", bg = "lightblue")
    spacer11.grid(row = 37)
    spacer12 = Label (frame, text = " ", bg = "lightblue")
    spacer12.grid(row = 38)
    spacer13 = Label (frame, text = " ", bg = "lightblue")
    spacer13.grid(row = 36)
    spacer14= Label (frame, text = " ", bg = "lightblue")
    spacer14.grid(row = 37)
    spacer15 = Label (frame, text = " ", bg = "lightblue")
    spacer15.grid(row = 38)
    spacer13 = Label (frame, text = " ", bg = "lightblue")
    spacer13.grid(row = 39)
    spacer14= Label (frame, text = " ", bg = "lightblue")
    spacer14.grid(row = 40)
    spacer15 = Label (frame, text = " ", bg = "lightblue")
    spacer15.grid(row = 41)
    root.mainloop()
    
    
def activation():
    time.sleep(2)
    print("help")
    mainscreen()

def loadingscreen():
    #Create the loading screen for the application
    mixer.init()
    mixer.music.load("D:\peace.mp3")
    mixer.music.play()
    global root
    root = Tk()
    root.attributes("-fullscreen", False)
    root.title("Cquential Launcher")
    root.attributes("-fullscreen", True)
    root.configure(bg="lightblue")
    frame2 = Frame(root)
    frame2.configure(bg="lightblue")
    frame2.pack()

    Welcome = Label(frame2, text="         Autonomous MIDI Workstation (ADAW)           ")
    Welcome.config(font=("Caligraphy", 44), bg = "lightblue")
    Welcome.pack()

    load = Label(frame2, text="loading...", bg="lightblue")
    load.pack()
    root.update()
    frame2.forget()
    time.sleep(2)
    #in the future I think you can use

    mainscreen()

loadingscreen()

