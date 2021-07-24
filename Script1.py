#Discription: This is demo automation script
#Date: 24/07/21
#Author : Om Deshmukh

from sys import *

def main():
	print("------Marvellous Infosystem------")
	print("Script Title;"+argv[0])

	if(len(argv) !=2):
		print("Insuffecient Arguements to the script")
		exit()

	if(argv[1]=="-u"):
		print("Use the script as Namne.py Parameter")

	if(argv[1]=="-h"):
		print("This is demo automation script")	

if __name__ == '__main__':
		main()	
