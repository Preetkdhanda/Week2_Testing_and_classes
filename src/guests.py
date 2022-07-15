class Guest:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def get_guest_name(self):
        return self.name
        
    def get_guest_age(self):
        return self.age