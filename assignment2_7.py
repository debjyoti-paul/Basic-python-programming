#Write a Python program to create a new list containing only even numbers from a given list. 
l1=[2,3,4,5,6,7,8,9,10,56,79,80,100]
length=len(l1)
l2=[]
for i in range(length):
    if(l1[i]%2==0):
        l2.append(l1[i])
print(l2)