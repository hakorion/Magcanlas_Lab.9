rows = int(input("Enter the number of rows:"))
num = 1
for i in range(1, rows + 1):
    print(*range(num, num + i))
    num+= i 