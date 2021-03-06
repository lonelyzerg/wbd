'''
Created on Sep 7, 2016

@author: Tianhang Lan
'''
from math import floor, degrees
import types
from __builtin__ import False
class Angle():
    def __init__(self):
        self.degree = 0         #set to 0 degrees 0 minutes   
        self.minute = 0.0       #set to 0 minute 0 minutes  
    
    def setDegrees(self, degrees = 0.0):
        inputType = type(degrees)
        if (inputType != types.IntType) & (inputType != types.FloatType):
            raise ValueError("Angle.setDegrees: Invalid input (input is not a number)")      #judge if input is a number
        while degrees < 0:
            degrees += 360
        while degrees >= 360:
            degrees -= 360      #mod 360
        self.degree = floor(degrees)
        self.minute = (degrees - self.degree)*60
        return self.degree + self.minute/60.0
    
    def setDegreesAndMinutes(self, angleString):
        minu = self.minute
        degr = self.degree
        
        if isinstance(angleString, basestring) == False:
            self.minute = minu
            self.degree = degr
            raise ValueError("Angle.setDegreesAndMinutes: Invalid input (input is not a string)")
        data = angleString.split("d")
        if len(data) != 2:
            self.minute = minu
            self.degree = degr
            raise ValueError("Angle.setDegreesAndMinutes: Invalid input (input is not formated)")
            errorTag = True
        
        try:
            self.degree = int(data[0])                    
        except:
            self.minute = minu
            self.degree = degr
            raise ValueError("Angle.setDegreesAndMinutes: Invalid input (degree is not a number)")      #judge the format of input
        else:
            if type(self.degree) == types.FloatType:
                self.minute = minu
                self.degree = degr
                raise ValueError("Angle.setDegreesAndMinutes: Invalid input (degree is a float, not an integer)")
            try:
                self.minute = int(data[1])
            except:
                try:
                    self.minute = float(data[1])
                except:
                    self.minute = minu
                    self.degree = degr
                    raise ValueError("Angle.setDegreesAndMinutes: Invalid input (minute is not a number)")
                else:
                    if round(self.minute,1) != float(self.minute):
                        self.minute = minu
                        self.degree = degr
                        raise ValueError("Angle.setDegreesAndMinutes: Invalid input (minute is not a one decimal number)")
        
        if self.minute < 0:
            self.minute = minu
            self.degree = degr
            raise ValueError("Angle.setDegreesAndMinutes: Invalid input (minute is not positive)")       #judge the format of input
        if self.degree < 0:
            self.minute = - self.minute
            self.degree += 360
                
        while self.minute >= 60:
            self.minute -= 60
            self.degree += 1        #mod 60
        while self.minute < 0:
            self.minute += 60
            self.degree -= 1
                
        while self.degree < 0:
            self.degree += 360
        while self.degree >= 360:
            self.degree -= 360      #mod 360     
        return self.degree + self.minute/60.0
    
    def add(self, angle = None):
        if isinstance(angle,Angle) == False:
            raise ValueError("Angle.add: Invalid input (input is not an angle)")     #judge the format of input
        self.degree += angle.degree
        self.minute += angle.minute
        while self.minute >= 60:
            self.minute -= 60
            self.degree += 1        #mod 60
        while self.degree >= 360:
            self.degree -= 360      #mod 360
        return self.degree + self.minute/60.0
    
    def subtract(self, angle = None):
        if isinstance(angle,Angle) == False:
            raise ValueError("Angle.subtract: Invalid input (input is not an angle)")        #judge the format of input
        self.degree -= angle.degree
        self.minute -= angle.minute
        while self.minute >= 60:
            self.minute -= 60
            self.degree += 1
        while self.minute < 0:
            self.minute += 60
            self.degree -= 1        #mod 60
        while self.degree >= 360:
            self.degree -= 360
        while self.degree < 0:
            self.degree += 360      #mod 360
        return self.degree + self.minute/60.0

    def compare(self, angle = None):
        if isinstance(angle,Angle) == False:
            raise ValueError("Angle.compare: Invalid input (input is not an angle)")
        if self.degree > angle.degree:
            return 1
        else:
            if self.degree < angle.degree:
                return -1
            else:
                if self.minute > angle.minute:
                    return 1
                else:
                    if self.minute < angle.minute:
                        return -1
                    else:
                        return 0
    
    def getString(self):
        self.degree = int(self.degree)
        return str(self.degree)+"d"+str(round(self.minute,1))
    
    def getDegrees(self):
        return self.degree + round(self.minute,1)/60.0