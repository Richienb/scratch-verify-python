import unittest
from scratch_verify import create_code

class Test(unittest.TestCase):

    def test_create_code(self):
        code = create_code()

        self.assertEqual(len(code), 6)
        self.assertEqual(type(code), str)

unittest.main()
