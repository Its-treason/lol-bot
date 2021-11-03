#! python3
from time import sleep
import util
import cords
import actions

util.formatConsole()
opened = util.centerClient()

if not opened:
    util.log(msg='Error: League Client not running!')
    exit()

clientCheckPixel1 = util.getPixel(cords.ClientCheckPos1.x, cords.ClientCheckPos1.y)
clientCheckPixel2 = util.getPixel(cords.ClientCheckPos2.x, cords.ClientCheckPos2.y)

try:
    while True:

        while not util.isGameRunning():
            sleep(2)

            clientCheckPixelNow1 = util.getPixel(cords.ClientCheckPos1.x, cords.ClientCheckPos1.y)
            clientCheckPixelNow2 = util.getPixel(cords.ClientCheckPos2.x, cords.ClientCheckPos2.y)

            if (clientCheckPixel1 != clientCheckPixelNow1) & (clientCheckPixel2 != clientCheckPixelNow2):
                util.log('Status', 'Accepting Match')
                actions.acceptMatch()
            elif (clientCheckPixel1 == clientCheckPixelNow1) & (clientCheckPixel2 != clientCheckPixelNow2):
                util.log('Status', 'Selecting Champ')
                sleep(1)
                actions.selectChamp()
            else:
                util.log('Status', 'Waiting for Lobby')
                actions.findMatch()


        # Warten damit das LeageGame sichtbar ist
        sleep(10)

        util.centerGame()

        # Zeichnet Pixel des Ladebildschirms auf
        sleep(2)
        pixelLoad = util.getPixel(cords.Pos1.x, cords.Pos1.y)
        util.log('Status', 'In loading screen')

        # Pixel des Ladebildschirms vergleichen um Spiel zu erkennen
        while util.getPixel(cords.Pos1.x, cords.Pos1.y) == pixelLoad:
            sleep(2)

        util.log('Status', 'Game started')

        actions.levelUp()
        sleep(12)
        actions.move(-10)
        sleep(60)

        i = 0

        while util.isGameRunning():
            sleep(10)

            if i % 5 == 0:
                actions.levelUp()
                actions.doAbilities()

            actions.move(i)
            i = i + 1

        util.log('Status', 'Game ended')

        while clientCheckPixel2 != util.getPixel(cords.ClientCheckPos2.x, cords.ClientCheckPos2.y):
            sleep(1)
            actions.findMatch()

except KeyboardInterrupt:
    util.log('Status', 'Got KeyboardInterrupt - Exiting')
    exit()
