# Write a program to generate random password which shall
# combine upper case alphabets, lower case alphabets, digits and
# special characters. You shall prepare separate dictionary items
# called “lower”, “upper”, “digits”, “special” and values shall be
# stored accordingly. From this array, based on the user’s choice
# random password shall be generated. You shall make sure that
# atleast one character is selected from all specified choices. Use
# dictionary / list as applicable

import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
special = '!@#$%^&*()'

password = [random.choice(lower), random.choice(
    upper), random.choice(digits), random.choice(special)]

while len(password) < 15:
    choice = random.choice([lower, upper, digits, special])
    password.append(random.choice(choice))

password = ''.join(password)

print('Your Random Password is:', password)
