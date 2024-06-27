
#1. Registrar libro
#2. Listar todos los libros
#3. Registrar venta
#4. Imprimir reporte de ventas
#5. Generar txt
#6. Salir del Programa
import funciones as fn

while True:
    print("=====Menu Principal=====")
    print("(1) Registrar Libro")
    print("(2) Listar todos los libros")
    print("(3) Registrar venta")
    print("(4) Imprimir reporte de ventas")
    print("(5) Generar txt")
    print("(6) Salir del programa")
    op= int(input("ingrese una opcion: "))
    if op == 1: 
        fn.registrar

    if op == 2:
        fn.lista_todos_los_libros

    if op == 6:
        print("Muchas gracias por consultar")
        break
    
    else:
        print("La opcion es invalida")