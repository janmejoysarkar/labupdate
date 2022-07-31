#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 11:06:56 2022

@author: janmejoy
"""
import os
import glob
import time
from datetime import datetime
    
while True:
    
    tqcmpath='/home/janmejoy/Dropbox/SUIT_Docs/TQCM Datalog/*'
    chamberpath= '/home/janmejoy/Dropbox/SUIT_Docs/Vacuum Chamber Datalog/*'
    
    ### TQCM ##
    tqcmfiles= glob.glob(tqcmpath) #glob gives list of files based on a path pattern
    latestfile= max(tqcmfiles, key= os.path.getctime) #selecting latest file based on modification time
    
    tqcmfile= open(latestfile, 'r')
    filedata= tqcmfile.readlines()
    tqcmfile.close()
    tqcm= filedata[len(filedata)-1].split(' ')
    
    ## Vacuum Chamber ##
    
    latestfolder= max(glob.glob(chamberpath), key= os.path.getctime)
    vc= max(glob.glob(latestfolder + '/*'), key= os.path.getctime)
    
    ## HTML ##
    file= open('parent.html', 'r')
    html= file.readlines()
    file.close()
    
    wp= open('webpage.html', 'w') #Compose the HTML
    
    wp.write('<!DOCTYPE html> \n<html> \n<body> \n<h1>Chamber Vitals</h1> \n')
    
    wp.write('</body> \n</html> \n')
    
    wp.write('<p><h3>Vacuum Chamber HMI (Last Updated: '+vc[56:66]+str(' at ')+vc[75:83]+' )</h3></p>')
    wp.write('<img src="'+vc+'" width= "800">')
    
    wp.write('<p><h3>TQCM</h3></p>')
    wp.write(filedata[1]+'(mm-dd-yyyy)<br>')
    wp.write('Last Readout: '+tqcm[0]+' sec <br>')
    wp.write('Delta Frequency= '+tqcm[3]+' Hz/hr <br>')
    wp.write('Sensor temperature= '+tqcm[2]+' degC <br>')
    wp.write('Sensor Frequency= '+tqcm[1]+' Hz <br>')
    wp.write('<p><small>Janmejoy Sarkar | SUIT Mission</p>')
    
    wp.write('</body> \n</html>')
    wp.close()
    
    print('Last updated: '+ str(datetime.now()))
    time.sleep(1800)
