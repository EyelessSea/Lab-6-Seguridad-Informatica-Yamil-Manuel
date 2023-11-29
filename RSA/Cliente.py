import MatematicasParaElPrograma
import socket


Mensaje_Descifrado = []


Host = "LocalHost"
Puerto = 8000

Mi_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Mi_Socket.connect((Host, Puerto))

Mensaje_1 = "Recibida variable e\n"
Mensaje_2 = "Recibida llave n\n"
Mensaje_3 = "Fi(n) recibido\n"
Mensaje_4 = "Tu mensaje esta siendo descifrado, dejalo en mis manos\n"

for i in range(1):    
    e = Mi_Socket.recv(1024)
    e = int(e.decode(encoding = "ascii", errors = "ignore"))
    
    Mi_Socket.send(Mensaje_1.encode(encoding="ascii", errors="ignore"))
 
    n = Mi_Socket.recv(1024)
    n = int(n.decode(encoding = "ascii", errors = "ignore"))

    Mi_Socket.send(Mensaje_2.encode(encoding="ascii", errors="ignore"))
   
for i in range(1):
    fi_n = Mi_Socket.recv(1024)
    fi_n = int(fi_n.decode(encoding = "ascii", errors = "ignore"))
    
    Mi_Socket.send(Mensaje_3.encode(encoding="ascii", errors="ignore"))

    Mensaje_Cifrado = Mi_Socket.recv(1024)
    Mensaje_Cifrado = Mensaje_Cifrado.decode(encoding = "ascii", errors = "ignore")
    
    Mi_Socket.send(Mensaje_4.encode(encoding="ascii", errors="ignore"))
    

Mensaje_Cifrado = Mensaje_Cifrado.split(",")
Mensaje_Cifrado.pop()

for pos in range(0, len(Mensaje_Cifrado)):
    Mensaje_Cifrado[pos] = int(Mensaje_Cifrado[pos])

d = MatematicasParaElPrograma.modinv(e, fi_n)  

for m in Mensaje_Cifrado:
    Descifrado = pow(m, d) % n
    Mensaje_Descifrado.append(Descifrado)


print("Decifrado en ASCII:", Mensaje_Descifrado, "\n")

Descifrado = ""

for i in Mensaje_Descifrado:
    Descifrado += chr(i)
    
print("Decifrado:", Descifrado)

Salida = open('mensajerecibido.txt','w')
Salida.write(Descifrado)
Salida.close()
