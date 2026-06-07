#theory khatay

print("www.date.com\\date")#for printing a back slash
print(r"www.date.com\date")#raw string
import re
pattern= re.compile(r"")#raw string? difference between raw string and string?
print(type(pattern))
#1
import re
word =input("please enter your  string: ")
pattern = re.compile(r"[0-9]+")
result=pattern.sub("_",word)#change the no. in underscore input  452dyuti , output _dyuti, input  dyuti452 , output dyuti_
print(result)#input deb452 , output deb_(group of no. is substituted by one underscore)

#2
import re
word =input("please enter your  string: ")
pattern = re.compile(r"[0-9]")# without +
result=pattern.sub("_",word)#input 345thingh , output ___thingh  (every number is substituted by underscore)
print(result)
#.sub? used for replacing 
#3
import re
word =input("please enter your  string: ")
pattern = re.compile(r"[a-c]")
result=pattern.sub("_",word)
print(result)
#4
import re
word =input("please enter your  string: ")
pattern = re.compile(r"\d+")
result=pattern.sub("_",word)
print(result)

#5

import re
word =input("please enter your  string: ")
pattern = re.compile(r"\d{2}")# input 234y output  _4y
result=pattern.sub("_",word)
print(result)

#6
import re
word =input("please enter your  string: ")
pattern = re.compile(r"\d{5,}")#input 
result=pattern.sub("_",word)
print(result)



#wac that replaces all the group of digits 0 to 3 with percentages
import re
word =input("please enter your  string: ")
pattern = re.compile(r"[0-3]+")
result=pattern.sub("%",word)
print(result)




#use dir
import re
word ="ABCabc123"
pattern = re.compile(r"[0-3]+")
result=pattern.sub("%",word)
print(dir(result))#print all methods of string
print(help(result.isalpha))
print(dir(pattern))#print all method of pattern




print(dir(pattern))#print all method of pattern, one of them is  'fullmatch'-> what is that?
print(help(pattern.fullmatch))#fullmatch(string, pos=0, endpos=9223372036854775807) method of re.Pattern instance ,Matches against all of the string.


#all non digit replace by &

import re
word =input("please enter your  string: ")
pattern = re.compile(r"\D+")
result=pattern.sub("&",word)
print(result)




#all wide space  replace by 5
#check weather James  in the string or not
word="Bond!James Bond."
pattern=re.compile(r"James")
#try match , full match , search , find  , find all , find title  from raima'
#print(pattern.match(word))
#print(word.match(pattern))
#not working , how to write the code?



#write a string in  quots "my room no. is 305 and section is 12"
#extract allthe digits separetly in groups


word="my room no. is 305 and section is 12"
pattern=re.compile("\D+")
result=pattern.sub(" ", word)
print (result)
#not correct but works do it using search ,...etc...




word="my room no. is 305 and section is 12"
pattern=re.compile(r"\d+")
print(pattern.findall(word))# out put ['305', '12']


import re
user_id=input(" enter user id : ")
pattern=r"^USER\d{3}[^A-Za-z0-9][A-Z]+$"# or , "^USER\d{3}\W{1}[A-Z]+$"

if re.fullmatch(pattern,user_id):
    print("valid:)")
else:
    print("invalid:(")    

import re
user_id=input(" enter user id : ")
pattern=r"^USER\d{3}[^A-Za-z0-9][A-Z]+$"# or , "^USER\d{3}\W{1}[A-Z]+$"

if re.match(pattern,user_id):
    print("valid:)")
else:
    print("invalid:(")    







