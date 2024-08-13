class Book:
    def __init__(self,bookname,author,publicationyear,num_pages):
        self.bookname=bookname
        self.author=author
        self.publicationyear=publicationyear
        self.num_pages=num_pages
    def reading(self):
        print("Books are great for the mind!")
        print("Book Name: "+self.bookname)
        print("Author: "+self.author)
        print("Publication year: "+str(self.publicationyear))
        print("Number of Pages: "+str(self.num_pages))

#calling object    
book1=Book("Harry Potter and the Philosophers Stone","J.K.Rowling",1998,223)
book1.reading()
book2=Book("Diary of a Wimpy Kid","Jeff Kinney",2007,225)
book2.reading()

#HOMEWORK: create a class caled report card where she mentions the name of the kid his math mark his language mark and if he passed or failed