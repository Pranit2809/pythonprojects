class Person:
    def __init__(self,fn,ln,age):
        self.fn=fn
        self.ln=ln
        self.age=age
    def printname(self):
        print(self.fn+" "+self.ln)
        print(self.age)
p1=Person("Mark","Smith",35)
p1.printname()

class Student(Person):
   #pass
   def __init__(self,fn,ln,age):
      # Person.__init__(self,fn,ln,age)
        super().__init__(self,fn,ln,age)
s1=Student("Mikey","Smith",11)
s1.printname()
#create a class called vegetables where I mention the name the price and the days till expiry vegetables is a parent class
#do the same thing with a child class called fruits