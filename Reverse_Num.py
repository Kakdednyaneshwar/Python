#Program to reverse a number
x = int(input("Enter a number :"))
rev_x = 0
while x > 0:
    rev_x = rev_x*10 + x%10 
    x = x//10
print(rev_x)



