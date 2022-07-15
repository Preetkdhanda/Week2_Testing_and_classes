class Guest:
    def __init__(self, name, age, wallet):
        self.name = name
        self.age  = age
        self.wallet = wallet

    def get_guest_name(self):
        return self.name
        
    def get_guest_age(self):
        return self.age

    def get_guest_money(self):
        return self.wallet

    def pay_fee(self, fee):
        self.wallet -= fee

