import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", 'sys', 'PyQt5', 'csv'], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"


setup(  name = "my prog",
    version = "1.0",
    description = "My application!",
    options = {"build_exe": build_exe_options},
    executables = [Executable("kod (другая копия)2.py", base = base)])
input("Press Enter")
