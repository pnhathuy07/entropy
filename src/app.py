from functions import inp
from encryption import encrypt, decrypt
from destroy import destroy

selection = inp('Do you want to encrypt/decrypt the file or destroy the file completely?',
                'Encrypt', 'Decrypt', 'Destroy')

if selection == 'A':
    encrypt()
elif selection == 'B':
    decrypt()
elif selection == 'C':
    destroy()
