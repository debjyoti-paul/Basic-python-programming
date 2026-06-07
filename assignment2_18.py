# Write a Python program to combine two lists into a dictionary using the zip() function. 
n=int(input("enter the no of items in dictionary: "))
l1=[]
l2=[]
for i in range(n):
    key=input("enter key: ")
    l1.append(key)
for i in range(n):
    value=input("enter value: ")
    l2.append(value)
dict1=dict(zip(l1,l2))
print(dict1)    
        