#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 6 de jan de 2019

@author: Jefferson Capovilla
'''

import os
import string
from shutil import copyfile
import countryinfo
import random
    
def mapImage():
    '''
    map each image with a corresponding letter
    '''
    print (string.ascii_lowercase)
    alphabetList = list(string.ascii_lowercase)
    alphabetList.append(".")
    alphabetList.append(" ")
    print (alphabetList)
    
    imageList = []
    fileList = os.listdir("/home/jefcap/eclipse-workspace/secret_message/alphabet")
    for fileName in fileList:
        imageList.append(fileName)
    imageList.sort()
    print (imageList)
    return alphabetList, imageList
    pass

def createCityNameList():
    countryinfo.countries[0]["name"]
    cityNameList = []
    for cityName in countryinfo.countries:
        cityNameList.append(cityName["name"])
    cityNameList.sort()
    return cityNameList
    

def createImageFolder(alphabetList, imageList, message):
    '''
    generate a folder that contain the message using the images
    '''
    srcDir = "/home/jefcap/eclipse-workspace/secret_message/alphabet"
    dstDir = "/home/jefcap/eclipse-workspace/secret_message/secretmessage"
    saved_path = os.getcwd()
    print ("Currently working dir: "+ saved_path)
    os.chdir("/home/jefcap/eclipse-workspace/secret_message/")
    
    cityNameList = createCityNameList()
        
    cityIndex = 0
    for letter in message:
        letterIndex = alphabetList.index(letter)
        alphabetImageLetter = imageList[letterIndex]
        #copy corresponding image to secretmessage folder
        srcFilename = srcDir + "/" + alphabetImageLetter
        #
        outputFilename = cityNameList[cityIndex]
        cityIndex = cityIndex + 1 
        randomNumber = random.randint(1,1001)
        dstFilename = dstDir + "/" + str(randomNumber) +  outputFilename
#         dstFilename = dstDir + "/" + outputFilename  #for not encoded message, comment line above and uncomment this
        copyfile(srcFilename, dstFilename)

def createSecretMessage(message):
    ''' 
    Create a secret message based on the images available, each representing
    one letter.
    ''' 
    [alphabetList, imageList] = mapImage()
    
    createImageFolder(alphabetList, imageList, message)
    pass
    

if __name__ == '__main__':
    message = "type here your secret message"
    message.lower()
    createSecretMessage(message)
    pass