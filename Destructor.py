'''Destructor :- It will remove the object from the memory /delete an object
destructor is given by __del__() - dunder method. If not given is called automatically when object is not in use
'''

class x:
    def __init__(self,n): #Cunstructor
        self.n = n
        print(f"{self.n}Object created ")
    def __del__(self):  #Destructor
        print(f"{self.n}Object deleted")
a = x("new 1")
b = x("new 2")
del a


#####################################################
class myname:
    def __init__(self,name):
        self.name = name
        print(f'{self.name} occupies space in memory')
    def __del__(self):
        print(f'{self.name} remove from memory')
#constructor is being called..
obj1 = myname("Dk")
obj2 = myname("Ajeet")

#destructor is called
del obj1
del obj2

##############################################################
#Create class employee ,accept gross salary, display net salary after deduting tax.
#tax will be 20% for salary above 1000000 and 10% fro <1000000>

class employee:
    def __init__(self):
        self.name = ''
        self.gross = 0
        self.net = 0
    def accept(self):
        self.name = input("Enter your name :")
        self.gross = float(input("Enter your gross salary :"))
    def calc_tax(self):
        tax = 0
        if self.gross>= 100000:
            tax = self.gross * 20/100
            self.net = self.gross - tax
        else:
            tax = self.gross * 10/100
            self.net = self.gross - tax
        return tax
    def display(self):
        print(f'Hello {self.name}, {self.calc_tax()} will be deducted from your gross salary, nt salary will be  {self.net:.2f}')

e1 = employee()
e1.accept()
e1.display()

    

    







