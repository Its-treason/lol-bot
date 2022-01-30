from time import sleep
import pyautogui as pg
import pydirectinput as di
import coordinates
from time import time
from win32api import GetKeyState
from win32con import VK_CAPITAL

import util


def startMatch():
    window = util.focusClient()
    if not window:
        return

    findMatch = util.getCordsWithImage('images/find_match.png', window=window)
    if findMatch:
        util.log('Action', 'Finding match')
        util.mouseClick(findMatch)

    acceptMatch = util.getCordsWithImage('images/accept_match.png', window=window)
    if acceptMatch:
        util.log('Action', 'Accepting Match')
        util.mouseClick(acceptMatch)

    adcRole = util.getCordsWithImage('images/select_adc.png', window=window)
    if adcRole:
        util.log('Action', 'Selecting champion')
        util.mouseClick(adcRole)

        firstChamp = coordinates.champ1ChampSelect.getCoordinates(window)
        util.mouseClick(firstChamp)

        lockInChamp = util.getCordsWithImage('images/lock_in.png', window=window)
        if lockInChamp:
            util.mouseClick(lockInChamp)


def gotoLobby():
    window = util.focusClient()
    okBtn = util.getCordsWithImage('images/ok.png', window=window, confidence=0.75)
    if okBtn:
        util.mouseClick(okBtn)

    skipHonerBtn = util.getCordsWithImage('images/skip_honor.png', window=window)
    if skipHonerBtn:
        util.mouseClick(skipHonerBtn)

    playAgainBtn = util.getCordsWithImage('images/play_again.png', window=window)
    if playAgainBtn:
        util.mouseClick(playAgainBtn)


def buyItem():
    window = util.focusGame()
    openShop = util.getCordsWithImage('images/shop.png', window=window, confidence=0.9)

    print(openShop)

    if not openShop:
        return

    util.mouseClick(openShop)
    sleep(0.2)
    item = util.getCordsWithImage('images/shop_recommended_item.png')
    if item:
        di.click(int(item.x), int(item.y), clicks=5, interval=0.05)

    sleep(0.2)
    util.pressBtn('escape')


def move(offset=0):
    deCenterCamara()

    window = util.focusGame()
    mapCords = coordinates.mapMid.getCoordinates(window=window)
    pg.moveTo(mapCords.x + ((0.0007 * window.width) * offset), mapCords.y - ((0.00125 * window.height) * offset))
    di.mouseDown()
    sleep(0.2)
    di.mouseUp()

    midOfScreenCords = coordinates.middleOfScreen.getCoordinates(window=window)
    pg.moveTo(midOfScreenCords.x, midOfScreenCords.y)
    util.pressBtn('a')

    centerCamara()


def doAbilities():
    util.log('Action', 'Doing some abilities')
    window = util.focusGame()

    buttons = ['q', 'w', 'e', 'r', 'd', 'f', '4']
    for button in buttons:
        sleep(0.1)
        midOfScreenCords = coordinates.middleOfScreen.getCoordinates(window=window)
        pg.moveTo(midOfScreenCords.x, midOfScreenCords.y)
        di.press(button)


def levelUp():
    window = util.focusGame()
    levelUpBtn = util.getCordsWithImage('images/level_up.png', window=window)

    if levelUpBtn:
        util.log('Action', 'Leveling up')
        util.mouseClick(levelUpBtn)


def recallOnLowHealth():
    window = util.focusGame()
    healthLow = util.getCordsWithImage('images/health_low.png', window=window, confidence=0.95)
    if not healthLow:
        return

    util.log('Action', 'Recalling due to low health')

    # This is basicly the move function, but with a fixed offset and rightClick instead of a
    deCenterCamara()

    window = util.focusGame()
    mapCords = coordinates.mapMid.getCoordinates(window=window)
    pg.moveTo(mapCords.x + ((0.0007 * window.width) * -10), mapCords.y - ((0.00125 * window.height) * -10))
    di.mouseDown()
    sleep(0.2)
    di.mouseUp()

    midOfScreenCords = coordinates.middleOfScreen.getCoordinates(window=window)
    pg.moveTo(midOfScreenCords.x, midOfScreenCords.y)
    util.mouseClick(button='right')

    centerCamara()

    sleep(10)
    di.press('b')
    sleep(10)


def centerCamara():
    window = util.focusGame()
    centerCamBtn = util.getCordsWithImage('images/cam_not_centered.png', window=window, confidence=0.9)
    if centerCamBtn:
        centerCamBtn.y = centerCamBtn.y - 2
        util.mouseClick(centerCamBtn)


def deCenterCamara():
    window = util.focusGame()
    centerCamBtn = util.getCordsWithImage('images/cam_centered.png', window=window, confidence=0.9)
    if centerCamBtn:
        centerCamBtn.y = centerCamBtn.y - 2
        util.mouseClick(centerCamBtn)


def mainActions(startTime):
    sleep(1)
    centerCamara()
    levelUp()
    recallOnLowHealth()

    currentTime = int(time()) - startTime
    if currentTime % 60 == 0:
        doAbilities()

    offset = (currentTime - 300) / 13
    if offset < 0:
        offset = 0
    if currentTime % 2 == 0:
        move(offset)


def disableCapsLock():
    if GetKeyState(VK_CAPITAL):
        pg.press('capslock')
        util.log('Info', 'Disabled Caps-Lock')
