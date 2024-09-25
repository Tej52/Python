num = str(input("Enter a number : "))
product = 1

for i in range(len(num)):
    product *= int(num[i])
else:
    print(product)