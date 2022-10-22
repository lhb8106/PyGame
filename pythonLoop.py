count = 1
num = 0

for i in range(10, 54):
    if(i <= num):
        continue
    for num in range(i, i+count):
        print(num, end=' ')
    count += 1
    print()
