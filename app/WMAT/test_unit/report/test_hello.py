import unittest

class Hello(unittest.TestCase):

    def testHello(self):
        print("Good afternoon!")

    def testHand(self):
        print("Hand")

if __name__ == '__main__':
    Hello().testHello()

