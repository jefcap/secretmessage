#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 6 de jan de 2019

@author: Jefferson Capovilla
'''

import os

def rename_files():
    #get the filenames from folder
    secretMessagePath = "/home/jefcap/eclipse-workspace/secret_message/secretmessage"
    file_list = os.listdir(secretMessagePath)
    print (file_list)
    
    saved_path = os.getcwd()
    print ("Currently working dir: "+ saved_path)
    os.chdir(secretMessagePath)
    #for each file, rename filename
    for file_name in file_list:
        table = str.maketrans(dict.fromkeys('0123456789'))
        os.rename(file_name, file_name.translate(table))
    os.chdir(saved_path)
    

if __name__ == '__main__':
    rename_files()
    pass