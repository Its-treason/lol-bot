#! python3
from time import sleep
import util
import actions
import pyautogui as pg

util.formatConsole()

isRunning = util.centerClient()
if not isRunning:
    util.log('Error', 'League Client is not running!')
    exit(1)

try:
    while True:
        # join queue
        util.log('Status', 'In Queue')
        util.centerClient()

        # click until the game-window opens
        while not util.isGameRunning():
            actions.StartMatch()
            sleep(1)

        util.log('Status', 'Match Found')

        # wait until the LeagueGame is visible
        sleep(10)

        util.centerGame()

        util.log('Status', 'In loading screen')

        # MapIcon is the Middle icon of the Map
        while not util.getCordsWithImage('images/map_icon.png'):
            sleep(1)

        util.log('Status', 'Match Started')

        while not util.getCordsWithImage('images/exit_now.png'):
            actions.buyChamp()
            actions.collectItemDrops()

        exitNow = util.getCordsWithImage('images/exit_now.png')
        pg.moveTo(exitNow.x, exitNow.y)
        pg.click()
        pg.mouseDown(button='left')
        sleep(0.3)
        pg.mouseUp(button='left')

        # wait until game is closed and maximize client
        sleep(10)
        util.centerClient()
        sleep(5)

        util.log('Status', 'Match ended')

        # click on "play again" to start new match
        actions.playAgain()

except KeyboardInterrupt:
    util.log('Status', 'Got KeyboardInterrupt - Exiting')
