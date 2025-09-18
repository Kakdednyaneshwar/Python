#check whether entered number is prime or not
#prime number- number divisible by 1 and itself

x = int(input("Enter a number :"))
fl = False   #Use of  boolean variable
for i in range(2,x,1):
    if x%i == 0:
        fl = True
        break  #Break - Statement which stop the loop
if fl == True:
   print("Not prime number")
else:
   print("Prime Number")

# WAP to print Prime Number between 1 and 50..

