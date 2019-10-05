n = input("enter input")
while (n != n[::-1]):
    rev = n[::-1]
    n = int(rev) + int(n)
    n= str(n)
print(n)

