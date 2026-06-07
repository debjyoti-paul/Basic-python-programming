#Write a Python program to traverse a tuple and count how many elements are even numbers.
tup1=(1,2,4,7,9,10,80,75)
length=len(tup1)
count=0
for i in range(length):
    if(tup1[i]%2==0):
        count+=1
print(count)