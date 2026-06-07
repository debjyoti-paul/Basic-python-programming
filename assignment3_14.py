#Write a recursive function to flatten a nested list (e.g., [1, [2, [3, 4], 5]] → [1, 2, 3, 4, 5]).
def flatten(lst):
    result = []
    for item in lst:
        if type(item) == list:
            result.extend(flatten(item))#for list extend
        else:
            result.append(item)#for adding item
    return result
l1=[1, [2, [3, 4], 5]]
print(flatten(l1))