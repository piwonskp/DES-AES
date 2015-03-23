from Crypto.Cipher import DES, AES

key="key12345"
text="secret12secret12secret12secret12"
IV="00000000"
n=8
des = DES.new(key, DES.MODE_ECB)

for i in range(0, len(text), n):
    temp=''
    for j in range(i,len(text[:i+n])):
        temp+= chr(ord(text[j])^ord(IV[j-i]))
    IV = des.encrypt(temp)
    print (IV)

#print (DES.new(key, DES.MODE_CBC, "00000000").encrypt(text))

