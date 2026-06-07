#Write a recursive function to find the GCD of two numbers using the Euclidean algorithm. 
def gcd(a,b):
    rem=a%b
    if b==0:
        return a
    if rem==0:
        return b
    else:
        return gcd(b,rem)
num1=int(input("enter the 1st number: "))   
num2=int(input("enter the 2nd number: "))
print(gcd(num1,num2))    
