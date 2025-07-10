import random,string

def generator(length):
    if length<4:
        raise ValueError("password should be more the 4 character...")
    
    uppercase=string.ascii_uppercase
    lowercase=string.ascii_lowercase
    digit=string.digits
    spl_char="!@#$%^&*()'/?><,.|\[]"


    password=[random.choice(uppercase),
              random.choice(lowercase),
              random.choice(digit),
              random.choice(spl_char)]

    all_char=uppercase+lowercase+digit+spl_char

    password +=random.choices(all_char,k=length-4)

    random.shuffle(password)

    return ''.join(password)

try:
    length=int(input("enter the length of password:"))
    password=generator(length)
    print("generated password:",password)

except ValueError as e:
    print(e)






