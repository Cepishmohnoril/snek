from car import Car

car_1 = Car("ЗАЗ", "Таврія", "1990", "Червоний")
car_2 = Car("ЗАЗ", "Славута", "2000", "Синій")

print(car_1.make, car_1.model, car_1.year, car_1.color)

car_1.drive()
car_1.stop()

print(car_2.make, car_2.model, car_2.year, car_2.color)

car_2.drive()
car_2.stop()