import MatematicasParaElPrograma

Letras_Ascii = []
Mensaje_Cifrado = []
Mensaje_Descifrado = []

Entrada = open('mensajeentrada.txt','r') 

for i in Entrada.read():
    Letras_Ascii.append(ord(i))

Entrada.close()

print(Letras_Ascii,"\n")
    
#Público
P = 569
Q = 839 

n = P*Q
fi_n = (P-1)*(Q-1)

seguir = True
while seguir:
    e = int(input("Ingrese valor de e: "))
    if MatematicasParaElPrograma.mcd(e, fi_n) == 1:
        seguir = False
    else:
        print("El maximo comun divisor debe ser 1")
        
d = MatematicasParaElPrograma.modinv(e, fi_n)

#Cifrado
for m in Letras_Ascii:
    Cifrado = pow(m, e) % n
    Mensaje_Cifrado.append(Cifrado)

#Descifrado
for m in Mensaje_Cifrado:
    Descifrado = pow(m, d) % n
    Mensaje_Descifrado.append(Descifrado)


print("Decifrado en ASCII:", Mensaje_Descifrado, "\n")

Descifrado = ""

for i in Mensaje_Descifrado:
    Descifrado += chr(i)
    
print("Decifrado:", Descifrado)






