
import guardarLeerJSON

def crear_camper():
    campers = guardarLeerJSON.leerJSON("campers.json")

    print("------ CREAR CAMPER ------")

    ID = input("ID del camper: ")

    for i in campers:
        if i.get("ID") == ID:
            print ("Ya existe un camper con ese ID")
            return
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        direccion = input("Dirección: ")
        acudiente = input("Acudiente: ")
        celular = input("Celular: ")
        jornada = input("Jornada (1 o 2): ")
        clave = input("Clave: ")

        estado = input("Estado (proceso de inscripcion / inscrito / aprobado / cursando / graduado): ").lower()


        nuevo_camper = {
        "nombre": nombre,
        "apellido": apellido,
        "ID": ID,
        "direccion": direccion,
        "acudiente": acudiente,
        "celular": celular,
        "fijo": "0",
        "jornada": jornada,
        "estado": estado,
        "IDgrupo": None,
        "llamadaAtencion": [],
        "riesgo": None,
        "rendimiento": None,
        "fechaInicial": None,
        "pruebaInicial": {
            "teorica": None,
            "practica": None,
            "definitiva": None
        },
        "clave": clave
    }

    match estado:
        case "proceso de inscripcion":
            pass 
        case "inscrito" | "aprobado":
            nuevo_camper["fechaInicial"] = input("Fecha inicial (dd-mm-aaaa): ")

        case "cursando":
            nuevo_camper["fechaInicial"] = input("Fecha inicial (dd-mm-aaaa): ")
            nuevo_camper["IDgrupo"] = input("ID del grupo: ")
            nuevo_camper["pruebaInicial"]["teorica"] = int(input("Nota teórica: "))
            nuevo_camper["pruebaInicial"]["practica"] = int(input("Nota práctica: "))

        case "graduado":
            nuevo_camper["fechaInicial"] = input("Fecha inicial (dd-mm-aaaa): ")
            nuevo_camper["IDgrupo"] = input("ID del grupo: ")
            nuevo_camper["rendimiento"] = input("Rendimiento (alto / medio / bajo): ")
            nuevo_camper["riesgo"] = input("Riesgo (si / no): ")

        case "_":
            print ("Estado no valido")
            return
    campers.append(nuevo_camper)
    guardarLeerJSON.guardarJSON("campers.json", campers)
    print("Camper creado correctamente")

crear_camper()
