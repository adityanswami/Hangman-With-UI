from distutils.core import setup # Need this to handle modules
import py2exe
import random
# import tkinter
import tkinter

setup(
    options = {'py2exe': {'bundle_files': 2, 'compressed': True}},
    window = [{'script': "hangman.py",
               'icon_resources': [ (0, "icon.ico")]}],
    zipfile = None,
)