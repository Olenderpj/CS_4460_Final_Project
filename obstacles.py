from HelperFunctions import *

class Obstacle:

    def __init__(self, handle, coordinates, name):
        self.handle = handle
        self.coordinates = coordinates
        self.name = name
        self.accuracy = calculateAccuracy()

    def __str__(self):
        return f"--------------------------------------------------------------------------------\n" \
               f"Handle: {self.handle}\n" \
               f"Name: {self.name}\n" \
               f"Coordinates: {self.coordinates[0]}, {self.coordinates[1]}\n" \
               f"Accuracy: {self.accuracy}" \

