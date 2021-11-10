from time import sleep
import pyautogui as pg
import coordinates as cords
import util


def startMatch():
    window = util.focusClient()

    findMatchBtn = util.getCordsWithImage('images/find_match.png', window=window)
    if findMatchBtn:
        pg.moveTo(findMatchBtn.x, findMatchBtn.y)
        pg.click()
        return

    acceptMatchBtn = util.getCordsWithImage('images/accept_match.png', window=window, confidence=0.9)
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


def levelUp(count=1):
    util.log('Action', 'Level Up - ' + str(count) + ' times')
    levelUpBtn = util.getCordsWithImage('images/level_up.png')

    i = 0
    while i < count:
        i = i + 1
        util.mouseClick(levelUpBtn)


def refreshShop(count=1):
    util.log('Action', 'Refresh Shop Up - ' + str(count) + ' times')
    refreshShopBtn = util.getCordsWithImage('images/refresh_shop.png')

    i = 0
    while i < count:
        i = i + 1
        util.mouseClick(refreshShopBtn)


def giveItems():
    util.log('Action', 'Give Items')
    window = util.focusGame()
    if not window:
        return

    for item in cords.items:
        for champ in cords.champs:
            pg.moveTo(item.getCoordinates(window).x, item.getCoordinates(window).y)
            pg.mouseDown(button='left')
            pg.moveTo(champ.getCoordinates(window).x, champ.getCoordinates(window).y, 0.05)
            pg.mouseUp(button='left')


def selectAugmentPart():
    window = util.focusGame()

    augment = util.getCordsWithImage('images/augment_part.png', window=window)
    if augment:
        util.log('Action', 'Picking Augment')
        util.mouseClick(augment)
        sleep(1)


def spendGold():
    window = util.focusGame()

    enoughCoins = util.getCordsWithImage('images/5x_coins.png', window=window, confidence=0.9)
    if enoughCoins:
        util.log('Action', 'Spending Gold')
        levelUp(4)


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
        giveItems()

    grey = util.getCordsWithImage('images/grey_question_mark.png', confidence=0.7, window=window)
    if grey:
        util.log('Action', 'Picking up Grey Drop')
        util.mouseClick(cords=grey, button='right')
        sleep(4)
        giveItems()

    gold = util.getCordsWithImage('images/gold_question_mark.png', confidence=0.6, window=window)
    if gold:
        util.log('Action', 'Picking up Gold')
        util.mouseClick(cords=gold, button='right')
        sleep(4)
        giveItems()


def canRunMainLoop():
    return not util.getCordsWithImage('images/exit_now.png') and \
           not util.getCordsWithImage('images/continue.png') and \
           util.isGameRunning()
