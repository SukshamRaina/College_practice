# n=int(input())
# l=len(str(n))
# print(l)
# temp=n
# sum=0
# while temp>0:
#     sum+=(temp%10)**l
#     temp//=10
# # if sum==n:
# #     print("Armstrong number")
# # else:
# #     print("Not Armstrong number")
# print("Armstrong Number") if sum==n else print("Not Armstrong")


# str="abracadabra"
# lst=list(str)
# print(lst)
# print(type(lst))
# print(str.index("b"))

#List comprehension
#a shorthand to create list in single line is called as List comprehension

# lst=[x**2 for x in range(1,11)]
# print(lst)
# evenlst=[x for x in range(1,11) if x%2==0]
# print(evenlst)
# oddlst=[x for x in range(1,11) if x%2!=0]
# print(oddlst)

# a=[]
# for i in range(1,6):
#     a.append(i*2)
# print(a)
# b=[i*2 for i in range(1,6)]
# print(b)

# lst=[x for x in range(1,50) if x%7==0]
# print(lst)
# a=[]
# for num in range(2,9):
#     if num<5:
#         a.append(num)
#     else:
#         a.append(num*2)
# print(a)
# a=[num if num<5 else num*2 for num in range(2,9)]
# print(a)

# lst=[35,63,22,15,9,88,77]
# lst2=[x for x in lst if x%3==0]
# print(lst2)

# list=[("a",11),("b",12),("c",13)]
# NL=[n*3 for (x,n) in list if x=='b' or x=='c']
# print(NL) 
lst=[x**y for x in [10,5,2] for y in [2,3,4]]
print(lst)