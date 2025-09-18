#check whether enterd number is an armstrong number/not..
#Example - 1234 = 1**4+2**4+3**4+4**4     456 = 4**3+5**3+6**3..

x = input("Enter a number :")
p = len(x)  #Number of digit /length
x = int(x)  #Change datatype to int
temp = x    # Copy origanal number
res = 0

for i in range(p):
   #d = tem%10 #Get the last digit..
   #n = d**p  #Find power to number of digit..
   #res = res + n  #Add the result..
    res = res+((temp%10)**p)
    temp = temp//10  #reduce the number..
if x == res :
    print("Armstrong Number",x,res)
else:
    print("Not Armstrong Number",x,res)