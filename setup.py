from cx_Freeze import setup, Executable
import sys
import os

base = None

if sys.platform == 'win32':
    base = "Win32GUI"
    
os.environ['TCL_LIBRARY'] = r"C:\Users\Arpan20\OneDrive\Desktop\Python\Projects\Youtube downloader\python3"
os.environ['TCL_LIBRARY'] = r"C:\Users\Arpan20\OneDrive\Desktop\Python\Projects\Youtube downloader\python39"


executables = [Executable("Youtube Video Downloader.py", base=base, icon = "icon.ico")]

packages = ["idna"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "Youtube Downloader",
    options = {"build_exe":{"packages":["tkinter","os"],"include_files":["icon.ico", 'python3.dll','python39.dll']}},
    version = "<1.0.1>",
    description = '<This is the free youtube downloader, By this application you should able to Download the videos from YouTube. Thankyou>',
    executables = executables
)