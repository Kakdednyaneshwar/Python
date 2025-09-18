#write a program to Vowel or Not
s = input("Enter a alphabate :")

if len(s) > 1 or len(s) == 0:
    print("Enter a single Alphabat")
else:
    if s in 'AEIOUaeiou':  #in - It is a membership operator
        print("It is vowel")
    else:
        print("Not a vowel")


#Write a function to count and return the number of vowels in a string.. 
def vowels(s):
    count = 0
    for i in s:
        if i in 'AEIOUaeiou':
            count += 1 
    return count  
s = input("Enter some text :")
print(f'Number of vowels in given string ids {vowels(s)}')

