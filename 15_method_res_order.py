
class A:

    def show(self):
        print('Method A')

class B(A): 

    def show(self):
        print('Method B')

class C(A):

    def show(self):
        print('Method C')

class D(B, C):
    pass

d_obj = D()
d_obj.show()   # Method B milay ga righ-to-left check hoti classes check 

print(D.mro()) # iska output [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# mro - method resolution order jb child class kay multiple parents houn or jesay upper D kay 2 or un main 
# same name methods houn tw how we know kay konsa method chalay ga iskayliye python eik order follow krta hai
# called mro decide karta hai ke kaun sa method actually call hoga yani kay python sb classes main eik order say
# dhundta hai kay woo methid kahan hai jo call hua in mro order.