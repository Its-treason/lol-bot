class Coordinates:
    def __init__(self, xx, yy):
        self.x = xx
        self.y = yy


class RelativCoordinates:
    def __init__(self, xx, yy):
        self.x = xx
        self.y = yy

    def getCoordinates(self, window):
        absoluteX = window.left + window.width * self.x / 100
        absoluteY = window.top + window.height * self.y / 100

        return Coordinates(absoluteX, absoluteY)


champ1ChampSelect = RelativCoordinates(30, 23)

middleOfScreen = RelativCoordinates(50, 50)
mapMid = RelativCoordinates(91, 85)
