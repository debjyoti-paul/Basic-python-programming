#ls1=[1,2,3,4]
#print(ls1.append(5))
#print(ls1.pop)
#ls2=[6,7,8,9]

#ls3=ls1+ls2
#print(ls3)
#print(ls1)
#print(ls2)
#ls1.extend(ls2)
#print(ls1)
#print(ls2)##

#students=[('a', 90),('b', 40),('c',75)]
#students.sort(key=lambda x:x[1])
#print(students)

#object qriented paradime, stack and queue implamentation along with object and classes
#what is class and object?  what is instance?
#what is object oriented paradime?#what is constructer?parameterise constucter? nonparameterise constructer?
#diffenent between class variable and constructer variable?
#what is class method?




class BankAccount:

   def __init__(self):
        self.name=input('enter the name of the account:')#why self is used? b1=self, then b2=self
        self.Balance=int(input('enter the balance:'))#name and balance are constructer variable(nonparameter)
#n and b are constructer variable(nonparameter)
b1=BankAccount()    #b1 is the object
print(b1.name)
print (b1.Balance)
b2=BankAccount()    #b2 is the object
print(b2.name)
print (b2.Balance)

class BankAccount:
    interest_rate=.05
    def __init__(self,n,b):
        self.name=n
        self.balance=b
    def deposite(self, amount):
        if amount>0:
            self.balance+=amount
            return self.balance
        return "invalid deposite amount"    
    def withdrawl(self ,amount):
        if 0<amount<=self.balance:
            self.balance-=amount
            return self.balance
        return "invalid withdrawl amount"
    def apply_interset(self):
        interest_amt=self.balance*BankAccount.interest_rate
        self.balance+=interest_amt
        return self.balance
n=input('enter  name :')
b=int(input('enter balance:'))
b1=BankAccount(n,b)
print(b1.name)
print(b1.balance)
b1.deposite(1000)
print('balance of b1  '+str(b1.balance))
#print('balance of b3'+b3.balance)  will not work why?
#what is actual parameter , formal parameter?
n=input('enter name:')#ei ta o porer line ta na likhle ager input niye eeeii kaj hobee
b=int(input('enter balance:'))
b2=BankAccount(n,b)
print(b2.name)
print(b2.balance)
b2.withdrawl(500)
print('balance of b2 '+str(b2.balance))
print(b2.apply_interset())
#print('balance of b4'+b4.balance)  will not work why?
#er  pore interest er sathe balance dekhabo ki kore??????????????????


#data hiding and encapsulation?



class BankAccount2:
    interest_rate=.05
    def __init__(self,n,b):
        self.name=n
        self.__balance=b#__balance lekha holo jate keu value ta ke interpret korte na pare
    def view_balance(self) :
        #print(self.__balance) #either
        return self.__balance  #-----> eta likhle output ee'none' asbe na
       #   noile outpute 'none' asche as eta  kichuii return korche na
b3=BankAccount2("atin ", 4000)
print(b3.name)
print(b3.view_balance())

#stack using python
#what is stack??????????????stack can be implemented by list or numpyarray
#what is queue????????????? insertion end ee hoy , delete hoy prothom theke
#object oriented paradime
class stack:
    def __init__(self):
        self.items=[]#name of the list is append
    def push(self,val):
        self.items.append(val)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items==[]#return true if list is empty
    def size(self):
        return len(self.items)    
#what is function oriented paradime?
#input a list , pop some element , enter some element , get the length of the list, check weather it is empty or not?
#implement queue using class and list?
class queue:#made queue
    def __init__(self):
        self.items=[]
    def insert(self, val):    
        self.items.append(val)
    def delete(self):
        self.items2=self.items[::-1]
        self.item3=self.items2.pop()
        self.items=self.item3
        return self.items

#kaj korche kina bujhte parchi na as input nite parchi na


