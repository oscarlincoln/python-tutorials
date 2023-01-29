# write a program to find the largest number on the list
# using for loop
oscar =[1,2,3,4,5,6,3,]
max = oscar[0]
for item in oscar:
    if item > max:
        max = item
print(max)
