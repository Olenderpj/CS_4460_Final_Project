
class ObstacleList:

    def __init__(self):
        self.obstacles = []

    def addObstacle(self, obstacle):
        self.obstacles.append(obstacle)

    def getAverageCertainty(self):

        totalCertainty = 0

        for i in self.obstacles:
            totalCertainty += i.getCertainty()

        if len(self.obstacles) == 0:
            return 0
        else:
            return totalCertainty / len(self.obstacles)

    def getAllObstacles(self):
        return self.obstacles
