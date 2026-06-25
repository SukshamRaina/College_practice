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
# lst=[x**y for x in [10,5,2] for y in [2,3,4]]
# print(lst)

#Dictionary 
#these are used to store data values in key value pairs.
#1.unordered collection of data values
#2.Mutable
#3. they dont allow duplicates

# dict={
#     "name":"Ravi",
#     "name":"raj",
#     "cgpa":8.2,
#     "marks":88
#     }

# print(dict)


# print()
# for key,values in dict.items():
#     print(key,values)

# print()
# for key in dict.keys():
#     print(key)
# print()
# for val in dict.values():
#     print(val)
# nulldic={}
# nulldic["name"]="yaseen"
# print(nulldic)

student={
    "name":"Ravi",
    "age":20,
    "score":{
    "Eng":100,
    "math":99
    }
    }

# print(student["score"])
# print("Math",student["score"]["math"])

#Dictionary Methods
# #1. dict.keys() - returns a list of all the keys in the dictionary
# print("keys:", list(student.keys()))
# #2. dict.values() - returns a list of all the values in the dictionary
# print("values:", list(student.values()))
# #3. dict.items() - returns a list of all the key-value pairs in the dictionary
# print("items:", list(student.items()))
# #4. dict.get(key) - returns the value associated with the specified key
# print("get:", student.get("name"))
# #5. dict.update(other_dict) - updates the dictionary with key-value pairs from another dictionary
# student.update({"age":21})
# print("updated student:", student)
# #6. dict.pop(key) - removes the key-value pair with the specified key from the dictionary and returns the value
# removed_value = student.pop("age")
# print("removed value:", removed_value)
#7. dict.clear() - removes all key-value pairs from the dictionary
#8. dict.copy() - returns a shallow copy of the dictionary
#9. dict.fromkeys(seq, value) - creates a new dictionary with keys from the specified sequence and values set to the specified value
# new_dict = student.fromkeys(["name", "age"], "N/A")
# print("new dictionary:", new_dict)

# print("score keys:", list(student["score"].keys()))
# pairs=(list(student.items()))
# print(list(pairs[2][1].items())[0])
# print()

# print(student.get("name"))

# student.update({"city":"delhi","age":21})
# print(student)

#Set
#Set is an unordered collection of items. Items in a set are not in any specific order
#Set is mutable, which means we can add or remove items from it
#Set does not allow duplicate items
#Set is unordered, which means we cannot access items by index

#Values allowed:int,float,tuple,string,frozenset
#values not allowed: list,dict,set

#Set Method:
#1. set.add(item) - adds an item to the set
#2. set.remove(item) - removes an item from the set
#3. set.discard(item) - removes an item from the set if it exists
#4. set.pop() - removes and returns an arbitrary item from the set
#5. set.clear() - removes all items from the set
#6. set.copy() - returns a shallow copy of the set
#7. set.union(other_set) - returns a new set containing all items from both sets
#8. set.intersection(other_set) - returns a new set containing only items that are in both sets
#9. set.difference(other_set) - returns a new set containing items that are in the first set but not in the second set
#10. set.symmetric_difference(other_set) - returns a new set containing items that are in either set, but not both

# st=set({1,2,3,4})
# print(st)
# print(type(st))
# st=frozenset(st)
# print(st)
# print(type(st))

#Empty Set
# st2=set()
# print(st2)
# print(type(st2))

# set={1,2,3}
# set2={1,4,6}
# print(set.union(set2))
# print(set.intersection(set2))
# print(set.difference(set2))
# print(set.symmetric_difference(set2))
# set.add(5)
# print(set)
# set.remove(1)
# print(set)
# set.discard(2)
# print(set)
# set.pop()
# print(set)
# set.clear()
# print(set)

# s = input().strip()
# freq = {}
# for i in s:
#     freq[i] = freq.get(i, 0) + 1
# for i in sorted(freq):
#     print(i, freq[i])



