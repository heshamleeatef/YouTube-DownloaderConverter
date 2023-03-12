import os
import subprocess
import tkinter
import tkinter.messagebox
import tkinter.ttk
import requests
import sys
import fnmatch
import text_entry_fix

# declarations
current_folder = os.getcwd()
global ffmpeg_folder
global ytdlp_name
global lines
languages_present = []


# startup checks definitions
# connectivity check
def check_connectivity():
    try:
        requests.get("http://www.google.com")
        return True
    except:
        return False


# yt-dlp check
# def check_ytdlp():
#     try:
#         global ytdlp_name
#         ytdlp_name = (fnmatch.filter(os.listdir(), "*yt*dlp*"))[0]
#         return True
#     except IndexError:
#         return False


# ffmpeg check
# def check_ffmpeg():
#     try:
#         global ffmpeg_folder
#         ffmpeg_folder = (fnmatch.filter(os.listdir(current_folder), "*ffmpeg*"))[0]
#         return True
#     except IndexError:
#         return False


# startup checks executions
# connectivity check
if not check_connectivity():
    tkinter.messagebox.showinfo(title="YouTube Downloader/Converter by Lee", message="You have no internet connection.")
    sys.exit()

# yt-dlp check
# if not check_ytdlp():
#     tkinter.messagebox.showinfo(title="YouTube Downloader/Converter by Lee", message="yt-dlp.exe is missing.")
#     sys.exit()

# ffmpeg check
# if not check_ffmpeg():
#     tkinter.messagebox.showinfo(title="YouTube Downloader/Converter by Lee", message="ffmpeg folder is missing.")
#     sys.exit()


# main definitions
# get path
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# download function
def download():
    link = entry_box.get()
    link_criteria1 = "youtube.com/"
    link_criteria2 = "watch"
    link_criteria3 = "youtube-nocookie.com/embed/"
    link_criteria4 = "youtube.com/embed"
    link_criteria5 = "youtube.com/v/"
    link_criteria6 = "youtube.com/e/"
    link_criteria7 = "youtu.be/"
    if (link_criteria1 and link_criteria2 in link) or \
            link_criteria3 in link or \
            link_criteria4 in link or \
            link_criteria5 in link or \
            link_criteria6 in link or \
            link_criteria7 in link:
        # subprocess.run('"{}\\{}" {} --no-playlist -P "{}\\Downloaded Videos"'.format(current_folder, ytdlp_name, link, current_folder))
        subprocess.run('"{}" {} --no-playlist -P "{}\\Downloaded Videos"'.format(resource_path("yt-dlp.exe"), link, current_folder))
        # os.startfile(current_folder + '\\Downloaded Videos')
        clear()
    else:
        tkinter.messagebox.showinfo(title="YouTube Downloader/Converter by Lee", message="Please, enter a valid link.")
        clear()


# download playlist function
def download_playlist():
    link = entry_box.get()
    link_criteria1 = "youtube.com/"
    link_criteria2 = "watch"
    link_criteria3 = "list"
    link_criteria4 = "youtu.be/"
    link_criteria5 = "list"
    if (link_criteria1 and link_criteria2 and link_criteria3 in link) or \
            (link_criteria4 and link_criteria5 in link):
        # subprocess.run('"{}\\{}" {} -P "{}\\Downloaded Videos"'.format(current_folder, ytdlp_name, link, current_folder))
        subprocess.run('"{}" {} -P "{}\\Downloaded Videos"'.format(resource_path("yt-dlp.exe"), link, current_folder))
        # os.startfile(current_folder + '\\Downloaded Videos')
        clear()
    elif link_criteria1 in link:
        tkinter.messagebox.showinfo(title="YouTube Downloader/Converter by Lee", message="Please, enter a valid playlist link.")
        clear()
    else:
        tkinter.messagebox.showinfo(title="YouTube Downloader/Converter by Lee", message="Please, enter a valid link.")
        clear()


# convert function
def convert():
    link = entry_box.get()
    link_criteria1 = "youtube.com/"
    link_criteria2 = "watch"
    link_criteria3 = "youtube-nocookie.com/embed/"
    link_criteria4 = "youtube.com/embed"
    link_criteria5 = "youtube.com/v/"
    link_criteria6 = "youtube.com/e/"
    link_criteria7 = "youtu.be/"
    if (link_criteria1 and link_criteria2 in link) or \
            link_criteria3 in link or \
            link_criteria4 in link or \
            link_criteria5 in link or \
            link_criteria6 in link or \
            link_criteria7 in link:
        # subprocess.run('"{}\\{}" --ffmpeg-location "{}/{}/bin" {} --no-playlist -x --audio-format mp3 --audio-quality 0 -P "{}\\Converted Audio"'.format(current_folder, ytdlp_name, current_folder, ffmpeg_folder, link, current_folder))
        subprocess.run('"{}" --ffmpeg-location "{}" {} --no-playlist -x --audio-format mp3 --audio-quality 0 -P "{}\\Converted Audio"'.format(resource_path("yt-dlp.exe"), resource_path("ffmpeg\\bin"), link, current_folder))
        # os.startfile(current_folder + '\\Converted Audio')
        clear()
    else:
        tkinter.messagebox.showinfo(title="YouTube Downloader/Converter by Lee", message="Please, enter a valid link.")
        clear()


# convert playlist function
def convert_playlist():
    link = entry_box.get()
    link_criteria1 = "youtube.com/"
    link_criteria2 = "watch"
    link_criteria3 = "list"
    link_criteria4 = "youtu.be/"
    link_criteria5 = "list"
    if (link_criteria1 and link_criteria2 and link_criteria3 in link) or \
            (link_criteria4 and link_criteria5 in link):
        # subprocess.run('"{}\\{}" --ffmpeg-location "{}/{}/bin" {} -x --audio-format mp3 --audio-quality 0 -P "{}\\Converted Audio"'.format(current_folder, ytdlp_name, current_folder, ffmpeg_folder, link, current_folder))
        subprocess.run('"{}" --ffmpeg-location "{}" {} -x --audio-format mp3 --audio-quality 0 -P "{}\\Converted Audio"'.format(resource_path("yt-dlp.exe"), resource_path("ffmpeg\\bin"), link, current_folder))
        # os.startfile(current_folder + '\\Converted Audio')
        clear()
    elif link_criteria1 in link:
        tkinter.messagebox.showinfo(title="YouTube Downloader/Converter by Lee", message="Please, enter a valid playlist link.")
        clear()
    else:
        tkinter.messagebox.showinfo(title="YouTube Downloader/Converter by Lee", message="Please, enter a valid link.")
        clear()


# clear function
def clear():
    entry_box.delete(0, tkinter.END)


# open videos folder function
def open_videos():
    os.startfile(current_folder + '\\Downloaded Videos')


# open audio folder function
def open_audio():
    os.startfile(current_folder + '\\Converted Audio')


# read string after = symbol
def get_second_part(word):
    return word.split("=")[1]


# language files check, to read any .txt file in current directory
language_files_list = fnmatch.filter(os.listdir(current_folder), "*.txt")

# language files processing, checks for validity of the read .txt files, and stores their contents in lists named by the first 2 letters of the language name
for a in range(len(language_files_list)):
    with open(current_folder + '\\' + language_files_list[a], 'r') as current_file:
        lines = []
        for b, line in enumerate(current_file):
            lines.append(line.strip())
        vars()[(get_second_part(lines[2])[:2])] = lines
        if lines[0] == "YouTube Downloader/Converter by Lee":
            if lines[1] == "ver=0.4":
                if lines[13] == "end":
                    languages_present.append(get_second_part(lines[2]))


# language selection, and application
def language_select(event):
    language_selected = languages_present.index(language_drop_down_list.get(), 0)
    for a in range(len(language_files_list)):
        with open(current_folder + '\\' + language_files_list[a], 'r') as current_file:
            lines = []
            for b, line in enumerate(current_file):
                lines.append(line.strip())
            vars()[(get_second_part(lines[2])[:2])] = lines
            if lines[0] == "YouTube Downloader/Converter by Lee":
                if lines[1] == "ver=0.4":
                    if lines[13] == "end":
                        languages_present.append(get_second_part(lines[2]))
    label.config(text=get_second_part(vars()[languages_present[language_selected][:2]][4]))
    clear_button.config(text=get_second_part(vars()[languages_present[language_selected][:2]][5]))
    download_button.config(text=get_second_part(vars()[languages_present[language_selected][:2]][6]))
    download_playlist_button.config(text=get_second_part(vars()[languages_present[language_selected][:2]][7]))
    convert_button.config(text=get_second_part(vars()[languages_present[language_selected][:2]][8]))
    convert_playlist_button.config(text=get_second_part(vars()[languages_present[language_selected][:2]][9]))
    open_videos_button.config(text=get_second_part(vars()[languages_present[language_selected][:2]][10]))
    open_audio_button.config(text=get_second_part(vars()[languages_present[language_selected][:2]][11]))


# gui
# main window
root = tkinter.Tk()
root.geometry("800x200")
root.bind_all("<Key>", text_entry_fix.text_entry_fix, "+")

# gui window
main_window = tkinter.Frame(root)
main_window.pack()
topframe = tkinter.Frame(root)
topframe.pack(side=tkinter.TOP)
leftframe = tkinter.Frame(root)
leftframe.pack(side=tkinter.LEFT)
rightframe = tkinter.Frame(root)
rightframe.pack(side=tkinter.RIGHT)
bottomframe = tkinter.Frame(root)
bottomframe.pack(side=tkinter.BOTTOM)

# title bar
root.title("YouTube Downloader/Converter by Lee")

# label at the top of the window
label = tkinter.Label(topframe, text="Enter a YouTube link:", font=('*Font', 24))
label.pack(side=tkinter.TOP)

# textbox
entry_box = tkinter.Entry(topframe, width=25, font=('*Font', 18))
entry_box.pack(side=tkinter.LEFT, fill=tkinter.X, padx=5, pady=5)

# language drop-down menu
language_drop_down_list = tkinter.ttk.Combobox(topframe, width=10, font=('*Font', 12), state="readonly", values=languages_present)
language_drop_down_list.bind("<<ComboboxSelected>>", language_select)
language_drop_down_list.pack(side=tkinter.LEFT, padx=5, pady=5)

# clear textbox button
clear_button = tkinter.Button(topframe, width=10, text="Clear", font=('*Font', 16), command=clear)
clear_button.pack(side=tkinter.LEFT, padx=5, pady=5)

# download button
download_button = tkinter.Button(root, width=15, text="Download", font=('*Font', 16), command=download)
download_button.pack(side=tkinter.LEFT, padx=5, pady=5)

# download playlist button
download_playlist_button = tkinter.Button(root, width=15, text="Download playlist", font=('*Font', 16), command=download_playlist)
download_playlist_button.pack(side=tkinter.LEFT, padx=5, pady=5)

# convert button
convert_button = tkinter.Button(root, width=15, text="Convert", font=('*Font', 16), command=convert)
convert_button.pack(side=tkinter.LEFT, padx=5, pady=5)

# convert playlist button
convert_playlist_button = tkinter.Button(root, width=15, text="Convert playlist", font=('*Font', 16), command=convert_playlist)
convert_playlist_button.pack(side=tkinter.LEFT, padx=5, pady=5)

# open videos button
open_videos_button = tkinter.Button(bottomframe, width=15, text="Open Videos Folder", font=('*Font', 16), command=open_videos)
open_videos_button.pack(side=tkinter.LEFT, padx=5, pady=5)

# open audio button
open_audio_button = tkinter.Button(bottomframe, width=15, text="Open Audio Folder", font=('*Font', 16), command=open_audio)
open_audio_button.pack(side=tkinter.LEFT, padx=5, pady=5)

root.mainloop()
