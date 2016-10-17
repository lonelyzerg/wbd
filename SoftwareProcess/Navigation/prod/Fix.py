'''
Created on 10/10/2016

@author: Tianhang 
'''
import os.path.isfile as isfile
import time
import xml.etree.ElementTree as ET
import math

class Fix():
    def __init__(self, logFile = "log.txt"):
        if (isinstance(logFile, str)):
            raise ValueError("Fix.__init__: Invalid input (input is not a String)")      #judge if input is a string
            return
        if logFile.length < 1:
            raise ValueError("Fix.__init__: Invalid input (input length less than 1)")      #judge if input length >= 1
            return
        self.logName = logFile
        try:
            self.logFile = open(self.logName, "a+")
        except:
            raise ValueError("Fix.__init__: unable to open or create the file")      #if unable to open or create, raise exception
            return
        time = time.gmtime()
        self.sightingFile = None
        self.sightingFileSet = False
        self.writeLog("Start of log", time.gmtime())
        
    def setSightingFile(self, sightingFile = None):
        if (isinstance(sightingFile, str)):
            raise ValueError("Fix.setSightingFile: Invalid input (input is not a String)")      #judge if input is a string
            return
        if sightingFile.length < 1:
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
            self.writeLog("End of sighting file" + self.sightingFile)
            return
        et = None
        try:
            et = ET.ElementTree(file = self.sightingFile)
            fix = et.getroot()
            for sightings in fix:
                for attr in sightings:
                    tup = [None, None, None, None, 0, 72, 1010, "natural"]
                    if attr.tag == "body":
                        if len(attr.text) < 1:
                            raise ValueError("Fix.getSightings: sighting data invalid")
                            self.writeLog("End of sighting file" + self.sightingFile)
                            return
                        tup[0] = (attr.text)
                        
                    if attr.tag == "date":
                        try:
                            dat = attr.text.split("-")
                            if not (dat.length == 3 and len(dat[0]) == 4 and len(dat[1]) == 2 and len(dat[2]) == 2):
                                raise ValueError("Fix.getSightings: sighting data invalid")
                                self.writeLog("End of sighting file" + self.sightingFile)
                                return
                            int(dat[0])
                            int(dat[1])
                            int(dat[2])
                        except:
                            raise ValueError("Fix.getSightings: sighting data invalid")
                            self.writeLog("End of sighting file" + self.sightingFile)
                            return
                        tup[1] = (attr.text)
                        
                    if attr.tag == "time":
                        try:
                            dat = attr.text.split(":")
                            if not (dat.length == 3 and len(dat[0]) == 2 and len(dat[1]) == 2 and len(dat[2]) == 2):
                                raise ValueError("Fix.getSightings: sighting data invalid")
                                self.writeLog("End of sighting file" + self.sightingFile)
                                return
                            int(dat[0])
                            int(dat[1])
                            int(dat[2])
                        except:
                            raise ValueError("Fix.getSightings: sighting data invalid")
                            self.writeLog("End of sighting file" + self.sightingFile)
                            return
                        tup[2] = (attr.text)
                        
                    if attr.tag == "observation":
                        try:
                            dat = attr.text.split("d")
                            if not dat.length == 2:
                                raise ValueError("Fix.getSightings: sighting data invalid")
                                self.writeLog("End of sighting file" + self.sightingFile)
                                return
                            dat[0] = float(dat[0])
                            dat[1] = float(dat[1])
                            if dat[0] < 0 or dat[0] >= 90 or dat[1] < 0 or dat[1] >= 60:
                                raise ValueError("Fix.getSightings: sighting data invalid")
                                self.writeLog("End of sighting file" + self.sightingFile)
                                return
                            tup[3] = dat
                        except:
                            raise ValueError("Fix.getSightings: sighting data invalid")
                            self.writeLog("End of sighting file" + self.sightingFile)
                            return
                        
                    if attr.tag == ("height"):
                        try:
                            tup[4] = (float(attr.text))
                            if tup[4] < 0:
                                raise ValueError("Fix.getSightings: sighting data invalid")
                                self.writeLog("End of sighting file" + self.sightingFile)
                                return
                        except:
                            raise ValueError("Fix.getSightings: sighting data invalid")
                            self.writeLog("End of sighting file" + self.sightingFile)
                            return
                        
                    if attr.tag == "temperature":
                        try:
                            tup[5] = ((float(attr.text) - 32) * 5 / 9)
                            if tup[5] > 120 or tup[5] < -20:
                                raise ValueError("Fix.getSightings: sighting data invalid")
                                self.writeLog("End of sighting file" + self.sightingFile)
                                return
                        except:
                            raise ValueError("Fix.getSightings: sighting data invalid")
                            self.writeLog("End of sighting file" + self.sightingFile)
                            return
                        
                    if attr.tag == ("pressure"):
                        try:
                            tup[6] = (int(attr.text))
                            if tup[6] < 100 or tup[6] > 1100:
                                raise ValueError("Fix.getSightings: sighting data invalid")
                                self.writeLog("End of sighting file" + self.sightingFile)
                                return
                        except:
                            raise ValueError("Fix.getSightings: sighting data invalid")
                            self.writeLog("End of sighting file" + self.sightingFile)
                            return
                        
                    if attr.tag == ("horizon"):
                        if attr.text != "artificial":
                            tup[7] = 0
                        else:
                            if attr.text == "natural":
                                tup[7] = attr.text
                            else:
                                raise ValueError("Fix.getSightings: sighting data invalid")
                                self.writeLog("End of sighting file" + self.sightingFile)
                                return
                        tup[7] = (attr.text)
                        
                if tup[0] == None or tup[1] == None or tup[2] == None or tup[3] == None:
                    raise ValueError("Fix.getSightings: Lack mandatory tag")
                    self.writeLog("End of sighting file" + self.sightingFile)
                    return
                
                if tup[7] != 0:
                    tup[7] = (-0.97 * math.sqrt(tup[4])) / 60.0
                refraction = (-0.00452 * tup[6]) / (273.0 + tup[5]) / math.tan(tup[3][0] + tup[3][1]/60.0)
                adjAlt = tup[7] + refraction + tup[3][0] + tup[3][1]/60.0
                self.writeLog(tup[0] + "\t" + tup[1] + "\t" + tup[2] + "\t" + str(adjAlt))
                
        except:
            raise ValueError("Fix.getSightings: unable to parse the xml file")
            self.writeLog("End of sighting file" + self.sightingFile)
            return
        return ("0d0.0", "0d0.0")
    
    def writeLog(self, content, t):
        string = "LOG:\t" + str(t.tm_year) + "-" + str("{:0>2d}".format(t.tm_mon)) + "-" + str("{:0>2d}".format(t.tm_mday)) \
            + " " + str("{:0>2d}".format(t.tm_hour)) + ":" + str("{:0>2d}".format(t.tm_min)) + ":" + str("{:0>2d}".format(t.tm_sec)) \
            + "-6:00\t" + content + "\n"
        self.logFile.write(string)
        
        
            
            
