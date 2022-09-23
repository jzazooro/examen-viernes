from clases.ejercicio1 import sumalistas
from clases.ejercicio2 import contarelementos
from clases.ejercicio4 import

listauno=[1, 1, 1]
listados=[2, 2, 2]
listatres=[3, 3, 3]
listacuatro=[4, 4, 4]

def main():

    print("Ejercicio 1: ")
    sumalistas(listauno)
    print("la primera lista es: ", listauno)
    sumalistas(listados)
    print("la segunda lista es: ", listados)
    sumalistas(listatres)
    print("la tercera lista es: ", listatres)
    sumalistas(listacuatro)
    print("la cuarta lista es: ", listacuatro)

    print("Ejercicio 2: ")

    print("Ejercicio 3: ")
    a=list(range(11))
    print("la lista resultante al primer enunciado es: ", a)
    b=list(range(-10, 1))
    print("la lista resultante al segundo enunciado es: ", b)
    c=list(range(0, 21, 2))
    print("la lista resultante al tercer enunciado es: ", c)
    d=list(range(-19, 0, 2))
    print("la lista resultante al cuarto enunciado es: ", d)
    e=list(range(0, 50, 5))
    print("la lista resultante al quinto enunciado es: ", e)

    print("Ejercicio 4: ")

if __name__=='__main__':
    main()