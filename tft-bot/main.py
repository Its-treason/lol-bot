#! python3
from time import sleep
import util
import actions

util.formatConsole()

isRunning = util.focusClient()
if not isRunning:
    util.log('Error', 'League Client is not running!')
    sleep(5)
    exit(1)

try:
    while True:
        # join queue
        util.log('Status', 'In Queue')
        util.focusClient()

        # click until the game-window opens
        while not util.isGameRunning():
            actions.startMatch()
            sleep(1)

        util.log('Status', 'Match Found')

        # wait until the LeagueGame is visible
        sleep(10)

        util.focusGame()

        util.log('Status', 'In loading screen')

        # MapIcon is the Middle icon of the Map
        while not util.getCordsWithImage('images/map_icon.png'):
            sleep(1)

        util.log('Status', 'Match Started')

        while not util.getCordsWithImage('images/exit_now.png') and not util.getCordsWithImage('images/continue.png'):
            sleep(1)
            actions.selectAugmentPart()
            actions.buyChamp()
            actions.collectDrops()

        exitBtn = util.getCordsWithImage('images/exit_now.png')
        if not exitBtn:
            exitBtn = util.getCordsWithImage('images/continue.png')
        util.mouseClick(exitBtn)

        util.log('Status', 'Match ended')

        # wait until game is closed and maximize client
        sleep(10)
        util.focusClient()

        # click on "play again" to start new match
        actions.playAgain()

except KeyboardInterrupt:
    util.log('Status', 'Got KeyboardInterrupt - Exiting')
