def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    """Calcula el inverso multiplicativo modular de 'a' módulo 'm'."""
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("el inverso modular no existe")
    else:
        return x % m

def mcd(a, b):
     """Calcula el máximo común divisor de 'a' y 'b'."""
     resto = 0
     while(b > 0):
      resto = b
      b = a % b
      a = resto
     return a
