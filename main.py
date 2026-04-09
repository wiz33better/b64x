#encode
#input 
string = input("Enter the string: ")
stringX =""
encoded = string.encode("utf-8")
for byte in encoded:
    stringX += format(byte,'08b')
    
b_string = stringX
while len(b_string)%6 != 0:
    b_string += "0"

chunks = []
decimals = []
for i in range(0, len(b_string), 6):
    chunk = b_string[i : i+6]
    chunks.append(chunk)
    decimal = int(chunk, 2)
    decimals.append(decimal)
base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

result = ""
for i in decimals:
        character = base64_chars[i]
        result += character
if len(encoded)%3 == 1:
     result += "=="
elif len(encoded)%3 == 2:
     result += "="
print(result)

