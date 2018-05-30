
import os

def getItem(key:str) -> str:
    
    storageDir = "key-storage/"        
    if not os.path.isdir(storageDir):
        os.makedirs(storageDir)
        
    path = storageDir + key

    #open file & write file
    with open(path, 'r') as keyFile:
        line = keyFile.readline()
        return line
    
    return ""



def storeItem(key:str, val:str) -> bool:

    storageDir = "key-storage/"        
    if not os.path.isdir(storageDir):
        os.makedirs(storageDir)
        
    path = storageDir + key

    #open file & write file
    with open(path, 'w') as keyFile:
        writtenChars = keyFile.write(val)

        return writtenChars == len(val)
    
    return False


def hasItem(key:str) -> bool:
        
    storageDir = "key-storage/"        
    if not os.path.isdir(storageDir):
        os.makedirs(storageDir)

    path = storageDir + key

    try:
        with open(path, 'r') as keyFile:
            return True
    except FileNotFoundError:
        return False

    return False


def removeItem(key:str) -> bool:
        
    storageDir = "key-storage/"        
    if not os.path.isdir(storageDir):
        os.makedirs(storageDir)

    path = storageDir + key

    try:
        os.remove(path)
    except FileNotFoundError:
        return False

    return True