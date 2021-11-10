class Coordinates:
    def __init__(self, xx, yy):
        self.x = xx
        self.y = yy


class RelativCoordinates:
    def __init__(self, xx, yy):
        self.x = xx
        self.y = yy

    def getCoordinates(self, window):
        if not window:
            raise Exception('Argument window must be set')

        absuluteX = window.left + window.width * self.x / 100
        absuluteY = window.top + window.height * self.y / 100

        return Coordinates(absuluteX, absuluteY)


item1 = RelativCoordinates(11.3, 69.4)
item2 = RelativCoordinates(13.3, 66.2)
item3 = RelativCoordinates(12.1, 63.1)
item4 = RelativCoordinates(14.5, 61.3)
item5 = RelativCoordinates(13.3, 58.1)
item6 = RelativCoordinates(14.1, 54.4)
items = [item1, item2, item3, item4, item5, item6]

champ1 = RelativCoordinates(50.0, 59.4)
champ2 = RelativCoordinates(45.7, 52.5)
champ3 = RelativCoordinates(50.0, 43.8)
champs = [champ1, champ2, champ3]
