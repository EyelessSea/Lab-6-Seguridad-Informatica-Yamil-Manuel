Letras_Ascii = []
Mensaje_Cifrado = []
Mensaje_Decifrado = []

Entrada = open('mensajeentrada.txt','r')

for i in Entrada.read():
    Letras_Ascii.append(ord(i))

Entrada.close()

print(Letras_Ascii,"\n")
    

P=199
G=70  

A=13 

k = pow(G,A) % P 

print("clave pública: (G,P,k) =(", G,",", P,",", k,")\n")

Cifrado =  ""


B=45 
y1 = pow(G,B) % P

for i in Letras_Ascii:
    m = i
    y2 = pow(k,B)*m % P
    Mensaje_Cifrado.append(y2)
    Cifrado += chr(y2)
    
print("Cifrado GAMAL:", Mensaje_Cifrado,"\n")

print("Cifrado:", Cifrado, "\n")

print("Cb(",Letras_Ascii,",",B,") = (",y1,",",Mensaje_Cifrado,")\n")


for i in Mensaje_Cifrado:
    y2 = i
    m = (pow(y1,(P-1-A))*y2) % P
    Mensaje_Decifrado.append(m)

print("Decifrado en ASCII:", Mensaje_Decifrado, "\n")

Decifrado = ""

for i in Mensaje_Decifrado:
    Decifrado += chr(i)
    
print("Decifrado:", Decifrado)
