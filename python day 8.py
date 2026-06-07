def electric_bill():
    unit=int(input("enter the unit of electricity consumed:"))
    if unit<=100:
        bill=unit*1
        print("****************************************************")
        print("the bill for unit ", unit ," is " , bill ," rs")
        print("****************************************************")
    elif unit>100 and unit<=200:
        bill1=100*1
        bill2=(unit-100)*2 
        print("the bill for first 100 unit  is " , bill1 ," rs")
        print("the bill for remaining unit  is " , bill2 ," rs")
        print("*****************************************************")
        print("the  total bill  is             " , bill1+bill2 ," rs")
        print("*****************************************************")
    elif unit>200:
        bill1=100*1
        bill2=100*2 
        bill3=(unit-200)*5  
        print("the bill for first 100 unit  is " , bill1 , " rs")
        print("the bill for next 100  unit  is " , bill2 , " rs")
        print("the bill for remaining unit  is " , bill3 , " rs")
        print("*****************************************************")
        print("the total bill  is              " , bill1+bill2+bill3 , " rs") 
        print("******************************************************")
           
electric_bill() 


#q1
#student=[('701',"apabrita",75),...of 5 students]
#1. write a user define function named is_eligibleturns true if mark is less than 30 , 
# otherwise false.,the list is passed as an argument
#    use  the above function with filter operation to extract the eligible student  
#2.using lambda function with map create a new list with student ids and
#  updated marks where students get a grace mark of 5 if ther score is below 30

student_record=[("730","Udipta",100),("749","Apabrita",40),("723","Iqran",0),("701","Srinjoy",25),("733","Sourasrota",80)]
def is_eligible(l1):
    flag=[]
    for i in l1:
        if i[2] < 30:
            flag.append("true")
        else:
            flag.append("false")
    return flag
print(is_eligible(student_record))
id_eligible=[]
for i in range(len(is_eligible(student_record))):
    if is_eligible(student_record)[i]=="true":
        id_eligible.append(student_record[i][0])
print(id_eligible)

new_update=[]
for i in student_record:
    if i[2]<30:
        new_update.append((i[0],i[2]+5))
    else:
        new_update.append((i[0],i[2]))
print(new_update)

#done using lambda , map ,filter
def is_eligible(student):
    if student[2] < 30:
        return True
    else:
        return False

eligible_students = list(filter(is_eligible, student_record))
print("Eligible students:", eligible_students)

updated_marks = list( map(lambda s: (s[0], s[2] + 5 if s[2] < 30 else s[2]), student_record))
print("Updated list:", updated_marks)


#recurssion
#stac data structure ?
#stac is a abstract data type, what is primitive data type?

def factorial(n):
    if n==0:
        return 1#base case
    else :
        return n*factorial(n-1)#recursion
    
num=int(input("enter a number: "))    
print(factorial(num))



#what is stack?types of stack?
#what is link list?
#python uses a c implementation task under c python. 
#each function call generate PyFrameObject , it have the code object , local variables 
# stored in f local , instruction pointer, refercence to the calling frame in f_back in each
#when recusin happen a new pyframeobject created for each call , these obj together fornm a link stag , when  a base case    is hit ,frame unwind in reverse returning results
#pyton has a default  recursion limit ,1000 ,called recursion depth , controlled by  sys.getrecursionlimit()
#and from disha's copy
#how link list work?#how stack using link list work?stack overflow?
def factorial1(n,depth=0):#using head recursion
    indent="  "*depth
    print(f"{indent}CALL factorial1({n})")# f for giving format
    if n == 0:
        print(f"{indent}RETURN 1")
        return 1
    else:
        result=n*factorial1(n-1,depth+1)
    print(f"{indent}RETURN {result}")
    return result
n=int(input("enter a number: "))
print(factorial1(n))

def fact_tail(n ,acc=1):#using tail recursion
    if n==0:
        return acc
    return fact_tail(n-1 , acc*n)



#head recursion , tail recursion
#q2 n=4 
#****
# ***
#  **
#   * 
#print this using recursion
def star(n,row=0):
    if row== n:
        return
    else:
        print(" "*row+"*"*(n-row))
    star(n,row+1)
n=int(input("enter a number: "))
print(star(n))

#this is done by loop not by recursion|
def star(n):#                  <------|
    i=0
    j=n
    while i<=n:
        print(" "*i+"*"*j)
        i+=1
        j=n-i
    print("\n")
    return
num=int(input("enter a number: "))
star(num)

#you are climbing a staircase , for each  move you can climb 1 step or 2 step  .
# Find in how many distinct way you can reach the n th step  ,not n+1 step, do it using recursion ,
# not using permutation or combination 
# also this is a combinatory problem 
# this is very important programm  as this is a typical dynammic program , which also use recursion.
def ways(n):
    if n<= 1:
        return 1
    else:
        return ways(n-1)+ways(n-2)
    
print(ways(4)) 


def ways(n ,memo={}):#memoization ,stop up dynamic approch
    if n in memo:
        return memo[n]
    if n<= 1:
        return 1
    else:
        memo[n]=ways(n-1 , memo)+ways(n-2 ,memo)
    return memo[n]    
    
print(ways(4))    
