import guardarLeerJSON

def actualizarAprobarInscritos():
    campers=guardarLeerJSON.leerJSON("campers.json")
    listaCampers=[i for i in campers if i["estado"]=="inscrito"]
    print("los campers que actualmente se encuentran en estado 'inscrito' son: \n")
    print(f"{"nombre":<20}|{"ID":15}|{"nota teorica":<15}|{"nota practica":<15}|{"nota total":<15}")
    for i in listaCampers:
        print(f"{i["nombre"]+" "+i["apellido"]:<20}|{i["ID"]:15}|{i["pruebaInicial"]["teorica"]:<15}|{i["pruebaInicial"]["practica"]:<15}|{((i["pruebaInicial"]["teorica"] + i["pruebaInicial"]["practica"])/2):<15}")
    print(f"la nota minima para aprobar a los camper es de 60.")
    opcion=input("""Escoja una de las siguientes opciones:
    1) auto-actualizar los estados de todos los campers segun la nota total
        Aprobado si la nota total >=60
        Reprobado si la nota total <60
    2) actualizar el estado de un camper particular del""")
actualizarAprobarInscritos()