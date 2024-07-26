A = int(input("Enter the value of A: "))
B = int(input("Enter the value of B: "))
C = int(input("Enter the value of C: "))
if (A >= B) and (A >= C):
  largest = A
elif (B >= A) and (B >= C):
  largest = B
elif (C >= A) and (C >= B):
  largest = C
print("The Largest Number is", largest)

