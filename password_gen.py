import string
import random

def password_generator(length,number,symbols):
    
    chars = string.ascii_letters

    #checks if numebrs are included
    if number:
        chars = chars + string.digits
    
    #checks if symbols are included
    if symbols:
        chars = chars + string.punctuation
    
    #main genertor that gives back a password, with a specified lenght
    generator = random.choices(chars, k=length)
    
    return "".join(generator)

if __name__ == '__main__':
    print(password_generator(True,True,1))
    
    
    

