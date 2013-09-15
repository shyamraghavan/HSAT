import binascii
from crypto import *

# Asks user for target filename (.format should be included)
fileName = raw_input("Enter target filename: ")

# Stores the file format from filename, hi.pdf... fileFormat will store pdf
fileFormat = fileName.split(".")[1] 

# Opens the file, stores all file data in variable fileData
inputFile = open(fileName)
fileData = inputFile.read()
encryptedData = encryptString(fileData)

# Gets the length of the data in the file
fileLength = len(fileData)

# New list to store format, length, and data
fileList = []

def stringToBin(string):
	return bin(int(binascii.hexlify(string), 16))

def BinToString(binaryString):
	return binascii.unhexlify('%x' % binaryString)

def constructFileList(fileName):
	
	binaryEncryptedData = stringToBin(encryptedData)
	binaryFileFormat = stringToBin(fileFormat)
	
	dataLength = len(binaryEncryptedData)
	
	splitList = []
	for x in range(0, dataLength, 2):
		splitList.append(binaryEncryptedData[x:x+2])
	
	fileList.append(fileFormat)
	fileList.append(dataLength)
	fileList.append(splitList) # fileList[2] gives data (string)
	
	return fileList
