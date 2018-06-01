
import os
import base64
import shutil

def read(key:str, name:str) -> bytes:
    
    storageDir = "key-storage/"        
    if not os.path.isdir(storageDir):
        os.makedirs(storageDir)
    
    storageDirForKey = storageDir + key        
    if not os.path.isdir(storageDirForKey):
        return ""
        
    path = storageDirForKey + "/" + name

    #open file & write file
    try:
        with open(path, 'rb') as keyFile:
            return keyFile.read()    
    except FileNotFoundError:
        return b""

    return b""


def store(key:str, name:str, val:bytes) -> bool:
    
    storageDir = "key-storage/"        
    if not os.path.isdir(storageDir):
        os.makedirs(storageDir)
    
    storageDirForKey = storageDir + key        
    if not os.path.isdir(storageDirForKey):
        os.makedirs(storageDirForKey)
        
    path = storageDirForKey + "/" + name

    #open file & write file
    with open(path, 'wb') as keyFile:
        writtenBytes = keyFile.write(val)
        return writtenBytes == len(val)
    
    return False


def storeString(key:str, val:str) -> bool:
    return store(key, "string", val.encode('utf8'))


def getString(key:str) -> str:
    fileData = read(key, "string")
    return str(fileData, 'utf8')


def storeFile(key:str, val:bytes) -> bool:
    return store(key, "file", val)


def getFilePath(key:str) -> str:
    storageDir = "key-storage/"            
    storageDirForKey = storageDir + key        
    return storageDirForKey + "/file"


def storeISFileFlag(key:str, value: bool) -> bool:
    if value:
        return store(key, "isFile", "true".encode('utf8'))
    else:
        return store(key, "isFile", "false".encode('utf8'))


def getISFileFlag(key:str) -> bool:
    fileData = read(key, "isFile")
    return str(fileData, 'utf8') == "true"


def hasAPIKey(key:str) -> bool:
        
    storageDir = "key-storage/"        
    if not os.path.isdir(storageDir):
        os.makedirs(storageDir)        
        
    storageDirForKey = storageDir + key        
    if not os.path.isdir(storageDirForKey):
        return False
    
    return True


def removeAPIKey(key:str) -> bool:
        
    storageDir = "key-storage/"        
    if not os.path.isdir(storageDir):
        os.makedirs(storageDir)
        
    storageDirForKey = storageDir + key        
    if not os.path.isdir(storageDirForKey):
        return False

    try:
        shutil.rmtree(storageDirForKey)
    except OSError:
        return False

    return True