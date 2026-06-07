#python day 17

import random

#generate a random no between 1 to 10
n=random.randint(1,10)
print (n)

import math
#find sqrt of no
res=math.sqrt(25)
print(res)

from collections import Counter
data=['a','b','c','a','a']
count=Counter(data)#camel case for class and all lower case for function
print (count)


import math
print(dir(math))
print(math.e)



#dir(math)gives only names as strings not the actual object ,so from the name we can not diffrtiate among class, func, var
#getattr(math)converge the string name to a actual object
import random
import math
function=[f for f in dir(math) if callable(getattr(math,f))]
#getattr ==getattribule,function is a callable object means it is function not a  variable
print(function)
print(getattr(math,'sqrt'))

m=math.ceil(4.2)#o/p=5
o=math.floor(4.2)#o/p=4
print(m,o)
f=math.factorial(4)#o/p=24
p=math.pow(2,3)#o/p=8
print(f,p)
print(math.sin(math.pi/2))
import random
import math
function=[f for f in dir(math) if callable(getattr(math,f))]#getattr ==getattribule,function is a callable object means it is function not a  variable
print(function)
print(getattr(math,'sqrt'))
#give type errorprint(math.dist(math.pi/2))
print(math.degrees(math.pi))


#a ladder is leaning against  wall ,length of ladder=10 ft,angle with ground =60 degree, 
# find the heigth reached till the wall
x=10*(math.sin(math.pi/3))
print(x)


print(math.sqrt.__doc__)# o/p->Return the square root of x.
print(help(math.sqrt))
import random
#print the function in random module
#print(dir(random))
#function=[f for f in dir(random)if callable(getattr(random,f))]

n=random.random()
print(n)
n=random.randint(10,20)
print(n)

print(random.randint.__doc__)
print(random.seed.__doc__)



print(random.randrange(1,10,2))#1=startpoint ,10=openend point,2=step
#print(help(random.choice))
print(random.choice([10,120,157]))#every sequence type of data can be given,a variable ,blank list cannot work here
print(random.choices([110,1290,130,140,150,160,170,180,190,200],k=2))#it may not give unique choices

print(random.sample([110,1290,130,140,150,160,170,180,190,200],k=2))#give unique choices

#consider alist of names of 10 students ,devide them into two random groups
l1=['a','b','c','d','e','f','g','h','i','j']
grp1=list((random.sample(['a','b','c','d','e','f','g','h','i','j'],k=5)))
print(grp1)
grp2=list(set(l1)-set(grp1))
print(grp2)
#consider a list of 10 students where each students info is given as ("name","m/f").
#divide students into 2 grps keep generating until atleast

import random
while(True):
    group1=((random.sample([("avi","m"),("pari","f"),("adi","m"),("pakhi","f"),("ishaan","m"),("netra","f"),("moksh","m"),("neel","m"),("ri","f")],k=5)))
    
    group2=list(set(l1)-(set(group1)))
    count1=count2=0
    for name in group1:
        if name[1]=="f":
            count1=count1+1
    for name in group2:
        if name[1]=="f":
            count2=count2+1
    if count1>=2 and count2>=2:
        print(group1,group2) 
        break
      

#bakita khatay and day 16 also
#how will you distinguish between the naming system of variable , function , class
#import random
#generate a random  integer no. between  to 10
#n=random.randint(1,10)#first module name (.) then function name , so it is in lower case
#print(n)'''

#import math
#find square root of a num
#result=math.sqrt(25)#first module name (.) then function name, so it is in lower case
#print(result)

#from collections import Counter #counter is a class , so it is camalcase
#data =['a','b','c','a','a']
#count=Counter(data)
#print(count)#o/p: Counter({'a': 3, 'b': 1, 'c': 1})

#some uses of math module
#import math
#print(dir(math))#constructer defined by __(name)__  
#print(math.lcm(25,75))
#use help metod to understand the modules
#print(help(math.e))
#functions=[f for f in dir(math) if callable(getattr(math,f))]#getattr= get attribute , callabel er kaj ki? to check it is a function or not
#print(functions)
# dir(any module name) only give names as strings not the actual object 
#gettattr(math , f) converts the string name to an actual object
#print(getattr(math,'sqrt')) #o/p: <built-in function sqrt>
#math.ceil , math.floor  having valu 4.8

#some uses of math module
#import math
#print(math.ceil(4.8))#o/p: 5
#print(math.floor(4.8))#o/p; 4
#print(math.factorial(13))
#print(math.pow(2,3))
#print(math.log(1))# base e
#print(math.log10(1))# base 10
#passs the angel as radian in trigometric function
#print(math.sin(math.pi/2))
#print(math.degrees(math.pi/2))
#print(math.radians(90))

#a ladder is leaning against a wall. length of the ladder is  10 feet and angel is 60 degree.find the height it reached
#import math
#height=(math.sin(math.pi/3))*10
#print("height reached by ladder is " , height,"feet")

#explore sqerrrot function throuh help
#import math
#print(help(math.sqrt))
#o/p:Help on built-in function sqrt in module math:

#sqrt(x, /)
#    Return the square root of x.

#None
#print(math.sqrt.__doc__)#o/p: Return the square root of x.(doc gives details of the module)

#print functions from random module
#import random
#print(dir(random))

#some use of random module
#import random
#n=random.random()#first random is a module , second random is the function
#print(n)
#print(help(random.random()))# x in intervel [0,1)
#n2=random.random()#give error
#n2=random.randint(10,20)
#print(n2)
#print(help(random.randint(10,20))) # x in [a,b]
#random.seed(10)
#n=random.randint(10 , 20)#o/p: is only 19 why?
#print(n)
#print(help(random.randrange))#o/p:????????????????????, meaning?????????????
#print(random.randrange(1,10))#here the options are all integers
#print(random.randrange(1,10,2))# here the options are 1,3,5,7,9
#difference between randrange , randint , random functions?
#print(random.choice(1,10,2))
#print(help(random.choice([110,120,157])))
#print((random.choice([110,120,157])))#optins are 110, 120, 157# you can use list,tuple , etc  any sequential type of data
#print(random.choice(['kolkata','mumbai','chennai','delhi']))
#print(help(random.choices([1,11,111,1111,11111,111111,1111111],k=3)))
#print(random.choices([1,11,111,1111,11111,111111,1111111],k=3))# can give three same  numbers.simple random sampling with replacement
#diference between choice and choices
#print(random.sample([1,11,111,1111,11111,111111,1111111],k=3))# never be same no.simple random sampling without replacement

#consider a list of names of 10 students divide the students into two random groups
#l1=[]
#for i in range(0,10):
#   name=input("name of the student :")
#   l1.append(name)

#print(l1)
#g1=random.sample(l1,k=5)
#print(g1)
#g2=[set(l1)-set(g1)]
#print(g2)

#consider a list of 10 students like [(name , M/F)..... of 10 students ]
#divide the list into two groups of 5 ,keep generating this group  for having each group at least 2 female student
# 
#l2=[]
#for i in range(0,10):
#    name=input("name of the student :")
#    gender=input("M for male and F for female:")
#    l2.append((name , gender))
#print(l2)
#while(True):
#    g11=random.sample(l2,k=5)
#    g22=list(set(l2)-set(g11))
#    count1=count2=0
#    for student in g11:
#        if student[1]=="F":
#            count1+=1
#    for student in g22:
#        if student[1]=="F":
#            count2+=1
#    if count1>=2 and count2>=2:
#       print(g11,g22)
#       break
#l3=[]
#for i in range(0,10):
#    name=input("name of the student :")
#    gender=input("M for male and F for female:")
#    l3.append((name , gender))
#print(l3)
#while (True):
#    gr1=random.sample(l3,k=3)
#    l4=list(set(l3)-set(gr1))
#    gr2=random.sample(l4,k=3)
#    gr3=list(set(l4)-set(gr2))
#    count1=count2=count3=0
#    for student in gr1:
#        if student[1]=="F":
#            count1+=1
#    for student in gr2:
#        if student[1]=="F":
#            count2+=1
#    for student in gr3:
#        if student[1]=="F":
#            count3+=1
#    if count1>=1 and count2>=1 and count3>=1:
#        print(gr1 , gr2 , gr3)
#        break

#Explore module by yourself




