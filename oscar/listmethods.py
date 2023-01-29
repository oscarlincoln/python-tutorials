numbers = [1,2,3,4,5,6,5,4]

# adding an item to the list 
numbers.append(20)
print(numbers)

# inserting an item at any position in the list 
numbers.insert(0,14)
print(numbers)

# removing an item  from the list
numbers.remove(5)
print(numbers)

# removing last item on the list
numbers.pop()
print(numbers)

# checking for the index of an item in the list 
print(numbers.index(1))

# checking for the existence of an item in the list 
print(50 in numbers) #it will return a boolean
print(5 in numbers)

# counting the occurance of an item in the list 
print(numbers.count(4))

# sorting the list 
numbers.sort()
print(numbers)

# sorting in descending order
numbers.sort()
numbers.reverse()
print(numbers)

# making a copy of the list 
number = numbers.copy()
numbers.append(2)
print(numbers)
print(number)