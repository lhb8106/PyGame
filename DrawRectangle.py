n = int(input("enter number of o: "))
for i in range(n):
    for j in range(n*2):
        if i in (0, n-1) or j in (0, n*2-1):
            print('o', end='')
        else:
            print(' ', end='')
    print()
