class Home:
    def __init__(self, name, age, weight, height=16):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    # def grow(self, height=1):
    #     self.height += height

Eva = Home("Eva", 5, 18, 180)
# Eva.grow(height=18)
print(Eva.name)
print(Eva.height)
print(Eva.age)
print(Eva.weight)

Tigger = Home("Tigger", 8, 12, 19)
print(Tigger.name)
print(Tigger.height)
print(Tigger.age)
print(Tigger.weight)


Max = Home("Max", 3, 19, 18)
print(Max.name)
print(Max.height)
print(Max.age)
print(Max.weight)














    # def __init__(self):
    #     self.name1 = "Tigger"
    #     self.age1 = 3
    #     self.weight1 = 16
    #
    # def __init__(self):
    #     self.name2 = "Max"
    #     self.age2 = 2
    #     self.weight2 = 18
#
# nick = Home()
# print(nick.name, nick.age, nick.weight, nick.name1, nick.age1, nick.weight1, nick.name2, nick.age2, nick.weight2)