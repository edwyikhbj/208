import socket
from threading import Thread
from tkinter import *
from tkinter import ttk, filedialog

SERVER = None
IP_ADDRESS = '127.0.0.1'
PORT = 8050
BUFFER_SIZE = 4096

font = "Calibri"

def musicWindow():
  window = Tk()
  window.title("Music Window")
  window.geometry("300x300")
  window.configure(bg="#87CEFA")

  selectLabel = Label(window, text="Select Song", bg="#87CEFA", font=(font, 8))
  selectLabel.place(x=2, y=1)

  listbox = Listbox(window, height=10, width=39, activestyle="dotbox", bg="#87CEFA", borderwidth=2, font=(font, 10))
  listbox.place(x=10, y=18)

  scrollbar1 = Scrollbar(listbox)
  scrollbar1.place(relheight=1, relx=1)
  scrollbar1.config(command=listbox.yview)

  playButton = Button(window, text="Play", width=10, bg="#87CEEB", bd=1, font=(font, 10))
  playButton.place(x=30, y=200)

  stopButton = Button(window, text="Stop", width=10, bg="#87CEEB", bd=1, font=(font, 10))
  stopButton.place(x=200, y=200)

  uploadButton = Button(window, text="Upload", width=10, bg="#87CEEB", bd=1, font=(font, 10))
  uploadButton.place(x=30, y=250)

  downloadButton = Button(window, text="Download", width=10, bg="#87CEEB", bd=1, font=(font, 10))
  downloadButton.place(x=200, y=250)

  infoLabel = Label(window, text="", fg="#00F", font=(font, 8))
  infoLabel.place(x=4, y=200)

  window.mainloop()


def setup():
  global SERVER, IP_ADDRESS, PORT
  SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  SERVER.connect((IP_ADDRESS, PORT))

  musicWindow()

setup()