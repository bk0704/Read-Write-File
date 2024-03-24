def writeToFile(fileName, fileText):
    #create and write on a file
    with open(fileName, "w") as f:
        f.write(fileText)
        f.close
def appendToFile(fileName, fileText):
    #append a file already writen
    with open(fileName, "a") as f:
        f.write(fileText)
        f.close
def readFromFile(fileName):
    with open(fileName, "r") as f:
        return f.read()

writeToFile('greet.txt', 'Hello!\n')
appendToFile('greet.txt', 'Goodbye!\n')
assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'