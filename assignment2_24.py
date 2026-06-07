#Write a Python program to find the top K frequent elements in a list. 
l1=[1,2,2,2,3,3,3,4,4]
freq_dist=[]
l2=[]
for i in range (len(l1)):
    count=0
    if l1[i] not in l1[:i]:
        for j in range (i,len(l1)):
            if l1[i]==l1[j]:
               count +=1
    if count>0:
        freq_dist.append(count)                     
maximum=max(freq_dist)    
for i in range (len(l1)):
    count=0
    if l1[i] not in l1[:i]:
        for j in range (i,len(l1)):
            if l1[i]==l1[j]:
               count +=1
    if(maximum==count):
        l2.append((l1[i],count))    
print (l2)