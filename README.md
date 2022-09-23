# examen-viernes

El enlace al repositorio de GitHub de este proyecto es el siguiente: [GitHub](https://github.com/jzazooro/examen-viernes.git)

Hemos realizado los cuatro ejercicios propuestos sobre listas.

El ejercicio extra lo he resuelto en la pagina web y adjunto captura de pantalla para que sea comprobable.

![WhatsApp Image 2022-09-23 at 18 33 28](https://user-images.githubusercontent.com/91785177/192010597-f772df18-f4f6-4260-86e7-687dd779dc58.jpeg)

El codigo creado para realizar este examen es el siguiente: 

### main:

```
from lanzador import main
if __name__=='__main__':
    main()
```

### Lanzador

```
from ejercicio1 import sumalistas
from ejercicio2 import contarelementos
from ejercicio4 import tabla

def main():

    print("Ejercicio 1: ")
    listauno=[1, 1, 1]
    listados=[2, 2, 2]
    listatres=[3, 3, 3]
    listacuatro=[4, 4, 4]
    sumalistas(listauno)
    print("la primera lista es: ", listauno)
    sumalistas(listados)
    print("la segunda lista es: ", listados)
    sumalistas(listatres)
    print("la tercera lista es: ", listatres)
    sumalistas(listacuatro)
    print("la cuarta lista es: ", listacuatro)

    print("Ejercicio 2: ")
    cadenatexto=input("escribe lo que quieras: ")
    contarelementos(cadenatexto)

    print("Ejercicio 3: ")
    a=list(range(11))
    print("la lista resultante al primer enunciado es: ", a)
    b=list(range(-10, 1))
    print("la lista resultante al segundo enunciado es: ", b)
    c=list(range(0, 21, 2))
    print("la lista resultante al tercer enunciado es: ", c)
    d=list(range(-19, 0, 2))
    print("la lista resultante al cuarto enunciado es: ", d)
    e=list(range(0, 51, 5))
    print("la lista resultante al quinto enunciado es: ", e)

    print("Ejercicio 4: ")
    tabla()
```

### Ejercicio 1:

```
def sumalistas(lista):
    sumadenotas=sum(lista)
    lista.append(sumadenotas)
```

### Ejercicio 2: 

```
def contarelementos(cadenadetexto):
    if 3<=len(cadenadetexto)<10:
        print("True")
    else: 
        print("False")
```

### Ejercicio 4: 

```
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
```

### Nota:
no hay un archivo que sea "ejercicio3.py" por que como no he usado funciones para resolverlo, todo su codigo está dentro del lanzador en la funcion main()
