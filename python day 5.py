#python day 5
#string opration
str1="python"
#print(str1[42]) index error
print(str1[2:42])
print(len(str1))
str2=''' good morning . the day is so beautiful'''
print(len(str2))
str3=" we are learning python "
print(str3)
print(str3.strip())
print(str3.lstrip())
print(str3.rstrip())
str4=" we,are,learning,python "
str5=str4.split(',')
str6=str4.split('e')
print(str5 ,str6)
c=str3.count('e')
print(c)

str7="ABSERT"
print(str7.isupper())

str8="absert"
print(str8.islower())
print(str8.isalpha())
print(str8.isascii())
print(str8.isalnum())
print(str8.startswith('ab'))
print(str8.isdigit())
print(str8.endswith('ab'))
print(str8.isdecimal())


# # WAPP that takes an user id from user and check the follows:  \
# 1. all of them are uppercase  
# 2.id starts with USER 
# 3. it followed by three digits 
# 4. followed by one special character
# 5. followed by any character  

#first method
id =(input('write your user id'))
if(id.isupper() and id.startswith('USER')):
    id1= id[4:7]
    if(id1.isdigit()):
        id2=id[7:8]
        if not(id2.isalnum()):
            print('valid id:)') 
else:
    print('invalid id:(')
    
id =(input('write your user id'))
id1= id[4:7]
id2=id[7:8]
if(id.isupper() and id.startswith('USER') and id1.isdigit()):
        if( id2.isdigit() or id2.isalpha()):
            print('invalid id:(') 
        else:
            print("valid id:)")    
else:
    print('invalid id:(')



#second method 
import re
user_id=input(" enter user id : ")
pattern=r"^USER\d{3}[^A-Za-z0-9][A-Z]+$"# or , "^USER\d{3}\W{1}[A-Z]+$"

if re.fullmatch(pattern,user_id):
    print("valid:)")
else:
    print("invalid:(")    


#check palindrome 
string=input("enter a word")
r_string=string[::-1]
if (string == r_string):
    print("palindrome ")
else:
    print("not a palindrome")    


#rotation 
s1=input("enter some alphabets")
s3=input("enter another alphabets")
if s3 in(s1+s1):
    print("second string is a rotation string")
else:
    print(" second string is not a rotation string")


# count the no of alphabets in a word
word=input("enter some alphabets:")
l1=list(word)
length=len(l1)
print(length)
#count the no of unique alphabets in a word
s1=set(word)
length=len(s1)
print(length)




#to take one sentence from user and list out the unique words
sent=input("write a sntence:")
sent1= sent.split(' ')
sent1=set(sent1)
sent2=list(sent1)
print(sent2)


# to find the largest palindrome substring
user=input("enter a word:")
max=0
pali=[]
pali2=[]
length=len(user)
for i in range (length):
    for j in range (i+1):
        user_p=user[j:i+1]
        if user_p==user_p[::-1]:
            if len(user_p)>= max:
                max=len(user_p)
                pali.append(user_p)
for i in pali:
    if len(i)==max:
        pali2.append(i)       
print(max)
print(pali2)         
print(pali)
        