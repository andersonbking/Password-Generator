import random

print('Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^*().,?0123456789'

number = int(input('Amount of passwords to generate: '))
length = int(input('Input password length: '))

print('\nHere are your passwords:')

for _ in range(number):
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    print(password)
