#function and recurssion
def greet():    #defining function
    print("Hello World")

greet()#calling function    

def greet(t):    #defining function
    print("Hello " +t)
name=input("enter the name:")
greet(name)#calling function    

def add(a,b):
    return a+b
def multiply(a,b):
    return a*b
def substract(a,b):
    return a-b
def division(a,b):
    return a/b
def modulas(a,b):
    return a%b
def operate( func,x,y):
    return(func(x,y))

print(operate(add,4,5))
print(operate(multiply,4,5))
print(operate(substract,4,5))
print(operate(division,4,5))
print(operate(modulas,4,5))

def calculation(a,b):
    return a+b ,a-b , a*b ,a/b ,a%b
v,w,x,y,z=calculation(67,3)
print(v,w,x,y,z)


def calculation(a,b=6):
    return a+b ,a-b , a*b ,a/b ,a%b
v,w,x,y,z=calculation(3)
print(v,w,x,y,z)

def calculation(a,b=6):
    return a+b ,a-b , a*b ,a/b ,a%b
v,w,x,y,z=calculation(b=3,a=2)
print(v,w,x,y,z)

#function inside a function
def outerfunc(v1):
    def innerfunc():
        return "hello"
    s1=innerfunc()+v1
    print(s1)
outerfunc('students')

def add(*n):
    sum=0
    for i in n:
        sum+=i
    print(sum)    
    
add(2,3)
add(2,3,4,5,6,7,8,9,10,11)
#what is the data type of n?'*'  means is a tuple type of data
#'**' means dict type of data

def students(**details):
    for k,v in details.items():
        print(k,':',v)
students(name="students",roll="743", subject="data science")

#lamda function
# in python a lamda func is an anonimous func def using the keyword lamda, it can take any no. of arguments but contains only one expression whose result is return autometically

square=lambda x:x*x #first 'x' is return , after : the details of the function
print(square(5))

add=lambda x,y:x+y
print(add(2,3))#canot write multiple work

max=lambda x,y:x if x>y else y
print(max(6,8))

max=lambda x,y:x if x>y else y
a=int(input("enter a no:"))
print(max(a,8))

def operate(x):
    return lambda y:x+y
f=operate(10)
print(f(5))

#map function using lambda
l1=[20,30,40,50]
result=list(map(lambda x:x*2,l1))
print(result)

l1=[20,30,40,50]
result=map(lambda x:x*2,l1)
print(result)#lazy evalution

l1=[20,30,40,50]
result=map(lambda x:x*2,l1)
r=list(result)
print(r)#      <--|
#                 |       
#internal method --
#for x in l1:
    #yeild lambda(x)


l1=[20,30,40,50]
result=map(lambda x:x*2,l1)
print(next(result))#calculation is only done for first element
print(next(result))
print(next(result))
print(next(result))

l1=[20,30,40,50]
l2=[x*2 for x in l1]#eager evalution
print(l2)
#both are not  same(oporerta and nicherta)
l1=[20,30,40,50]
result=list(map(lambda x:x*2,l1))
print(result)

#filtering operation
l1=[20,37,35,50]
l3=list(filter(lambda x:x%2==0,l1))
print(l3)

#difference between eger evalution and lazy evalution?

student=[('a',90),('b',40),('c',75)]
student.sort(key=lambda x:x[1])
print(student)#printing in sorted ordered

