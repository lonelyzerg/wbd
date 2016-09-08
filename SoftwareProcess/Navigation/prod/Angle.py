from math import floor
import types
from warnings import catch_warnings
class Angle():
    def __init__(self):
        self.degree = 0       #set to 0 degrees 0 minutes   
        self.minute = 0.0
    
    def setDegrees(self, degrees):
        inputType = type(degrees)
        if (inputType != types.IntType) & (inputType != types.FloatType):
            raise Exception("Angle.setDegrees: Invalid input (input is not a number)")
        while degrees < 0:
            self.degree += 360
        while self.degree >= 360:
            self.degree -= 360
        self.degree = floor(degrees)
        self.minute = degrees - self.degree
        return self.degree + round(self.minute/60,1)
    
    def setDegreesAndMinutes(self, degrees):
        if type(degrees) != types.StringTypes:
            raise Exception("Angle.setDegreesAndMinutes: Invalid input (input is not a string)")
        data = degrees.split("d")
        if len(data) != 2:
            raise Exception("Angle.setDegreesAndMinutes: Invalid input (input is not formated)")
        try:
            self.degree = int(data[0])
        except ValueError:
            raise Exception("Angle.setDegreesAndMinutes: Invalid input (degree is not an integer)")
        else:
            try:
                self.minute = int(data[1])
            except:
                try:
                    self.minute = float(data[1])
                except:
                    raise Exception("Angle.setDegreesAndMinutes: Invalid input (minute is not a number)")
                    
            else:
                if self.minute < 0:
                        raise Exception("Angle.setDegreesAndMinutes: Invalid input (minute is not positive)")
                while self.minute >= 60:
                    self.minute -= 60
                    self.degree += 1
                while self.degree < 0:
                    self.degree += 360
                while self.degree >= 360:
                    self.degree -= 360
                return self.degree + round(self.minute/60,1)
    
    def add(self, angle):
        if type(angle) != Angle:
            raise Exception("Angle.add: Invalid input (input is not an angle)")
        self.degree += angle.degree
        self.minute += angle.minute
        while self.minute >= 60:
            self.minute -= 60
            self.degree += 1
        while self.degree >= 360:
            self.degree -= 360
        return self.degree + round(self.minute/60,1)
    
    def subtract(self, angle):
        if type(angle) != Angle:
            raise Exception("Angle.subtract: Invalid input (input is not an angle)")
        self.degree -= angle.degree
        self.minute -= angle.minute
        while self.minute >= 60:
            self.minute -= 60
            self.degree += 1
        while self.minute <= 0:
            self.minute += 60
            self.degree -= 1
        while self.degree >= 360:
            self.degree -= 360
        while self.degree < 0:
            self.degree += 360
        return self.degree + round(self.minute/60,1)

    def compare(self, angle):
        if type(angle) != Angle:
            raise Exception("Angle.compare: Invalid input (input is not an angle)")
        if self.degree > angle.degree:
            return 1
        else:
            if self.degree < angle.degree:
                return -1
            else:
                return 0
    
    def getString(self):
        return str(self.degree)+"d"+str(self.minute)
    
    def getDegrees(self):
        return self.degree + round(self.minute/60,1)