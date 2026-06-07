#Write a Python program to iterate through a string and count the number of vowels present in it. 
s1="vowel"
length=len(s1) 
count=0
for i in range(length):
    if(s1[i]=='a'or s1[i]=='e'or s1[i]=='i'or s1[i]=='o'or s1[i]=='u'):
        count+=1
print(count)