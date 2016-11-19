'''
Created on 10/10/2016

@author: Tianhang 
'''

import time
import xml.etree.ElementTree as ET
import math
import os.path as path
from math import floor


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
        self.ariesFile = None
        self.starFile = None
        self.sightingFileSet = False
        self.ariesFileSet = False
        self.starFileSet = False
        self.writeLog("Log file:\t" + path.abspath(logFile), time.gmtime())
        
    def setSightingFile(self, sightingFile = None):
        if not isinstance(sightingFile, str):
            raise ValueError("Fix.setSightingFile: Invalid input (input is not a String)")      #judge if input is a string
            return
        if len(sightingFile) < 5:
            raise ValueError("Fix.setSightingFile: Invalid input (input length less than 1)")      #judge if input length >= 1
            return
        if sightingFile[-4:] != ".xml":
            raise ValueError("Fix.setSightingFile: Invalid input (input is not an xml file)")      #judge if input is .xml
            return
        if not path.isfile(sightingFile):
            raise ValueError("Fix.setSightingFile: File not exit")      #judge if input is a file
            return
        if self.sightingFile != None:
            self.sightingFile.close()
        self.sightingFile = None
        try:
            self.sightingFile = open(sightingFile, "a") 
            self.sightingFile.close()          
        except:
            raise ValueError("Fix.setSightingFile: unable to open or create the xml file")      #if unable to open or create, raise value error
            return
        self.sightingFileSet = True
        self.sightName = sightingFile
        self.writeLog("Sighting file:\t" + path.abspath(sightingFile), time.gmtime())
        return path.abspath(sightingFile)           
    
    def setAriesFile(self, ariesFile = None):
        if not isinstance(ariesFile, str):
            raise ValueError("Fix.setAriesFile: Invalid input (input is not a String)")      #judge if input is a string
            return
        if len(ariesFile) < 4:
            raise ValueError("Fix.setAriesFile: Invalid input (input length less than 1)")      #judge if input length >= 1
            return
        if ariesFile[-4:] != ".txt":
            raise ValueError("Fix.setAriesFile: Invalid input (input is not an txt file)")      #judge if input is .txt
            return
        if not path.isfile(ariesFile):
            raise ValueError("Fix.setAriesFile: File not exit")      #judge if input is a file
            return
        if self.ariesFile != None:
            self.ariesFile.close()
        self.ariesFile = None
        try:
            self.ariesFile = open(ariesFile, "a") 
            self.ariesFile.close()          
        except:
            raise ValueError("Fix.setAriesFile: unable to open or create the txt file")      #if unable to open or create, raise value error
            return
        self.ariesFileSet = True
        self.ariesName = ariesFile
        self.writeLog("Aries file:\t" + path.abspath(ariesFile), time.gmtime())
        return path.abspath(ariesFile) 
    
    def setStarFile(self, starFile = None):
        if not isinstance(starFile, str):
            raise ValueError("Fix.setStarFile: Invalid input (input is not a String)")      #judge if input is a string
            return
        if len(starFile) < 4:
            raise ValueError("Fix.setStarFile: Invalid input (input length less than 1)")      #judge if input length >= 1
            return
        if starFile[-4:] != ".txt":
            raise ValueError("Fix.setStarFilee: Invalid input (input is not an txt file)")      #judge if input is .txt
            return
        if not path.isfile(starFile):
            raise ValueError("Fix.setStarFile: File not exit")      #judge if input is a file
            return
        if self.starFile != None:
            self.starFile.close()
        self.starFile = None
        try:
            self.starFile = open(starFile, "a") 
            self.starFile.close()          
        except:
            raise ValueError("Fix.setStarFile: unable to open or create the txt file")      #if unable to open or create, raise value error
            return
        self.starFileSet = True
        self.starName = starFile
        self.writeLog("Star file:\t" + path.abspath(starFile), time.gmtime())
        return path.abspath(starFile) 
    
    def getSightings(self):        
        if not (self.sightingFileSet and self.ariesFileSet and self.starFileSet):
            raise ValueError("Fix.setStarFile: Files not set")
        outputList = []
        et = None
        self.faultCount = 0 
        try:
            et = ET.ElementTree(file = self.sightName)
            fix = et.getroot()
            self.list = None
            for sightings in fix:
                self.fault = False
                tup = [None, None, None, None, 0, 22.2222222, 1010, 1, 0, None, None]
                for attr in sightings:                    
                    if attr.tag == "body":
                        if attr.text == None or len(attr.text) < 1:
                            self.fault = True
                            break
    #                             raise ValueError("Fix.getSightings: sighting data invalid")
                        tup[0] = (attr.text)
                        
                    if attr.tag == "date":
                        try:
                            dat = attr.text.split("-")
                            self.date = time.strptime(attr.text, "%Y-%m-%d")
                            if not (len(dat) == 3 and len(dat[0]) == 4 and len(dat[1]) == 2 and len(dat[2]) == 2):
                                self.fault = True
                                continue
    #                                 raise ValueError("Fix.getSightings: sighting data invalid")
                            int(dat[0])
                            int(dat[1])
                            int(dat[2])
                        except:
                            self.fault = True
                            continue                     
    #                             raise ValueError("Fix.getSightings: sighting data invalid")
                        tup[1] = self.date
                        
                    if attr.tag == "time":
                        try:
                            dat = attr.text.split(":")
                            self.time = time.strptime(attr.text, "%H:%M:%S")
                            if not (len(dat) == 3 and len(dat[0]) == 2 and len(dat[1]) == 2 and len(dat[2]) == 2):
                                self.fault = True
                                continue
    #                                 raise ValueError("Fix.getSightings: sighting data invalid")
                            int(dat[0])
                            int(dat[1])
                            int(dat[2])
                        except:
                            self.fault = True
                            continue
    #                             raise ValueError("Fix.getSightings: sighting data invalid")
                        tup[2] = self.time
                        
                    if attr.tag == "observation":
                        try:
                            dat = attr.text.split("d")
                            if not len(dat) == 2:
                                raise ValueError("Fix.getSightings: sighting data invalid")
                            dat[0] = float(dat[0])
                            dat[1] = float(dat[1])
                            if (dat[0] < 0 or dat[0] >= 90 or dat[1] < 0 or dat[1] >= 60) or (dat[0] == 0 and dat[1] <0.1):
                                self.fault = True
                                continue
    #                                 raise ValueError("Fix.getSightings: sighting data invalid")
                            tup[3] = dat
                        except:
                            self.fault = True
                            continue
    #                             raise ValueError("Fix.getSightings: sighting data invalid")
                        
                    if attr.tag == ("height"):
                        try:
                            tup[4] = (float(attr.text))
                            if tup[4] < 0:
                                self.fault = True
                                tup[4] = None
                                continue
    #                                 raise ValueError("Fix.getSightings: sighting data invalid")
    #                                 return
                        except:
                            self.fault = True
                            tup[4] = None
                            continue
    #                             raise ValueError("Fix.getSightings: sighting data invalid")
    #                             return
                        
                    if attr.tag == "temperature":
                        try:
                            tup[5] = ((float(attr.text) - 32) * 5 / 9.0)
                            if tup[5] > 120 or tup[5] < -20:
                                self.fault = True
                                continue
    #                                 raise ValueError("Fix.getSightings: sighting data invalid")
    #                                 return
                        except:
                            self.fault = True
                            continue
    #                             raise ValueError("Fix.getSightings: sighting data invalid")
    #                             return
                        
                    if attr.tag == ("pressure"):
                        try:
                            tup[6] = (int(attr.text))
                            if tup[6] < 100 or tup[6] > 1100:
                                self.fault = True
                                continue
    #                                 raise ValueError("Fix.getSightings: sighting data invalid")
                        except:
                            self.fault = True
                            continue
    #                             raise ValueError("Fix.getSightings: sighting data invalid")
                        
                    if attr.tag == ("horizon"):
                        if attr.text == "Artificial" or attr.text == "artificial":
                            tup[7] = 0
                        else:
                            if attr.text == "Natural" or attr.text == "natural":
                                tup[7] = 1
                            else:
                                self.fault = True
                                continue
    #                                 raise ValueError("Fix.getSightings: invalid horizon")                   
    #                                 return
                
                if tup[0] == None or tup[1] == None or tup[2] == None or tup[3] == None or self.fault == True:
                    self.faultCount += 1
                    continue 
                             
                 
                self.fault = False
                lat = None
                #lot = None
                templat = None
                tempsha = None
                self.sha = [None, None]
                self.gha1 = [None, None]
                self.gha2 = [None, None]   
                self.gha = [None, None]
                 
                st = open(self.starName)
                for line in st:
                    try:
                        line = line.replace("\n", "")
                        content = line.split("\t")
                        if content[0] == tup[0]:
                            print content[1]
                            starDate = time.strptime(content[1], "%m/%d/%y")
                            if starDate == tup[1]:
                                lat = content[3].split("d")
                                a = int(lat[0])
                                b = float(lat[1])
                                if len(lat) != 2 or a < -90 or a >= 90 or b < 0 or b >= 60:
                                    self.fault = True
                                    break
                                tempsha = content[2].split("d")
                                a = int(tempsha[0])
                                b = float(tempsha[1])
                                if len(tempsha) != 2 or a < 0 or a >= 360 or b < 0 or b >= 60:
                                    self.fault = True
                                    break
                                tup[9] = content[3]
                                self.sha[0] = a
                                self.sha[1] = b
                                print line
                                break
                            else:
                                if starDate < tup[1]:
                                    templat = content[3].split("d")
                                    a = int(templat[0])
                                    b = float(templat[1])
                                    if len(templat) != 2 or a < -90 or a > 90 or b < 0 or b >= 60:
                                        self.fault = True
                                        break
                                    tempsha = content[2].split("d")
                                    a = int(tempsha[0])
                                    b = float(templat[1])
                                    if len(tempsha) != 2 or a < 0 or a >= 360 or b < 0 or b >= 60:
                                        self.fault = True
                                        break
                                else:
                                    if templat == None or tempsha == None:
                                        self.fault = True
                                        break
                                    tup[9] = content[3]
                                    self.sha[0] = a
                                    self.sha[1] = b
                                    break                                    
                    except:
                        self.fault = True
                        break
                st.close()
                ar = open(self.ariesName)
                for line in ar:
                    try:
                        line = line.replace("\n", "")
                        content = line.split("\t")
                        temptime = time.strptime(content[0], "%m/%d/%y")          
                        if temptime == tup[1]:
                            if int(content[1]) == tup[2].tm_hour:
                                temp = content[2].split("d")
                                self.gha1[0] = int(temp[0])
                                self.gha1[1] = float(temp[1])
                                if self.gha1[0] >= 360 or self.gha1[0] < 0 or self.gha1[1] >= 60.0 or self.gha1[1] < 0.0:
                                    self.fault = True
                                    break
                            else:
                                if int(content[1]) == self.time.tm_hour + 1 and self.gha1[0] != None and self.gha1[1] != None:
                                    temp = content[2].split("d")
                                    self.gha2[0] = int(temp[0])
                                    self.gha2[1] = float(temp[1])
                                    if self.gha2[0] >= 360 or self.gha2[0] < 0 or self.gha2[1] >= 60.0 or self.gha2[1] < 0.0:
                                        self.fault = True
                                        break
                                    break
                        else:
                            if  temptime.tm_year == tup[1].tm_year and temptime.tm_mon == tup[1].tm_mon and temptime.tm_mday == tup[1].tm_mday + 1:
                                if int(content[1]) == 0 and self.gha1[0] != None and self.gha1[1] != None:
                                    temp = content[2].split("d")
                                    self.gha2[0] = int(temp[0])
                                    self.gha2[1] = float(temp[1])
                                    if self.gha2[0] >= 360 or self.gha2[0] < 0 or self.gha2[1] >= 60.0 or self.gha2[1] < 0.0:
                                        self.fault = True
                                        break
                                    break
                    except:
                        self.fault = True
                        break
                ar.close()

                try:
                    gha = self.gha1[0] + self.gha1[1]/60.0 + abs(self.gha2[0] + self.gha2[1]/60.0 - (self.gha1[0] + self.gha1[1]/60.0)) * (tup[2].tm_min * 60 + tup[2].tm_sec)/3600
                    self.gha[0] = floor(gha)
                    self.gha[1] = round((gha - self.gha[0]) * 60, 1)
                    while self.gha[0] >= 360:
                        self.gha -= 360
                    tup[10] = str(self.gha[0]) + "d" + str(self.gha[1])
                except:
                    self.fault = True

                if tup[9] == None or tup[10] == None or self.fault == True:  
                    self.faultCount += 1
                    continue 
    #                                      
    #                     return            
                if tup[7] != 0:
                    tup[7] = (-0.97 * math.sqrt(tup[4])) / 60.0
                refraction = (-0.00452 * tup[6]) / (273.0 + tup[5]) / math.tan((tup[3][0] + tup[3][1] / 60.0) / 180 * math.pi)
                adjAlt = tup[7] + refraction + tup[3][0] + tup[3][1]/60.0
                tup[8] = str(int(adjAlt)) + "d" + str(round((adjAlt - int(adjAlt)) * 60, 1))                
                if self.fault:
                    self.faultCount += 1
                    continue  
                outputList.append(tup)
                outputList = sorted(outputList, key = lambda outputList:(outputList[1], outputList[2]), reverse = True)
                for item in outputList:
                    self.writeLog(item[0] + "\t" + time.strftime("%Y-%m-%d",item[1]) + "\t" + time.strftime("%H:%M:%S",item[2]) + "\t" + item[8] + "\t" + item[9] + "\t" + item[10], time.gmtime())
                
#                 self.writeLog(tup[0] + "\t" + tup[1] + "\t" + tup[2] + "\t" + adjustedAltitude, time.gmtime()) 
             
        except:
            self.writeLog("End of sighting file" + self.sightName, time.gmtime())
            raise ValueError("Fix.getSightings: unable to parse the xml file")           
            return
        self.writeLog("Sighting errors:\t" + str(self.faultCount), time.gmtime())
        self.writeLog("End of sighting file " + self.sightName, time.gmtime())
        return ("0d0.0", "0d0.0")
    
    def writeLog(self, content, t):
        self.logFile = open(self.logName, "a+")
        string = "LOG:\t" + str(t.tm_year) + "-" + str("{:0>2d}".format(t.tm_mon)) + "-" + str("{:0>2d}".format(t.tm_mday)) \
            + " " + str("{:0>2d}".format(t.tm_hour)) + ":" + str("{:0>2d}".format(t.tm_min)) + ":" + str("{:0>2d}".format(t.tm_sec)) \
            + "-6:00\t" + content + "\n"
        self.logFile.write(string)
        self.logFile.close()
