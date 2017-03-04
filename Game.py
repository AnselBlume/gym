from Cylinder import *
from random import random, sample

# TODO: everything
class Game:
    # Maximum random temperature to initialize the cylinders to
    TEMP_MAX = 1000

    # Date for the current frame
    date = ""

    # List of cylinders
    cylinders = []

    """total: total number of cylinders 
    fast_size: size of fast portion"""
    def __init__(self, total, fast_size):
        self.total = total
        self.fast_size = fast_size

        # Initialize Game with cylinders with random temperatures and locations
        self.__initRandomCylinders()

        # Set min and max temperatures
        self.maxTemp = 0
        self.minTemp = 0

        self.__setMinMaxTemps() 

    # Private methods for internal use
    def __setMinMaxTemps(self):
     '''   for cylinder in cylinders:
            if cylinder.getTemperature()>self.maxTemp:
                self.maxTemp=cylinder.getTemperature()
                pass
            pass
        for cylinder in cylinders:
            if cylinder.getTemperature()<self.minTemp:
                self.minTemp=cylinder.getTemperature()
                pass
            pass'''

    # Initializes the game with cylinders with ranodm temperatures and locations
    def __initRandomCylinders(self):
        # Initialize Cylinder objects
        for i in xrange(self.total):
            randTemp = random() * self.TEMP_MAX
            newCylinder = Cylinder(randTemp, Placement.SLOW)
            self.cylinders.append(newCylinder)

        # Pick random cylinders to be placed in fast storage
        moveToFast = sample(xrange(self.total), self.fast_size)

        print str(moveToFast)

        for i in moveToFast:
            self.cylinders[i].setPlacement(Placement.FAST)
            

    # Public Methods

    # Sets the date string
    def setDate(self, date):
        self.date = date

    # Gets the date string
    def getDate(self):
        return self.date

    def swap(self, i, j):
        """swapping rectangle i with rectangle j"""
        pass

    def change_color(self, i, color):
        """color is... something"""

    def get_states(self, i):
        """returns: array of numbers"""
        pass

    def get_fast_states(self):
        """returns: array of numbers"""
        pass

    def get_slow_states(self):
        """returns: array of numbers"""
        pass

    def fitness(self):
        """returns number 0.0 - 1.0"""
        pass
    def bucket(self,cylinder):
        bucket=math.floor((cylinder.getTemperature()-minTemp)/(maxTemp-minTemp))
        pass
    def updateMax(self,cylinder):
        if cylinder.getTemperature()>self.maxTemp:
                self.maxTemp=cylinder.getTemperature()
                pass
        pass
    def updateMin(self,cylinder):
        if cylinder.getTemperature()<self.minTemp:
                self.minTemp=cylinder.getTemperature()
                pass
        pass

if __name__ == "__main__":
    game = Game(10, 3)

    for cylinder in game.cylinders:
        print str(cylinder)