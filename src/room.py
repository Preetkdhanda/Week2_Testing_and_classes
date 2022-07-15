class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.guest = []
        self.song = []


    def get_room_name(self):
        return self.name 

    def get_room_capacity(self):
        return self.capacity

    def get_song_list(self):
        return self.song

    def add_song_to_song_list(self, song):
        self.song.append(song)
             
    def add_guest_to_room_with_capacity(self, guest):
        if self.capacity >= len(self.guest):
         self.guest.append(guest)

        else:
            return "Room is full"

    
            

        