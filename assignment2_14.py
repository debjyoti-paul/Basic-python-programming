#Write a Python program to swap keys and values in a dictionary. 
dict1={'a':1,'b':2,'c':3}
keys=[]
values=[]
for k in dict1.keys():
    keys.append(k)
for v in dict1.values():
    values.append(v)
dict2=dict(zip(values,keys))
print(dict2)