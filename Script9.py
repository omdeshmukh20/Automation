#Discription: Contents of directory are
#Date: 31/07/21
#Author : Om Deshmukh

from sys import*
import os
import hashlib

def CalculateChecksum(path,blocksize=1024):
	fd=open(path,'rb')
	hobj=hashlib.md5()

	buffer=fd.read(blocksize)
	while len(buffer)>0:
		hobj.update(buffer)
		buffer=fd.read(blocksize)

	fd.close
	return hobj.hexdigest()	

def DirectoryTraversal(path):
	print("Contents of directory are")

	for Folder, Subfolder ,Filename in os.walk(path):
		print("Directory name is"+Folder)
		for sub in Subfolder:
			print("Subfolder of "+Folder+"is"+sub)
		for file in Filename:
			print("File name id:"+file)	

			actualpath=os.path.join(Folder,file)
			hash=CalculateChecksum(actualpath)
			print(hash)

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
