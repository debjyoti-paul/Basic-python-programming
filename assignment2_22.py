# Write a Python program to find the longest substring in a string without repeating characters.
user=input("enter a word: ")
length=len(user)
pali=[]
max_len=0
for i in range(length):
    for j in range(i, length):
        user_p = user[i:j+1]
        flag = True
        for k in range(len(user_p)):
            if user_p[k] in user_p[k+1:]:
                flag = False
                break
        if flag:
            if len(user_p) > max_len:
                max_len = len(user_p)
                pali = [user_p]
            elif len(user_p) == max_len:
                pali.append(user_p)

print("Length:", max_len)
print("Longest substrings:", pali)