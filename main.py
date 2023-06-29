from Peluqueria import *
import numpy as np
import random as nr
ciclo = True




arreglo_clinte = np.array([])


def grabarcita(arreglo_clinte):
    cit = grabarcita()
    c = False
    while c == False:
        g = cit.self.Cita(input("Ingrese Cita"))
    c = False







def buscarcita(arreglo_clinte):
    bus = buscarcita()


def salir():
    print(".......")
    return False


while ciclo:
    print("Menu Mechas Locas")
    print("-------------------")
    print("1) Grabar Cita")
    print("2)Buscar")
    print("3)Imprimir Atencion")
    print("4)Salir")
    try:
        op = int(input("Seleccione (1-4):"))
        match op:
            case 1:
                print("Grabar Cita")
                arreglo_clinte = grabarcita(arreglo_clinte)
            case 2:
                print("Buscar")
                buscarcita(arreglo_clinte)
            case 3:
                print("Imprimir Atencion")
            case 4:
                ciclo = salir()

    except BaseException as error:
        print(f"Error:{error}")
