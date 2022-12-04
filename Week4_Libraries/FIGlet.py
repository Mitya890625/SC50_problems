from pyfiglet import Figlet
import random
figlet = Figlet()
arr = figlet.getFonts()   
i = random.randint(0, 100)
figlet.setFont(font=arr[i])
print(figlet.renderText('Hello pisi'))