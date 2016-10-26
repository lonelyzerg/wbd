'''
Created on 10/10/2016

@author: Tianhang 
'''

import time
import xml.etree.ElementTree as ET
import math

class Fix():
    def __init__(self, logFile = "log.txt"):
        if not isinstance(logFile, str):
            raise ValueError("Fix.__init__: Invalid input (input is not a String)")      #judge if input is a string
            return
        if len(logFile) < 1:
            raise ValueError("Fix.__init__: Invalid input (input length less than 1)")      #judge if input length >= 1
            return
        self.logName = logFile
        try:
            self.logFile = open(self.logName, "a+")
        except:
            raise ValueError("Fix.__init__: unable to open or create the file")      #if unable to open or create, raise exception
            return
        self.sightingFile = None
        self.sightingFileSet = False
        self.writeLog("Start of log", time.gmtime())
        self.logFile.close()
        
    def setSightingFile(self, sightingFile = None):
        if not isinstance(sightingFile, str):
            raise ValueError("Fix.setSightingFile: Invalid input (input is not a String)")      #judge if input is a string
            return
        if len(sightingFile) < 1:
            raise ValueError("Fix.setSightingFile: Invalid input (input length less than 1)")      #judge if input length >= 1
            return
        if sightingFile[-4:] != ".xml":
            raise ValueError("Fix.setSightingFile: Invalid input (input is not an xml file)")      #judge if input is .xml
            return
        if self.sightingFile != None:
            self.sightingFile.close()
        self.sightingFile = None
        try:
            self.sightingFile = open(sightingFile, "a+") 
            self.sightingFile.close()          
        except:
            raise ValueError("Fix.setSightingFile: unable to open or create the xml file")      #if unable to open or create, raise exception
            return
        self.sightingFileSet = True
        self.sightName = sightingFile
        self.writeLog("Start of sighting file" + sightingFile, time.gmtime())
        return sightingFile            

    def getSightings(self):        
        if not self.sightingFile:
            raise ValueError("Fix.getSightings: sighting file not set")
        et = None
        try:
            et = ET.ElementTree(file = self.sightName)
            fix = et.getroot()
            for sightings in fix:
                tup = [None, None, None, None, 0, 72, 1010, "natural"]
                for attr in sightings:                    
                    if attr.tag == "body":
                        if len(attr.text) < 1:
                            raise ValueError("Fix.getSightings: sighting data invalid")
                        tup[0] = (attr.text)
                        
                    if attr.tag == "date":
                        try:
                            dat = attr.text.split("-")
                            time.strptime(attr.text, "%Y-%m-%d")
                            if not (len(dat) == 3 and len(dat[0]) == 4 and len(dat[1]) == 2 and len(dat[2]) == 2):
                                raise ValueError("Fix.getSightings: sighting data invalid")
                            int(dat[0])
                            int(dat[1])
                            int(dat[2])
                        except:                            
                            raise ValueError("Fix.getSightings: sighting data invalid")
                        tup[1] = (attr.text)
                        
                    if attr.tag == "time":
                        try:
                            dat = attr.text.split(":")
                            time.strptime(attr.text, "%H:%M:%S")
                            if not (len(dat) == 3 and len(dat[0]) == 2 and len(dat[1]) == 2 and len(dat[2]) == 2):
                                raise ValueError("Fix.getSightings: sighting data invalid")
                            int(dat[0])
                            int(dat[1])
                            int(dat[2])
                        except:
                            raise ValueError("Fix.getSightings: sighting data invalid")
                        tup[2] = (attr.text)
                        
                    if attr.tag == "observation":
                        try:
                            dat = attr.text.split("d")
                            if not len(dat) == 2:
                                raise ValueError("Fix.getSightings: sighting data invalid")
                            dat[0] = float(dat[0])
                            dat[1] = float(dat[1])
                            if (dat[0] < 0 or dat[0] >= 90 or dat[1] < 0 or dat[1] >= 60) or (dat[0] == 0 and dat[1] <0.1):
                                raise ValueError("Fix.getSightings: sighting data invalid")
                            tup[3] = dat
                        except:
                            raise ValueError("Fix.getSightings: sighting data invalid")
                        
                    if attr.tag == ("height"):
                        try:
                            tup[4] = (float(attr.text))
                            if tup[4] < 0:
                                raise ValueError("Fix.getSightings: sighting data invalid")
                                
                                return
                        except:
                            raise ValueError("Fix.getSightings: sighting data invalid")
                            
                            return
                        
                    if attr.tag == "temperature":
                        try:
                            tup[5] = ((float(attr.text) - 32) * 5 / 9)
                            if tup[5] > 120 or tup[5] < -20:
                                raise ValueError("Fix.getSightings: sighting data invalid")
                                
                                return
                        except:
                            raise ValueError("Fix.getSightings: sighting data invalid")
                            
                            return
                        
                    if attr.tag == ("pressure"):
                        try:
                            tup[6] = (int(attr.text))
                            if tup[6] < 100 or tup[6] > 1100:
                                raise ValueError("Fix.getSightings: sighting data invalid")
                        except:
                            raise ValueError("Fix.getSightings: sighting data invalid")
                        
                    if attr.tag == ("horizon"):
                        if attr.text == "Artificial":
                            tup[7] = 0
                        else:
                            if attr.text == "Natural":
                                tup[7] = attr.text
                            else:
                                raise ValueError("Fix.getSightings: sighting data invalid")
                        tup[7] = (attr.text)
                        
                if tup[0] == None or tup[1] == None or tup[2] == None or tup[3] == None:
                    raise ValueError("Fix.getSightings: Lack mandatory tag")
                    
                    return
                
                if tup[7] != 0:
                    tup[7] = (-0.97 * math.sqrt(tup[4])) / 60.0
                refraction = (-0.00452 * tup[6]) / (273.0 + tup[5]) / math.tan(tup[3][0] + tup[3][1]/60.0)
                adjAlt = tup[7] + refraction + tup[3][0] + tup[3][1]/60.0
                adjustedAltitude = str(int(adjAlt)) + "d" + str(round((adjAlt - int(adjAlt)) * 60, 1))
                self.writeLog(tup[0] + "\t" + tup[1] + "\t" + tup[2] + "\t" + adjustedAltitude, time.gmtime())                
        except:
            self.writeLog("End of sighting file" + self.sightName, time.gmtime())
            raise ValueError("Fix.getSightings: unable to parse the xml file")           
            return
        self.writeLog("End of sighting file" + self.sightName, time.gmtime())
        return ("0d0.0", "0d0.0")
    
    def writeLog(self, content, t):
        self.logFile = open(self.logName, "a+")
        string = "LOG:\t" + str(t.tm_year) + "-" + str("{:0>2d}".format(t.tm_mon)) + "-" + str("{:0>2d}".format(t.tm_mday)) \
            + " " + str("{:0>2d}".format(t.tm_hour)) + ":" + str("{:0>2d}".format(t.tm_min)) + ":" + str("{:0>2d}".format(t.tm_sec)) \
            + "-6:00\t" + content + "\n"
        self.logFile.write(string)
        self.logFile.close()
