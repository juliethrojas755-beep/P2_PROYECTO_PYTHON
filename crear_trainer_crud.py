import guardarLeerJSON
def crear_trainer():
    trainers =guardarLeerJSON.leerJSON("trainers.json")
    print("------CREA TRAINER-------")

    ID= input (" ID del trainer: ")

    for i in trainers:
        if i ["ID"] ==ID:
            print  ("Ya existe un trainer con ese ID")

    nombre= input ("Nombre: ")
    apellido= input ("Apellido: ")
    celular= input ("Celular: ")
    especialidad= input ("Especialidad: ")
    estado= "activo"
    clave= input ("Clave: ")

    nuevo_trainer = {
        "ID": ID,
        "nombre": nombre,
        "apellido": apellido,
        "celular": celular,
        "especialidad": especialidad,
        "estado": estado,
        "clave":clave

    }
    trainers.append(nuevo_trainer)
    guardarLeerJSON.guardarJSON("trainers.json", trainers)
    print ("Trainer creado correctamente")

crear_trainer()
