
from typing import Dict
from server.storage import *
import traceback


def handleGetKey(message: Dict) -> Dict[any,any]:
    key = ""
    try:
        key = message["key"]
    except KeyError:
        return {"err": "malformed_request"}

    if not hasItem(key):
        return {"err": "key_not_found"}

    value = getItem(key)

    return {"value": value}


def handleSetKey(message: Dict) -> Dict[any,any]:
    key = ""
    value = ""
    try:
        key = message["key"]
        value = message["value"]
    except KeyError:
        return {"err": "malformed_request"}

    if not hasItem(key):
        return {"err": "key_not_found"}

    value = storeItem(key, value)

    return {"result": value}


def handleMessage(message: Dict) -> Dict[any,any]:
    print(message)

    try:
        reply = {"err": "unkown_type"}
        
        if(message["type"] == "get_key"):
            return handleGetKey(message)

        if(message["type"] == "set_key"):
            return handleSetKey(message)
            
    except:        
        #print(sys.exc_info())
        traceback.print_exc()

        return {"err": "format_or_auth_error"}

    return reply