import random
password = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$&"
length_password = int(input("Enter password length: "))
a = "".join(random.sample(password,length_password))
print(f"Your password is {a}")