# Dependent Class
class Engine:

    def __init__(self, engine_type):
        self.engine_type = engine_type
    
    def start(self):
        return 'Engine Starting.....' 

class Car:
                                     # default value agr user na day tw V8 hogi value engine type kee    
    def __init__(self, name, color, engine_type = 'V8'):
        
        self.name = name
        self.color = color
        self.engine = Engine(engine_type)    # Composition engine object car object main created car destroy tw engine bhee destroy

    def show_detail(self):
        print(f'Car: {self.name} - {self.engine.engine_type} {self.engine.start()}') # Composition car calling engine class method


my_car = Car('Mustang', 'Red', 'V8') # Car created real car actual object 
my_car.show_detail()

# del krrahay my_car object engine bhee destroy hojaiga (Proves Composition)
del my_car

# tried to access engine method failed. proves composition
my_car.engine.start()
