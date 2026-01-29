class circle():
    pi=3.14

    def __init__(self):
        self.redius=0.0
        self.area=0.0
        self.circumference=0.0

    def accept(self):
        self.redius=float(input("enter redius:"))

    def calculculatearea(self):
        self.area=circle.pi *self.redius*self.redius

    def calculatecircumference(self):
        self.circumference=2*circle.pi*self.redius

    def display(self):
        print("redius:",self.redius) 
        print("area:",self.area)           
        print("circumference:",self.circumference)           

obj1=circle()
obj1.accept()
obj1.calculatecircumference()
obj1.calculculatearea()
obj1.display()