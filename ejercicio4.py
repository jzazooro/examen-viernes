from distutils.log import error
from logging import exception


def tabla():
    f=int(input("¿Cuantas filas entre 1 y 9 desea que tenga la tabla?: "))
    c=int(input("¿Cuantas columnas entre 1 y 9 desea que tenga la tabla?: "))
    if f<1 or f>9 or c<1 or c>9:
        raise exception("Has cometido un error, Los numeros deben ser mayores que 1 y menores que 9")
    for i in range(0, f):
        print("")
        for e in range(0, c):
            print(" CR7 ", end='')