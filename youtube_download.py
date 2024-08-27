from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def download_video(url, save_path, picture_quality):
    try:
        yt = YouTube(url, on_progress_callback=show_progress)
        streams = yt.streams.filter(progressive=True, file_extension='mp4', resolution=picture_quality)
        if streams:
            highest_res_stream = streams.get_highest_resolution()
            highest_res_stream.download(output_path=save_path)
            print("Video Downloaded successfully!")
        else:
            print(f"No video available with resolution '{picture_quality}'.")
    except Exception as e:
        print(e)

def show_progress(stream, chunk, bytes_remaining):
    total_bytes = stream.filesize
    bytes_downloaded = total_bytes - bytes_remaining
    percent = (bytes_downloaded / total_bytes) * 100
    print(f"Downloading... {percent:.2f}% complete", end='\r')

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected Folder: {folder}")
    
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a YouTube URL: ")
    save_dir = open_file_dialog()

    if save_dir:
        quality = input("Enter the desired picture quality (e.g., 480p, 720p): ")
        print("Download Starting.....")
        download_video(video_url, save_dir, quality)
    else:
        print("Invalid save location")






        
# from pytube import YouTube
# import tkinter as tk
# from tkinter import filedialog

# def download_video(url,save_path):
#     try:
#         yt = YouTube(url)
#         streams = yt.streams.filter(progressive=True,file_extension='mp4')
#         highest_res_stream = streams.get_highest_resolution()
#         highest_res_stream.download(output_path=save_path)
#         print("Video Downloaded succesfully!")
#     except Exception as e:
#         print(e)

# def open_file_dialog():
#     folder = filedialog.askdirectory()
#     if folder:
#         print(f"Selected Folder : {folder}")
    
#     return folder

# if __name__ == "__main__":
        
#     root = tk.Tk()
#     root.withdraw()

#     video_url = input("Please enter a YouTube URL: ")
#     save_dir = open_file_dialog()

#     if save_dir:
#         print("Started Download..... ")
#         download_video(video_url,save_dir)
#     else:
#         print("Invalid save location")



