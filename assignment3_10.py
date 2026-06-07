#Write a recursive function to generate all subsets of a set (power set)
def subsets(s, current=[]):
    if len(s) == 0:
        print(current)
        return
    # Exclude first element
    subsets(s[1:], current)
    # Include first element
    subsets(s[1:], current + [s[0]])
lst=[]
n=int(input("enter the no. of elements:"))
for i in range(n):
    num=int(input("enter number:"))
    lst.append(num)
subsets(lst)