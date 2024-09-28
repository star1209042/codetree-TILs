n= int(input())

for i in range(n):
    print(" "*(n - (i + 1)),end="")
    print("*"*(2*i+1), end = "")
    print()
for i in range(n - 2, -1, -1):

    print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    print(" "*(i-1),end="")