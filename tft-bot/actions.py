import pyautogui as pg
from time import sleep
import util
import coordinates as cords


def StartMatch():
    findMatchBtn = util.getCordsWithImage('images/find_match.png')
    if findMatchBtn:
        pg.moveTo(findMatchBtn.x, findMatchBtn.y)
        pg.click()
        return

    acceptMatchBtn = util.getCordsWithImage('images/accept_match.png')
    if acceptMatchBtn:
        pg.moveTo(acceptMatchBtn.x, acceptMatchBtn.y)
        pg.click()
        # Move the mouse off the acceptBtn so it can be detected again
        pg.moveTo(50)


def buyChamp():
    basePath = 'images/champions/'
    fileExtension = '.png'

    champions = ['caitlyn', 'heimerdinger', 'jhin', 'kog_maw', 'lulu', 'miss_fortune', 'poppy', 'tristana', 'vex',
                 'ziggs']

    for champion in champions:
        pos = util.getCordsWithImage(basePath + champion + fileExtension)
        if not pos:
            continue

        pg.moveTo(pos.x, pos.y)
        pg.mouseDown(button='left')
        sleep(0.1)
        pg.mouseUp(button='left')


def LevelUp(amountClicks=0):
    util.log('Action', 'Level Up: ' + str(amountClicks))
    j = 0
    pg.moveTo(cords.LevelUpBtn.x, cords.LevelUpBtn.y, cords.TIME_BETWEEN)

    while j < amountClicks:
        j = j + 1

        pg.mouseDown(button='left')
        sleep(cords.TIME_BETWEEN)
        pg.mouseUp(button='left')


def Walk():
    util.log('Action', 'Walk')

    for pos in cords.Poses:
        pg.moveTo(pos.x, pos.y, cords.TIME_BETWEEN)
        pg.mouseDown(button='right')
        sleep(cords.TIME_BETWEEN)
        pg.mouseUp(button='right')

        sleep(2.5)


def MatchFinish():
    util.log('Action', 'Match Finish')
    pg.moveTo(cords.ContinueBtn.x, cords.ContinueBtn.y, cords.TIME_BETWEEN)
    pg.mouseDown()
    sleep(cords.TIME_BETWEEN)
    pg.mouseUp()
    sleep(1)
    pg.moveTo(cords.ExitMatchBtn.x, cords.ExitMatchBtn.y, cords.TIME_BETWEEN)
    pg.mouseDown()
    sleep(cords.TIME_BETWEEN)
    pg.mouseUp()


def GiveItems():
    util.log('Action', 'Give Items')

    for item in cords.Items:
        for champ in cords.Champs:
            pg.moveTo(item.x, item.y, cords.TIME_BETWEEN)
            pg.mouseDown(button='left')
            pg.moveTo(champ.x, champ.y, cords.TIME_BETWEEN)
            pg.mouseUp(button='left')
            sleep(cords.TIME_BETWEEN)


def playAgain():
    while True:
        sleep(3)
        okBtn = util.getCordsWithImage('images/ok.png')
        if okBtn:
            pg.moveTo(okBtn.x, okBtn.y)
            pg.click()
            continue

        playBtn = util.getCordsWithImage('images/play_again.png')
        if playBtn:
            print(playBtn)
            pg.moveTo(playBtn.x, playBtn.y)
            pg.click()
            continue

        break

def collectItemDrops():
    blue = util.getCordsWithImage('images/blue_item_drop.png')
    if blue:
        pg.moveTo(blue.x, blue.y)
        pg.mouseDown(button='right')
        sleep(0.1)
        pg.mouseUp(button='right')
        sleep(5)

    grey = util.getCordsWithImage('images/grey_item_drop.png')
    if grey:
        pg.moveTo(grey.x, grey.y)
        pg.mouseDown(button='right')
        sleep(0.1)
        pg.mouseUp(button='right')
        sleep(5)
