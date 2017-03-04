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

        self.updateColors() 

    # Private methods for internal use

    # Updates max and min temperatures in the cylinders array
    def __updateMinMaxTemps(self):
        self.minTemp = self.maxTemp = self.cylinders[0].getTemperature()

        for cylinder in self.cylinders:
            temperature = cylinder.getTemperature()

            if temperature > self.maxTemp: 
                self.maxTemp = temperature
            elif temperature < self.minTemp:
                self.minTemp = temperature

    # Initializes the game with cylinders with ranodm temperatures and locations
    def __initRandomCylinders(self):
        # Initialize Cylinder objects
        for i in xrange(self.total):
            randTemp = random() * self.TEMP_MAX
            newCylinder = Cylinder(randTemp, Placement.SLOW)

            self.cylinders.append(newCylinder)

        # Pick random cylinders to be placed in fast storage
        moveToFast = sample(xrange(self.total), self.fast_size)

        for i in moveToFast:
            self.cylinders[i].setPlacement(Placement.FAST)
            
    # Returns a number from {1,...,10} representing the color based on the temperature
    def __computeColorBucket(self, cylinder):
        # Get relative position of temperature in terms of range [0, 1]
        pos = float(cylinder.getTemperature() - self.minTemp) / (self.maxTemp - self.minTemp)

        return int(pos * 10) # Shift to range [0, 10]

    # Public Methods

    # Updates the color values of the cylinders
    def updateColors(self):
        self.__updateMinMaxTemps()

        for cylinder in self.cylinders:
            cylinder.setColorBucket(self.__computeColorBucket(cylinder))

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



if __name__ == "__main__":
    game = Game(10, 3)

    for cylinder in game.cylinders:
        print str(cylinder)

    print "MaxTemp: " + str(game.maxTemp)
    print "MinTemp: " + str(game.minTemp)