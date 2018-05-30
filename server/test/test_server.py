import unittest

from server.storage import *
from server.messagehub import *

class test_server (unittest.TestCase):
       

    def test_trivial(self):
        self.assertEqual(1,1) 


    def test_storage(self):
        removeItem("test-key")

        result = removeItem("test-key")
        self.assertFalse(result, "failed1")

        result = hasItem("test-key")
        self.assertFalse(result, "failed2")
        
        result = storeItem("test-key", "test-value2")
        self.assertTrue(result, "failed3")

        readValue = getItem("test-key")
        self.assertEqual(readValue, "test-value2")

        result = hasItem("test-key")
        self.assertTrue(result, "failed4")

        result = removeItem("test-key")
        self.assertTrue(result, "failed5")


    def test_get_key(self):

        result = storeItem("test-key", "test-value42")
        self.assertTrue(result, "failed1")

        message = {"type":"get_key", "key":"test-key"}
        result = handleGetKey(message)
        self.assertEqual(result["value"], "test-value42")

        result = removeItem("test-key")
        self.assertTrue(result, "failed2")

        message = {"type":"get_key", "key":"test-key"}
        result = handleGetKey(message)
        self.assertEqual(result["err"], "key_not_found")
        
        message = {"type":"get_key", "no_key_exists":"haha"}
        result = handleGetKey(message)
        self.assertEqual(result["err"], "key_not_found")


    def test_set_key(self):

        result = storeItem("test-key", "test-value42")
        self.assertTrue(result, "failed1")
        
        message = {"type":"set_key", "key":"test-key", "value":"test-value23"}
        result = handleSetKey(message)
        self.assertEqual(result["result"], True)
                
        message = {"type":"set_key", "key":"test-key23", "value":"test-value23"}
        result = handleSetKey(message)
        self.assertEqual(result["err"], "key_not_found")
                
        message = {"type":"set_key", "no_key_exists":"haha"}
        result = handleSetKey(message)
        self.assertEqual(result["err"], "key_not_found")

