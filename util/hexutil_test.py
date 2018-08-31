import unittest
import hexutil

class Test(unittest.TestCase):
    def test_encodeString(self):
        self.assertEqual(hexutil.encodeString('hello'), '0x68656c6c6f')
        self.assertEqual(hexutil.encodeString('123'), '0x313233')

    def test_decodeStr(self):
        self.assertEqual(hexutil.decodeString('0x1234'), b'\x124')
    def test_encodeToString(self):
        self.assertEqual(hexutil.encodeToString(b'hello'), '0x68656c6c6f')

    def test_encodeBytes(self):
        self.assertEqual(hexutil.encodeBytes(b'hello'), b'68656c6c6f')

    def test_decodeBytes(self):
        self.assertEqual(hexutil.decodeBytes(b'68656c6c6f'), b'hello')

    def test_encodeBigInt(self):
        self.assertEqual(hexutil.encodeBigInt(123), b'\x7b')
        self.assertEqual(hexutil.encodeBigInt(53452345), bytes.fromhex('032f9e39'))
        self.assertEqual(hexutil.encodeBigInt(7237005577332262213973186563042994240829374041602535253248099000494570602496), bytes.fromhex('10000000000000000000000000000000000000000000002a646e18c953780000'))

    def test_decodeBigInt(self):
        self.assertEqual(hexutil.decodeBigInt('0x7B'), 123)
        self.assertEqual(hexutil.decodeBigInt('0x10000000000000000000000000000000000000000000002a646e18c953780000'), 7237005577332262213973186563042994240829374041602535253248099000494570602496)

    def test_encodeInt64(self):
        self.assertEqual(hexutil.encodeInt64(123), b'\x7b')
        self.assertEqual(hexutil.encodeInt64(922337203685477807), bytes.fromhex('0ccccccccccccdaf'))

    def test_decodeInt64(self):
        self.assertEqual(hexutil.decodeInt64('0x7b'), 123)
        self.assertEqual(hexutil.decodeInt64('0xccccccccccccdaf'), 922337203685477807)

    def test_encodeFloat64(self):
        self.assertEqual(hexutil.encodeFloat64(123).hex(), '42f60000')
        self.assertEqual(hexutil.encodeFloat64(-561.2863).hex(), 'c40c5253')

    def test_decodeFloat64(self):
        self.assertEqual(hexutil.decodeFloat64('0x42f60000'), 123)
        self.assertEqual(hexutil.decodeFloat64('0x424e4b31'), 51.573429107666016)
        self.assertEqual(hexutil.decodeFloat64('c40c5253'), -561.2863159179688)

    def test_stripPrefix(self):
        self.assertEqual(hexutil.stripPrefix('0x1234'), '1234')
        self.assertEqual(hexutil.stripPrefix('1234'), '1234')
        self.assertEqual(hexutil.stripPrefix('0x'), '')

    def test_addPrefix(self):
        self.assertEqual(hexutil.addPrefix('1234'), '0x1234')
        self.assertEqual(hexutil.addPrefix('0x1234'), '0x1234')

if __name__ == '__main__':
    unittest.main()
