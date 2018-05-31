
import os
import base64

def getItem(key:str) -> str:
    
    storageDir = "key-storage/"        
    if not os.path.isdir(storageDir):
        os.makedirs(storageDir)
        
    path = storageDir + key

    #open file & write file
    with open(path, 'r') as keyFile:
        line = keyFile.readline()
        return base64.b64decode(bytes(line, 'utf-8')).decode("utf-8") 
    
    return ""



def storeItem(key:str, val:str) -> bool:

    val = base64.b64encode(bytes(val, 'utf-8'))
    val = val.decode("utf-8") 

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