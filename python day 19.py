#inheritance
class User:#parent class
    def __init__(self,email,username):
        self.email=email
        self.username=username
    def login(self):
        print(f'{self.username} has logged in')
class Customer(User):#single inheritance 
    def __init__(self, email, username,loyalty_points=0):
        super().__init__(email ,username)#we can call a constructor explicitly by super() only
        self.loyalty_points=loyalty_points
    def place_order(self,item):
        print(f'{self.username} has ordered {item}.')
    def display(self):
        print(f'from Customer class')
customer1=Customer("abc@gmail.com","Alice")
customer1.login()
customer1.place_order("laptop")
class Subscriber:#parent class
    def __init__(self):
        self.subscribtion_status="Active"
        self.discount_rate=0.2
    def apply_premimum_discount(self,price):
        final_price=price*(1-self.discount_rate)
        print(f'Subscriber discount applied ! New Price:{final_price}')
    def display(self):
        print(f'{self.subscribtion_status} from Subscriber class')
class Procustomer(Customer,Subscriber):#multiple inheritance
    def __init__(self,username,email,loyalty_points=0):
        Customer.__init__(self,username,email,loyalty_points=0)
        Subscriber.__init__(self)
    def show_dashboard(self):
        print(f'Welcome Back {self.username}!Status:{self.subscribtion_status}')
vip1= Procustomer("abcgmail","Alice")
vip1.login()
vip1.place_order("laptop")
vip1.apply_premimum_discount(4000)
vip1.show_dashboard()
vip1.display()


#dimond shape problem of multiple inheritance  class method resolution order
class A:
    def greet(self):
        print("Hello from A")
class B(A):
    def greet(self):
        print("Hello from B")
class C(A):
    def greet(self):
        print("Hello from C")
class D(B,C):
    pass
obj1=D()
obj1.greet()
super(D,obj1).greet()#sees B #[D,B,C,A]
super(B,obj1).greet()#sees C
super(C,obj1).greet()#sees A
obje=B()
obje.greet()


class A:
    def greet(self):
        print("Hello from A")
class B(A):
    def greet(self):
        print("Hello from B")
class C(A):
    def greet(self):
        print("Hello from C")
class D(C,B):
    pass
obj2=D()
obj2.greet()


class A:
    def greet(self):
        print("Hello from A")
class B(A):
    def greet(self):
        print("Hello from B")
class C(A):
    pass
class D(C,B):
    pass
obj3=D()
obj3.greet()


class A:
    def greet(self):
        print("Hello from A")
class B(A):
    pass
class C(A):
    pass
class D(C,B):
    pass
obj4=D()
obj4.greet()


class A:
    def greet(self):
        print("Hello from A")
class B(A):
    def greet(self):
        print("Hello from B")
class C(A):
    def greet(self):
        print("Hello from C")
class D(B,C):
    pass



obj5=D()
A.greet(obj5)#class name with function name



#data abstraction
class Emp:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    def display(self):
        print("salary=",self.__salary)
emp1=Emp("BOB",500000)
print (emp1.name)
#print(emp1.__salary) do not show salary
print (emp1.display())



