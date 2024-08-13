class Testclass:
    x=2
t1=Testclass()
print(t1)

class Bike:
    def __init__ (self,speed,model,size,comfort):
        self.speed=speed
        self.model=model
        self.size=size
        self.comfort=comfort
    def Display(self):
        print("Bikes rating:")
        print("Maximum Speed in kmph: "+str(self.speed))
        print("Model: "+self.model)
        print("Size: "+str(self.size))
        print("Comfort out of 10: "+str(self.comfort))
    
Bike1=Bike(32,"Extra Comfort",28,9)
Bike1.Display()
Bike2=Bike(54,"Very Fast", 24, 3)
Bike2.Display()
#Write a program to calculate the annual salary and raises of the employees

class Employee:
    raise_amount=1.02
    def __init__ (self,fn,ln,salary):
        self.fn=fn
        self.ln=ln
        self.salary=salary
    def fullname(self):
        return f"{self.fn}{self.ln}"
    def Salary(self):
        self.salary=int(self.salary*12*self.raise_amount)
    
employee1=Employee("Joe ","Carpenter",4500)
print(employee1.fullname())
employee1.Salary()
print(employee1.salary)
employee2=Employee("Mark ","Colt",10000)
print(employee2.fullname())
employee2.Salary()
print(employee2.salary)
#write a program to find out the details of the pacient with their name height and weight, Use the height and weight to calculate BMI, Display if heart rate is too high or too low