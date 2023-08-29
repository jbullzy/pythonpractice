# Password Generator

import random

password_length = 10

characters = ''.join(chr(i) for i in range(128))

characterlist = list(characters)

# print(characters)
# print(characterlist)

password = ''.join(random.choice(characterlist) for i in range(password_length))
print(password)