import unittest

from src.song import *

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("It's not right but its okay", "Whitney Houston")


    def test_getting_song_name(self):
     return self.assertEqual("It's not right but its okay", self.song.name)

    def test_getting_song_artist(self):
        return self.assertEqual("Whitney Houston", self.song.artist)