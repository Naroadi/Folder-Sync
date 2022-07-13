# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 01:27:47 2022

@author: naroa
"""
import logging
#Using time for the interval.
import time
#Using dirsync for synchronizing folders.
from dirsync import sync

import sys



#Standard values that I used for testing. 
source_path = r"C:\Users\naroa\Desktop\Test1"
target_path = r"C:\Users\naroa\Desktop\Test1Copy"
logging_path="logs.txt"
interval_seconds=0.5

#Updated arguments

try:
    source_path		 =     sys.argv[1]
    target_path 	 =     sys.argv[2]
    logging_path  	 =     sys.argv[3]
    interval_seconds = int(sys.argv[4])
except:
	pass

#Define portable function

def FolderSync(source = source_path, target = target_path, log_path = logging_path, interval = interval_seconds):
#buffer txt file bacause sync function cant write in 2 places at the same time             
    buffer_file=open("buffer.txt",'a')
#logger for sync fucntion to write in buffer file

    log = logging.getLogger('default_logger')
    log.setLevel(logging.INFO)
    hdl = logging.StreamHandler(buffer_file)
    hdl.setFormatter(logging.Formatter('%(message)s'))
    log.addHandler(hdl)

    logs_file = open(log_path, 'a')
    
    counter=0

    try:
        while True:
        
#syncing source and target with 'sync' and deletion with purge
            sync(source, target ,'sync',logger=log, purge=True) 

#Read from buffer the new log

            read_buffer = open("buffer.txt", "r")
            new_log=read_buffer.read()
            
#Clear buffer
            
            open('buffer.txt', 'w').close()

#Write in console and in logging file the new log

            counter+=1
            t=time.localtime()
            current_time = time.strftime("%a, %d %b %Y %H:%M:%S", t)
            
            print(counter)
            print(current_time)
            print(new_log)
            logs_file.write(str(counter)+"\ncurrenttime\n ")
            logs_file.write(new_log)
            
#Wait interval seconds

            time.sleep(interval)
            
#If Key press abort

    except KeyboardInterrupt:
        pass
#Control+C Causes keyboardInterrupt
    logs_file.close()
    read_buffer.close()
    buffer_file.close()
#Call function

FolderSync()

#Last check

print('Succes')