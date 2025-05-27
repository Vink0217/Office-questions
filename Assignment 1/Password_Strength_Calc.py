'''
Q6) Password Strength Checker 
Check if a password is strong (has uppercase, lowercase, digits, and special characters). 
'''
password = str(input("Enter Password: "))
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','_','-','+','=','<','>']
Uppercase = any(i.isupper() for i in password)
digits = any(i in numbers for i in password)
symbols = any(i in symbols for i in password)

if Uppercase and digits and symbols:
    print("Very Strong Password")
elif Uppercase and digits:
    print("Slightly Strong Password")
elif Uppercase and symbols:
    print("Strong Password")
elif symbols and digits:
    print("Slightly Strong Password")
else:
    print("Weak")
