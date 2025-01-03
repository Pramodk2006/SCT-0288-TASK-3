import re
def checkstrength(password):
    length_score= len(password)>=8
    uppercase_score=bool(re.search(r'[A-Z]',password))
    lowercase_score=bool(re.search(r'[a-z]',password))
    numbers_score=bool(re.search(r'[0-9]',password))
    specialchar_score=bool(re.search(r'[!@#$%^&*()-+=:.,~<>?]',password))
    strength=length_score+uppercase_score+lowercase_score+numbers_score+specialchar_score
    if strength==5:
        return "strong password"
    elif strength>=3:
        return "moderate"
    else:
        return "weak password"
password=input("Enter the password")
f=checkstrength(password)
print(f)