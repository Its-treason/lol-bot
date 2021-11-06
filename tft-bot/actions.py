import pyautogui as pg
from time import sleep
import util
import coordinates as cords


def startMatch():
    window = util.focusClient()

    findMatchBtn = util.getCordsWithImage('images/find_match.png', window=window)
    if findMatchBtn:
        pg.moveTo(findMatchBtn.x, findMatchBtn.y)
        pg.click()
        return

    acceptMatchBtn = util.getCordsWithImage('images/accept_match.png', window=window)
    if acceptMatchBtn:
        pg.moveTo(acceptMatchBtn.x, acceptMatchBtn.y)
        pg.click()
        # Move the mouse off the acceptBtn so it can be detected again
        pg.moveRel(0, 100)


def buyChamp():
    window = util.focusGame()

    basePath = 'images/champions/'
    fileExtension = '.png'

    champions = ['caitlyn', 'heimerdinger', 'jhin', 'kog_maw', 'lulu', 'miss_fortune', 'poppy', 'tristana', 'vex',
                 'ziggs']

    for champion in champions:
        pos = util.getCordsWithImage(basePath + champion + fileExtension, window=window)
        if not pos:
            continue

        util.log('Action', 'Buying Champion: ' + champion)
        pg.moveTo(pos.x, pos.y)
        pg.mouseDown(button='left')
        sleep(0.1)
        pg.mouseUp(button='left')


def levelUp(amountClicks=1):
    util.log('Action', 'Level Up - ' + str(amountClicks) + ' times')
    j = 0
    pg.moveTo(cords.LevelUpBtn.x, cords.LevelUpBtn.y, cords.TIME_BETWEEN)

    while j < amountClicks:
        j = j + 1

        #util.mouseClick(playBtn)


def giveItems():
    item = util.getCordsWithImage('images/armor.png', confidence=0.5)
    if item:
        print('Found Item')
        pg.moveTo(item.x, item.y)


def selectAugmentPart():
    window = util.focusGame()

    augment = util.getCordsWithImage('images/augment_part.png', window=window)
    if augment:
        util.log('Action', 'Picking Augment')
        util.mouseClick(augment)


def playAgain():
    while True:
        sleep(3)
        okBtn = util.getCordsWithImage('images/ok.png')
        if okBtn:
            util.mouseClick(okBtn)
            continue

        playBtn = util.getCordsWithImage('images/play_again.png')
        if playBtn:
            util.mouseClick(playBtn)
            continue

        break


def collectDrops():
    window = util.focusGame()

    blue = util.getCordsWithImage('images/blue_questionmark.png', confidence=0.6, window=window)
    if blue:
        util.log('Action', 'Picking up Blue Drop')
        util.mouseClick(cords=blue, button='right')
        sleep(4)

    grey = util.getCordsWithImage('images/grey_question_mark.png', confidence=0.7, window=window)
    if grey:
        util.log('Action', 'Picking up Grey Drop')
        util.mouseClick(cords=grey, button='right')
        sleep(4)

    gold = util.getCordsWithImage('images/gold_question_mark.png', confidence=0.6, window=window)
    if gold:
        util.log('Action', 'Picking up Gold')
        util.mouseClick(cords=gold, button='right')
        sleep(4)

    coin = util.getCordsWithImage('images/coin.png', confidence=1, window=window)
    if coin:
        util.log('Action', 'Picking up Gold Coin')
        util.mouseClick(cords=coin, button='right')
        sleep(4)
