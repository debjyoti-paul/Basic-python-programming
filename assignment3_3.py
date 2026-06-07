#Write a recursive function to count the number of digits in a number.
def count(num,cnt=1):
    if num//10==0:
        return cnt
    else:
        num=num//10
        return count(num,cnt+1)
num=int(input("enter a number: "))    
print(count(num))    