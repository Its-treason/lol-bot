import os
import shutil
import sys
from cx_Freeze import setup, Executable

__version__ = '1.0.0'
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

include_files = ['images']
includes = []
excludes = []
packages = ['pyautogui', 'time', 'datetime', 'pyautogui', 'cv2', 'psutil']

setup(
    name='Tft-Bot',
    description='A bot for TFT',
    version=__version__,
    executables=[Executable('main.py', base=base)],
    options={'build_exe': {
        'packages': packages,
        'includes': includes,
        'include_files': include_files,
        'include_msvcr': True,
        'excludes': excludes,
    }},
)

path = os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir))
build_path = os.path.join(path, 'build', 'exe.win32-3.7')
