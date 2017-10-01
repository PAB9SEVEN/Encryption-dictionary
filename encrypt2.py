message=raw_input("enter a message to be encrypted")
encrypted=""
for letter in message:
    if(letter==" "):
        encrypted+=" "
    elif(ord(letter)+5>ord('z')):
        encrypted+=chr(ord(letter)+5-26)
    else:

        encrypted+=chr(ord(letter)+5)

        
    
print encrypted
