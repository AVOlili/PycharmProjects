class Car():
    """一次模拟汽车"""
    def __init__(self, make, model, year):
         self.make = make
         self.model = model
         self.year = year
         self.odometer_reading = 0
        #汽车描述
    def get_descriptive_name(self):
        long_name = str(self.year)+" "+self.make+" " +self.model
        return long_name.title()
        #汽车里程表查看
    def read_odometer(self):
        print("这辆车已经行驶了"+ str(self.odometer_reading) + "公里 ")
        #更新里程表
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("你不能回滚里程表！")
        #增加里程
    def increment_odometer(self,miles):
        self.odometer_reading += miles


####电池类：
class Battery():
    """模拟电动汽车电瓶容量"""
    def __init__(self,battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        """打印出一条描述电瓶容量的消息"""
        print('这车的电池容量为' + str(self.battery_size) + 'kwh')

    def get_range(self):
        """打印一条描述电瓶续航里程的消息"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "这辆车充满电可以走"+str(range)+"公里"
        print(message)

###电瓶车：
class ElectricCar(Car):
    """
    电动汽车的独特之处
    初始化父类的属性，再初始化电动汽车特有的属性
    """
    def __init__(self, make, model, year):
        super().__init__( make, model, year)
        self.battery =  Battery()
