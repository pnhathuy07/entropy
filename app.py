from functions import inp

from encryption import encode, decode
from destroy import destroy

selection = inp('Do you want to encode/decode the file or destroy the file completely?', '', '', 'Encode', 'Decode', 'Destroy').upper()
if selection == 'A': encode()
elif selection == 'B': decode()
elif selection == 'C': destroy()
