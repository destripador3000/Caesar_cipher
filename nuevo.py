#Generador de contraseñas con letras, números y caracteres especiales
#
import random
import re
#Lista de mayusculas a escoger
mayusculas=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","x","y","z"]
#Lista numeros a escoger
numeros=["1","2","3","4","5","6","7","8","9","10"]
#Lista de caracteres a escoger
caracteres=["#","%,","&","/,","(",")","?","¡","!","@","-","_","^",",",";","."]
#Lista donde se guardaran los valores aleatorios
original=[]
#Primer ciclo que 
for i in range(1,6):
    primero = random.choice(mayusculas)
    original.append(primero)
for j in range(1,6):
    segundo =random.choice(numeros)
    chere =random.choice(caracteres)
    original.append(segundo)
    original.append(chere)

pasword = reversed(original)        

contrasenna ="".join(pasword)

     
print("su contraseña es: " + contrasenna +" de "+ str(len(contrasenna))+ " caracteres")    

def evaluar_contrasena(contrasena):
    # Verificar la longitud mínima de la contraseña
    if len(contrasena) < 8:
        return "La contraseña debe tener al menos 8 caracteres."

    # Verificar la presencia de al menos una letra mayúscula
    if not re.search(r'[A-Z]', contrasena):
        return "La contraseña debe contener al menos una letra mayúscula."

    # Verificar la presencia de al menos una letra minúscula
    if not re.search(r'[a-z]', contrasena):
        return "La contraseña debe contener al menos una letra minúscula."

    # Verificar la presencia de al menos un número
    if not re.search(r'[0-9]', contrasena):
        return "La contraseña debe contener al menos un número."

    # Verificar la presencia de al menos un carácter especial
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', contrasena):
        return "La contraseña debe contener al menos un carácter especial."

    return "La contraseña es segura."

contrasena = input("Ingrese la contraseña: ")
resultado = evaluar_contrasena(contrasena)
print(resultado)
    