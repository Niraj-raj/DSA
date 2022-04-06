class library:
    def __init__(self,listofbooks):
        self.books=listofbooks
    def displayabilablebooks(self):
        print("Books present in this library are:  ")
        for book in self.books:
            print("    *" +book)

    def borrowbooks(self,bookname):
        if bookname in self.books:
            print(f"You have been issued {bookname}.Please keep it safe and return within 30 days, Thanks....")
            self.books.remove(bookname)
            return True #for return successful 
        else:
            print("Sorry this book already been issued someonr else .please try again ")
            return False #not successfully    

    def returnbooks(self,bookname):
        self.books.append(bookname)
        print("Thenks.. for returning it hope you enjoy have a graet day ahead")            

class Students:
    def requestbook(self):
        self.book=input("Enter the book name which you want to borrow: ")
        return self.book

    def returnbook(self):
        self.book=input("Enter the book name which you want to return: ")
        return self.book    

if __name__=="__main__":
    centallibary=library(['Algorithm','CDS','Compiler'])
    Student=Students()
    #centallibary.displayabilablebooks()
    while(True):
        welcomemsg='''
        ====Welcome to centrel library====
        1.List of all Books
        2.Request a book
        3.Return/Add a book
        4.Exit the central library'''
        print(welcomemsg)
        a=int(input("enter the above options: "))
        if a==1:
            centallibary.displayabilablebooks()
        elif a==2:
            centallibary.borrowbooks(Student.requestbook())
        elif a==3:
            centallibary.returnbooks(Student.returnbook())
        elif a==4:
            print("thanks for chosing central library.Have a great day ahead! ")
            exit()
        else:
            print("invilad choise..")                

