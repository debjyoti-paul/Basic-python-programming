#theory khatay
i=1
while(i<=10):
    print(i)
    i+=1
def rec(value):
    if value==10:
        print("i am stop printing at" ,value)
    else:
        print("i am  printing at " ,value)    
        value+=1
        print("changed value to ",value)
        print("****************************")
        rec(value)
rec(5)   
#rec(11)     #infinite loop
def rec1(value):
    if value>=10:
        print("i am stop printing at" ,value)
    else:
        print("i am  printing at " ,value)    
        value+=1
        print("changed value to ",value)
        print("****************************")
        rec(value)
rec1(11)  #now it is not infinite loop
#using recursion  and iteration with {while()} , sum of n no.
i=1#using loop
sum=0
n=int(input("enter n:"))
while():
    if(i==n):# you can also write (i>=n)
        print(i , end=" =")
        sum=sum+i
        break
    else:
        print(  i ,end=" +")
        sum=sum+i
        i+=1
print(sum)#something wrong with this program

def recsum(n ,current=1 ):#default value assigning to the value
    
    #base case
    if (current==n):
        print(n,end="=")
        return n
    #print the current value with a "+" sign    
    print(current, end="+")
    #recursive step:add current to the sum of rest
    return current+recsum(n, current+1)
#
#
n=10 #int(input("enter n:"))
total=recsum(n)
print(total)#output of the program is "1+2+3+4+5+6+7+8+9+10=55"
def rec_add(n):
    if n==1:
        return 1
    return n+ rec_add(n-1)
num= 5 #int(input("enter n:"))
total=rec_add(num)
print(total) # input=5 , output=15

#indirect recursion eg:
def is_even(n):
    if n==0:
        return True
    return is_odd(n-1)
def is_odd(n):
    if n==0:
        return False
    return is_even(n-1)

num1=5
res1=is_even(num1)
print(res1)
num2=6
res2=is_even(num2)
print(res2)
num3=4
res3=is_odd(num3)
print(res3)
num4=5
res4=is_odd(num4)
print(res4)



#turns count
def playerA(n):
    if n==0:
        return
    print("player a's turn")
    playerB(n-1)
def playerB(n):
    if n==0:
        return
    print("player b's turn")
    playerA(n-1)
playerA(6)





# print this series 1 2 3 4 5   3 1  2 3 4 5 6  4 2  3 4 5 6 7  5 3   (increase by 1 , 5 times ;; decrease by 2 , 2 times)
def playerA(n,x=1):
    if n == 0:      # stopping condition
        return
    
    print("Player A:")
    last = x
    for i in range(5):
        print(last, end=" ")
        last += 1
    
    print("\n")
    playerB(n - 1 , last - 1 )   # pass the last printed value


def playerB(n, y=1 ):
    if n == 0:      # stopping condition
        return
    
    print("Player B:")
    print(y-2, y-4)
    print()
    
    playerA(n-1, y-3)  # continue from decreased value


playerA(4)
def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+fibo(n-2)
    
n=10
for i in range(0,n):
    print(fibo(i), end=" ") 