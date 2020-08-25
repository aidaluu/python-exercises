import time
import pickle

def inputNumber(message):
    while True:
        try:
            num = int(input(message))
            return num
        except Exception:
            print("Invalid input! :(")

def openMemo(fileName):
    try:
        file = open(fileName,"r")
        fileContent = file.read()
        file.close()
        return 1
    except IOError:
        return 0
    
def returnFileAsList(fileName):
    file = open(fileName,"r")

    lines = file.readlines()
    fileAsList = []

    for line in lines:
        trimmedLine = line.replace("\n","")
        fileAsList.append(trimmedLine)
    
    file.close()
    return fileAsList

def createEntry(newEntryText):
    timestamp = time.strftime("%X %x")
    separator = ":::"
    entry = newEntryText + separator + timestamp
    return entry

def main():
    fileName = "memo.dat"
    fileOpenSuccessful = openMemo(fileName)
    if fileOpenSuccessful == False:
        print("Error in file, creating new file memo.dat.")
        file = open(fileName,"w+")
        file.close()
    fileAsList = returnFileAsList(fileName)

    while True:
        print("(1) Read memo\n(2) Add entry\n(3) Edit entry\n\
(4) Remove entry\n(5) Save and quit")
        
        selection = int(input("\nWhat do you want to do?: "))
        
        # Read memo
        if selection == 1:
            for i in fileAsList:
                print(i)
        
        # Add entry
        elif selection == 2:
            newEntryText = input("New entry text: ")
            fileAsList.append(createEntry(newEntryText))
        
        # Edit entry
        elif selection == 3:
            numberOfEntrys = len(fileAsList)
            print("There are",numberOfEntrys,"entrys on the list.")
            userInput = inputNumber("Which one do you want to edit?: ")
            if userInput > numberOfEntrys:
                print("Invalid input! :(")
            else:
                entryToEdit = fileAsList.pop(userInput-1)
                print(entryToEdit)
                newEntryText = input("New entry text: ")
                fileAsList.insert(userInput,createEntry(newEntryText))
            
        # Remove entry
        elif selection == 4:
            numberOfEntrys = len(fileAsList)
            print("There are",numberOfEntrys,"entrys on the list.")
            userInput = inputNumber("Which one do you want to remove?: ")
            if userInput > numberOfEntrys:
                print("Invalid input! :(")
            else:
                entryToEdit = fileAsList.pop(userInput-1)
                print("Entry",entryToEdit,"deleted.")
        
        # Save and quit
        elif selection == 5:
            file = open(fileName,"wb")
            pickle.dump(list(reversed(fileAsList)),file)
            file.close()
            print("Saved and quitting... Bye! :)")
            break
            
if __name__ == "__main__":
    main()
