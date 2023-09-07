#user enter the year
year = int(input("Enter year: "))

#Leap year check
if year % 4 == 0 and year % 100 != 0:
  print(year, "is a Leap year")
elif year % 100 == 0:
  print (year, "is not a Leap year")
elif year % 400 ==0:
  print(year, "is a Leap year")
else:
  print(year, "is not a Leap year")