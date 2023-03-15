list = [1,2,3]

#assign item by index

list[0] = 6

print(list)

#swapping Value
tmp = list[1]
list[1] = list[2]
list[2]= tmp

print(list)

#another way to swap the itme

list[1], list[2] = list[2], list[1]

print(list)

#append Itme to the end

list.append(111)
list.append(222)
list.append(333)

print(list)

#remove item from end

list.pop()
print(list)

#inser item at index

list.insert(1,444)
print(list)

#remove item at index

del list[1]
print(list)

#list copy

list1 = list.copy()
print(list1)
list1.append(777)
print(list1)
print(list)