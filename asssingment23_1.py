class bookstore():

    NoOfBooks=0

    def __init__(self,name,author):
        self.Name=name
        self.Author=author
        bookstore.NoOfBooks+=1

    def display(self):
        print(self.Name,"by",self.Author,"no of books:",bookstore.NoOfBooks)


obj1=bookstore("linux programing","robert love")
obj1.display()

obj2=bookstore("c programing","dennis ritchie")
obj2.display()