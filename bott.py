
import requests
from bs4 import BeautifulSoup
import random
import os
import colorama
from termcolor import colored
from pyfiglet import Figlet
from colorama import Fore
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


cuan=0

try:
    for i in range(cuentas):
        session=requests.session()
        headerss={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
        session.get(pagina,headers=headerss)

        name=random.choice(c)
        apellido=random.choice(apellidos)
        namee=f"{name}+{apellido}"

        username=random.randint(100,2000)
        usernamee=f"{name}{apellido}{str(username)}"
        username=usernamee.lower()

        email=f"{name}{random.randint(1,10)}{username}@gmail.com"
        email=str(email.lower())


        password=""

        for i in range(10):
            password+=str(random.choice(pas))

        d=session.get("https://socialrebel.co-faa3.xyz/home/user/register.php",headers=headerss)
        soup=BeautifulSoup(d.content,"xml")
        token=soup.find("input",{"name":"_token"}).get("value")

        dataa={"_token":token,"name":name,"username":username,"email":email,"password":password,"password_confirmation":password}

        session.post("https://socialrebel.co-faa3.xyz/home/user/register.php",headers=headerss,data=dataa)
        cuan+=1
        print(f"{cuan} cuentas creadas de {cuentas}")


    d=Figlet(font="standard")
    print(colored(d.renderText(f"Terminado {cuentas} creadas"),"red"))
    os.system("pause")
except:
    print(colored("Revisa tu conexion a internet"),"red")
    os.system("pause")