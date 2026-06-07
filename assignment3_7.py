#Write a recursive function to find the maximum element in a list. 
def maximum(l):
    max=l[0]
    length=len(l)
    if length==1:
        return max
    if max < l[1]:
        max=l[1]
    l[1]=max    
    l.pop(0)
    return maximum(l)  
l=[]
n=int(input("enter the no of element in the list: ")) 
for i in range (n):
    num=int(input("enter the element: "))  
    l.append(num)
print(maximum(l))