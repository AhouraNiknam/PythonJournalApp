#Create New File
print("")
journalDate = input("Date: ")
journalText = input("\n")
print("")

#Write into text file
myFile = open("test.txt", "a") #append to add at end of text file
myFile.write("\n")
myFile.write("Date: " + journalDate + "\n\n")
myFile.write(journalText)
myFile.write("\n\n")
myFile.close()