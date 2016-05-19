# create a pirate class
# it should have 2 methods
# drink_rum()
# hows_goin_mate()
# if the drink_rum was called at least 5 times:
# hows_goin_mate should return "Arrrr!"
# "Nothin'" otherwise

class Pirate():
    def __init__(self):
        self.i = 0

    def drink_rum(self):
        self.i += 1
        if self.i >=5:
            return self.hows_goin_mate()
        else:
            return "Nothin'"

    def hows_goin_mate(self):
        return "Arrrr!"

captain = Pirate()
print(captain.drink_rum())
print(captain.drink_rum())
print(captain.drink_rum())
print(captain.drink_rum())
print(captain.drink_rum())
print(captain.drink_rum())
