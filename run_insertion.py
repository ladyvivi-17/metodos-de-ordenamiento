# -*- coding: utf-8 -*-
from funciones import *
from insertion import *
import threading
import time

def main():
    op = " "

    while op != "s" and op != "S":
        print"------------------------------------------"
        print("\t\tMETODOS DE ORDENAMIENTO\t\t")
        print("(a). Inserción Directa ")
        print("(b). Ordenamiento por Mezcla (Merge Sort) ")
        print("(c). Ordenamiento por Montones (Heap Sort) ")
        print("(d). Ordenamiento rápido (Quick Sort) ")
        print("(e). Ordenamiento por Conteo (Counting Sort) ")
        print("(f). Ordenamiento por Radix Sort ")
        print("(s). Salir")

        op = raw_input("Digite una Opción: ")

        if op == "a" or op == "A": # inserción Directa

            tiempo_inicial = time.time()
            lista = crearLista()
            nombre = nombreArchivo()
            #llenarLista(lista, 1000)
            nreg = canRegistros()
            llenarLista(lista, nreg)
            crearCsv(lista, nombre)
            #imprimirLista(lista)

            # ordenar
            lista_ordenada = crearLista()
            leerCsv(lista_ordenada, nombre)

            nlista = crearLista()
            nlista2 = arreglalista(lista_ordenada,nlista)

            tam = longitud(nlista2)
            insercionDirecta(nlista2, tam)
            tiempo_inicial_hilo = time.time()
            hilo = threading.Thread(target=insercionDirecta, args=(lista_ordenada, tam))
            hilo.start()
            #imprimirLista(nlista2)
            tiempo_final = time.time() - tiempo_inicial
            tiempo_final_hilo = time.time() - tiempo_inicial_hilo
            print ("tiempo de espera sin hilos")
            imprimirTiempo(tiempo_final)
            print ("tiempo de espera con hilos")
            imprimirTiempo(tiempo_final_hilo)

        if op == "b" or op == "B": #Ordenamiento por Mezcla (Merge Sort)

            tiempo_inicial = time.time()
            lista = crearLista()
            nombre = nombreArchivo()
            nreg = canRegistros()
            llenarLista(lista, nreg)
            crearCsv(lista, nombre)
            #imprimirLista(lista)

            lista_ordenada = crearLista()
            leerCsv(lista_ordenada, nombre)

            nlista = crearLista()
            nlista2 = arreglalista(lista_ordenada, nlista)
            List2 = sorted(nlista2, reverse = True)

            #print "Lista 1 "
            #print nlista2
            #print "Lista 2 "
            #print List2
            merge_sort(nlista2)
            #imprimirLista(nlista2)

            tam = longitud(nlista2)
            tiempo_inicial_hilo = time.time()
            hilo = threading.Thread(target=insercionDirecta, args=(lista_ordenada, tam))
            hilo.start()
            tiempo_final = time.time() - tiempo_inicial
            print ("tiempo de espera sin hilos")
            imprimirTiempo(tiempo_final)
            tiempo_final_hilo = time.time() - tiempo_inicial_hilo
            print ("tiempo de espera con hilos")
            imprimirTiempo(tiempo_final_hilo)

        if op == "c" or op == "C": #Ordenamiento por Montones (Heap Sort)

            tiempo_inicial = time.time()
            lista = crearLista()
            nombre = nombreArchivo()
            nreg = canRegistros()
            llenarLista(lista, nreg)
            crearCsv(lista, nombre)
            imprimirLista(lista)

            # ordenar
            lista_ordenada = crearLista()
            leerCsv(lista_ordenada, nombre)

            nlista = crearLista()
            nlista2 = arreglalista(lista_ordenada,nlista)

            tam = longitud(nlista2)
            heap_sort(nlista2)
            imprimirLista(nlista2)
            tiempo_inicial_hilo = time.time()
            hilo = threading.Thread(target=insercionDirecta, args=(lista_ordenada, tam))
            hilo.start()
            tiempo_final = time.time() - tiempo_inicial
            print ("tiempo de espera sin hilos")
            imprimirTiempo(tiempo_final)
            print ("tiempo de espera con hilos")
            imprimirTiempo(tiempo_final_hilo)

        if op == "d" or op == "D": #Ordenamiento rápido (Quick Sort)

            tiempo_inicial = time.time()
            lista = crearLista()
            nombre = nombreArchivo()
            nreg = canRegistros()
            llenarListaConteo(lista, nreg)
            crearCsv(lista, nombre)
            imprimirLista(lista)

            # ordenar
            lista_ordenada = crearLista()
            leerCsv(lista_ordenada, nombre)

            nlista = crearLista()
            nlista2 = arreglalista(lista_ordenada,nlista)

            tam = longitud(nlista2)
            quicksort(nlista2, 0, tam - 1)
            #quicksort(nlista2, tam)
            tiempo_inicial_hilo = time.time()
            hilo = threading.Thread(target=insercionDirecta, args=(lista_ordenada, tam))
            hilo.start()
            imprimirLista(nlista2)
            tiempo_final = time.time() - tiempo_inicial
            print ("tiempo de espera sin hilos")
            imprimirTiempo(tiempo_final)
            print ("tiempo de espera con hilos")
            imprimirTiempo(tiempo_final_hilo)

        if op == "e" or op == "E": #Ordenamiento rápido (Quick Sort)

            tiempo_inicial = time.time()
            lista = crearLista()
            nombre = nombreArchivo()
            nreg = canRegistros()
            llenarLista(lista, nreg)
            crearCsv(lista, nombre)
            imprimirLista(lista)

            # ordenar
            lista_ordenada = crearLista()
            leerCsv(lista_ordenada, nombre)

            nlista = crearLista()
            nlista2 = arreglalista(lista_ordenada,nlista)

            tam = longitud(nlista2)
            #print len(nlista2)
            counting_sort(nlista2, len(nlista2))
            #counting_sort(nlista2, 7)
            imprimirLista(nlista2)
            tiempo_inicial_hilo = time.time()
            hilo = threading.Thread(target=insercionDirecta, args=(lista_ordenada, tam))
            hilo.start()
            tiempo_final = time.time() - tiempo_inicial
            print ("tiempo de espera sin hilos")
            imprimirTiempo(tiempo_final)
            print ("tiempo de espera con hilos")
            imprimirTiempo(tiempo_final_hilo)

        if op == "f" or op == "F": #Ordenamiento Radix Sort

            tiempo_inicial = time.time()
            lista = crearLista()
            nombre = nombreArchivo()
            nreg = canRegistros()
            llenarLista(lista, nreg)
            crearCsv(lista, nombre)
            imprimirLista(lista)

            # ordenar
            lista_ordenada = crearLista()
            leerCsv(lista_ordenada, nombre)

            nlista = crearLista()
            nlista2 = arreglalista(lista_ordenada,nlista)

            radix_sort(nlista2)
            tam = longitud(nlista2)
            imprimirLista(nlista2)
            tiempo_inicial_hilo = time.time()
            hilo = threading.Thread(target=insercionDirecta, args=(lista_ordenada, tam))
            hilo.start()
            tiempo_final = time.time() - tiempo_inicial
            print ("tiempo de espera sin hilos")
            imprimirTiempo(tiempo_final)
            print ("tiempo de espera con hilos")
            imprimirTiempo(tiempo_final_hilo)

        if op == "S" or op == "s":

            print "Hasta Pronto."
            exit()

        else:
            print("Digite una Opción \n")

if __name__ == '__main__':
	main()