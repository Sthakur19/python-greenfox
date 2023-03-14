n = int(input("Please enter the number here :"))

list = []

for i in range(1, n+1):
    num = int(input("please enter numnber here"))
    list.append(num)
    
avg=sum(list) / n
print("Aveage =", avg)

