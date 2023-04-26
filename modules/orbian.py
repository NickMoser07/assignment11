from math import pi
from random import shuffle # Hint hint
from random import randint
import time

class Orbian:
    # DO NOT MODIFY THE CONSTRUCTOR
    def __init__(self, name, headRadius, bodyRadius, bodyHeight):
        # NOTE: These are constants
        self.__HEAD_RADIUS = headRadius
        self.__BODY_RADIUS = bodyRadius
        self.__BODY_HEIGHT = bodyHeight
        self.__NAME = name
        self.__BIRTH_TIME = time.time()

        # This is the only variable
        self.__adult = False

    def __getHeadVolume(self):
        return 4 / 3 * pi * self.__getHeadRadius() ** 3

    def __getBodyVolume(self):
        return pi * self.__getBodyRadius() ** 2 * self.__getBodyHeight()

    def __ageCheck(self):
        # Become an adult at 2
        if self.getAge() >= 2:
            self.__adult = True

    ####### ADD OTHER REQUIRED METHODS BELOW. SEE THE ASSIGNMENT DESCRIPTION AND OTHER STARTER CODE FOR INSIGHT ######
    def getName(self):
        return self.__NAME
    def getAge(self):
        return round((time.time() - self.__BIRTH_TIME)/5, 2)
    def getVolume(self):
        self.__growUp()
        return round((pi * self.__BODY_RADIUS ** 2 * self.__BODY_HEIGHT) + (4 / 3 * pi * self.__HEAD_RADIUS ** 3))
    def __growUp(self):
        if not self.__adult:
            self.__ageCheck()
            if self.__adult:
                self.__HEAD_RADIUS *= 2
                self.__BODY_RADIUS *= 2
                self.__BODY_HEIGHT *= 4
            
        

    def __str__(self):
        self.__growUp()
        return self.__NAME
    def __len__(self):
        self.__growUp()
        return self.__BODY_HEIGHT + self.__HEAD_RADIUS *2
    def __eq__(self, other):
        self.__growUp()
        return ((pi * self.__BODY_RADIUS ** 2 * self.__BODY_HEIGHT) + (4 / 3 * pi * self.__HEAD_RADIUS ** 3)) == ((pi * other.__BODY_RADIUS ** 2 * other.__BODY_HEIGHT) + (4 / 3 * pi * other.__HEAD_RADIUS ** 3))
    def __gt__(self, other):
        self.__growUp()
        return ((pi * self.__BODY_RADIUS ** 2 * self.__BODY_HEIGHT) + (4 / 3 * pi * self.__HEAD_RADIUS ** 3)) > ((pi * other.__BODY_RADIUS ** 2 * other.__BODY_HEIGHT) + (4 / 3 * pi * other.__HEAD_RADIUS ** 3))
    def __add__(self, other):
        self.__growUp()
        charList = [i for i in self.__NAME] + [i for i in other.__NAME]
        avgLen = (len(self.__NAME) + len(other.__NAME)) // 2
        shuffle(charList)
        name = ""
        for i in range(avgLen):
            name += charList[i]
        headRadius = round((self.__HEAD_RADIUS + other.__HEAD_RADIUS) * 0.25)
        bodyRadius = round((self.__BODY_RADIUS + other.__BODY_RADIUS) * 0.25)
        bodyHeight = round((self.__BODY_HEIGHT + other.__BODY_HEIGHT) * 0.125)
        return Orbian(name, headRadius, bodyRadius, bodyHeight)
    



