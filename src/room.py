from email import feedparser


class Room:
    def __init__(self, name, capacity, fee, till    ):
        self.name = name
        self.capacity = capacity
        self.fee = fee
        self.till = till
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
        if self.capacity > len(self.guest):
         self.guest.append(guest)
       
    def check_if_guest_can_afford_fee(self, guest, fee):
        if guest.wallet < fee :
            return
        else:
             guest.wallet -= fee
             self.till += fee


    
    
        

        ## this would have worked as the testing length against
        # capacity 
        #    def add_guest_to_room_with_capacity(self, guest):
        # if self.capacity <= len(self.guest):
        #     return "Room is full"
        # else:
        #     self.guest.append(guest)
        #     return f"Room count is now {len(self.guest)}"