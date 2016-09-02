from math import floor
import types
class Angle():
    def __init__(self):
        self.degree = 0       #set to 0 degrees 0 minutes
        self.minute = 0.0
    
    def setDegrees(self, degrees):
        inputType = types(degrees)
        if (inputType != types.IntType) & (inputType != types.FloatType):
            raise Exception("Angle.setDegrees: Invalid input (input is not a number)", inputType)
        self.degree = floor(degrees)
        self.minute = degrees - self.degree
    
    def setDegreesAndMinutes(self, degrees):
        pass
    
    def add(self, angle):
        pass
    
    def subtract(self, angle):
        pass
    
    def compare(self, angle):
        pass
    
    def getString(self):
        pass
    
    def getDegrees(self):
        pass