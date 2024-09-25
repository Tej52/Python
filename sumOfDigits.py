num = str(input("Enter a number : "))

sum = 0

# for i in range(0,len(num),1):

for i in range(len(num)):
    sum += int(num[i])
else:
    print(sum)