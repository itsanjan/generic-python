# This program gives examples about various list operations

# Suntax: list[start: end: step]

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#index =  0  1  2  3  4  5  6  7  8
#        -9 -8 -7 -6 -5 -4 -3 -2 -1

#List slicing
print('Original List:', myList)
print('First Element:',myList[0])
print('Second Element:',myList[1])
print('Elements from 0th Index to 4th Index:',myList[0:5])
print('Element at -7 or 3rd element',myList[-7])

#To append an element to a List
myList.append(10)
print('Append: {value} of lenght {lenght}'.format(value=myList, lenght=len(myList)))

#To sort the List
#print('Index of element \'6\':'myList.index(6)) #returns element '6'

#To sort the List
myList.sort()

#To remove an element from list by name
print('Poped Element:',myList.pop())

#To remobe a particular element in the list by name
myList.remove(6)
# print('Poped Element \''\':',myList')
print('removed 6',myList)
#To insert an element at a specificed Index
myList.insert(5, 6)
print('inserting',myList)

print('No of occurences of 1',myList.count(1))

#To extend a list that is insert multiple elements at once at the end of the List
myList.extend([11,0])
print('Extending list:',myList)

#To reverse a List
myList.reverse()
print('Reversed list',myList)
