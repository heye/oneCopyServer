
from typing import Dict
from server.storage import *
import traceback


def handleDownload(apikey: str) -> bytes:
    
    if not hasAPIKey(apikey):
        return b'';

    return getFilePath(apikey)


def handleUpload(data: bytes, apikey: str) -> Dict[any,any]:

    #check if api-key folder exists
    
    #delete temp.file

    #create & write temp.file

    #return json for success
    dataSize = len(data)
        
    print("file upload for: " + apikey)
    print("size: " + str(dataSize))

    if dataSize > 100000000:
        return {"err":"file_too_big"}

    reply = {"err": "unkown_type"}
    try:        
        if not hasAPIKey(apikey):
            return {"err": "key_not_found"}

        if not storeFile(apikey, data):
            return {"err": "err_writing_file"}
        else:
            storeISFileFlag(apikey, True)
            return {"result": True}
        
            
    except:        
        traceback.print_exc()
        return {"err": "format_or_auth_error"}

    return reply
