import tkinter as tk
from tkinter import ttk

from tkinter import filedialog
from moviepy.editor import VideoFileClip
import os

root = tk.Tk()

def convert_to_gif():
    file_path = filedialog.askopenfilename()
    video_clip = VideoFileClip(file_path)

    label = tk.Label(root, text="{}")
    video_clip.write_gif("output.gif") 
    message_label_window = tk.Toplevel(root)
    message_label_window.title("Finished")
    message_label_window.geometry("600x100") 
    message_label_window_label = tk.Label(message_label_window, text=f"File successfully generated and saved at \n{os.getcwd()}/output.gif")
    message_label_window_label.pack(pady=10)


root.geometry("500x200")

label = tk.Label(root, text="video2gif")
label.pack(pady=10)

select_button = tk.Button(root, text="Select Video File", command=convert_to_gif)
select_button.pack(pady=10)

root.mainloop()

