rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

arr = []
for i in range(rows):
    row = list(map(int, input(f"Enter {cols} numbers for row {i+1}: ").split()))
    arr.append(row)
odd = []
even = []

for i in range(rows):
    for j in range(cols):
        if arr[i][j] % 2 == 0:
            even.append(arr[i][j])
        else:
            odd.append(arr[i][j])

print("Odd elements =", odd)
print("Even elements =", even)