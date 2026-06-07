#Write a Python program to merge two sorted lists into a single sorted list without using  built-in sorting functions.
l1=[1,3,5,7]
l2=[2,4,6,8]
merged=l1+l2
length=len(merged)
for i in range(length):
    for j in range(length-1):
        if merged[j] > merged[j + 1]:
            temp=merged[j]
            merged[j]=merged[j + 1]
            merged[j + 1]= temp
print( merged)