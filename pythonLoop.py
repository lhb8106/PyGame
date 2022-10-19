count = 1
num2 = 9

for num1 in range(10, 54):
    if(num1 <= num2):
        continue
    for num2 in range(num1, num1+count):
        print(num2, end=' ')
    count += 1
    print()
