# WAP to find 2nd minimum element of list
# l=list(map(int,input("Enter element: ").split()))
# fmin=smin=float('inf')
# for i in l:
#     if i<fmin:
#         smin=fmin
#         fmin=i
#     elif i<smin and i>fmin:
#         smin=i

# print(smin)

#2 WAP to find sum of positive elements in list

# lst=list(map(int,input("Enter elements of list : ").split()))

# sum=0
# for i in lst:
#     if i>0:
#         sum+=i
# print("Sum:",sum)

#WAP to find missing element in list

# lst=list(map(int,input("Enter elements of list : ").split()))
# n=len(lst)+1
# total=(n*(n+1))//2
# s=sum(lst)
# print("Missing number: ",total-s)

# lst=list(map(int,input("Enter elements of list : ").split()))
# for i in range(max(lst),min(lst)-1,-1):
#     if i not in lst:
#         print("Missing number: ",i)
#         break
