list = [11,22,33,44,55]

for i in range(0,len(list)):
    print(list[i])

#for each look
print("-----")
for val in list:
    print(val)

print("------")
for ix, val in enumerate(list):
    print("list[" + str(ix) + "] = " + str(val))

print("----")

min = list[0]
for val in list:
    if min>val:
       min = val
print("Min valur is : " + str(min))

max = list[0]
for ix, val in enumerate(list):
    if max<val:
        max=val
print("Max val is : " + str(max) + " at index of " + str(ix)) 