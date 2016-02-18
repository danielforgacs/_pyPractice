import sys
import unittest

# print(sys.argv)
print(__name__)
print(__file__)

class TdeTest(unittest.TestCase):
    def test__tests_are_running(self):
        print('0th test')
        self.assertTrue(True)

if __name__ == '__main__':
    print('ok')

# unittest.main(module=__name__, argv=[__file__])

suite = unittest.TestLoader().loadTestsFromTestCase(TdeTest)
unittest.TextTestRunner(verbosity=2).run(suite)
