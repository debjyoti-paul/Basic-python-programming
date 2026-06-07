a=int(input("enter the length of 1st side:"))
b=int(input("enter the length of 2nd side:"))
c=int(input("enter the length of 3rd side:"))
if(a+b>=c and b+c>=a and c+a>=b ):
    print("valid triangle.")
    if(a==b==c):
        print("type: equilateral triangle")
    elif(a==b or b==c or c==a):
        print("type: isosceles triangle")
    else:
        print("type: scalene triangle")    
else:
    print("invalid triangle.")        