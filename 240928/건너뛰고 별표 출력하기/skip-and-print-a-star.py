n = int(input())

for i in range(1, n):
    if i != 1:
        print()
    
    for k in range(i):
        print("*", end = "")
    print()

for i in range(n):

    print()
    for j in range(n-i):
        print("*", end ="")
    print()