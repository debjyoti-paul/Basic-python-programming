#Write a Python program to remove duplicate elements from a list without using the set() function.
l1=[1,2,1,3,4,3,5,6,1] 
l2=[] 
length=len(l1)
for i in range(length):
    if l1[i] not in l2:
        l2.append(l1[i])
print(l2)