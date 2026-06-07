import re
pattern=re.compile(r" ")
password=input ("enter a password:")
copy1=password
copy2=password
copy3=password
count=0
if len(password) >=8:
    count+=1
    if re.search(r"[A-Z]{1,}",password):
        count+=1
        if re.search(r"[a-z]{1,}",password):
            count+=1
            if re.search(r"[0-9]{1,}",password):
                count+=1
                if re.search(r"[!@#$%^&*]{1,}",password):
                    count+=1                
print(count)         
if (count==5):
    print("password strength : strong") 
elif(3<=count<=4):
    print("password strength : moderate")
elif(1<=count<=2):
    print("password strength : weak")
          