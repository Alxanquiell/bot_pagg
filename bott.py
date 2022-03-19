import os

os.system("pip install bs4;pip install colorama;pip install pyfiglet;pip install termcolor")



import requests
from bs4 import BeautifulSoup
import random

import colorama
from termcolor import colored
from pyfiglet import Figlet
from colorama import Fore
from threading import Thread
colorama.init()




nombres="""
Guadalupe,
Reinalda,
Alberta,
Paula,
Paola,
Juana,
Carla,
Carolina,
Estefania,
Adelaida,
Angela,
Donata,
Dora,
Catalina,
Jorgelina,
Elena,
Helena,
Ana,
Ines,
Eulalia,
Nieves,
Remedios,
Rosario,
Valeria
"""

c=nombres.replace(" ","").replace("\n","").split(",")

apellidos="Francis","Hernanadez","Gonzalez","Salinas","Navarro","Setion","Cruz","Garcia","Gomez","Curiel","Verduzco","Varela","Rosas","Valdez","Vanegas","Rosas","Vanegas","Vineros","Espinosa","cabreto","Corderno","Leffmans","Maldonado","Martinez"
letras="abcdefghijklmnopkrstuvwxyz"
numeros="1234567890"
pas=str(letras+numeros)


d=Figlet(font="standard")
print(colored(d.renderText("Bienvenido a usar este bot :D"),"blue"))
print(Fore.RED,"Bot valido para la pagina https://socialrebel.co-faa3.xyz/")

pagina=input("Introduce el link de referido: ")

while True:
    try:
        cuentas=int(input("Introduce el numero de cuentas:"))
        break
    except:
        pass

while True:
    try:
        hilos=int(input("Introduce el numero de hilos:"))
        break
    except:
        pass


cuan=0

d=0
def main():
    global d
    global cuan
    global hilos
    global cuentas
    global pagina

    for i in range(int(cuentas/hilos)):
        session=requests.session()
        headerss={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0"}
        session.get(pagina,headers=headerss)
   

        name=random.choice(c)
        apellido=random.choice(apellidos)
        namee=f"{name} {apellido}"

        username=random.randint(100,2000)
        usernamee=f"{name}{apellido}{str(username)}"
        username=usernamee.lower()

        email=f"{name}{random.randint(1,10)}{username}@gmail.com"
        email=str(email.lower())


        password=""

        for i in range(10):
            password+=str(random.choice(pas))

        d=session.get("https://socialrebel.co-faa4.xyz/home/user/register.php",headers=headerss)
        soup=BeautifulSoup(d.content,"xml")
        token=soup.find("input",{"name":"_token"}).get("value")

        dataa={"_token":token,"name":namee,"username":username,"email":email,"password":password,"password_confirmation":password}

        session.post("https://socialrebel.co-faa4.xyz/home/user/register.php",headers=headerss,data=dataa)
        cuan+=1
        print(f"{cuan} cuentas creadas de {cuentas}")


    d=Figlet(font="standard")
    print(colored(d.renderText(f"Terminado {cuentas} creadas"),"red"))
    os.system("pause")

            
    
if __name__=="__main__":
    theread=[]
    for i in range(hilos):
        p=Thread(target=main)
        theread.append(p)
    for i in theread:
        i.start()

