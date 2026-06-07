def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1, n2):
    if (n2==0):
        return print("the divisor can not be zero.")
    return n1/n2
def operate(func,n1,n2):
    return func(n1,n2)
operations={"add":add , "sub":sub, "mul":mul , "div":div}
n1=int(input("Enter 1st number:"))  
n2=int(input("Enter 2nd number:"))  
while(True):
    choice =(input("type add for addition  , sub for subtraction , mul for multiplication , div for division:  ")) 
    result=operate(operations[choice],n1 , n2)
    print(result)
    ques=input("for furthur operations type y otherwise n:")
    if(ques=='y'):
        continue
    else:
        break 