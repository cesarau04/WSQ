def checkBanana(nameFile):
    openFile = open(nameFile, encoding='utf-8') #Open file
    fileRead = openFile.read() #Read file
    fileLower = fileRead.lower() #Conver file to lowercase
    fileList = fileLower.split() #Make the list
    occurrence = fileList.count('banana')
    return occurrence


def main():
    nameFile = input('Name of the file you want to open:\n')
    print('The occurrence of banana is', checkBanana(nameFile))

if __name__ == "__main__":
    main()
