import os
import threading
import time

from tkinter import *     # * means that you're importing everything in the tkinter module
from tkinter import filedialog
from tkinter import ttk  # ttk stands for themed tkinter. Used to improve the aesthetic of buttons & widgets
from ttkthemes import themed_tk as tk  # used to integrate themes into GUI
import tkinter.messagebox   # used to show a pop up window

from mutagen.mp3 import MP3
from pygame import mixer

# ------------------------------------------------------------------------------------------------------------------- #

"""creating a window"""
# windows - contains statusbar, leftFrame, rightFrame
window = tk.ThemedTk()
window.get_themes()  # Returns a list of all themes that can be set
window.set_theme("clearlooks")  # Sets the theme
window.configure(background="#fbf7f5")  # changing the bg color of the window
window.title("Beat")  # changing the title of the window

# ------------------------------------------------------------------------------------------------------------------- #

"""creating the statusbar"""
statusbar = ttk.Label(window, text="Welcome to Beat", relief=SUNKEN, font=("Times New Roman", 14, "italic"))
# statusbar.configure(bg="#b8d2d5")
statusbar.pack(side=BOTTOM, fill=X)
# SUNKEN makes it look like a button
# anchor parameter provides the location of the text
# side parameter of pack is for the orientation and differentiates it from text
# fill parameter expands the status bar to either ends of the window

"""creating the menubar"""
menubar = Menu(window)
window.config(menu=menubar)
# ensures that the menubar appears at the top and prepares the menubar so it can receive submenus

play_List = []  # contains the filename + path

# ------------------------------------------------------------------------------------------------------------------- #


def open_file():
    global filename
    # you can now use the variable name wherever you want throughout the code
    filename = filedialog.askopenfilename()
    add_music(filename)


index = 0


def add_music(fname):

    global index
    # creating a listbox
    fname = os.path.basename(fname)  # fname = filename without path
    playlist.insert(index, fname)  # adding song to playlist
    play_List.insert(index, filename)
    playlist.pack(pady=15)


def delete_music():
    selection = playlist.curselection()
    selection = int(selection[0])
    playlist.delete(selection)  # deletes music from listbox
    play_List.pop(selection)  # deletes music from list of songs because it takes up space
    #  .remove needs the fname


def quitting():
    tkinter.messagebox.showinfo("AWWW", "Do you really want to leave? :(")
    Action().stop()  # stops music if playing
    window.destroy()  # quits the window without giving error
# ------------------------------------------------------------------------------------------------------------------- #


"""creating the submenu"""
subMenu = Menu(menubar, tearoff=0)  # using menubar instead of window to differentiate the two types of menu
menubar.add_cascade(label="File", menu=subMenu)  # cascade = dropdown menu
subMenu.add_command(label="Open", command=open_file)
subMenu.add_command(label="Force Quit", command=quitting)


def about_beat():
    tkinter.messagebox.showinfo("About Beat", "This project is created by Callista Roselynn using the tkinter module.")


subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About Beat", command=about_beat)


mixer.init()  # initializing the mixer
# ------------------------------------------------------------------------------------------------------------------- #


"""Creating Top Frame"""
# leftFrame - contains playlist, addButton, deleteButton, slider
topFrame = Frame(window)
topFrame.configure(background="#fbf7f5")
topFrame.pack(padx=15, pady=15)
# leftFrame.pack(side=LEFT, padx=30, pady=15)
#  positions left frame on the left

playlist = Listbox(topFrame)  # playlist contains only filename
playlist.pack(pady=15)

addButton = ttk.Button(topFrame, text="+ Add", command=open_file)
addButton.pack(side=LEFT, padx=10)

deleteButton = ttk.Button(topFrame, text="- Delete", command=delete_music)
deleteButton.pack(side=LEFT)

# ------------------------------------------------------------------------------------------------------------------- #


"""Creating Middle Frame"""
middleFrame = Frame(window)
middleFrame.configure(background="#fbf7f5")
middleFrame.pack()

durationLabel = ttk.Label(middleFrame, text="Duration : 00:00")
# durationLabel.configure(bg="#fbf7f5")
durationLabel.pack()

remaining_Label = ttk.Label(middleFrame, text="Ends in : 00:00", relief=GROOVE)
# remaining_Label.configure(bg="#fbf7f5")
remaining_Label.pack(pady=10)
# ------------------------------------------------------------------------------------------------------------------- #


class Time:
    def __init__(self):
        self.paused = False

    def music_duration(self, play_selection):

        file_type = os.path.splitext(play_selection)
        # splits the file path into a list, 1st index in list is the extension

        if file_type[1] == ".mp3":  # for .mp3 file formats:
            audio = MP3(play_selection)
            total_duration = audio.info.length

        else:  # for .wav file formats:
            x = mixer.Sound(play_selection)  # loads the music file
            total_duration = x.get_length()  # calculates the value of the music in seconds

        # getting the length in minutes and seconds
        minutes, seconds = divmod(total_duration, 60)
        minutes = round(minutes)
        seconds = round(seconds)  # round function rounds up the values
        duration = "{:02d}:{:02d}".format(minutes, seconds)
        # formatting how the minutes and seconds will appear
        # 2d = 2 decimal places, 0 is added in case of 1 digit
        durationLabel["text"] = "Duration" + "-" + duration

        timee = threading.Thread(target=self.count_time, args=(total_duration,))
        # args needs to be in tuple/list form
        # threading enables the function to work simultaneously as the other functions
        timee.start()
        # print(file_type[1]) just to show the extension is ghe first index

    def count_time(self, current_time):

        global durationLabel

        # mixer.music.get_busy(): Returns false value when we stop, exits the while loop (music stops)
        # get_busy also causes the thread to quit, stop and destroy itself
        while current_time and mixer.music.get_busy():
            if self.paused:
                continue
                # continue ignores all the statement under else
            else:
                minutes, seconds = divmod(current_time, 60)
                minutes = round(minutes)
                seconds = round(seconds)
                duration = "{:02d}:{:02d}".format(minutes, seconds)
                remaining_Label["text"] = "Ends in" + "-" + duration
                time.sleep(1)  # subtract per second
                current_time -= 1  # subtracts 1 second from the total duration when music plays
# ------------------------------------------------------------------------------------------------------------------- #


paused = False


class Action:

    def __init__(self):
        self.mute = False
        self.statusbar = statusbar
        self.index = index

    def play(self):

        global paused

        if paused:
            mixer.music.unpause()
            self.statusbar["text"] = "Rezoom"
            # executed when paused is initialized. It resumes the music from the moment of paused.
            paused = False
        else:  # executed when paused not initialized
            self.stop()
            time.sleep(1)
            # lets the mp3 player buffer for 1 second to switch music if we don't click stop b4 switching
            selection = playlist.curselection()
            # identifies which music you are selecting in the playlist
            # Returns the value of the index in the listbox in a tuple
            selection = int(selection[0])  # type casted the tuple into a int value to match index
            play_selection = play_List[selection]  # retrieve song and store it under play_selection
            mixer.music.load(play_selection)
            # loads any music file you choose to open
            # requires the whole path name to load
            mixer.music.play()
            self.statusbar["text"] = "Playing music" + "-" + os.path.basename(play_selection)
            # edits the label for status bar to playing music + filename
            # os.path.basename removes the path of the file and displays only the name of the file
            Time().music_duration(play_selection)

    def stop(self):

        mixer.music.stop()
        self.statusbar["text"] = "Don't Stop me Now! :("
        # edits the label for status bar to music stopped

    def pause(self):

        global paused

        paused = True  # not needed
        mixer.music.pause()
        self.statusbar["text"] = "le Music is Paused"

    def next_music(self):

        global play_List

        self.stop()
        time.sleep(1)
        self.index += 1
        nextt = play_List[self.index]
        mixer.music.load(nextt)
        mixer.music.play()
        self.statusbar["text"] = "Thank u, next"
        Time().music_duration(nextt)

    def previous_music(self):

        global play_List

        self.stop()
        time.sleep(1)
        self.index -= 1
        previouss = play_List[self.index]
        mixer.music.load(previouss)
        mixer.music.play()
        self.statusbar["text"] = "I want U back"
        Time().music_duration(previouss)

    def rewind(self):

        self.play()
        self.statusbar["text"] = "Again and again and AGAIN"

    def set_vol(self, value):

        vol = float(value) / 100
        mixer.music.set_volume(vol)
        # set_vol only takes values from 0 to 1
        # dividing by 100 to get a float value that can be interpreted by the set_volume function

    def muted(self):

        global previousVol
        global volPic
        global volumeButton
        global mutePic

        if self.mute:  # un-mute Music
            mixer.music.set_volume(previousVol*0.01)  # to make it easier to interpret value
            volumeButton.configure(image=volPic)
            volume.set(previousVol)  # sets the volume back to previous setting
            self.mute = False
        else:  # mute music
            mixer.music.set_volume(0)  # mute music
            volumeButton.configure(image=mutePic)  # changes the image when clicked
            previousVol = volume.get()  # gets the value of volume before muted
            volume.set(0)
            self.mute = True

# ------------------------------------------------------------------------------------------------------------------- #


"""Creating a Button for the main buttons"""
# Button frame contains the play, pause and stop Music buttons
buttonFrame = Frame(middleFrame, relief=RAISED)
# acts as a grouper so whatever you edit on this frame will not affect the entire window
buttonFrame.configure(background="#fbf7f5")
buttonFrame.pack(padx=15, pady=20)
# pad parameter creates space for the three buttons
# grid system automatically gives space on the sides so no need for padx

playPic = PhotoImage(file="Icon images/play.png")
playButton = Button(buttonFrame, image=playPic, command=Action().play)
# creating a button and linking it to a specific function
playButton.grid(row=0, column=2, padx=5)

stopPic = PhotoImage(file="Icon images/stop.png")
stopButton = Button(buttonFrame, image=stopPic, command=Action().stop)
stopButton.grid(row=0, column=3, padx=5)
# stopButton.pack(side = LEFT, padx = 5)
# pack parameter arranges/aligns the widgets vertically automatically

pausePic = PhotoImage(file="Icon images/pause.png")
pauseButton = Button(buttonFrame, image=pausePic, command=Action().pause)
pauseButton.grid(row=0, column=1, padx=5)

nextPic = PhotoImage(file="Icon images/next.png")
nextButton = Button(buttonFrame, image=nextPic, command=Action().next_music)
nextButton.grid(row=0, column=4, padx=5)

previousPic = PhotoImage(file="Icon images/previous.png")
previousButton = Button(buttonFrame, image=previousPic, command=Action().previous_music)
previousButton.grid(row=0, column=0, padx=5)

# ------------------------------------------------------------------------------------------------------------------- #


"""Creating the Bottom Frame"""
# Bottom frame contains the volume, mute and rewind feature
bottomFrame = Frame(middleFrame)
bottomFrame.configure(background="#fbf7f5")
bottomFrame.pack(padx=15, pady=15)

rewindPic = PhotoImage(file="Icon images/rewind.png")
rewindButton = ttk.Button(bottomFrame, image=rewindPic, command=Action().rewind)
rewindButton.grid(row=0, column=0)

mutePic = PhotoImage(file="Icon images/mute.png")
volPic = PhotoImage(file="Icon images/speaker.png")
volumeButton = ttk.Button(bottomFrame, image=volPic, command=Action().muted)
volumeButton.grid(row=0, column=1)

# Scale() creates a scale widget, min to max vol, orientation = horizontal, link to function
volume = ttk.Scale(bottomFrame, from_=0, to=100, orient=HORIZONTAL, command=Action().set_vol)
volume.set(50)  # sets the scale bar to 50
mixer.music.set_volume(0.5)  # setting a default value when program is excecuted
volume.grid(row=0, column=2, pady=20, padx=25)

# ------------------------------------------------------------------------------------------------------------------- #


window.protocol("WM_DELETE_WINDOW", quitting)
# protocol handler tells the x button what to do
window.mainloop()
# makes sure the window doesn't disappear