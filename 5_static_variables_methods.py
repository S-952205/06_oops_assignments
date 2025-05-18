# Ek MathUtils class banani hai jisme ek static method add(a, b) ho jo do numbers ka sum 
# return kare. Koi class ya instance variables use nahi karni.

class MathUtils:
    
    @staticmethod
    def add(a, b):
        return a + b
    

result = MathUtils.add(5, 2)
print("Sum:", result)  