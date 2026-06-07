#Write a Python program to count the frequency of each element in a list. 
l1=[1,2,2,2,3,3,3,4,4]
freq_dist=[]
for i in range (len(l1)):
    count=0
    if l1[i] not in l1[:i]:
        for j in range (i,len(l1)):
            if l1[i]==l1[j]:
               count +=1
    if count>0:
        freq_dist.append((l1[i],count))               
print (freq_dist)