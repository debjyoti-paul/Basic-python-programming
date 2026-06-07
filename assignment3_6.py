#Write a recursive function to convert a decimal number to binary.  
def decimal(num):
    num2=num//2
    if num==0:
        return ""
    else:
        return decimal(num2)+str(num%2)
num=int(input("Enter a number: "))
result=decimal(num)
if result == "":
    result = "0"
print(result)