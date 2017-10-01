message=raw_input('enter the message you want to encrypt').upper()
encrypted = ""
for letter in message:
    if letter == " ":
        encrypted+=" "
    elif ord(letter)+5 > ord('Z'):
        encrypted+=chr(ord(letter)+5-26)
    else:
        encrypted+=chr(ord(letter)+5)
print encrypted
    
#in case u want to decrypt the mesage we can actually just swith the signs thats it     
