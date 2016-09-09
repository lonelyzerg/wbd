'''
Created on 9/7/2016

@author: lonelyzerg
'''
import unittest
from Navigation.prod.Angle import Angle

class Test(unittest.TestCase):
    
    def testSetDegrees(self):
        angle = Angle()
        self.assertEquals(angle.setDegrees(30.5),30.5)
        
    def testSetDegrees2(self):
        angle = Angle()
        self.assertEquals(angle.setDegrees(390.5),30.5)

    def testSetDegrees3(self):
        angle = Angle()
        self.assertEquals(angle.setDegrees(-390.56),329.4)
        
    def testSetDegreesAndMinutes(self):
        angle = Angle()
        self.assertEquals(angle.setDegreesAndMinutes("120d15"),120.3)
        
    def testSetDegreesAndMinutes2(self):
        angle = Angle()
        self.assertEquals(angle.setDegreesAndMinutes("420d61"),61.0)

    def testSetDegreesAndMinutes3(self):
        angle = Angle()
        self.assertEquals(angle.setDegreesAndMinutes("-420d61"),299.0)    
    def testAdd(self):
        angle = Angle()
        angle.setDegrees(25.2)
        angle2 = Angle()
        angle2.setDegrees(340.7)
        self.assertEquals(angle.add(angle2), 5.9)
        
    def testSub(self):
        angle = Angle()
        angle.setDegrees(25.2)
        angle2 = Angle()
        angle2.setDegrees(40.7)
        self.assertEquals(angle.subtract(angle2), 344.5)
        
    def testCompare(self):
        angle = Angle()
        angle.setDegrees(25.2)
        angle2 = Angle()
        angle2.setDegrees(40.7)
        self.assertEquals(angle.compare(angle2), -1)
        
    def testCompare2(self):
        angle = Angle()
        angle.setDegrees(25.2)
        angle2 = Angle()
        angle2.setDegrees(40.7)
        self.assertEquals(angle2.compare(angle), 1)

    def testCompare3(self):
        angle = Angle()
        angle.setDegrees(25.2)
        angle2 = Angle()
        angle2.setDegrees(25.2)
        self.assertEquals(angle2.compare(angle), 0)
        
    def testCompare4(self):
        angle = Angle()
        angle.setDegrees(385.2)
        angle2 = Angle()
        angle2.setDegrees(-334.8)
        self.assertEquals(angle2.compare(angle), 0)
        
    def testget1(self):
        angle = Angle()
        angle.setDegrees(25.24)
        self.assertEquals(angle.getDegrees(),25.2)
        
    def testget2(self):
        angle = Angle()
        angle.setDegrees(25.25)
        self.assertEquals(angle.getString(),"25d15.0")

    def testget3(self):
        angle = Angle()
        angle.setDegrees(25.266)
        self.assertEquals(angle.getString(),"25d16.0")