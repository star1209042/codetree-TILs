def print_num(n):
    if n == 0:
        return

    print_num(n-1)
    print(n, end = " ")

def print_num_rev(n):
    if n == 0:
        return
    print(n, end = " ")
    print_num_rev(n-1)



n = int(input())
print_num(n)
print()
print_num_rev(n)