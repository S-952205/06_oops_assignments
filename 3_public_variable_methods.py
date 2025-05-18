# iss program main humnay Car class banani or public variable brand or public method start() banakr
# class say bahr access krnay.


class Car:

    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f'{self.brand} car Started.....')



car_1 = Car('Ferrari')
print(car_1.brand)
car_1.start()