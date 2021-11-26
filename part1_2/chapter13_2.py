#BT 4

class Horse:
    def __init__(self,name, rank, ridder):
        self.name = name
        self.rank = rank
        self.ridder = ridder

class Person:
    def __init__(self, name):
        self.name = name


person = Person("Sussan")

horse = Horse("Tom", "A", person)

print(horse.ridder.name)
