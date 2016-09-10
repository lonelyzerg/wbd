'''
Created on Sep 7, 2016

@author: lonelyzerg
'''
import unittest
from Navigation.prod.Angle import Angle

class Test(unittest.TestCase):
    #valid part
    def test_setDegrees(self):
        angle = Angle()
        self.assertEquals(angle.setDegrees(30.5),30.5)
        
    def test_setDegrees2(self):
        angle = Angle()
        self.assertEquals(angle.setDegrees(390.5),30.5)

    def test_setDegrees3(self):
        angle = Angle()
        self.assertEquals(angle.setDegrees(-390.56),329.4)
        
    def test_setDegreesAndMinutes(self):
        angle = Angle()
        self.assertEquals(angle.setDegreesAndMinutes("120d15"),120.3)
        
    def test_setDegreesAndMinutes2(self):
        angle = Angle()
        self.assertEquals(angle.setDegreesAndMinutes("420d61"),61.0)

    def test_setDegreesAndMinutes3(self):
        angle = Angle()
        self.assertEquals(angle.setDegreesAndMinutes("-420d61"),299.0)    
    def test_add(self):
        angle = Angle()
        angle.setDegrees(25.2)
        angle2 = Angle()
        angle2.setDegrees(340.7)
        self.assertEquals(angle.add(angle2), 5.9)
        
    def test_sub(self):
        angle = Angle()
        angle.setDegrees(25.2)
        angle2 = Angle()
        angle2.setDegrees(40.7)
        self.assertEquals(angle.subtract(angle2), 344.5)
        
    def test_compare(self):
        angle = Angle()
        angle.setDegrees(25.2)
        angle2 = Angle()
        angle2.setDegrees(40.7)
        self.assertEquals(angle.compare(angle2), -1)
        
    def test_compare2(self):
        angle = Angle()
        angle.setDegrees(25.2)
        angle2 = Angle()
        angle2.setDegrees(40.7)
        self.assertEquals(angle2.compare(angle), 1)

    def test_compare3(self):
        angle = Angle()
        angle.setDegrees(25.2)
        angle2 = Angle()
        angle2.setDegrees(25.2)
        self.assertEquals(angle2.compare(angle), 0)
        
    def test_compare4(self):
        angle = Angle()
        angle.setDegrees(385.2)
        angle2 = Angle()
        angle2.setDegrees(-334.8)
        self.assertEquals(angle2.compare(angle), 0)
        
    def test_get1(self):
        angle = Angle()
        angle.setDegrees(25.24)
        self.assertEquals(angle.getDegrees(),25.2)
        
    def test_get2(self):
        angle = Angle()
        angle.setDegrees(25.25)
        self.assertEquals(angle.getString(),"25d15.0")

    def test_get3(self):
        angle = Angle()
        angle.setDegrees(25.266)
        self.assertEquals(angle.getString(),"25d16.0")
        
    #invalid part
    def test_setDegreesF(self):
        angle = Angle()
        expectedString = "Angle.setDegrees:"
        with self.assertRaises(Exception) as context:
            angle.setDegrees("3.01")
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Major:  failure to check for invalid input")

    def test_setDegreesAndMinutesF(self):
        angle = Angle()
        expectedString = "Angle.setDegreesAndMinutes:"
        with self.assertRaises(Exception) as context:
            angle.setDegreesAndMinutes("3.01d1")
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Major:  failure to check for invalid input")
        
    def test_setDegreesAndMinutesF2(self):
        angle = Angle()
        expectedString = "Angle.setDegreesAndMinutes:"
        with self.assertRaises(Exception) as context:
            angle.setDegreesAndMinutes("3d")
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Major:  failure to check for invalid input")

    def test_setDegreesAndMinutesF3(self):
        angle = Angle()
        expectedString = "Angle.setDegreesAndMinutes:"
        with self.assertRaises(Exception) as context:
            angle.setDegreesAndMinutes("d1")
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Major:  failure to check for invalid input")
        
    def test_addF(self):
        angle = Angle()
        expectedString = "Angle.add:"
        with self.assertRaises(Exception) as context:
            angle.add("120d10")
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Major:  failure to check for invalid input")
        
    def test_subF(self):
        angle = Angle()
        expectedString = "Angle.subtract:"
        with self.assertRaises(Exception) as context:
            angle.subtract("120d1")
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Major:  failure to check for invalid input")
        
    def test_compareF(self):
        angle = Angle()
        expectedString = "Angle.compare:"
        with self.assertRaises(Exception) as context:
            angle.compare("120d1")
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Major:  failure to check for invalid input")