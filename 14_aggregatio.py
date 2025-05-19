# iss program main humnay aggregation implement kee hai aggregation means weak relation jb do objects ka relation
# tw hai apas main lekin esa nhi hai kay 1 object khtm hoga tw dusra bhee khtm hoga. employe instance ko 
# department main pass kiya.

# Employee Class (Independent Class)
class Employee:

    def __init__(self, name, id):
        self.name = name   # Employee name
        self.id = id       # Employee ID

    def show_info(self):
        print(f'Name: {self.name} - Id: {self.id}')   # Prints employee details


# Department Class (Using Aggregation)
class Department:

    def __init__(self, depname):
        self.depname = depname    # Department name
        self.employee = []        # Empty list to store employee objects (AGGREGATION STARTS HERE) ex: emp1, emp2 etc
        

    # emp main employe class ka reference mtlb instance store hai 
    def add_employe(self, emp): # Adding employee object to the list (AGGREGATION IMPLEMENTATION)
        self.employee.append(emp) # employe object store


    # printing depart name and calling employe method to show employe info.
    def show_employe(self):
        print(f'{self.depname}')
        for emp in self.employee:  # emp main emp1 ayga jismain show_info method hai or call hoga
            emp.show_info()  # employe method call kiya


# Creating Employee Objects (Independent Objects)
emp1 = Employee('Syed Sufyan', '123')
emp2 = Employee('Irva Shah', '456')



# Creating Department and Adding Employees
dep = Department('Finance')   # Create Finance department
dep.add_employe(emp1)         # Add first employee (AGGREGATION USAGE) 
dep.show_employe()            # Show department info and employees

# delete krdiya phir bhee emp1 or emp2 ko frk nhi pray ga qynke employe independent hai bhalay depart khtm hoo
# employe khtm nhi hoga weak relation hai dono eik dusray kay owner nhi hain na employe na department
del dep  # Proving Aggregation - Department deleted but employees still exist

print(emp1.name)


# Employees are created independently
# Department just references them
# Employees survive department deletion