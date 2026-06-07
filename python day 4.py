#q1
l1=[1,2,3,4]
repeat_check = False
for i in range (len(l1)):
    for j in range (i+1,len(l1)):
        if l1[i]==l1[j]:
            repeat_check=True
print(repeat_check)   

#q2     
l2=[2,3,4,3,4,5,3,1]
repeat_check = False
for i in range (len(l2)):
    print("i is",i)
    for j in range (i+1,len(l2)):
        print("j is",j)
        if l2[i]==l2[j]:
            repeat_check=True
            break
    if repeat_check==True:
        break 
print(repeat_check)        

#q3
l3=[2,3,4,3,4,5,3,1]
repeat_check = False
for i in range (len(l3)):
    for j in range (i+1,len(l3)):
        if l3[i]==l3[j]:
            print("The repeating element is",l3[i])        
            repeat_check=True
            break
    if repeat_check==True:
            break
          
#q4
l4=[2,3,4]
repeat_check = False
for i in range (len(l4)):
    for j in range (i+1,len(l4)):
        if l4[i]==l4[j]:
            print(l4[i])        
            repeat_check=True
            break
    if repeat_check==True:
            break 
if repeat_check==False:
    print("No Repetation") 
     
#q5  
l5=[2,3,3,4,4,5,5,6,3]
l6=[]
for i in range (len(l5)):
    for j in range (i+1,len(l5)):
        if l5[i]==l5[j]:
            l6.append(l5[j])
            break
print(l6)
s1=set(l6)
l=list(s1)
print(l)
#q6
l7=[1,2,3,2,3,2]
freq_dist=[]
for i in range (len(l7)):
    count=0
    if l7[i] not in l7[:i]:
        for j in range (i,len(l7)):
            if l7[i]==l7[j]:
               count +=1
    if count>0:
        freq_dist.append((l7[i],count))               
print (freq_dist)

#q7
l7=[1,2,3,2,3,2]
place=[]
repeat_check=False
for i in range (len(l7)):
     for j in range (i+1,len(l7)):
        if l7[i]==l7[j]:
            place. append ((l7[i],[i,j]))
        break          
print (place)

#q7
l1=[1,2,2,2,3,3,3,4,4]
l2=[]
for i in range (len(l1)):
    for j in range (i+1 , len(l1)):
        if l1[i]==l1[j]:
            l2. append ((l1[j], [i,j]))
        break 
print(l2)  

