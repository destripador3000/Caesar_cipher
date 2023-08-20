# Hacer un Cifrado César para Strings en Python
# Emulación de Cifrado César con llave de descifración


ALFABETO = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
CIFRADO = {"G":1,"H":2,"I":3,"J":4,"K":5,"L":6,"M":7,"N":8,"O":9,"P":10,"Q":11,"R":12,"S":13,"T":14,"U":15,"V":16,"W":17,"X":18,"Y":19,"Z":20,"A":21,"B":22,"C":23,"D":24,"E":25,"F":26}

def codificado():
    palabra = input("Escribe la palabra a cifrar: ")
    llaves = []
    new = palabra.upper()
    for i in new:
        for k,v in CIFRADO.items():
            if v == ALFABETO[i]:
                llaves.append(k)
    duplicado = "".join(llaves)            
    print(duplicado)
    return duplicado
               

def decodificado():
    llaves = []
    descifrar = secreto
    for i in descifrar:
       for k,v in ALFABETO.items():
           if v == CIFRADO[i]:
               llaves.append(k)
    duplicado="".join(llaves)           
    print (duplicado)

secreto = codificado()
decodificado()
