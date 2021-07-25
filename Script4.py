#Discription: Giving arguements.
#Date: 25/07/21
#Author : Om Deshmukh

import os
import time
import psutil
from sys import *

def ProcessDisplay(FolderName="Marvellous"):
    
    Data = []

    if not os.path.exists(FolderName):
    	os.mkdir(FolderName)

    return
        
    for proc in psutil.process_iter():
        value = proc.as_dict(attrs = ['pid','name','username'])
        Data.append(value)
        
    return Data
    
def main():
    print("------ Marvellous Infosystems ------")
    print("Script title : "+argv[0])

    if(len(argv) !=2):
    	print("Insufficient arguement")
    	exit()

    if(argv[1]=="-u"):
    	print("Usage:Application_Name Directory_NAme")
    	exit()

    if(argv[1]=="-h"):
    	print("Help: It is used to create log file of running process")
    	exit()	

    arr = ProcessDisplay()
    for element in arr:
        print(element)
        
if __name__ == "__main__":
    main()
