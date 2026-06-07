#Write a Python program to find the sum of all elements in a given list.  
l1=[2,3,4,5,6,7,8,9,10,56,79,80,100]
length=len(l1)
sum=0
for i in range(length):
    sum=sum+l1[i]
print(sum)