#Check if person is eligible to vote (check age )

age = int(input("Enter your age :"))

if age >= 18 and age <100:
    print("Eligible to vote")
else:
    print("You are not eligible to vote")


#WAP to check either person can vote and display as 'hello <name of person >,'you are 
#<eligiblw/not eligiblw to vote

def person(age,name):
    if age>=18 and age <100:
        print(f'Hello {name} ,you are eligible to vote')
    else:
        print(f"Hello {name}, you are not eligible to vote")
person(age = int(input("Enter Your age:")),name = input("Enter your name:"))
