import random
import string

def createPass(length):

    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

print('''

 /$$$$$$$                               /$$$$$$                                                     /$$                        
| $$__  $$                             /$$__  $$                                                   | $$                        
| $$  \ $$ /$$$$$$   /$$$$$$$ /$$$$$$$| $$  \__/  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$ 
| $$$$$$$/|____  $$ /$$_____//$$_____/| $$ /$$$$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$|____  $$|_  $$_/   /$$__  $$ /$$__  $$
| $$____/  /$$$$$$$|  $$$$$$|  $$$$$$ | $$|_  $$| $$$$$$$$| $$  \ $$| $$$$$$$$| $$  \__/ /$$$$$$$  | $$    | $$  \ $$| $$  \__/
| $$      /$$__  $$ \____  $$\____  $$| $$  \ $$| $$_____/| $$  | $$| $$_____/| $$      /$$__  $$  | $$ /$$| $$  | $$| $$      
| $$     |  $$$$$$$ /$$$$$$$//$$$$$$$/|  $$$$$$/|  $$$$$$$| $$  | $$|  $$$$$$$| $$     |  $$$$$$$  |  $$$$/|  $$$$$$/| $$      
|__/      \_______/|_______/|_______/  \______/  \_______/|__/  |__/ \_______/|__/      \_______/   \___/   \______/ |__/                                         
                                                                                                     by Siddhesh More.
      [ Github : https://github.com/Siddesh0002T ]
      [Instagram : https://www.instagram.com/Siddhesh0002t ]                                     
''')
length = int(input("Enter the length of the password: "))


print("Generated Password:", createPass(length))