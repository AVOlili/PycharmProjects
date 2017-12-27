from Car import Car

#从Car.py导入Car类

my_new_car = Car("奥迪", "A4", 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()