# Write a Python program to find two numbers in a list that add up to a given target value (Two Sum problem). 
l1=[2,11,7,15]
target=9
for i in range(len(l1)):
    for j in range(i + 1, len(l1)):
        if l1[i] + l1[j] == target:
            print("Indices:", i, j)
            print("Numbers:", l1[i], l1[j])
            break