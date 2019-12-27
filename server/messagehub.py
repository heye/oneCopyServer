
from typing import Dict
from storage import *
import traceback


def handleGetKey(message: Dict) -> Dict[any,any]:
    key = ""
    try:
        key = message["key"]
    except KeyError:
        return {"err": "malformed_request"}

    if not hasAPIKey(key):
        return {"err": "key_not_found"}

    value = getString(key)
    is_file = getISFileFlag(key)

    return {"value": value, "is_file": is_file}


def handleSetKey(message: Dict) -> Dict[any,any]:
    key = ""
    value = ""
    try:
        key = message["key"]
        value = message["value"]
    except KeyError:
        return {"err": "malformed_request"}

    if not hasAPIKey(key):
        return {"err": "key_not_found"}

    value = storeString(key, value)
    storeISFileFlag(key, False)

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