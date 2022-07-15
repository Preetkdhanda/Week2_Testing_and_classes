import unittest

from src.guests import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):

        self.guest = Guest("Preet", 29)


    def test_guest_name(self):
        self.assertEqual("Preet", self.guest.name)
    
    def test_get_guest_age(self):
        self.assertEqual (29, self.guest.age)

    