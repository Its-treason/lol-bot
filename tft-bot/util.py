import os
from datetime import datetime
from time import sleep
import psutil
import pyautogui
from coordinates import Coordinates
import sys
import configparser
from traceback import format_exc


def isGameRunning():
    return "League of Legends.exe" in (p.name() for p in psutil.process_iter())


def mouseClick(cords=None, button='left'):
    if cords is not None:
        pyautogui.moveTo(cords.x, cords.y)
    elif cords is not Coordinates:
        raise Exception('cords must be of Type Coordinates')

    try:
        # MouseUp before MouseDown to make sure the mouse is Up
        pyautogui.mouseUp(button=button)
        pyautogui.mouseDown(button=button)
        sleep(0.1)
        pyautogui.mouseUp(button=button)
    except Exception:
        logError(format_exc())


def focusClient():
    windows = pyautogui.getWindowsWithTitle("League of Legends")
    if 0 == len(windows):
        return False

    window = windows[0]
    try:
        window.restore()
        window.show()
        window.activate()
    except Exception:
        logError(format_exc())
    return window


def focusGame():
    windows = pyautogui.getWindowsWithTitle("League of Legends (TM) Client")
    if 0 == len(windows):
        return False

    window = windows[0]
    try:
        window.restore()
        window.show()
        window.activate()
    except Exception:
        logError(format_exc())
    return window


def getCordsWithImage(image, confidence=0.8, grayscale=False, window=None):
    image = getResourcePath(image)

    btn = None
    try:
        if window is not None:
            btn = pyautogui.locateOnWindow(image, window.title, confidence=confidence, grayscale=grayscale)
        else:
            btn = pyautogui.locateOnScreen(image, confidence=confidence, grayscale=grayscale)
    except Exception:
        pass

    if btn is None:
        return False

    return Coordinates(btn.left + (btn.width / 2), btn.top + (btn.height / 2))


def formatConsole():
    os.system('cls')

    version = getEnvVar('version')
    if version is None:
        version = 'vDEV'
    buildNumber = getEnvVar('buildNumber')
    if buildNumber is None:
        buildNumber = 'Not available'

    welcome = """
Build-Checksum: %s
  ______ ______ ______      ____          __
 /_  __// ____//_  __/     / __ ) ____   / /_
  / /  / /_     / /______ / __  |/ __ \ / __/
 / /  / __/    / //_____// /_/ // /_/ // /_
/_/  /_/      /_/       /_____/ \____/ \__/
  github.com/its-treason/lol-bot - %s
""" % (buildNumber, version)
    print(welcome)


def log(loc='', msg=''):
    if loc != '':
        loc = '[' + loc + '] '

    date = '[' + datetime.today().strftime('%Y-%m-%d %H:%M:%S') + '] '

    print(date + loc + msg)


def logError(errorMsg):
    log('Error', 'An Error occurred during execution')
    print("""
    ======== Start of Debug output ========
    %s
    ======== End of Debug output ========
    If this happens more frequently, report this error at https://github.com/Its-treason/lol-bot/issues
    """ % errorMsg)


def getResourcePath(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')

    return os.path.join(base_path, relative_path)


def getEnvVar(var):
    if not os.path.exists(getResourcePath('build/build.ini')):
        return None

    conf = configparser.ConfigParser()
    conf.read(getResourcePath('build/build.ini'))

    if var in conf['build']:
        return conf['build'][var]

    return None
