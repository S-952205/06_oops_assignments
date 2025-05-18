# iss program main humnay Person class banai jismain constructor banakr name kee property set kee
# then humnay teacher class banai jismain super function ka use krkay humnay base class Person kay constructor
# ko call kiya or name bheja plus teacher class nay eik apni property subject bhee jo khud set kee.


# Base Class
class Person:

    def __init__(self, name):
        self.name = name


# Child Class
class Teacher(Person):

    def __init__(self, name, subject):

        # base class constructor called.
        super().__init__(name) # super() say hum base class kay constructor ko call krtay hain
        self.subject = subject # yeh subject teacher class kee apni hai.


p1 = Person('Ali')
print(p1.name)

t1 = Teacher('Zara', 'Math')
print(t1.name, t1.subject)

