# Ek Counter class banani hai jo track rakhe ke kitnay objects ban chuke hain. Is ke
# liye class variable aur cls wala class method istemal karna hai.


class Counter:

    count = 0     # class variable

    # constructor
    def __init__(self):
        Counter.count +=1  # hr baar object banany pay class variable count 1 say brhaya jata hai


    # class method issay hum class attributes ko access or modify krsktay
    @classmethod
    def show_count(cls):
        print(f'Total Objects: {cls.count}')


count1  = Counter() # 1st object created
count2  = Counter()
count3  = Counter()
Counter.show_count()


