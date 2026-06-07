#bakita khatay
n=[20,23,25,24,56,78,99]
def is_even(i):
    return i%2==0
l1=[is_even(i) for i in n]
print(l1)
l2=[x for x in n if is_even(x)]
print(l2)
#why we are converting the result in list? because object is created otherwise(hopefully lazy evalution)
n_f=filter(is_even,n)
#print(n_f) will not work se why this will also happen in map and lambda
print(list(n_f))

#list given , output-> sum of square of even numbers , use only filter and map

l=[2,3,4,5,6,7,8,9,10]

def sqr(x):
    return x*x
def is_even(x):
    return x%2==0

even= filter(is_even,l)
squares=map(sqr,even)#only object generate 
res=sum(squares)#
print(res)
# print(even)   what will these give?

#using 1 line of code
res1=sum(map(sqr,filter(is_even, l)))
#using lambda , map , filter
print(res1)
evens=filter(lambda x: x%2==0 , l)#is_even er jaygay eta lekha holo
sqrs=map(lambda x:x**2 , evens)
result=sum(sqrs)
print(result)

#above do in one code
l2=[7,8,6,34]
result=sum(map(lambda x:x**2 ,filter(lambda x: x%2==0 , l2)))
print(result)

#we can apply lambda , filter , map  in any type of iterables(list , dict etc.)

employees=[
{"name":"amit", "salary":45000, "dept":"IT"},
{"name":"anit", "salary":75000, "dept":"HR"},
{"name":"sara", "salary":60000, "dept":"IT"},
{"name":"david", "salary":45000, "dept":"finance"},
{"name":"john", "salary":50000, "dept":"IT"}
]

#filter the IT department using lambda and without lambda
it_employee=filter(lambda x :x ["dept"]=="IT", employees) 
#print(list(it_employee))  #eii gulo likle total bonus 0 asche
#it emplou=yee will get 10% bonus:
#bonus=map(lambda x: x["salary"]*.10 , it_employee)
#print(list(bonus)) # eii gulo likle total bonus 0 asche
#sum of bonus
#total=sum(bonus)
#print(total)
#find the name of employees whose bonus is greater than 5000
bonus_5000=filter(lambda x: x["salary"]*.10>=50000 , it_employee)#do not use print method in between this
name=list(map(lambda emp:emp["name"] , bonus_5000))

print(name)



#from disha

emp = [{"name":"amit","salary":70000,"dept":"IT"},
    {"name":"anit","salary":75000,"dept":"HR"},
    {"name":"sara","salary":60000,"dept":"IT"},
    {"name":"david","salary":45000,"dept":"FINANCE"},
    {"name":"john","salary":50000,"dept":"IT" },]

it_emp=filter(lambda x : x["dept"]=="IT",emp)
#print(list(it_emp))      
bonus=map(lambda x:x["salary"]*.10,it_emp)
#print(list(bonus))
#total=sum(bonus)
#print(total)
bonp=filter(lambda x : x>5000 ,bonus )
print(list(bonp))


