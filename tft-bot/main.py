from time import sleep
import util
import actions
from traceback import print_exc

util.formatConsole()

isRunning = util.focusClient()
if not isRunning:
    util.log('Error', 'League Client is not running!')
    sleep(5)
    exit(1)


def mainLoop():
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
            sleep(2)
            actions.selectAugmentPart()
            actions.buyChamp()
            actions.collectDrops()
            actions.spendGold()

        sleep(3)

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


try:
    mainLoop()
except (KeyboardInterrupt, Exception) as exception:
    if isinstance(exception, KeyboardInterrupt):
        util.log('Status', 'Got KeyboardInterrupt - Exiting')
    else:
        util.log('Error', 'An Error occurred during execution')
        print('======== Start of Debug output ========')
        print_exc()
        print('======== End of Debug output ========')
        print('Please report this Issue at https://github.com/Its-treason/lol-bot/issues')
        print('')
        sleep(1)
        input('Press any Key to exit...')
