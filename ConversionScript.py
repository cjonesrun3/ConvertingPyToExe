import cx_Freeze
import os
import sys
from cx_Freeze import Executable
from cx_Freeze import setup

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

os.environ['TCL_LIBRARY'] = 'c:\\users\\Your user name\\AppData\\local\\programs\\python\\Python36-32\\tcl\\tcl8.6'
os.environ['TK_LIBRARY'] = 'c:\\users\\Your user name\\AppData\\local\\programs\\python\\python36-32\\tcl\\tk8.6'



executables = [Executable(script='name of py file.py', base=base, icon='.ico name')]

file_one = 'c:\\users\\your user name\\AppData\\local\\programs\\python\\python36-32\\DLLs\\tcl86t.dll'
file_two = 'c:\\users\\your user name\\AppData\\local\\programs\\python\\python36-32\\DLLs\\tk86t.dll'

setup(
    name='HourGlassRequests',
    options={'build_exe': {"packages": ['tkinter'], 'include_files': [file_one, file_two, '.ico name']}},
    version='2019.1',
    description='Prototype',
    executables=executables

)

"""
If using a .ico, ensure that it's a try .ico image. Otherwise, your .py file will compile, but your .ico image will not work. There will also be no error message available 
and compilation will still occur. 
"""
