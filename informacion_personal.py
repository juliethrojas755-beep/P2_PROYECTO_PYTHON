
def ver_info_camper(camper):
    print("----INFORMACIÓN PERSONAL CAMPER----")
    print(f"ID: {camper['IDcamper']}")
    print(f"Nombre: {camper['nombre']} {camper['apellido']}")
    print(f"Estado: {camper['estado']}")
    print(f"Jornada: {camper.get('jornada', 'No asignada')}")

def ver_info_trainer(trainer):
    print("----- INFORMACIÓN PERSONAL TRAINER----")
    print(f"ID: {trainer['IDtrainer']}")
    print(f"Nombre: {trainer['nombre']}")
    print(f"Especialidad: {trainer['especialidad']}")
    
    if trainer.get("horario") is None:
        print("Horario: No asignado")
    else:
        print(f"Horario: {trainer['horario']}")
    

def ver_info_coordinacion(coord):
    print("----INFORMACIÓN PERSONAL COORDINACIÓN----")
    print(f"Nombre: {coord['nombre']}")
    print("Rol: Coordinador académico")

def ver_info_personal(usuario, rol):

    if rol == "camper":
        ver_info_camper(usuario)

    elif rol == "trainer":
        ver_info_trainer(usuario)

    elif rol == "coordinacion":
        ver_info_coordinacion(usuario)

    else:
        print(" Rol no válido")


