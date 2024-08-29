# Hacer un programa que reciba el nombre, fecha de nacimiento,sexo,ciudad de residencia de un estudiante que se va a inscribir en el curso de programacion y que genere un recibo de la inscripcion detallado.

nombre:str = str(input("Nombre Alumno: "))
fecha = str(input("Fecha de nacimiento: "))
genero:str = str(input("Genero: "))
ciudad:str = str(input("Ciudad de residencia: "))
programa:str = str(input("Ingrese el Programa: ")).lower()
valor:int = int(input("Valor total matricula: "))

def inscripcion(nombre:str, fecha:str, genero:str, ciudad:str, valor:int):
 if programa == "programacion":  
    print("Ingrese su nombre ", nombre)
    print("Ingrese su fecha de nacimiento", fecha)
    print("Ingrese su genero", genero)
    print("Inngrese la ciudad de residencia", ciudad)
    print(30 * "-")
    print("Matriculado: \n", "Programa: programacion \n", "Duracion: 2 años \n", "Salon: 115 \n", "Bloque: 3 \n")
    print("Valor total matricula", valor)
 else:
    print("el programa no existe", programa)
 
inscripcion(nombre, fecha, genero, ciudad, valor)