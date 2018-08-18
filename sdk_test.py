from ctypes import *
import unittest
import sdk

hexutil = CDLL('./lib/hexutil/hexutil.so')

c3 = sdk.NewC3(stateFilePath = './lib/state.json')

class TestSDK(unittest.TestCase):
    def test_registerAndInvokeMethod(self):
        key = ""
        val = ""
        expectKey = "expectKey"
        expectVal = "expectVal"
        methodName = "foo"

        inputKey = c_char_p(hexutil.EncodeString(c_char_p(expectKey.encode('utf-8')))).value.decode('utf-8')
        inputVal = c_char_p(hexutil.EncodeString(c_char_p(expectVal.encode('utf-8')))).value.decode('utf-8')

        def setStuff(k, v):
            nonlocal key
            key = k

            nonlocal val
            val = v

        c3.registerMethod(methodName, setStuff)
        c3.invoke(methodName, inputKey, inputVal)

        self.assertEqual(expectKey, key)
        self.assertEqual(expectVal, val)

if __name__ == '__main__':
    unittest.main()
