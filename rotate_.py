# Cifrador que asemeja la manera de ROT13.
# 
# 
cifrado_1=["A","B","C","D","E","F","G","H","I","J","K","L","M"]
cifrado_2=["N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def cifrado():
    palabra=input("Escribe la palabra a cifrar: ")
    h=[]
    n=[]
    new=palabra.upper()
    for i in new:
        if i in cifrado_1:
        
            pola = cifrado_1.index(i)
            h.append(cifrado_2[pola])
        elif i in cifrado_2:
            pola2=cifrado_2.index(i)
            n.append(cifrado_1[pola2])

    cifrado=h + n
    c = "".join(cifrado)
    print(c)

cifrado()
