# for i in range(2,11,2):
#     print(i,end=" ")

#for i in range(1,11):
#   if(i%2==0):
#       print(i,end=" ")

# i=1
# while(i<11):
#     if i%2==0:
#         print(i,end=" ")
#     i+=1

# n= int(input("Enter n: "))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)

# Pattern 1
# * * * 
# * * * 
# * * * 

# for i in range(3):
#         print("*"*3, end="\n")


# Pattern 2
# * 
# * * 
# * * * 
# * * * * 
# n=int(input("Enter : "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print('*', end=" ")
#     print()

# n=int(input("Enter : "))
# for i in range(1,n+1):
#         print("* "*i,end="\n")

#Pattern 3

# * * * * * 
# * * * * 
# * * * 
# * * 
# *

# for i in range(5):
#     for j in range(5,i,-1):
#         print("*", end=" ")
#     print()

# for i in range(5,0,-1):
#     print("*"*i,end="\n")


# Pattern 4:
#           * 
#         * * * 
#       * * * * * 
#     * * * * * * * 

# for i in range(5):
#     for j in range(5,i,-1):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     for j in range(i-1):
#         print("*", end=" ")
#     print()

# n=int(input("Enter : "))
# for i in range (n):
#     print(" "*(n-i-1),end=" ")
#     print("*"*(2*i+1))

#Pattern 5:
# Inverted pyramid
# *********
#  *******
#   *****
#    ***
#     *

# n=int(input("Enter number :"))
# for i in range (n,-1,-1):
#     print(" "*(n-i),end=" ")
#     print("*"*(2*i-1))

# Pattern 6: Hollow Square
# *****
# *   *
# *   *
# *   *
# *****
# n=int(input("Enter number :"))

# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end =" ")
#     print()

#Pattern 7 : Diamond
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

# n=int(input("Enter : "))
# for i in range (n):
#     print(" "*(n-i-1),end=" ")
#     print("*"*(2*i+1))
# for i in range (n-1,-1,-1):
#     print(" "*(n-i),end=" ")
#     print("*"*(2*i-1))

# Pattern 8 :ButterFly 
# *      *
# **    **
# ***  ***
# ********
# ***  ***
# **    **
# *      *

# n = int(input("Enter the number of rows: "))

# for i in range(1, n + 1):
#     print("*" * i, end="")
#     print(" " * (2 * (n - i)), end="")
#     print("*" * i)


# for i in range(n - 1, 0, -1):
#     print("*" * i, end="")
#     print(" " * (2 * (n - i)), end="")
#     print("*" * i)

# Pattern 9:
# A 
# A B 
# A B C 
# A B C D 
# A B C D E 

# n=int(input("Enter : "))
# for i in range(n):
#     for j in range(i+1):
#         print(chr(ord('A')+j), end=" ")
#     print()

#Right angled triangle
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
#Inverted Right angled triangle
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()  