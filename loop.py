rows = int(input("Enter the number of rows:"))
# First loop: prints the upper half of the diamond (increasing pattern)
for i in range(1, rows + 1):
 for j in range(i):
   print("*", end=" ") # Print stars on the same line separated by
 print() # Move to the next line after each row
# Second loop: prints the lower half of the diamond (decreasing pattern)
for i in range(rows - 1, 0, -1):
 for j in range(i):
    print("*", end=" ") # Print stars on the same line separated by
print()
