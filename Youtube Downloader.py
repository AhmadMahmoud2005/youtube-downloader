from pytube import YouTube
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

def download():
    download_button.config(state=DISABLED)
    label_of_download = Label(root, text=f"Wait for download...")
    label_of_download.grid(row=9, column=0)
    root.update_idletasks()
    link_path = entry2.get()
    link_video = entry1.get()
    clip = YouTube(link_video)
    if combo_path.get() == "video":
        clip.streams.filter(progressive=True, res=combo_quality.get()).first().download(output_path=link_path)
    else:
        clip.streams.filter(progressive=False, type=combo_path.get(), abr='160kbps').first().download(output_path=link_path)
    messagebox.showinfo("Success", f'The Download is finished Successfully, you will find your video at:\n{link_path}')
    label_of_download.destroy()
    download_button['state'] = NORMAL


def selectedcombo(event):
    if combo_path.get() == "audio":
        combo_quality.config(state=DISABLED)
    else:
        combo_quality.config(state=NORMAL)

def browse():
    root.filename = filedialog.askdirectory(initialdir="This PC", title="Browse the path")
    entry2.insert(0, root.filename)


# set the window of app
root = Tk()
root.geometry('525x300')
root.title('Youtube Downloader')
label_of_entry = Label(root, text="Enter the video link: ")
label_of_entry.grid(row=0, column=0) # label of entry

label_space = Label(root, text=" ")
label_space.grid(row=1, column=0) # space

label_combo_path = Label(root, text="Choose the video type:")
label_combo_path.grid(row=2, column=0) # label of combobox of the type of the video

label_space = Label(root, text=" ")
label_space.grid(row=3, column=0) # space

label_combo_quality = Label(root, text="Choose the video quality:")
label_combo_quality.grid(row=4, column=0) # label of combobox of the quality

label_space = Label(root, text=" ")
label_space.grid(row=5, column=0) # space

label_entry2 = Label(root, text="Enter the video path:")
label_entry2.grid(row=6, column=0)

label_space = Label(root, text=" ")
label_space.grid(row=7, column=0) # space

entry1 = Entry(root, width=50)
entry1.grid(row=0, column=1) # entry of the video link

entry2 = Entry(root, width=40)
entry2.grid(row=6, column=1) # entry of the video Path in the device

combo_path = ttk.Combobox(root, values=("video", "audio"))
combo_path.set("video")
combo_path.bind("<<ComboboxSelected>>", selectedcombo)
combo_path.grid(row=2, column=1) # combobox of the type of the video

combo_quality = ttk.Combobox(root, values=("144p", "360p", "720p"))
combo_quality.grid(row=4, column=1) # combobox of the quality of the video
combo_quality.set("360p")

download_button = ttk.Button(root, text="Download", width=20, command=download)
download_button.grid(row=8, column=1) # download button

browse_button = ttk.Button(root, text="Browse", command=browse)
browse_button.grid(row=6, column=2) # browse button

root.mainloop()
