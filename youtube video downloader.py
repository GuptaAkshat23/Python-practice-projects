from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = Youtube(url)
        streams = yt.streams.filter(progressive = True, file_extension ="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path = save_path)
        print("Video Downloaded Successfully")
    except Exception as e:
        print(e)


def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder
            
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    url = input("Enter the URL of the video you want to download: ")
    save_path = open_file_dialog()

    if save_path:
        print("Starting download")
        download_video(url, save_path)
    else:
        print("No folder selected")