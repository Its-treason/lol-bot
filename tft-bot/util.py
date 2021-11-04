import psutil
import PIL
import os
import win32gui
import pyautogui
from datetime import datetime
from coordinates import Coordinates


def isGameRunning():
    return "League of Legends.exe" in (p.name() for p in psutil.process_iter())


def getPixel(x, y):
    return PIL.ImageGrab.grab().load()[x, y]


def centerClient():
    try:
        # safe client to be in foreground after the match is finished
        leagueClient = win32gui.FindWindow(0, "League of Legends")
        win32gui.SetForegroundWindow(leagueClient)
        win32gui.BringWindowToTop(leagueClient)
        win32gui.MoveWindow(leagueClient, 50, 50, 1280, 720, True)
    except():
        return False
    return True


def centerGame():
    try:
        # get game in foreground when started
        leagueGame = win32gui.FindWindow(0, "League of Legends (TM) Client")
        #win32gui.MoveWindow(leagueGame, 50, 50, 1280, 800, True)
        #win32gui.SetForegroundWindow(leagueGame)
        #win32gui.BringWindowToTop(leagueGame)
    except():
        return False
    return True


def getCordsWithImage(image):
    btn = pyautogui.locateOnScreen(image, confidence=0.8)
    if btn is None:
        return False

    return Coordinates(btn.left + (btn.width / 2), btn.top + (btn.height / 2))


def formatConsole():
    os.system('cls')
    welcome = """
  ______ ______ ______      ____          __
 /_  __// ____//_  __/     / __ ) ____   / /_
  / /  / /_     / /______ / __  |/ __ \ / __/
 / /  / __/    / //_____// /_/ // /_/ // /_
/_/  /_/      /_/       /_____/ \____/ \__/
  github.com/its-treason/lol-bot - v11.22.1

"""
    print(welcome)


def log(loc='', msg=''):
    if loc != '':
        loc = '[' + loc + '] '

    date = '[' + datetime.today().strftime('%Y-%m-%d %H:%M:%S') + '] '

    print(date + loc + msg)
