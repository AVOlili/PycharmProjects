from Car import ElectricCar
mycar = ElectricCar('特斯拉','model s',2016)
print(mycar.get_descriptive_name())
mycar.battery.describe_battery()
mycar.battery.get_range()