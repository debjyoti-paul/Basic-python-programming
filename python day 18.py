class Calculator:
    def multiply(self,*args):
        result=1
        for num in args:
            result *=num
        return result
#create object
calc=Calculator()

#using different arguments
print(calc.multiply())
print(calc.multiply(2))
print(calc.multiply(4,5))
print(calc.multiply(4,5,6,7))

#handling polymorphism with calss(duck typing in run timming)
class Circle:
    def area(self):
        x=int(input("enter the value of radius"))
        print("Area=pi X r X r is",x*x*3.14)

class Square:
    def area(self):
        x=int(input("enter the value of the side"))
        print("Area=side X side is",x*x)

def show_area(shape):
    shape.area()   

c= Circle()
s= Square()
show_area(c)
show_area(s)


#operator overloading
class Number:
    def __init__(self,value):
        self.value=value
    #overloading +operator
    def __add__(self,other):
        return Number(self.value + other.value)
    def __str__(self):
        return str(self.value)
n1 = Number(10)
n2= Number(20)
n3=Number(30)
result=n1+n2+n3
print(result)
#create a class Student--with 2 attributes: name and marks. 
# Overload the greater than operation to compare marks of 2 students
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __gt__(self,other):
        if( self.marks > other.marks):
            return self.name
        else:
            return other.name
        
name1=Student("a",90)
name2=Student("b",85)
result=(name1>name2)
print(result)
#create a class-vector with 2 attributes: x and y. 
# Overload plus operation to add 2 vectors. Output should be in form of tuple(x,y)
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        #return Vector((self.x + other.x),(self.y + other.y))      vector object
        return Vector((self.x + other.x),(self.y + other.y))  # tuple
    def __str__(self):
        return f"({self.x},{self.y})"

n1=Vector(10,5)
n2=Vector(5,4)
n3=Vector(10,10)
result=n1+n2
print(result)
result2= n1+n2+n3
print(result2)

#define a class matrix, to represent a matrix using 2 d list,your calss should have
#1.a construstor
#2.2 operati9ons overload + - 
#3.implement the method to look like it a poper matrix
'''class Matrix:
    def __init__(self,matrix):
        self.matrix=matrix
    def __add__(self,other):
         n=0
         m=0
         for rows in other.matrix:
              n+=1
         for cols in other.matrix[0]:
              m+=1
         matr3=[]
         for rows in range(n):
              rowsum=[]
              for cols in range(m):
                   rowsum[cols]=self.matrix[cols]+other.matrix[cols]
              matr3.append(rowsum)
         return matr3
    def __sub__(self,other,n,m):
         n=0
         m=0
         for rows in other.matrix:
              n+=1
         for cols in other.matrix[0]:
              m+=1
         matr3=[]
         for rows in range(n):
              rowsum=[]
              for cols in range(m):
                   rowsum[cols]=self.matrix[cols]-other.matrix[cols]
              matr3.append(rowsum)
         return matr3


matr1=Matrix([[1,2],[3,4],[5,6]])
matr2=Matrix([[1,2],[3,4],[5,6]])
res=matr1+matr2
print(res)
res=matr1-matr2
print(res)'''


#file handling
'''import os
print(os.getcwd())
fp = open('sample.txt','w')
fp.write('we are learning python')
fp.close()
print(os.listdir('C:/Microsoft VS Code'))'''


#define a class matrix, to represent a matrix using 2 d list,your calss should have
#1.a construstor
#2.2 operati9ons overload + - 
#3.implement the method to look like it a poper matrix
class Matrix:
    def __init__(self, data):
        # Constructor: accepts a 2D list
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __add__(self, other):
        # Overload + operator
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have same dimensions for addition")

        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)

        return Matrix(result)

    def __sub__(self, other):
        # Overload - operator
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have same dimensions for subtraction")

        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] - other.data[i][j])
            result.append(row)

        return Matrix(result)

    def __str__(self):
        # Proper matrix-like display
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str.strip()


# Example usage
m1 = Matrix([[1, 2, 3],[4, 5, 6]])

m2 = Matrix([[7, 8, 9],[1, 2, 3]])

print("Matrix 1:")
print(m1)

print("\nMatrix 2:")
print(m2)

print("\nAddition:")
print(m1 + m2)

print("\nSubtraction:")
print(m1 - m2 )



import os
print(os.getcwd())# file handiling    
#fp=open('\\file name','\\mode of creating file')
fp=open('sample.txt','w')#save in current directory    here under C:\Users\SHRIBASH PAUL
fp.write("we are learning file handeling")
fp.close()
fp=open('sample.txt','r')#save in current directory    here under C:\Users\SHRIBASH PAUL
print(fp.read())
fp.close()
print(os.listdir('C:/Users/SHRIBASH PAUL/Downloads/programcheck'))
print(os.path.isfile('C:/Users/SHRIBASH PAUL/sample.txt'))#relative path and absolute path?????????????????
fp=open('C:/Users/SHRIBASH PAUL/Downloads/programcheck/diya2.txt','w')
fp.write('hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
fp.close()
fp=open('C:/Users/SHRIBASH PAUL/Downloads/programcheck/disha2.txt','w')
fp.write('hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
fp.close()
fp=open('C:/Users/SHRIBASH PAUL/Downloads/programcheck/diya2.txt','r')
print(fp.read())
fp.close()
#to read a fille we n  from disha   ...it is used to read the  , use of r+ , and w+, diff between r+ and w+
#

#, use of, a+, r+ , and w+, diff between r+ and w+ , try it at home

#read line , read lines  alsoooooo + dishar khataaa+ amar khata  + file with multiple lines





