import random
VOWELS=['a','e','i','o','u']
message=raw_input('enter a message')
new = ""
for letter in message:
    if letter not in VOWELS:
        new += letter

    else:
        new += random.choice(VOWELS)

print new
