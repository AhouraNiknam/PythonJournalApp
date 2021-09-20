import os.path

def newEntry():
    # Create New File
    print("")
    journalDate = input("Date: ")
    # add some conditional here so date appears as (MM/DD/YYYY)
    journalText = input("\n")
    print("")

    # Write into text file
    if os.path.exists("test.txt"):
        myFile = open("test.txt", "a")  # append to add at end of text file
        myFile.write("\n")
        myFile.write("Date: " + journalDate + "\n\n")
        myFile.write(journalText)
        myFile.write("\n\n")
        myFile.close()

# Read Only
def listEntries():
    print("\n------------------------------------------------------------------------")
    print("My Journal Entries: ")
    print("------------------------------------------------------------------------")

    # Check to make sure file exists before running code
    if os.path.exists("test.txt"):
        myFile = open("test.txt", "r")
        #loop line by line throught the journal file
        for line in myFile:
            if line == "*\n":
                break
            else:
                print(line, end="")
        myFile.close()

    else:
        print("No entries found.")

def helpScreen():
    # Help Screen
    print("\n------------------------------------------------------------------------")
    print("My Journal Help")
    print("------------------------------------------------------------------------\n")
    print("This is a program designed for daily journaling via the command line\n")
    print("Commands:\n")
    print("help - Display help for commands available")
    print("new - Create a new journal entry")
    print("list - View all journal entries")
    print("view <date> - View a single journal entry on given date")
    print("edit <date> - Edit a single journal entry on given date")
    print("delete <date> - Delete an existing journal entry on given date")
    print("delete all - Delete all journal entries")
    print("exit - Exits the program\n\n")

# Main Screen
print("\n------------------------------------------------------------------------")
print("Welcome to My Journal 1.0")
print("------------------------------------------------------------------------\n")
print("Type \"help\" if you need assistance\n")

while True:
    userCommand = input("Please enter a command: ")
    if userCommand == "exit" or userCommand == "Exit" or userCommand == "EXIT":
        break
    elif userCommand == "help" or userCommand == "Help" or userCommand == "HELP":
        helpScreen()
    elif userCommand == "list" or userCommand == "List" or userCommand == "LIST":
        listEntries()
    elif userCommand == "new" or userCommand == "New" or userCommand == "NEW":
        newEntry()
    else:
        print("Invalid input. Please try again")

# View Screen
# print("\n-------------------------------------------------")
# print("08/05/2018")
# print("-------------------------------------------------")
# print("Jounral Entry Title:\n")
# print("Main body paragraphs go here....")

# Edit Screen
# print("\n-------------------------------------------------")
# print("08/05/2018")
# print("-------------------------------------------------")
# print("This is where the new text goes _\n")

# Delete Screen
# print("\n-------------------------------------------------")
# print("Do you wish to delete this journal entry?")
# print("-------------------------------------------------")
# print("08/05/2018")
# print("Jounral Entry Title:")
# print("Main body paragraphs go here....\n")
# print("[YES / NO]  _")

# Delete All Screen
# print("\n-------------------------------------------------")
# print("Do you wish to delete all journal entries?\nThis will wipe the jounral clean.")
# print("-------------------------------------------------")
# print("[YES / NO]  _")
# print("Are you sure? [YES / NO] _")

# ---------------------------------------------------------------------------------------------------------
# givenList = [1, 2, 3, 1, 2, 5, 2, 3]
# newSet = set()
# for x in givenList:
#     newSet.add(x)
# print(newSet)

# newList = list()
# for x in newSet:
#     newList.append(x)
# print(newList)
# ---------------------------------------------------------------------------------------------------------
# Help Screen
# print("\n-------------------------------------------------")
# print("My Journal Help")
# print("-------------------------------------------------\n")
# print("This is a program designed for daily journaling via the command line\n")
# print("Commands:\n")
# print("help - Display help for commands available")
# print("new - Create a new journal entry")
# print("list - View all journal entries")
# print("view <date> - View a single journal entry on given date")
# print("edit <date> - Edit a single journal entry on given date")
# print("delete <date> - Delete an existing journal entry on given date")
# print("delete all - Delete all journal entries\n")

# New Screen
# new_date = input("What is the date? (MM/DD/YYYY) ")
# # print(new_date)
# print("\n-------------------------------------------------")
# print("Date: " + new_date)
# print("-------------------------------------------------")
# journal_text = input("Enter text below: \n")
# print(journal_text)

# List Scrreen
# print("\n-------------------------------------------------")
# print("Journal Entries:")
# print("-------------------------------------------------\n")
# print("08/05/2018 - This is an example text....")
# print("08/09/2018 - This is an example text....")
# print("08/12/2018 - This is an example text....")