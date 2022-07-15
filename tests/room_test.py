import unittest

from src.room import *
from src.song import *
from src.guests import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("RnB", 3, 5.00, 0)
        self.guest= Guest("Preet", 29, 100.00)
        self.guest1= Guest("Joe", 30, 20.00)
        self.guest2= Guest("Avin", 1, 50.00)
        self.guest3= Guest("Aman", 2, 70.00)
        self.song = Song("It's not right but its okay", "Whitney Houston")

    def test_room_name(self):
        self.assertEqual("RnB", self.room.name)

    def test_room_capacity(self):
        self.assertEqual(3,3)

    def test_song_list(self):
        self.assertEqual([], self.room.song)

    def test_adding_song_to_songlist(self):
        self.room.add_song_to_song_list(self.song)

        self.assertEqual(1, len(self.room.song))

    def test_adding_guest_to_room(self):
        self.room.add_guest_to_room_with_capacity(self.guest)
        self.assertEqual(1, len(self.room.guest))
        self.assertLessEqual(len(self.room.guest), self.room.capacity)
        

    def test_checking_if_room_doesnt_go_over_capacity(self):
        self.room.add_guest_to_room_with_capacity(self.guest)
        self.room.add_guest_to_room_with_capacity(self.guest1)
        self.room.add_guest_to_room_with_capacity(self.guest2)
        self.room.add_guest_to_room_with_capacity(self.guest3)
        self.assertEqual(3,len(self.room.guest))

    def test_checking_if_room_can_take_capacity(self):
        self.room.add_guest_to_room_with_capacity(self.guest)
        self.room.add_guest_to_room_with_capacity(self.guest1)
        self.room.add_guest_to_room_with_capacity(self.guest2)
        self.assertEqual(3, len(self.room.guest))

    def test_checking_if_fee_paid_is_added_to_till(self):
        self.room.check_if_guest_can_afford_fee(self.guest, 5)
        self.assertEqual(5.00, self.room.till)
        self.assertEqual(95.00, self.guest.wallet)