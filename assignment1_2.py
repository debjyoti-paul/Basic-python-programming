def union(s1,s2):
    result= s1.union(s2)
    return result
def intersection(s1,s2):
    result=s1.intersection(s2)
    return result
def setdiff(s1, s2):
    result=s1.difference(s2)
    return result
def symdiff(s1, s2):
    result=s1.symmetric_difference(s2)
    return result
def subset(s1,s2):
    result=s1.issubset(s2)
    return result
def superset(s1,s2):
    result=s1.issuperset(s2)
    return result 
def check(ele,ss):
    result= ele in ss 
    return result     
def operate(func, s1 , s2):
    return func(s1 , s2)

n1=int(input("enter how many element you want in set1:"))
n2=int(input("enter how many element you want in set2:"))
s1=set()
s2=set()
for i in range(n1):
    s11=int(input("enter an element for set 1: "))
    s1.add(s11)
for i in range(n2):
    s22=int(input("enter an element for set 2: "))
    s2.add(s22)
operations={"union":union, "intersection":intersection,"setdiff":setdiff,"symdiff":symdiff,"subset":subset,"superset":superset}
while(True):
    choice=input("type union or intersection or setdiff or symdiff or subset or superset : ")
    result=(operate(operations[choice], s1 , s2 ))
    print(result)
    ques=input("for furthur operations type y otherwise n:")
    if(ques=='y'):
        continue
    else:
        break
ele=int(input("enter element for searching: "))
sett=input("type s1 or s2:")
def cnt(ss):
    count=0
    for i in ss:
        count+=1
    return count 
def power(ss):
    power_set=[[]]
    for element in ss:
        new_subset=[]
        for subset in power_set:
            new_subset.append(subset+[element])
        power_set.extend(new_subset)
    return power_set 
ss={"s1":s1,"s2":s2}
result2=(check(ele , ss[sett]))
print(result2)
result3=(cnt(ss[sett]))
print("the no. of element in",sett,"is",result3) 
result4=power(ss[sett])
print("the power set of ",sett," is ", result4)
l1=[]
n3=int(input("how many elements you want in list:"))
for i in range(n3):
    l11=int(input("enter element:"))
    l1.append(l11)
print(l1)
s3=set(l1)
print("the set of ",l1, "is  set ",s3)  

                