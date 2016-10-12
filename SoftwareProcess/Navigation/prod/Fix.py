'''
Created on 10/10/2016

@author: Tianhang 
'''


class Fix():
    def __init__(self, logFile = "log.txt"):
        if (isinstance(logFile, str)):
            raise ValueError("Fix.__init__: Invalid input (input is not a String)")      #judge if input is a string
            return
        if logFile.length < 1:
            raise ValueError("Fix.__init__: Invalid input (input length less than 1)")      #judge if input length >= 1
            return
        self.logFile = open(logFile, "a+")
        
    def setSightingFile(self, sightingFile = None):
        if (isinstance(sightingFile, str)):
            raise ValueError("Fix.setSightingFile: Invalid input (input is not a String)")      #judge if input is a string
            return
        if sightingFile.length < 1:
            raise ValueError("Fix.setSightingFile: Invalid input (input length less than 1)")      #judge if input length >= 1
            return