n = int(input())

for i in range(n):
    if i == 0 or i == n:
        print("* "*n)
    else:
        print("* "* i + "  " *(n-i)+ "*")