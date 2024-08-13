#Multiple inheritance
"""
class Parentclass1:
    
class Parentclass2:
    
class Childclass(Parentclass1,Parentclass2)"""

class Pet:
    def speak(self):
        return "Animal speaks"
class Animal:
    def owner(self):
        return "Pranit is the owner"
class Dog(Pet,Animal):
    def bark(self):
        return "Dog barks"
hero=Dog()
print(hero.speak())
print(hero.owner())
print(hero.bark())

#multi level inheritance
"""
class Grandparent:
    
class Parent(Grandparent):
    
class Child(Parent)"""

class Animal:
    def owner(self):
        return "Pranit is the owner"
class Mammal(Animal):
    def youngones(self):
        return "Mammals produce young ones"
class Cat(Mammal):
    def speak(self):
        return "Cat says meow"
kitty=Cat()
print(kitty.owner())
print(kitty.youngones())
print(kitty.speak())

class Average:
    def calcaverage(self,num):
        num=0
        for i in range (5):
            num1=int(input("Input a number: "))
            num=num+num1
        num=num/5
        return num
class Simple_Interest:
    def calcsi(self,P,R,T):
     
        return (P*R*T)/100
class AverageSI(Average, Simple_Interest):
    def asi(self,num,P,R,T):
        print(self.calcaverage(num))
        print(self.calcsi(P,R,T))
num=[5,6,7,8,9]
P=int(input("Input the starting amount: "))
R=int(input("The Rate of interest in percentage: "))
T=int(input("The Amount of years of interest: "))
a=AverageSI()
a.asi(num,P,R,T)


