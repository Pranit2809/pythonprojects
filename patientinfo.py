import math
class Patient:
    def __init__ (self,fn,ln,weight,height,bmi):
        self.fn=fn
        self.ln=ln
        self.height=height
        self.weight=weight
        self.bmi=bmi
    def fullname(self):
        return f"{self.fn}{self.ln}"
    def bmic(self):
        self.height=self.height**2
        self.bmi=int(self.weight/self.height*10000)
    
patient1=Patient("Joe ","Carpenter",45,133,0)
print(patient1.fullname())
patient1.bmic()
print(patient1.bmi)
patient2=Patient("Mark ","Colt",65,182,0)
print(patient2.fullname())
patient2.bmic()
print(patient2.bmi)
#write a program to find out the details of the pacient with their name height and weight, Use the height and weight to calculate BMI AND DISPLAY IF THEY ARE OVERWEIGHT HEALTHY UNDERWEIGHT OR OBESE