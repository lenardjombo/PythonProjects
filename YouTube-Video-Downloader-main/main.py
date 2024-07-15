import tkinter
import customtkinter
from pytube import YouTube
def startdownload():
    try:
        ytlink = link.get()
        youtubeobject = YouTube(ytlink,on_progress_callback=on_progress)
        video = youtubeobject.streams.get_highest_resolution()
        
        title.configure(text = youtubeobject.title, text_color = "white")
        video.download()
        finish_Label.configure(text="Download Complete")
    except:
        finish_Label.configure(text='Invalid YouTubeLink',text_color = "red")
 
def on_progress(stream,chunk,bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size *100
    per = str(int(percentage_of_completion)) 
    pPercaentage.configure(text = per + '%')
    pPercaentage.update()
    
#system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Video Downloader")

#Adding UI elements
title = customtkinter.CTkLabel(app,text="Insert a YouTube Link")
title.pack(padx = 15,pady = 15)

#link input 
url_variable = tkinter.StringVar()

link = customtkinter.CTkEntry(app,width=350,height=45,textvariable=url_variable)
link.pack()

#finished downloading
finish_Label=  customtkinter.CTkLabel(app,text="")
finish_Label.pack(padx = 15,pady = 15)

#progress percentage
pPercaentage = customtkinter.CTkLabel(app,text = "0%")
pPercaentage.pack()

progressBar = customtkinter.CTkProgressBar(app,width=400)
progressBar.set(0)
progressBar.pack(padx = 15,pady = 15)


download = customtkinter.CTkButton(app,text="Download",command=startdownload)
download.pack(padx = 15,pady = 15)
#Run app
app.mainloop()