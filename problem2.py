day_value = int(input("Enter the Day Number: "))

if day_value == 0:
  print("Day is Sunday")
elif day_value == 1:
  print("Day is Monday")
elif day_value == 2:
  print("Day is Tuesday")
elif day_value == 3:
  print("Day is Wednesday")
elif day_value == 4:
  print("Day is Thursday")
elif day_value == 5:
  print("Day is Friday")
elif day_value == 6:
  print("Day is Saturday")
elif day_value >= 7:
  print("Enter a valid number")
elif day_value < 0:
  print("Enter a valid number")

