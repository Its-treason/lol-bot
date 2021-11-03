from time import sleep
import pyautogui as pg
import cords
import pydirectinput as di

import util


def findMatch():
    pg.moveTo(cords.StartMatchBtn.x, cords.StartMatchBtn.y, 0.2)
    pg.click()


def acceptMatch():
    pg.moveTo(cords.MatchAcceptBtn.x, cords.MatchAcceptBtn.y, 0.2)
    pg.click()


def selectChamp():
    pg.moveTo(cords.AdcTab.x, cords.AdcTab.y, 0.2)
    pg.click()
    sleep(0.2)
    pg.moveTo(cords.ChampSelect1.x, cords.ChampSelect1.y, 0.2)
    pg.click()
    sleep(0.2)
    pg.moveTo(cords.LockInChamp.x, cords.LockInChamp.y, 0.2)
    pg.click()


def buyItem():
    pg.moveTo(cords.OpenShop.x, cords.OpenShop.y, 0.2)
    pg.click()
    pg.moveTo(cords.FirstItem.x, cords.FirstItem.y, 0.2)
    pg.click()
    sleep(0.05)
    pg.click()
    sleep(1)
    pg.press('escape')


def move(offset=0):
    pg.moveTo(cords.MapMid.x + offset, cords.MapMid.y - offset, 0.2)
    util.mouseClick()
    sleep(0.1)
    pg.moveTo(cords.MapMid.x + offset, cords.MapMid.y - offset, 0.2)
    util.pressBtn('a')
    sleep(0.2)
    util.pressBtn('y')


def doAbilities():
    pg.moveTo(cords.MiddleOfScreen.x, cords.MiddleOfScreen.y, 0.2)
    di.click()
    util.pressBtn('y')

    buttons = ['q', 'w', 'e', 'r', 'd', 'f', '4']
    for button in buttons:
        sleep(0.2)
        pg.moveTo(cords.MiddleOfScreen.x, cords.MiddleOfScreen.y, 0.2)
        di.press(button)

def levelUp():
    pg.moveTo(cords.LevelUpR.x, cords.LevelUpR.y, 0.2)
    util.mouseClick()
    sleep(0.5)
    pg.moveTo(cords.LevelUpQ.x, cords.LevelUpQ.y, 0.2)
    util.mouseClick()
    sleep(0.5)
    pg.moveTo(cords.LevelUpW.x, cords.LevelUpW.y, 0.2)
    util.mouseClick()
    sleep(0.5)
    pg.moveTo(cords.LevelUpE.x, cords.LevelUpE.y, 0.2)
    util.mouseClick()
