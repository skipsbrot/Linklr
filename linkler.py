
'''
Creator: Skipsbrot
Start Date: 10/18/17
CPS: Early Beta
State:MLW(Main Logic Working)
Purpose: This program named Linklr is my attempt to make an automatic link sorter and searcher for us people who like to browse online files a ton
Main Logic: Load a whole file into a dynamic array. Then insert values for new links into the array created. THen output the whole array back into the file.
'''


import os,sys,argparse, datetime

parser = argparse.ArgumentParser()
parser.add_argument("event", help="This specifies what type of event you are creating. [create, search]")
parser.add_argument("type", help="This is what you would like to do woth the event. [link, OU, subOU]")
parser.add_argument('-d', '--debug', help="Turns on debug options", default="n")
parser.add_argument('-f', '--filename', help="Specified the filename used for repo", default="linkRepo.txt")
parser.add_argument('-o', '--OUnit', help="Specifies the ou to create a link ir subOU under.", default="NULL")
args = parser.parse_args()

fileName = args.filename


class Linklr:

	#function is called first to check if we already have a linkRepository file. 
	def fileCheck():
		
		if args.debug == "y": print("Calling Filecheck")#snats Implementation
		
		#These lines Check to see if the file exists. If the file does not then asks the user if he wants to create it. If he doesnt create the file the program exits
		if not os.path.exists(fileName):
			print("File Repo: " + fileName + " does not exist. Would you like to create it: ")#EDIT EDIT: make this print statement print without new line character
			if(input() == "y"):
				if args.debug == "y" : print("Creating File")#snats Implementation
				file = open(fileName, "w+")#file creation
				#file.write("File created on " + str(datetime.datetime.now()))#file date and Time are specified at top of file --- Wrote date and time at top of file but not needed at the moment. 
				file.close()
			else:
				print("Quitting...")#exit code
				quit()

	#function that is responsible for searching for user queries
	def search(arrayOfFile):                                       #Searching Implementation needs implementation
		if args.debug == "y": print("Searching")#snats Implementation
		if args.type == "OU":
			for i in range(len(arrayOfFile)):
				if arrayOfFile[i].rstrip().lstrip() == "-" + args.OUnit:
					j=i+1
					print("Found the following links under " + args.OUnit)
					while(j < len(arrayOfFile) and arrayOfFile[j][0:2] == "--"):
						print(arrayOfFile[j].rstrip().lstrip())
						j+=1
						
	#function that is responsible for creating new files, OUs, sub OUs and links.
	def create(arrayFileInput):
		ouIndex = 0
		if args.debug == "y": print("Creating")#snats Implementation
		if args.type == "OU":
			arrayFileInput.insert(0,"-" + args.OUnit + "\n")#created a new OU at the top of the file 
		
		elif args.type == "link":
			for i in range(len(arrayFileInput)):#Gets the index within the Arrays OU that we want to embed the link within\          #Main Login of file appending to array and then editing array and then appending array back to file works
																																	 #Need to beta test, clean uo code. ALso Implemenet OU creation
				if arrayFileInput[i] == "-" + args.OUnit.rstrip().lstrip() + "\n":#tests if the line is equal to OU inputted in -o argument
					ouIndex = i #if it is we set ouIndex to I 
					if args.debug == "y":print("Found OU at index " + str(ouIndex))#SNATS Implemenatation
					i = len(arrayFileInput) + 1 #and then exit the loop. -- for loop exit code. 
			
			print("Please enter your link: ")
			linkName = input()
			print("Please enter a description")
			description = input()
			arrayFileInput.insert(ouIndex + 1, "--" +  linkName + " @@ " + description + "\n")#
		
		Linklr.arrayWriter(arrayFileInput)#Calls arrayWriter which writes my array to the repo File
		if args.debug == "y":Linklr.printArray(arrayFileInput)#SNATS Implemenatation
		
	#writes given array to file
	def arrayWriter(arrayToWriteToFile):
		#If code exits early for some reason there will be no backup file after that first for loop run. The file will be gone. Create a backup file here. 
		#you idiot create the backup
		if args.debug == "y":print("Writing Array To File")
		repoFile = open(fileName, "w+")
		for i in range(len(arrayToWriteToFile)):
			repoFile.write(arrayToWriteToFile[i])
		
	
	#Function gets how many lines are in the file inputted
	def getFileLength(): ## -- function currently not in use -- keeping for further use if needed
		if args.debug=="y":print("Getting File Length")#SNATS Implemenatation
		repoFile = open(fileName, "r")
		lineCount = 0
		for line in repoFile:
			lineCount+=1
			
		if args.debug=="y":print("Length of file = " + str(lineCount))#SNATS Implemenatation
		return lineCount

	#Function get all current OUs within the repository file
	def getOUs(arrayOfFile):
		if args.debug == "y":print("Getting current OUs in repository")
		for i in range(len(arrayOfFile)):
			if(arrayOfFile[i][0:2] != "--"):
				print(arrayOfFile[i].rstrip().lstrip())
			
	#Takes each line of the file and puts that line as a index within the array
	def fileToArray():
		if args.debug=="y":print("Initializing file to Array")
		arrayOfFile = []
		fileRepo = open(fileName, "r")#Opens our file as read
		index = 0
		for line in fileRepo:#iterates through each line of the fileCheck
			arrayOfFile.insert(index, line)#that line gets assigned to a Dynamic array at the index of index
			index += 1
		return arrayOfFile#return the array of that file
	
	#Function purely for SNATS. 
	def printArray(arrayToPrint):#SNATS Function
		if args.debug == "y":print("Printing Array")#SNATS Implemenatation
		for i in range(len(arrayToPrint)):
			print("Index " + str(i) + " = " + arrayToPrint[i])
		
		
		
	def linkLrMain(self):
		if args.debug == "y": print("Calling Main")#snats Implementation
		#main calls file check to check if our repo file exists.
		Linklr.fileCheck()#first we check to see if out file exists
		arrayOfFile = Linklr.fileToArray()# first we take the whole repoFile and convert each line in that file to an index within an array. Returns array of the file
		
		
		#Functions are executed based on user input. 
		if args.event == "create":# if the user entered create for there first argument then this is executed
			if args.debug == "y":Linklr.printArray(arrayOfFile)#SNATS Implemenatation
			Linklr.create(arrayOfFile)#Then once we have the array of out file we can call a create. This creates what was specified in the second argument and -o argument
		elif args.event == "search":#if the user entered search for there first argument then this is executed
			if args.type == "OUs":
				Linklr.getOUs(arrayOfFile)
			else:	
				Linklr.search(arrayOfFile)#This will search the array of the file for keywords given in the search command
#fileLength = Linklr.getFileLength() not needed at the moment		
linkLrOB = Linklr()
linkLrOB.linkLrMain()
	