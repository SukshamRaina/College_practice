#WAP if list contains palindrome of elements .

# l=list(map(str,input().split()))

# print(l[::-1])
# if(l[::-1]==l):
#     print("List is palindrome")
# else:
#     print("List is not palindrome")
    
# s="Mietclass"
# print(s)
# print(id(s))
# s=s.replace("Miet","MIET")
# print (s)
# print(id(s))

#Palindrome approach 2
# n=input("Enter a list elements: ")
# list=n.split(",")
# print(list)

# rev=list.copy()
# rev.reverse()

# if list==rev:
#     print("List is palindrome")
# else:
#     print("List is not palindrome")

#Wap to find max element of list

# l=list(map(int,input("Enter element: ").split()))
# max=l[0]
# for i in l:
#     if max<i:
#         max=i
# print (max)

#Wap to find max element of list

# l=list(map(int,input("Enter element: ").split()))
# cnt=0
# for i in l:
#     if i%2==0:
#         cnt+=1
# print (f'There are {cnt} even elements in the list.')

#WAP to find 2nd largest element of list
# l=list(map(int,input("Enter element: ").split()))
# flar=float('-inf')
# slar=float('-inf')
# for i in l:
#     if i>flar:
#         slar=flar
#         flar=i
#     elif i>slar and i<flar:
#         slar=i

# print ("Second Largest:",slar)

# l=list(map(int,input("Enter element: ").split()))
# l.sort(reverse=True)
# print("Second Largest:"l[1])

# a=[10,20,30,[20,30]]
# print("List before modifying:",a)
# a[0]=100
# a[3][0]=10
# print("List after modifying:",a)





