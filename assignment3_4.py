#Write a recursive function to find the product of elements in a list.
def prod(l,mul=1):
    length=len(l)
    if length==0:
        return mul
    else:
        l1=l.pop()
        return prod(l,mul*l1)
ll=[]
n=int(input("enter the number of elements in list: "))
for i in range (n):
    num=int(input("enter number:"))
    ll.append(num)
print("your list is:", ll)       
print(prod(ll))