import random
import string

def createPass(lth):

    chara = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(chara) for _ in range(lth))
    
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

def getInput():
    ch = str(input("Do you want to create password ?(yes/no) : "))

    if(ch=="yes"):
        lth = int(input("Enter the length of the password: "))
        print("Generated Password:", createPass(lth))
        getInput()
    elif(ch=="no"):
       print("Thank you for using this program.")
    else:
       print("Invalid Input")
       getInput()

getInput()



