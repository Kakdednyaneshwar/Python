# Check whether enterd number is palindrome..
x = int(input("Enter a number :"))
tem = x
rev_x = 0

while tem > 0:
    rev_x = rev_x * 10 + tem % 10
    tem = tem // 10
if x == rev_x:
    print("Palindrome Number")
else:
    print("Not Palindrome")