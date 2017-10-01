encrypt={'a':'e','b':'f','c':'g','d':'h','e':'i','f':'j','g':'k','h':'l','i':'m','j':'n','k':'o','l':'p','m':'q','n':'r','o':'s','p':'t','q':'u','r':'v','s':'w','t':'x','u':'y','v':'z','w':'a','x':'b','y':'c','z':'d'}
message = raw_input('enter the message').lower()
encrypted = ""
for letter in message:
    if letter.lower() in encrypt:
        encrypted+=encrypt[letter]
    else:
        encrypted+=letter

print encrypted

