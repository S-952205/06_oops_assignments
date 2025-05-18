# iss program main humnay default bank name diya start main jokay class variable hai
# phir class variable ko class method say update kiya or jitnay bhee object banein gay 
# unko class method kee wajha say new bank name dikhay ga means jo class method say change hua.
# yani sub objects pay effect hua.

class Bank:

    bank_name = 'State Bank'


    @classmethod   # class method say class attribute kee value change krdee
    def bank_name_change(cls, new_name):
        cls.bank_name = new_name


bank_1 = Bank()
bank_2 = Bank()
print(Bank.bank_name)

# class method call jo class variable change krday ga
Bank.bank_name_change('NBP Bank')


print(bank_1.bank_name)
print(bank_2.bank_name)