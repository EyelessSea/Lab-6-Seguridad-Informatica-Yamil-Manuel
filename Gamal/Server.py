import socket

Mensaje_Cifrado = []
Mensaje_Descifrado = []


P=199
G=70 
A=int(input("Ingrese su valor de A: ")) 
k = pow(G,A) % P 

print("clave pública: (G,P,k) =(", G,",", P,",", k,")\n")


Host = "LocalHost"
Puerto = 8000

Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Server.bind((Host, Puerto))
Server.listen(1)
print("Servidor en espera\n")

Conexion, Addr = Server.accept()

for i in range(1):
    Conexion.send(str(P).encode(encoding="ascii", errors="ignore"))
    print((Conexion.recv(1024)).decode(encoding="ascii", errors="ignore"))
    Conexion.send(str(G).encode(encoding="ascii", errors="ignore"))
    print((Conexion.recv(1024)).decode(encoding="ascii", errors="ignore"))
    Conexion.send(str(k).encode(encoding="ascii", errors="ignore"))
    print((Conexion.recv(1024)).decode(encoding="ascii", errors="ignore"))
    Conexion.send(b'Solicitar y1')
    
    y1 = Conexion.recv(1024)
    y1 = int(y1.decode(encoding = "ascii", errors = "ignore"))
    Conexion.send(b'Solicitar mensaje encriptado')
    
    Cifrado = Conexion.recv(1024)
    Cifrado = Cifrado.decode(encoding="ascii", errors="ignore")
    
    print("\n")
    

    
Cifrado = Cifrado.split(",")

for i in Cifrado:
    if i != "":
        Mensaje_Cifrado.append(int(i))
        
    

   

for y2 in Mensaje_Cifrado:
    m = (pow(y1,(P-1-A))*y2) % P
    Mensaje_Descifrado.append(m)
    

Descifrado = ""

for i in Mensaje_Descifrado:
    Descifrado += chr(i)

M_Cif = ""

for i in Mensaje_Cifrado:
    M_Cif += chr(i)

print("Mensaje Cifrado:", M_Cif)
print("Mensaje Descifrado:", Descifrado)


Salida = open('mensajerecibido.txt','w')
Salida.write(Descifrado)
Salida.close()



