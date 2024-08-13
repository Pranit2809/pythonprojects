class Vegetable:
    def __init__(self,name,price,expiry):
        self.name=name
        self.price=price
        self.expiry=expiry
    def printname(self):
        print(self.name)
        print("Cost of "+self.name+":"+" $"+str(self.price))
        print("Days Until Expiry: "+str(self.expiry)+" days")
v1=Vegetable("Carrots",2,8)
v1.printname()
v2=Vegetable("Potato",1,12)
v2.printname()

class Fruit(Vegetable):
   pass

f1=Fruit("Watermelon",4,4)
f1.printname()
#create a class called vegetables where I mention the name the price and the days till expiry vegetables is a parent class
#do the same thing with a child class called fruits