import psutil
import PIL
import os
import win32gui
from datetime import datetime


def isGameRunning():
    return "League of Legends.exe" in (p.name() for p in psutil.process_iter())


def getPixel(x, y):
    return PIL.ImageGrab.grab().load()[x, y]


def centerClient():
    try:
        # Speichert den Client um diesen nach dem Game im Vordergrund zu haben
        leagueClient = win32gui.FindWindow(0, "League of Legends")
        win32gui.SetForegroundWindow(leagueClient)
        win32gui.BringWindowToTop(leagueClient)
        win32gui.MoveWindow(leagueClient, 50, 50, 1280, 720, True)
    except():
        return False
    return True


def centerGame():
    try:
        # Bringt Spiel in den Vordergrund, wenn es begonnen hat
        leagueGame = win32gui.FindWindow(0, "League of Legends (TM) Client")
        win32gui.MoveWindow(leagueGame, 50, 50, 1280, 800, True)
        win32gui.SetForegroundWindow(leagueGame)
        win32gui.BringWindowToTop(leagueGame)
    except():
        return False
    return True


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
