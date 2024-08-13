class Marks:
    def __init__ (self, name, rollnumber):
        self.name=name
        self.rollnumber=rollnumber
        self.marks=[]
        self.grade=""
        self.total=0
        self.percent=0
    def info(self):
        print("Student Name: "+self.name)
        print("Stduent Roll Number: "+str(self.rollnumber))
    def mark(self):
        print("Enter the marks of all 5 subjects")
        for i in range(5):
            self.marks.append(int(input("subject "+str(i+1)+":")))
    def calculate_percentage(self):
        for x in self.marks:
            self.total+=x
        self.percent=self.total/5
    def calculategrade(self):
        if self.percent>=90:
            self.grade="A"
            print(self.grade)
        elif self.percent>=80:
            self.grade="B"
            print(self.grade)
        elif self.percent>=70:
            self.grade="C"
            print(self.grade)
        elif self.percent>=60:
            self.grade="D"
            print(self.grade)
        else:
            self.grade="F"
            print(self.grade)

student1=Marks("Mike",42)
student1.info()
student1.mark()
student1.calculate_percentage()
student1.calculategrade()

#HOMEWORK FOR TUESDAY
#factorial of 5 is 5*4*3*2*1
#write a program to calculate factorials

