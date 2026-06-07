#Write a recursive function to count occurrences of a character in a string.  
def occur(s,ch,count=0):
    length=len(s)
    if length==0:
        return count
    if s[0]==ch:
        count+=1
    return occur(s[1:],ch,count)
s=str(input("enter a string: "))   
ch=str(input("enter the character: "))
print(occur(s,ch))
