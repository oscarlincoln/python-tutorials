# write a program to remove the duplicates in a list 
numbers = [1,2,3,3,4,5,5,5]
item = []
for number in numbers:
    if number not in item:
        item.append(number)
print(item)