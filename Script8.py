#Discription: Contents of directory are
#Date: 28/07/21
#Author : Om Deshmukh

from sys import*
import os

def DirectoryTraversal(path):
	print("Contents of directory are")

	for Folder, Subfolder ,Filename in os.walk(path):
		print("Directory name is"+Folder)
		for sub in Subfolder:
			print("Subfolder of "+Folder+"is"+sub)
		for file in Filename:
			print("File name id:"+file)	


def main():
	print("Marvellous Infosystem")
	print("Directory travels in script")

	if(len(argv)!=2):
		print("Error:Invalid num of arguements")
		exit()

	if(argv[1]=="-h") or (argv[1]=="-H"):
		print("It is directory cleaner script")
		exit()

	if(argv[1]=="-u") or (argv[1]=="-U"):
		print("Usage: Provide the absolute path ")
		exit()

	DirectoryTraversal(argv[1])

if __name__ == '__main__':
	main()
