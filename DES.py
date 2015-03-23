from Crypto.Cipher import DES, AES
from entropy import entropy

key="key12345"
text="secret12secret12secret12secret12"
des = DES.new(key, DES.MODE_CBC, "00000000")
des2 = DES.new(key, DES.MODE_ECB)
cipher = des.encrypt(text)
cipher2 = des2.encrypt(text)

print(cipher)
print(entropy(cipher))
print(cipher2)
print(entropy(cipher2))

keyaes="1234567890123456"
aes = AES.new(keyaes,AES.MODE_CBC,"0000000000000000")
encrypted = aes.encrypt(text)
aes2 = AES.new(keyaes,AES.MODE_ECB)
encrypted2 = aes2.encrypt(text)

print(encrypted)
print(entropy(encrypted))
print(encrypted2)
print(entropy(encrypted2))
