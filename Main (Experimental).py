import os
import subprocess
import tkinter
import tkinter.messagebox
import tkinter.ttk
import requests
import sys
import fnmatch
from text_entry_fix import text_entry_fix

# declarations
global ffmpeg_folder
global ytdlp_name
global lines
current_folder = os.getcwd()
language_pack, languages_detected = [], []


# startup checks definitions
# connectivity check
def check_connectivity():
    try:
        requests.get("https://www.google.com")
        return True
    except:
        return False


# yt-dlp check
def check_ytdlp():
    try:
        global ytdlp_name
        ytdlp_name = (fnmatch.filter(os.listdir(), "*yt*dlp*"))[0]
        return True
    except IndexError:
        return False


# ffmpeg check
def check_ffmpeg():
    try:
        global ffmpeg_folder
        ffmpeg_folder = (fnmatch.filter(os.listdir(current_folder), "*ffmpeg*"))[0]
        return True
    except IndexError:
        return False


# startup checks executions
# connectivity check
if not check_connectivity():
    tkinter.messagebox.showinfo(title="YouTube Downloader/Converter by Lee", message="You have no internet connection.")
    sys.exit()

# yt-dlp check
if not check_ytdlp():
    tkinter.messagebox.showinfo(title="YouTube Downloader/Converter by Lee", message="yt-dlp.exe is missing.")
    sys.exit()

# ffmpeg check
if not check_ffmpeg():
    tkinter.messagebox.showinfo(title="YouTube Downloader/Converter by Lee", message="ffmpeg folder is missing.")
    sys.exit()


# main definitions
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
        subprocess.run('"{}\\{}" {} --no-playlist -P "{}\\Downloaded Videos"'.format(current_folder, ytdlp_name, link, current_folder))
        os.startfile(current_folder + '\\Downloaded Videos')
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
        subprocess.run('"{}\\{}" {} -P "{}\\Downloaded Videos"'.format(current_folder, ytdlp_name, link, current_folder))
        os.startfile(current_folder + '\\Downloaded Videos')
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
        subprocess.run('"{}\\{}" --ffmpeg-location "{}/{}/bin" {} --no-playlist -x --audio-format mp3 --audio-quality 0 -P "{}\\Converted Audio"'.format(current_folder, ytdlp_name, current_folder, ffmpeg_folder, link, current_folder))
        os.startfile(current_folder + '\\Converted Audio')
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
        subprocess.run('"{}\\{}" --ffmpeg-location "{}/{}/bin" {} -x --audio-format mp3 --audio-quality 0 -P "{}\\Converted Audio"'.format(current_folder, ytdlp_name, current_folder, ffmpeg_folder, link, current_folder))
        os.startfile(current_folder + '\\Converted Audio')
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


# =================================================================================
# =================================================================================


# language files processing, checks for validity of the read .txt files, and stores their contents in lists named by the first 2 letters of the language name
for file_name in os.listdir(current_folder):
    info_from_file = {}
    if file_name.endswith('.txt'):
        with open(os.path.join(current_folder, file_name), 'r') as fp:
            lines = fp.readlines()
        for line in lines:
            parts = line.strip().split('=')
            if len(parts) == 2:
                info_from_file[parts[0]] = parts[1]
        language_pack.append(info_from_file)
for i in range(len(language_pack)):
    languages_detected.append(language_pack[i]['lang'])


# language selection, and application
def language_select(event):
    language_selected = languages_detected.index(language_drop_down_list.get(), 0)
    print(language_selected)
    label.config(text=language_pack[language_selected]['label'])
    clear_button.config(text=language_pack[language_selected]['clear_button'])
    download_button.config(text=language_pack[language_selected]['download_button'])
    download_playlist_button.config(text=language_pack[language_selected]['download_playlist_button'])
    convert_button.config(text=language_pack[language_selected]['convert_button'])
    convert_playlist_button.config(text=language_pack[language_selected]['convert_playlist_button'])


# =================================================================================
# =================================================================================


# gui
# main window
root = tkinter.Tk()
root.geometry("800x150")
root.bind_all("<Key>", text_entry_fix, "+")

# gui window
main_window = tkinter.Frame(root)
main_window.pack()

# title bar
root.title("YouTube Downloader/Converter by Lee")

# label at the top of the window
label = tkinter.Label(main_window, text="Enter a YouTube link:", font=('*Font', 24))
label.pack(side=tkinter.TOP)

# textbox
entry_box = tkinter.Entry(main_window, width=25, font=('*Font', 18))
entry_box.pack(side=tkinter.LEFT, fill=tkinter.X, padx=5, pady=5)

# clear textbox button
clear_button = tkinter.Button(main_window, width=10, text="Clear", font=('*Font', 16), command=clear)
clear_button.pack(side=tkinter.RIGHT, padx=5, pady=5)

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

# language drop-down menu
language_drop_down_list = tkinter.ttk.Combobox(main_window, width=10, font=('*Font', 12), state="readonly", values=languages_detected)
language_drop_down_list.bind("<<ComboboxSelected>>", language_select)
language_drop_down_list.pack(side=tkinter.RIGHT, padx=5, pady=5)

root.mainloop()
