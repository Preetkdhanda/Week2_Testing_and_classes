import unittest

from src.guests import Guest
from src.room   import Room

class TestGuest(unittest.TestCase):
    def setUp(self):

        self.guest = Guest("Preet", 29, 100.00)
        self.room = Room("RnB", 3, 5.00, 0)


    def test_guest_name(self):
        self.assertEqual("Preet", self.guest.name)
    
    def test_get_guest_age(self):
        self.assertEqual (29, self.guest.age)

    def test_get_wallet_total(self):
        self.assertEqual(100.00, self.guest.wallet)

    def test_pay_fee(self):
        self.guest.pay_fee(self.room.fee)
        self.assertEqual(95.00, self.guest.wallet)