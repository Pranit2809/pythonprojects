class ReportCard:
    def __init__(self,name,math,lang,pof):
        self.name=name
        self.math=math
        self.lang=lang
        self.pof=pof
    def report(self):
        print("This is your report card")
        print("Student Name: "+self.name)
        print("Your Mathematics mark: "+str(self.math))
        print("Your language mark: "+str(self.lang))
        print("Final Mark: "+self.pof)

#calling object    
reportcard1=ReportCard("Jimmy",68,31,"FAIL!!!")
reportcard1.report()
reportcard2=ReportCard("Billy",82,78,"Pass")
reportcard2.report()