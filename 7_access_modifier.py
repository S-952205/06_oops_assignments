# iss porgram main humnay employe class banai jismain attributes initialize krnay with different access modifiers
# or unko class say bahr eik eik krkay access krna hai.

class Employe:

    def __init__(self, name, salary, ssn):

        self.name = name       # Public Accessor
        self._salary = salary  # Protected Accessor
        self.__ssn = ssn       # Private Accessor



emp = Employe('Syed', 24000, '01-21')

# 1. Access Public (Allowed)
print("Public (name):", emp.name)        #  Works

# 2. Access Protected (Allowed but discouraged)
print("Protected (_salary):", emp._salary)  #  Works (but avoid)

# 3. Access Private (Error)
print("Private (__ssn):", emp.__ssn)     # Fails (AttributeError)


