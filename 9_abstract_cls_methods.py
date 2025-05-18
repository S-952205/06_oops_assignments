from abc import ABC, abstractmethod

class Shape(ABC):   # Abstract Class hai jo iss class ko inherit kray ga ussay lazmi area function use 
                    # krna hoga apni implementation dekr
    
    @abstractmethod
    def area(self) -> None:
        pass

class Rectangle(Shape):

    def __init__(self, width, height):

        self.width = width
        self.height = height


    # area function na use krtay tw error ata
    def area(self):   
        print(f'Area of rectangle is: {self.width * self.height}') # rectangle ka area calculate ka formula width * height


rect = Rectangle(4, 8)
rect.area()