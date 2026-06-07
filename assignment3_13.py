# Write a recursive function to check if a number is a palindrome without converting to string. 
def pali(num,rev=0):
    if num==0:
        return rev
    digit=num%10
    rev=(rev*10)+digit
    return pali(num//10, rev)
n=int(input("enter a number: "))    
print(pali(n)==n)
    
        