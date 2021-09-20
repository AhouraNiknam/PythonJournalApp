#Read Only
myFile = open("test.txt", "r")
journalEntries = myFile.read()
myFile.close()

print("\nMy Journal Entries: \n" + journalEntries)