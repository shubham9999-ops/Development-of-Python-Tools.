# Importing necessary packages
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog


# Defining CreateWidgets() function
# to create necessary tkinter widgets
def Widgets():
	head_label = Label(root, text="YouTube Video Downloader ",padx=12,pady=15,font="SegoeUI 20",bg="black",fg="White")
	head_label.grid(row=1,column=1,pady=10,padx=5)
	link_label = Label(root,text="YouTube Link :",bg="brown",fg="white",pady=5,padx=5)
	link_label.grid(row=2,column=0,pady=5,padx=7)
	root.linkText = Entry(root,width=35,textvariable=video_Link,font="Arial 14")					
	root.linkText.grid(row=2,column=1,pady=5,padx=7)
	destination_label = Label(root,text="Download Location :  ",bg="brown",fg="white",pady=5,padx=9)							
	destination_label.grid(row=3,column=0,pady=5,padx=5)
	root.destinationText = Entry(root,width=35,textvariable=download_Path,font="Arial 14")					
	root.destinationText.grid(row=3,column=1,pady=5,padx=7)
	browse_B = Button(root,text="Browse",command=Browse,width=10,bg="blue",fg="white",relief=GROOVE)
	browse_B.grid(row=3,column=2,pady=1,padx=20)
	Download_B = Button(root,text="Download Video",command=Download,width=20,bg="green",fg="white",pady=10,padx=15,relief=GROOVE,font="Georgia, 20")
	Download_B.grid(row=4,column=1,pady=20,padx=20)
	
def Browse():
	download_Directory = filedialog.askdirectory(
		initialdir="YOUR DIRECTORY PATH", title="Save Video")
	download_Path.set(download_Directory)

def Download():
	Youtube_link = video_Link.get()
	download_Folder = download_Path.get()
	getVideo = YouTube(Youtube_link)
	videoStream = getVideo.streams.first()
	videoStream.download(download_Folder)
	messagebox.showinfo("SUCCESSFULLY",
						"DOWNLOADED AND SAVED IN\n"
						+ download_Folder)
root = tk.Tk()
root.geometry("750x250")
root.resizable(False, False)
root.title("YouTube Video Downloader")
root.config(background="Black")
video_Link = StringVar()
download_Path = StringVar()
Widgets()
root.mainloop()

