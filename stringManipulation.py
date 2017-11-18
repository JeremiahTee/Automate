# raw string, ignores all escape characters
print(r'That is Carol\'s cat.')
print()

# multi-lines
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion. 

Sincerely,
Bob''')


# multi-line commenting
"""This is a test Python program
Written by Jeremiah Tiongson"""

# validating output
while True:
    print('Enter your age: ')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for you age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():  #isalnum() for alphanumeric
        break
    print('Passwords can only have letters and numbers')