

libros = []
ventas = []
genero = ['ficcion', 'no ciencia', 'ciencia']

def registrar():

    libro = input("Ingrese titulo del libro")
    titulo = input("Ingrese autor del libro")
    genero = input("Ingrese el genero del libro: (Ficción), (No Ficción), (Ciencia)")
    valor = int(input("Ingrese precio"))
    ({

    'libro': libros,
    'titulo': titulo, 
    'genero': genero, 
    'valor' : valor

   })

def listar_todos_los_libros():
    for i in (libros):
        print()
