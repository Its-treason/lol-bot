#! python3
import pyautogui as pg
import win32gui
from time import sleep
import psutil
import PIL
import util

class Coordinates:
    def __init__(self, xx, yy):
        self.x = xx
        self.y = yy

# Define Constans
TIME_BETWEEN = 0.3

# Define some Coordinates
StartMatchBtn = Coordinates(640, 730)
MatchAcceptBtn = Coordinates(690, 610)
BuyChampBtn = Coordinates(400, 800)
LevelUpBtn = Coordinates(250, 760)
Pos1 = Coordinates(400, 270)
Pos2 = Coordinates(1000, 480)
Pos3 = Coordinates(900, 260)
Poses = [Pos2, Pos1, Pos3]
ExitMatchBtn = Coordinates(600, 460)
ContinueBtn = Coordinates(690, 525)
Item1 = Coordinates(195, 605)
Item2 = Coordinates(220, 580)
Item3 = Coordinates(205, 555)
Item4 = Coordinates(235, 540)
Item5 = Coordinates(220, 515)
Item6 = Coordinates(230, 485)
Items = [Item1, Item2, Item3, Item4, Item5, Item6]
Champ1 = Coordinates(690, 525)
Champ2 = Coordinates(635, 470)
Champ3 = Coordinates(690, 400)
Champs = [Champ1, Champ2, Champ3]

# Distanz zwischen den Champs im Shop
ChampDistance = 150


def StartMatch():
    pg.moveTo(MatchAcceptBtn.x, MatchAcceptBtn.y, 1)
    pg.click()
    sleep(TIME_BETWEEN)
    pg.moveTo(StartMatchBtn.x, StartMatchBtn.y, 1)
    pg.click()


def BuyChamp(amount=0):
    util.log('Action', 'Buy Champ, Count: ' + str(amount))

    j = 0

    while j < amount:
        pg.moveTo(BuyChampBtn.x + (j * ChampDistance), BuyChampBtn.y, TIME_BETWEEN)
        pg.mouseDown(button='left')
        sleep(TIME_BETWEEN)
        pg.mouseUp(button='left')

        j = j + 1


def LevelUp(amountClicks=0):
    util.log('Action', 'Level Up: ' + str(amountClicks))
    j = 0
    pg.moveTo(LevelUpBtn.x, LevelUpBtn.y, TIME_BETWEEN)

    while j < amountClicks:
        j = j + 1

        pg.mouseDown(button='left')
        sleep(TIME_BETWEEN)
        pg.mouseUp(button='left')


def Walk():
    util.log('Action', 'Walk')

    for pos in Poses:
        pg.moveTo(pos.x, pos.y, TIME_BETWEEN)
        pg.mouseDown(button='right')
        sleep(TIME_BETWEEN)
        pg.mouseUp(button='right')

        sleep(2.5)


def MatchFinish():
    util.log('Action', 'Match Finish')
    pg.moveTo(ContinueBtn.x, ContinueBtn.y, TIME_BETWEEN)
    pg.mouseDown()
    sleep(TIME_BETWEEN)
    pg.mouseUp()
    sleep(1)
    pg.moveTo(ExitMatchBtn.x, ExitMatchBtn.y, TIME_BETWEEN)
    pg.mouseDown()
    sleep(TIME_BETWEEN)
    pg.mouseUp()


def GiveItems():
    util.log('Action', 'Give Items')

    for item in Items:
        for champ in Champs:
            pg.moveTo(item.x, item.y, TIME_BETWEEN)
            pg.mouseDown(button='left')
            pg.moveTo(champ.x, champ.y, TIME_BETWEEN)
            pg.mouseUp(button='left')
            sleep(TIME_BETWEEN)


util.formatConsole()

try:
    while True:
        sleep(2)

        # Queue betreten
        util.log('Status', 'In Queue')
        util.centerClient()

        # Klicke bis sich das Spielfenster öffnet
        while not util.isGameRunning():
            StartMatch()
            sleep(1)

        util.log('Status', 'Match Found')

        # Warten damit das LeageGame sichtbar ist
        sleep(20)

        util.centerGame()

        # Zeichnet Pixel des Ladebildschirms auf
        sleep(2)
        pixelLoad = PIL.ImageGrab.grab().load()[Pos1.x, Pos1.y]
        util.log('Status', 'In loading screen')

        # Pixel des Ladebildschirms vergleichen um Spiel zu erkennen
        while PIL.ImageGrab.grab().load()[Pos1.x, Pos1.y] == pixelLoad:
            sleep(1)

        util.log('Status', 'Match Started - Starting 15Min Timer')

        # Spiel hat begonnen und ein 15 Minuten - Timer hat begonnen
        x = 900
        while x > 0:
            util.centerGame()
            x = x - 1
            sleep(1)

            if x == 850:
                BuyChamp(1)
                BuyChamp(2)
                sleep(5)
                BuyChamp(1)
                BuyChamp(2)

            if x == 810:
                BuyChamp(2)
                Walk()

            if x == 775:
                BuyChamp(1)

            if x == 700:
                Walk()
                BuyChamp(1)
                LevelUp(1)
                GiveItems()

            if x == 660:
                BuyChamp(1)
                LevelUp(1)

            if x == 590:
                Walk()
                BuyChamp(1)
                GiveItems()

            if x == 320:
                BuyChamp(1)
                LevelUp(1)

            if x == 260:
                LevelUp(1)
                BuyChamp(2)
                Walk()
                GiveItems()

            if x == 60:
                LevelUp(20)
                Walk()

        timer = 0

        util.log('Status', 'Wait until life hits 0')

        # Nach 15min warten bis du gestorben bist und beende das Spiel
        while util.isGameRunning():
            MatchFinish()
            sleep(10)

            # jede Minute probieren
            if timer % 30 == 0:
                Walk()
                LevelUp(1)
                BuyChamp(1)
                GiveItems()

            timer = timer + 10

        util.log('Status', 'Finished Game - Going next')

        # Warten bis Spiel geschlossen und maximiere den Client
        sleep(10)
        util.centerClient()
        sleep(5)

        # Nochmal auf den Play-Button klicken um nochmal zu spielen
        StartMatch()

except KeyboardInterrupt:
    print('[Status] Got KeyboardInterrupt - Exiting')
