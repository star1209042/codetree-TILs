a = []
mul_3 = True
for i in range(5):
    a.append(int(input()))
    if a[i] % 3 !=0:
        mul_3 = False

if mul_3 == True:
    print(1)
else:
    print(0)