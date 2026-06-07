#write a function to count the number of digits in a number.
#def count_digit(num):
#    count=0
#    while(num>0):
#        count+=1
#        num=num//10
#    return count
#num=int(input("enter a number: "))
#print("the number of digits in the given number is: ",(count_digit(num)))
#working

#write a function to check whether a given integer is a prime number or not.

#def prime(num):
#    i=1
#    count=0
#    for i in range (2,num):
#        if(num%i==0):
#            count+=1
#        else :
#            continue    
#        i+=1
#    if count==2:
#        print(num , "is a prime number")
#    else:
#        print(num ,"is a not prime number ")    
#num=int(input("enter an integer: "))
#prime(num)



#write a function for an integer that prints its multiplication table upto 10.
#def multiply(integer):
#    count1=1
#    l=[]
#    while (count1<=10):
#        value=integer*count1
#        count1+=1
#        l.append(value)
#    return l
#integer=int(input('enter an integer'))
#print('the multiplication table for given integer is',(multiply(integer)))


#a list of integer given . Detect the prime no. and  output will be the list of prime no.
'''def prime(n):
    l2=[]
    count=0
    for i in range (1, n):
        if(n%i==0):
            count+=1
        else :
            continue    
        i+=1
    if count==2:
        l2.append(n)
        print(l2)

place=int(input("how many integer you want in the list:"))
l1=[]
for i in range (0,place):
    num=int(input("enter the integer:"))
    print(i)
    l1.append(num)
    i+=1
print("your list is " , l1)    
length=len(l1)
for i in range(0,length):
    n=l1[i]
    prime(n)
    i+=1
#not working    '''




def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_list(numbers):
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes


# given list
nums = [2, 5, 8, 11, 15, 17, 20]

result = prime_list(nums)
print("Prime numbers:", result)

#take any integer . like 28 , 
# where the output is key=prime factor and values are the frequency of the prime factor {(2:2) ,(7:1)}
#prime factorisation dictionary key-factors, value-number of times repeated
import math
def isPrime(num):
    flag=True
    for i in range(2,int((math.sqrt(num))+1)):
        if num==2:
            flag=True
            break
        if num%i==0:
            flag=False
            break
    return flag
    
def prime_factors(num):
    factor=[]
    count_prime=[]
    for i in range(2,num+1):
        if(num%i==0):
            factor.append(i)
    prime_factor=list(filter( isPrime,factor))
    print(prime_factor)

    for i in range(len(prime_factor)):
        count=0
        while(num%prime_factor[i]==0):
            count+=1
            num=num/prime_factor[i]
        count_prime.append(count)
    print(dict(zip(prime_factor,count_prime)))
num=int(input("enter a number: "))
prime_factors(num)

