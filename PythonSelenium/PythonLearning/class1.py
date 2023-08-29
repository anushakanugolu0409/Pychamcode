class rateofinterest:
    interest = 0.8

    def __init__(self,name,loan):
        self.name = name
        self.loan = loan

    def cal_inter(self):
        print("the rate of inteerest for  {}".format(self.name), self.loan*self.interest)

class student(rateofinterest):
    interest=0.04
    pass

c = student("mohan",50000)
c.cal_inter() # cal roi with the interest specified in child class
s= rateofinterest("mohan",50000)
s.cal_inter() # cal roi with the interest specified in parent class

class parent():
    print("parent class")

class child():
    print("child class")

class grandchild(parent, child): # multiple inherit propertities var n mthd frm parent class
    print("grandchild")
g = grandchild()

def func1():
    print("learnign od modules , import func")
