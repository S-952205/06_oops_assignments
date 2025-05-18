# humnay dog class banai or constructor say instance attribute initialize kiye or instance method banaya jo
# dog ka name or message print kray ga


class Dog:

    def __init__(self, name, breed):
        self.name = name    # instance attribute
        self.breed = breed  # instance attribute

    
    # instance method
    def bark(self):
        print(f"{self.name} (a {self.breed}) says: Woof Woof!")


dog = Dog('Max', 'Siberian Huskey')
dog.bark()