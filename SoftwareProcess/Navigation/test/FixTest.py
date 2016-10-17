'''
Created on 10/16/2016

@author: Tianhang Lan
'''
import unittest
import Navigation.prod.Fix as F

class Test(unittest.TestCase):

# Happy path
    def testNew(self):
        self.assertIsInstance(F.Fix("log.txt"), F.Fix)
        
    def testNew2(self):
        self.assertIsInstance(F.Fix(), F.Fix)
        
    def testSet(self):
        fix = F.Fix()
        self.assertEquals(fix.setSightingFile("sight.xml"), "sight.xml")
        
    def testGet(self):
        fix = F.Fix()
        fix.setSightingFile("sight.xml")
        self.assertEquals(fix.getSightings(),("0d0.0","0d0.0"))
        
    def testGet2(self):
        fix = F.Fix()
        fix.setSightingFile("empty.xml")
        self.assertEquals(fix.getSightings(),("0d0.0","0d0.0"))

# Sad path
    def testNewW(self):
        expectedString = "Fix.__init__:"
        with self.assertRaises(ValueError) as context:
            fix = F.Fix(1)                           
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])

    def testSetW(self):
        fix = F.Fix()
        expectedString = "Fix.setSightingFile:"
        with self.assertRaises(ValueError) as context:          
            fix.setSightingFile("sighting")                         
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])

    def testGetW(self):
        fix = F.Fix()
        fix.setSightingFile("badsight.xml")
        expectedString = "Fix.getSightings:"
        with self.assertRaises(ValueError) as context:
            fix.getSightings()                           
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
        
    def testGetW2(self):
        fix = F.Fix()
        expectedString = "Fix.getSightings:"
        with self.assertRaises(ValueError) as context:
            fix.getSightings()                           
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()