#Check whether string is palindrome..
s = input("Enter some text :")

rev_s = s[::-1]

if s.upper() == rev_s.upper():
    print("Palindrome")
else:
    print("Not Palindrome")


#Without slicing
s = input("Enter some String :")
rev_s = "" 
for c in s:
    rev_s = c + rev_s
    print(rev_s)
if s.upper() == rev_s.upper():
    print("Palindrome")
else:
    print("Not Palindrome")
