#Write a program to find the leap year

y = int(input("Enter year in format yyyy:"))

if y%100 == 0 and y%400 == 0:
    print("Leap year")
elif y%100 != 0 and y%4 == 0:
    print("Leap year")
else:
    print("Not a leap year")