import secrets
import string
from random import shuffle

print("PassR")
while True:
  print("")
  print("1) Generate Random Password")
  print("2) Scramble Password")
  y = input("Select your Option: ")
  print("")
  if y == "1":
  
  # define the alphabet
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
  
    alphabet = letters + digits + special_chars

  # fix password length
    pwd_length = 12
  
  # generate a password string
    pwd = ''
    for i in range(pwd_length):
      pwd += ''.join(secrets.choice(alphabet))
  
    print(pwd)
  
  # generate password meeting constraints
    while True:
      pwd = ''
      for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))
  
      if (any(char in special_chars for char in pwd) and 
          sum(char in digits for char in pwd)>=2):
            break
    print(pwd)
    
  if y == "2":
    word = input("Password to Scramble: ")
    import random
    w = word
    l = list(w)
    random.shuffle(l)
    y = ''.join(l)
    print("Scrambled Password: ", y)