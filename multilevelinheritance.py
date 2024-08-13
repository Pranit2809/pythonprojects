class Vehicle:
    def __init__ (self,brand,type):
        self.brand=brand
        self.type=type
    def showinfo(self):
        return f"brand:{self.brand},type:{self.type}"
class Car(Vehicle):
    def __init__ (self,brand,type,fueltype):
        super().__init__(brand,type)
        self.fueltype=fueltype
    def showcarinfo(self):
        return f"{self.showinfo()},fuel type:{self.fueltype}"
class ElectricCar(Car):
    def __init__ (self,brand,type,batterycapacity,model):
        super().__init__(brand,type,"Electric")
        self.batterycapacity=batterycapacity
        self.model=model
    def showelectriccarinfo(self):
        return f"{self.showcarinfo()},battery capacity:{self.batterycapacity},model:{self.model}"
e1=ElectricCar("Tesla","Car",100,"X")  
print(e1.showelectriccarinfo())     