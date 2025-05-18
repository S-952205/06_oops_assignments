# Student class banani hai jis mein "name" aur "marks" attributes hon. Constructor (init) ke through 
# in values ko initialize karna hai "self" keyword use karte hue. Phir display() method banana hai
# jo student ki details print kare.

class Student:

    def __init__(self, name, marks):
        
        self.name = name
        self.marks = marks

    def display(self):
        
        print("Name:", self.name)
        print("Marks:", self.marks)


stud_1 = Student('Syed', 98)
stud_1.display()