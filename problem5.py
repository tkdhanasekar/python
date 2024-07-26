year = int(input("Enter the year: "))
age = (2024 - year)
if (age >= 80):
  print("You are a Super Senior")
elif (age >= 60) and (age < 80):
  print("You are a Senior")
elif (age >= 20) and (age < 60):
  print("You are Young")
elif (age >= 11) and (age <= 19):
  print("You are a Teen")
elif (age >= 0) and (age < 10):
  print("You are a Kid")

