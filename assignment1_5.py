a = int(input("enter a number:"))
b = int(input("enter a number:"))
print("Before swapping:")
print("a =", a)
print("b =", b)
a = a ^ b
b = a ^ b#(a^b)^b
a = a ^ b#(a^b)^(a^b^b)
print("After swapping:")
print("a =", a)
print("b =", b)