#! python3
from time import sleep
import util
import actions
from traceback import print_exc, format_exc
from time import time
from win32api import GetKeyState
from win32con import VK_CAPITAL

util.formatConsole()
opened = util.focusClient()
actions.disableCapsLock()

if not opened:
    util.log(msg='Error: League Client not running!')
    exit()


def mainLoop():
    while True:

        while not util.isGameRunning():
            sleep(2)
            actions.startMatch()

        # Wait for the game to be visible
        sleep(10)

        util.log('Status', 'In loading screen')
        util.focusGame()

        while not util.getCordsWithImage('images/settings_icon.png', confidence=0.7):
            sleep(2)

        util.log('Status', 'Game started')
        startTime = int(time())

        while util.isGameRunning():
            try:
                actions.mainActions(startTime)
            except Exception:
                util.logError(format_exc())

            if GetKeyState(VK_CAPITAL):
                raise KeyboardInterrupt()

        util.log('Status', 'Game ended')

        # League client will freeze sometime after match ending, that causes the bot to crash
        sleep(10)

        while not util.getCordsWithImage('images/find_match.png'):
            sleep(1)
            actions.gotoLobby()


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

    sleep(5)
