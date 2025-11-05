steps = int(input("Enter the number of steps for the pyramid:"))
# Outer loop: controls the number of rows (from 1 to 'steps')
for i in range(1, steps + 1):
 # Inner loop: prints the multiplication results for each row
 for j in range(1, i + 1):
  print(i * j, end=" ") # Print the product of i and j on the same
print()
