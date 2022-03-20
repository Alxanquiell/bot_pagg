import os

os.system("pip install bs4;pip install colorama;pip install pyfiglet;pip install termcolor;pip install lxml")

import requests
from bs4 import BeautifulSoup
import random
import time
import colorama
from termcolor import colored
from pyfiglet import Figlet
from colorama import Fore
from threading import Thread
colorama.init()




nombres="""
Guadalupe,Reinalda,Alberta,Paula,Paola,Juana,Carla,Carolina,Estefania,Adelaida,Angela,Donata,Dora,Catalina,Jorgelina,Elena,Helena,Ana,Ines,Eulalia,Nieves,Remedios,Rosario,Valeria,Hugo,Ana,Helena,Enzo,Eric,Eva,Juan,Lara,Leo,Luz,Mar,Nora,Raul,Sara,Zeus,Ulises,Penelope,Helena,Hector,Isis,Alba,Alvaro,Alejandro,Emma,Kuscas,Lucia,Manuel,Mariana
"""

c=nombres.replace(" ","").replace("\n","").split(",")

apellidos="Francis","Hernanadez","Gonzalez","Salinas","Navarro","Setion","Cruz","Garcia","Gomez","Curiel","Verduzco","Varela","Rosas","Valdez","Vanegas","Rosas","Vanegas","Vineros","Espinosa","cabreto","Corderno","Leffmans","Maldonado","Martinez","Castillo","Benitez","Castro","Contreras","Leon","Diaz","Duarte","Espinoza","Fernandez","Flores","Garcia","Vasco","Gimenez","Gomez","Gutierrez"
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
        hilos=int(input("Introduce el numero de hilos(velocidad) recomendable 1,10 dependiendo del internet: "))

        if cuentas%hilos==0:
            break
        else:
            print(f"Introduce otro numero que sea divisible entre {cuentas}")

    except:
        pass


url=pagina.split("/")
url=url[2]



cuan=0

dd=0
def main():
    global dd
    global cuan
    global hilos
    global cuentas
    global pagina
    
    try:
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

            d=session.get(f"https://{url}/home/user/register.php",headers=headerss)
            soup=BeautifulSoup(d.content,"xml")
            token=soup.find("input",{"name":"_token"}).get("value")

            dataa={"_token":token,"name":namee,"username":username,"email":email,"password":password,"password_confirmation":password}

            session.post(f"https://{url}/home/user/register.php",headers=headerss,data=dataa)
            cuan+=1
            print(f"{cuan} cuentas creadas de {cuentas}")

    except requests.exceptions.ConnectionError:       
        if dd == 0:
            dd+=1
            
def ex():
    global dd
    global cuan
    global cuentas 
        
    while True:
        time.sleep(0.5)
        if cuan==cuentas:
            d=Figlet(font="standard")
            print(colored(d.renderText(f"Terminado,{cuentas} cuentas creadas"),"red"))
            os.system("pause")
            break
        elif dd==1:
            print("Revisa tu conexion a internet")
            os.system("pause")
            break





if __name__=="__main__":
    theread=[]
    for i in range(hilos):
        p=Thread(target=main,daemon = False)
        theread.append(p)
    for i in theread:
        i.start()

    pp=Thread(target=ex,daemon=False)
    pp.start()


