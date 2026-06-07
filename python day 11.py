#take any integer . like 28 , 
# where the output is key=prime factor and values are the frequency of the prime factor {(2:2) ,(7:1)}
#prime factorisation dictionary key-factors, value-number of times repeated
#import math
#def isPrime(num):
#    flag=True
#    for i in range(2,int((math.sqrt(num))+1)):
#        if num==2:
#            flag=True
#            break
#        if num%i==0:
#            flag=False
#            break
#    return flag
    
#def prime_factors(num):
#    factor=[]
#    count_prime=[]
#    for i in range(2,num+1):
#        if(num%i==0):
#            factor.append(i)
#    prime_factor=list(filter(lambda x: isPrime(x),factor))#filter only take boolean value so we used flag=true or false

#    for i in range(len(prime_factor)):
#        count=0
#        while(num%prime_factor[i]==0):
#           count+=1
#            num=num/prime_factor[i]
#        count_prime.append(count)
#    print(dict(zip(prime_factor,count_prime)))
#num=int(input("enter a number: "))
#prime_factors(num)


#scope and namespace of variable:?in python?what is name space?
#what is scope?relation between scope and name space and dictionary?
#the scope refers to the region in the program code where the variables and names are accesable.It also determines the visibality and life time 
#of a variable in the program code.Assigning a value , defining a function or class, or importing module , these operation creats a name
#and it's place  in the code define its scope.
#the  names or object which are accseable are called inscope , which are not are called out of scope.
#in python we have  a concept of LEGB(local , enclosed , global , built_in)
#the scope helps to avoid the variable naming collision and use of global names across the programs.
#Scopes are implemented as dict.which maps name to object 
#this dict. are called name spaces.
#the  dict. has names as key and object as value.....
var1=5#integer type of object not integer ,the important thing is object.

def ABC():
    var2=10
    print(var2)
    print(var1)
print(var1)#global variable=var1
#print(var2) we cannot print as it is local variale
ABC()
var1=5
def ABC():
    var2=10
    var1=23
    print(var2)
    print(var1)
ABC()    
print(var1)#give value 5 but why?what is variable scope overwriting?scope overwriting is also known as shadowing 
#print(var2) we cannot print 
var1=5
def ABC():
    var2=10
    global var1
    var1=23
    print(var2)
    print(var1)
ABC()    
print(var1)#give value 10 
#print(var2) we cannot print as local varable
#different between enclose and local
def outer():
    x=10#local for outer but enclosed for inner
    def inner():
        x=20
        print(x)#20 will be printed
    inner()
    print(x)#10 will be printed
outer()    

def outer():
    x=10#local for outer but enclosed for inner
    def inner():
        nonlocal x
        x=20
        print(x)#20 will be printed
    inner()
    print(x)#20 will be printed
outer()    
#what is overwriting in built_in name space?
#len=5
#print(len) not allowed also it works as len is a built -in function
#two methods 1. globals , 2. locals
var1=5
def ABC():
    var2=10
    global var1
    var1=23
    print(var2)
    print(var1)
    print("var1 is global?", var1 in globals())#----> kaj korche naa kano?
    print("var2 is local?", var2 in locals())#-----> kaj korche naa kan0?
ABC()    
print(var1)#give value 23
#print(var2) we cannot print as local varable
print(globals())# will give {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001597A29BB00>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'c:\\Users\\MSCLAB-142\\python day 11.py', '__cached__': None, 'var1': 23, 'ABC': <function ABC at 0x000001597A28A160>, 'outer': <function outer at 0x000001597A5C9BC0>}
print(locals()) # will give {'__name__': '__main__', '__doc__': 'import math\ndef isPrime(num):\n    flag=True\n    for i in range(2,int((math.sqrt(num))+1)):\n        if num==2:\n            flag=True\n            break\n        if num%i==0:\n            flag=False\n            break\n    return flag\n    \ndef prime_factors(num):\n    factor=[]\n    count_prime=[]\n    for i in range(2,num+1):\n        if(num%i==0):\n            factor.append(i)\n    prime_factor=list(filter(lambda x: isPrime(x),factor))#filter only take boolean value so we used flag=true or false\n\n    for i in range(len(prime_factor)):\n        count=0\n        while(num%prime_factor[i]==0):\n            count+=1\n            num=num/prime_factor[i]\n        count_prime.append(count)\n    print(dict(zip(prime_factor,count_prime)))\nnum=int(input("enter a number: "))\nprime_factors(num)', '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000021E541ABB00>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'c:\\Users\\MSCLAB-142\\python day 11.py', '__cached__': None, 'var1': 23, 'ABC': <function ABC at 0x0000021E544765C0>, 'outer': <function outer at 0x0000021E544D9BC0>}
#{'__name__': '__main__', '__doc__': 'import math\ndef isPrime(num):\n    flag=True\n    for i in range(2,int((math.sqrt(num))+1)):\n        if num==2:\n            flag=True\n            break\n        if num%i==0:\n            flag=False\n            break\n    return flag\n    \ndef prime_factors(num):\n    factor=[]\n    count_prime=[]\n    for i in range(2,num+1):\n        if(num%i==0):\n            factor.append(i)\n    prime_factor=list(filter(lambda x: isPrime(x),factor))#filter only take boolean value so we used flag=true or false\n\n    for i in range(len(prime_factor)):\n        count=0\n        while(num%prime_factor[i]==0):\n            count+=1\n            num=num/prime_factor[i]\n        count_prime.append(count)\n    print(dict(zip(prime_factor,count_prime)))\nnum=int(input("enter a number: "))\nprime_factors(num)', '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000021E541ABB00>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'c:\\Users\\MSCLAB-142\\python day 11.py', '__cached__': None,
#what is arguments in function?
#what about passing function as argument?
#what is decorater and raper concept?
def decor(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper
@decor
def greet():
    print("hello student ")
@decor    
def greet2():
    print("We are learning")

greet()
greet2()
#what is happening in the above  and below functions?

def sequence(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper
@sequence
def greet():
    print("hello student ")
@decor    
def greet2():
    print("We are learning")

greet()
greet2()

#what is lock file like structure?
#question---write a function in python wher the name of the function is time 
# and it give output how much time the fuction is taking to give the output?
import time

start = time.time()

for i in range(5):
    print("GeeksForGeeks")

time.sleep(1)
end = time.time()

print(f"Total runtime of the program is {end - start} seconds")#from geeksforgeek

#form copilot
import time as t  # Import time module but alias it to avoid name conflict

def time(func, *args, **kwargs):
    """
    Measures and prints the execution time of a given function.
    
    Parameters:
        func (callable): The function to execute.
        *args: Positional arguments for the function.
        **kwargs: Keyword arguments for the function.
    
    Returns:
        The result of the function call.
    """
    if not callable(func):
        raise TypeError("First argument must be a callable function.")
    
    start = t.perf_counter()  # High-precision start time
    result = func(*args, **kwargs)
    end = t.perf_counter()    # High-precision end time
    
    elapsed = end - start
    print(f"Execution time: {elapsed:.6f} seconds")
    
    return result


# Example usage:
def sample_task(n):
    """Example function that simulates work."""
    total = 0
    for i in range(n):
        total += i ** 2
    return total

# Measure execution time of sample_task
output = time(sample_task, 1_000_000)
print("Result:", output)

#argument and keyword argument:args is tuple and kearg is dict , what are the use of these?
def fun(*args):
    return sum(args)
print(fun(1,2,3))
def fun1(**kwargs):
    for k,val in kwargs .items():
        print(k,val)
fun1(a=1,b=2,c=3)        
#what is precission counter?
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start_time=time.perf_counter()
        result=func(*args,**kwargs)
        end_time=time.perf_counter()
        print (f"Executed function {func.__name__} in {end_time-start_time}s")#{func.__name__} will give function name
        return result
    return wrapper
@timer
def heavy_computation():
    time.sleep(1.5)#it will do nothing for 1.5 sec
    return "done!"
heavy_computation()    
@timer
def heavy_comp_add(a,b):
    time.sleep(1)
    return a+b
heavy_comp_add(5,8)

#4 functions, every argument is positive or not , check it by decor(no argument , 1 argument , 2 arguments , 3 arguments)
def positive(func):
    def wrapper(*args):
        result=func(*args)
        for arg in args:
            if arg==str:
                print(f"No positive argument in {func.__name__}, It is a string")
            elif arg==int or arg==float:
                if arg>0:
                    print("Positive argument")    
                else:
                 print("not Positive argument")   
        return result         
    return wrapper    
@positive
def abc():
    print("hello")    
abc()
@positive
def addition(a,b):
    print(a+b)
    return a+b
addition(2,-3)

#not doneeee!!!!!!!!!!!!!!!!!!!!!!!!!



