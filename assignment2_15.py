#Write a Python program to count the occurrence of each word in a given sentence using a dictionary.
string1=str(input("enter a sentence: ")) 
l1=string1.split(" ")
l2=[]
freq_dist=[]
for i in range (len(l1)):
    count=0
    if l1[i] not in l1[:i]:
        for j in range (i,len(l1)):
            if l1[i]==l1[j]:
               count +=1       
    if count>0:
        l2.append(l1[i])
        freq_dist.append(count)          
dict1=dict(zip(l2,freq_dist))
print(dict1)