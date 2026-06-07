import sys
a=9.8
b='a'
print(sys.getsizeof('a'))
print(sys.getsizeof(a))
c=True

e=99999998888886666
print(sys.getsizeof(e))
print ('hello')


complex1=5+7j
complex2=3+4j
print (complex1*complex2)
print (complex1+complex2)

list1=[2,4,6]
print (list1)

list2=[2,6.9,'abs', [6,7,8],False]
print (list2)

l1=list()
print(l1)
l1=[]
print(l1)

l1.append(4)
print (l1)
import copy #for deepcopy we have to import copy..
list4=[7,8,9]
list5=[91, 55, 87]
list4.append(list5)
print (list4)
list4.extend(list5)
print (list4)
    
list3=list5#shallow copy
print(list3)
list6=list5.copy()#shallow copy
print (list6)

list7=copy.deepcopy(list4)#deep copy
print(list7)
l4=[[1,2],[3,4]]
l5=l4.copy()
l6= copy. deepcopy(l4)
l4[0][0]=2
print(l4,l5,l6)

s1={1, 2, 3}
fs1=frozenset([1,2,3])
print (s1, fs1)

d={"a": 100 , "b" : 200}
print (d)

l9=[3]*4
print(l9)

list8=["mom ", "tue", "wed", "thurs", "fri","sat", "sun"]
indexofwed=list8. index("wed")
print (list8)
print (indexofwed)
print(list8. index("wed"))

list8. reverse()
print(list8)

print(list8[::-1])#give reverse
print(list8[3:4:5])
print(list8[::2])
print(list8[::3])
print(list8[:-1])
print(list8[-3:])

l10=[4, 67, 58, 90, 123, 54,0]
print(l10)
l10.sort(reverse= True)#ascending order
print (l10)
l10.sort(reverse= False)#decending order
print (l10)

v=l10.pop()
print (l10)
print(v)


del l10[0]
print(l10)

l10.clear()
print(l10)

l10=[4, 67, 58, 90, 123, 54,0]
del  l10[1:4:2]
print(l10)


#create a list of 4x5 , user input , remove 2 nd and 3 rd row using slicing operation
list10 =[[1,2,3,4,5], [6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
print(list10)
del list10[1:3]
print (list10)

print ("what is your name\n Debjyoti Paul")

print ("""what is your name
       Debjyoti Paul""")

d1="Hello , World"
print(d1)
print (len(d1))

d2= d1.lower()
print(d2)

d3=d1.upper()
print(d3)

d4=d1.capitalize()
print(d4)

d5=d1.swapcase()
print (d5)

d6= d2. title()
print (d6)

d7=d1.replace('Hello' , 'Hi')
print(d7)

print (d1.find('Hello'))
print (d1.find('world'))
print (d1.find('Hi'))#show default value as -1


print('we are'+'leraning' + 'python')
print (d1+d7)
print (d1+" " +d7)

#create a list of 4x5,remove 2nd and 3rd element of each row
list11 =[[1,2,3,4,5], [6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
print(list11)
for row in list11:
       del row[2:4]     
       
print(list11)













