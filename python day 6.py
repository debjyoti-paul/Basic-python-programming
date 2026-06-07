#tuple type of data

import sys
t=(10,20,30)
#t[0]=30 cannot be done
l1=[10, 20, 30]
print(sys.getsizeof(t))
print(sys.getsizeof(l1))
print(t[0])
print(t[-1])
print(t[1:3])


for i in t:
    print(i)
t2=(40,50)
t3=t+t2
print(t3)
print(t2*3)
print(10 in t2)
print(40 not in t2)
print(len(t))
print(min(t))
print(max(t))
print(sum(t3))
print(t.count(30))
print(t.count(2))
t4=t3*3
print(t4.count(30))
print(t4.index(30))
#tupple packing
t5=5,6,7
print(t5)
#tupple unpacking
print(t5)
a,b,c=t5
print(a)
print(b)
print(c)
#extended unpacking *** very important
t6=5,6,7,8,9
print(t6)
a,*b=t6
print(a)
print(b)#b keeps the list type of data
a,*b,c=t6
print(a)
print(b)#b keeps the list type of data
print(c)
#swap in c language
a=10
b=20
temp=a
a=b
b=temp
print(a,b)
#swap by tuple
a=40
b=50
a,b=b,a
print(a)
print(b)
#creat a tuple containing the following elements 4,7,2,7,9,2,5,7
#creats another tuple which removes all occurrence of 7
tupple=(4,7,2,7,9,2,5,7)
print(tupple)#how to use pop operation*******
new_tupple=()
for i in tupple:
    if i!=7:
        new_tupple=new_tupple+(i,)
print(new_tupple)

l1=list(tupple)
l2=[]
for i in l1:
    if i==7:
        continue
    else:
        l2.append(i)
print (l2)
newt=tuple(l2)
print(newt)

#data analysing with python we have in sem3
i=5
t1=(i)
t2=(i,)
new_t=()
print(type(t1))
print(type(t2))
print(type(new_t))



#set type of data
s1={1,2,3}
print(s1)
l1=[1,2,3,4,3,5,2]
s2=set(l1)#type casting operation
print(s2)

s3={}#doesnot create a blank set , it creates a blank dictionary
#how to create blank set
bs=set()

for i in s2:
    print(i)
#add operation
s2.add(10)#can not add multiple elements
s2.update([6,5,7])
print(s2)
s2.remove(6)
#s2.remove(13) element is not present so giving error
s2.discard(6)#element is not present  but not giving error
#s2.pop(1)
print(s2)
s2.clear()
print(s2)

s4={1,3,2,4}
s5={3,4,5,6}

#set operation
#1.union
print(s4|s5)
print(s4.union(s5))
#2.intersection
print(s4&s5)
print(s4.intersection(s5))
#remove the same element
print(s4-s5)
print(s4^s5)

s4={3,4}
s5={4,3,5,6}
print(s4.issubset(s5))
print(s4.issuperset(s5))
print(s4.isdisjoint(s5))

fs=frozenset([1,2,3])
print(fs)

#take a sentence and using string and set operation find the unique words*** do it in home
sent1=str(input('write one sentence:'))
sent2=sent1.split(" ")
print(sent2)
sent3=set(sent2)
print(sent3)


#set comprehension same as list comprehension  , what is list comprehension!!??
word={c for c in 'abbghccjddesa' if c not in'abc'}
print(word)

#dictionary type of data
d={'a':1,'b':2,'c':2}
d1=dict(a=1,b=2,c=3)
print(d,d1)
d1['d']=5
d1['d']=6
print(d1)

del d1['a']
print(d1)
#how to traverse a dictionary
#1.through keys
for i in d1.keys():
    print(i)
#2.through values
for i in d1.values():
    print(i)
#3.through key_value pair
for k,v in d1.items():
    print(k,v)
q=(('a',1),('b',2),('c',3))
d=dict(q)
l=[('a',1),('b',2),('c',3)]
o=dict(l)
print(q,d,l,o)
t1=('a','b','c')
t2=(100,200,300)
w=dict(zip(t1,t2))#two list or two tuple or one list one tuple
print(w)
k=('a','b','c')
d=dict.fromkeys(k,0)
print(d)
#w2=w shallow copy
w2=dict(w)#deep copy
print(w2)


#take geographic coordinates of n number cities as input,
# store city as values and geographic coordinates as key
n_city=int(input("enter the no of cities: "))
lat=[]
long=[]
name=[]
for i in range(n_city):
    latc=int(input("enter the latitute: "))
    lat.append(latc)
    longc=int(input("enter the longitute: "))
    long.append(longc)
    cn=str(input("enter the name of the city: "))
    name.append(cn)
latlong=zip(lat,long)
namedict=dict(zip(latlong,name))
print(namedict)