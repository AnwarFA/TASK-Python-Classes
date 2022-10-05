class Wallet:
    def __init__(self, money):
        self.money = money

    def credit(amount):
        self.money += amount
        print(f"credit: the new amount value for money is {self.money}")

    def debit(amount):
        self.money -= amount
        print(f"dedit: the new amount value for money is {self.money}")

wallet = Wallet(6)
#wallet = wallet()


class Person:
    # Implement the code here
    def __init__(self, name, location, money):
        self.name = name
        self.location = location
        self.wallet = wallet(money)
        
    def movTo(self, point):
        self.location = point
print(f"The new location for the {self.name} is {self.location}")

class Vendor(person):
    # implement Vendor!
    def __init__(self, name, location, money):
        super().__init__(name, location, money)
        self.range = 5
        self.price = 2

    def sellTo(self, customer, number_of_icecreams):
        self.location = customer.location
        self.wallet.credit(number_of_icecreams * self.price)
        customer.wallet.debit(number_of_icecreams * self.price)

vendor = Vendor("Abdallah", 3, 6)


class Customer(person):
    # implement Customer!
    def __init__(self, name, location, money):
        super().__init__(name, location, money)
    
    def _is_in_range(self, vender):
        distance = abs(self.location - vender.location)
        if distance <= vender.range:
            return True
        else:
            return False 
    
    def _have_enough_money(self, vender, number_of_icecreams):
        if self.wallet.money >= vendor.price * number_of_icecreams:
            return True
        else:
            return False

    def request_icecream(self, vender, number_of_icecreams):
        if self._is_in_range(vendor) and self._have_enough_money(vendor, number_of_icecreams):
            vendor.sellTo(self, number_of_icecreams)


customer = Customer("Abdallah", 3, 6)
vendor_aziz = Vendor("Asis", 10, 10) 
nearby_customer = Customer("MishMish", 11, 10)
distant_customer = Customer("Hamsa", 1000, 1000) 
broke_customer = Customer("Maskeen", 12, 0)
nearby_customer.request_icecream(vendor_aziz, 10)

print(nearby_customer.wallet.money)
print(vendor_aziz.wallet.money)
print(vendor_aziz.location)

distant_customer.request_icecream(vendor_aziz, 10)
print(distant_customer.wallet.money)
print(vendor_aziz.wallet.money)
print(vendor_aziz.location)

broke_customer.request_icecream(vendor_aziz, 1)
print(broke_customer.wallet.money)
print(vendor_aziz.wallet.money)
print(vendor_aziz.location)