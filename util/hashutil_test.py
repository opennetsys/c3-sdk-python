import unittest
import hashutil

class Test(unittest.TestCase):
    def test_new(self):
        self.assertEqual(len(hashutil.new().hex()), 64)

    def test_hash(self):
        self.assertEqual(hashutil.hash('hello world').hex(), '0ac561fac838104e3f2e4ad107b4bee3e938bf15f2b15f009ccccd61a913f017')

    def test_hashToHexString(self):
        self.assertEqual(hashutil.hashToHexString('hello world'), '0x0ac561fac838104e3f2e4ad107b4bee3e938bf15f2b15f009ccccd61a913f017')

    def test_equals(self):
        self.assertEqual(hashutil.equals('0x0ac561fac838104e3f2e4ad107b4bee3e938bf15f2b15f009ccccd61a913f017', 'hello world'), True)

if __name__ == '__main__':
    unittest.main()
