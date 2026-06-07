#create a list of lists , using user  input , where the inner lists are having same no. of element
rr=int(input('enter the no of rows: '))
cc=int(input('enter the no of elements: '))
cre_outlist=[]
for i in range (rr):
       cre_inlist=[]
       for j in range (cc):
              element=int(input("enter an element:"))
              print(i,j)
              cre_inlist.append(element)
       cre_outlist.append(cre_inlist)
print(cre_outlist)



#create a list of lists , using user  input , where the inner lists are having different no. of elements
rr=int(input('enter the no of rows: '))
cre_outlist=[]
for i in range (rr):
       cc=int(input('enter the no of elements: '))
       print(i)
       cre_inlist=[]
       for j in range (cc):
              element=int(input("enter an element: "))
              print(i,j)
              cre_inlist.append(element)
       cre_outlist.append(cre_inlist)
print(cre_outlist)


a= int (input('enter the first number'))
b=  int(input('enter the seond number'))
c= int( input('enter the third number'))
if a>b and a>c:
    print (' largest number is',a)
elif b>c and b>a:
    print ('largest number is',b)
elif c>a and c>b:
    print ('largest number is',c)
    
if a<b and a<c:
    print ('smallest number is',a)
elif b<c and b<a:
    print ('smallest number is',b)
elif c<a and c<b:
    print ('small56est number is',c)
 

l1=["a", "b" , "c"]
print('c'in l1)
print('c'not in l1)

v1= range(2,5)
print(v1)
v2=list(range(2,7))
print(v2)

n=5
i=1
while i<n:
    print(i)
    i+=1

#extracting the values of lists
l=[11,12,13,14,15]
print(l)
n1=len(l)
j=0
while j<n1:
    print(l[j])
    j+=1
    

l=[11,12,13,14,15]
print(l)  
for i in range(len(l)):
    print(l[i],i)

#extracting the values of lists wherev list is developed using range
v3=list(range(2,11))
print(v3)
n2=len(v3)
i=0
while i<n2:
    print (v3[i])
    i+=2

for k in range(22,25):
    print(k)

#extracting the values of lists wherev list is developed using range
l2=list(range(2,11,2))
print(l2)
for i in l2:
    print(i)
for i in  range(len(l2)):
    print(l2[i],i)   

#different operations of range
l3=list(range(11))
for u in range(5):
    print (u)
for u in range(2,5):
    print (u)
for u in range(1,10,2):
    print (u)
    
#use of break statement
l4=list(range(67,78))
for i in range (67, 77):
     if i==69:
         break
     print(i)

#use of continue statement
l5=list(range(6,22))
for i in range (6,22):
     if i==9:
         continue
     print(i)

#create a list with mathematical operation
l5= list(range(11))
l6=[i*2 for i in l5]
l7=[]
for i in l5:
    l7.append(i*2)
print(l5,l6,l7)

#extracting the +ve value from list
l8=[-4,-2 ,0,7,8]
p_l8=[i for i in l8 if i>0]
print (l8 , p_l8)

#absolute value
v4=-123
print(abs(v4))

a_l8=[abs(i) for i in l8]
print(a_l8)

l9=['  apple  ', '  banana  ' , '  orange  ']
c_l9=[i.strip() for i in l9]
c_l10=[i.lstrip() for i in l9]
c_l11=[i.rstrip() for i in l9]
print(l9 , c_l9 , c_l10 , c_l11)

#create a list of tuples where the second  element is square of first element
s_t=[(x,x**2) for  x in range (6)]
print(s_t)

#flattening a 2d list
l10=[[1,2,3],[4,5,6],[7,8,9]]
f_l10=[]
for row  in l10:
    print(row)
for row  in l10:
    for ele in row:
        print(ele)
        f_l10.append(ele)
print(f_l10)

f__l10=[ele for row in l10 for ele in row]
print (l10 , f__l10)

#find transpose of a 3*3 matrix
l11=[[1,3,5],[2,6,8]]
print(len(l11))
print(len(l11[0]))
t_l11=[[l11[j][i] for j in range (len(l11))] for i in range(len(l11[0]))]
print(l11, t_l11)

#alternative method for transpose
l12=[[1,2,3],[4,5,6]]
n_col=len(l12[0])
n_row=len(l12)
t_l12=[]

for i in range(n_col):
    row=[]
    for j in range(n_row):
        row.append(l12[j][i])
    t_l12.append(row)
print(t_l12)  

           
l12=[[11,22,33],[4,5,6],[7,8,9]]
n_col=len(l12[0])
n_row=len(l12)
t_l12=[]

for i in range(n_col):
    row=[]
    for j in range(n_row):
        row.append(l12[j][i])
    t_l12.append(row)
print(t_l12)             