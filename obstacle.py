import random


def generateCertainty():
    whole = random.randint(78, 86)
    decimal = random.randint(0, 100)

    return float(f"{whole}.{decimal}")


class Obstacle:

    def __init__(self, handle, xCoord, yCoord, alias):
        self.handle = handle
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.alias = alias
        self.certainty = generateCertainty()

    def getCertainty(self):
        return self.certainty

    def __str__(self):
        return f"ID: {self.handle}\n" \
               f"Name: {self.alias}\n" \
               f"Coord: X:{self.xCoord}, Y:{self.yCoord}\n" \
               f"Certainty: {self.certainty}% "
