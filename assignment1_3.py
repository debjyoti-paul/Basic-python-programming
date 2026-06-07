def circle(r):
    return 3.14*r*r
def rectangle(l,b):
    return l*b
def triangle(b,h):
    return 0.5*b*h
def square(a):
    return a*a
def parallelogram(b,h):
    return b*h
def cube(a):
    return a*a*a
def cuboid(l, b, h):
    return l*b*h
def sphere(r):
    return ((4/3)*3.14*r)
def cylinder(r, h):
    return 3.14*r*r*h
def cone(r,h):
    return ((1/3)*3.14*r*r*h)
ch=int(input("1:circle , 2:rectangle ,3:triangle , 4:square , 5:parallelogram , 6:cube ,7:cuboid ,8:sphere , 9:cylinder , 10:cone: "))
match ch:
    case 1:
        r=int(input("radius:"))
        print(circle(r))
    case 2:
        l=int(input("length:"))
        b=int(input("breath:"))
        print(rectangle(l,b))
    case 3:
        b=int(input("base:"))
        h=int(input("height:"))
        print(triangle(b,h))
    case 4:
        a=int(input("side:"))
        print(square(a))        
    case 5:
        b=int(input("base:"))
        h=int(input("height:"))
        print(parallelogram(b,h))    
    case 6: 
        a=int(input("side:"))
        print(cube(a))   
    case 7:
        l=int(input("length:"))
        b=int(input("breadth:"))
        h=int(input("height:"))
        print(cuboid(l,b,h))
    case 8:
        r=int(input("radius:"))
        print(sphere(r))
    case 9:
        r=int(input("radius:"))
        h=int(input("height:"))
        print(cylinder(r,h))
    case 10:
        r=int(input("radius:"))
        h=int(input("height:"))
        print(cone(r,h))