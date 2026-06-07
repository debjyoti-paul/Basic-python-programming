# Write a recursive function to perform binary search on a sorted list. 
def binary_search(l,target):
    if len(l)==0:
        return "False"
    mid=len(l)//2
    if l[mid]==target:
        return "True"
    else:
        if l[mid]<target:
            return binary_search(l[mid+1:],target)
        if l[mid]>target:
            return binary_search(l[:mid],target)
l1=[]
n=int(input("enter the no. of elements: "))
for i in range(n):
    num=int(input("enter a number: "))
    l1.append(num)
t=int(input("enter target: "))
print(binary_search(l1,t))