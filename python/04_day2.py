#list
#List is a built-in data structure in python which is used to store multiple items in a single variable.
#List is mutable, meaning we can change its content without changing its identity.
#List is ordered, meaning the items have a defined order, and that order will not change.
#List allows duplicate members.


# st="suksham"
# # st[0]="x"
# lst=list(st)
# print(lst[0])
# lst[0]="x"
# print(lst)

#list Slicing:
# list1=["20",20,1,22,33,88]
# print(list1[4:2:1])  # prints elements from index 4 to 2 with step 1
# print(list1[1:4])   # prints elements from the beginning to index 2
# print(list1[::])   # prints elements from index 1 to the end
# print(list1[1:len(list1)])    # prints all elements

# st="arjun"
# print(st[::2])  # prints every second character starting from index 0
# print(st[2:1:1])
# print(st[::-1])  # prints the string in reverse order

#List Methods:
list2=[2,1,4,6]
#1. append(): Adds an element at the end of the list
list2.append(8)
print(list2)
#2. extend(): Adds all elements of a list to another list
list2.extend([9,10])
print(list2)
#3. insert(): Adds an element at the specified position
#4. remove(): Removes the first item with the specified value
#5. pop(): Removes the element at the specified position
#6. clear(): Removes all the elements from the list
#7. index(): Returns the index of the first element with the specified value
#8. count(): Returns the number of elements with the specified value
#9. sort(): Sorts the list
list2.sort()
print("Sorted Array :",list2)
#10. reverse(): Reverses the order of the list
#11. copy(): Returns a copy of the list
#12. len(): Returns the number of elements in the list

print(max(list2))  # returns the maximum value in the list
print(min(list2))  # returns the minimum value in the list

list=["banana","apple","grapes","orange"]
list.sort(reverse=True)  # sorts the list in reverse order
print(list)
list.reverse()  # reverses the order of the list
print(list)
print()
list4=[1,2,3,4,5]
list4.insert(2,10)  # inserts 10 at index 2
print(list4)

print()
print(list4)
list4.remove(2)  # removes the first occurrence of 2
print(list4)
list4.pop(3)  # removes the element at index 3(default is -1, which removes the last element)
print(list4)


