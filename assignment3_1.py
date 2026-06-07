#Write a recursive function to check whether a string is a palindrome.  
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])
string = input("Enter a string: ")
if is_palindrome(string):
    print("Palindrome")
else:
    print("Not Palindrome")