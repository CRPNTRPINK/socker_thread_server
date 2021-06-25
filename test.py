class Person:
    def __init__(self, name, level, race):
        self.name = name
        self.level = level
        self.race = race

    def getName(self):
        return self.name


person = Person('Islam', 'Agiev', 'Human')
print(person.getName())