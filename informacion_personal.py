import guardarLeerJSON
def ver_info_camper():
    print("-"*80)
    print(f"\t----INFORMACIÓN PERSONAL CAMPER----")
    print("-"*80)
    ID=input("digite su ID:")
    campers=guardarLeerJSON.leerJSON("campers.json")
    for i in campers:
        if i["ID"]==ID:
            print(" ")
            print(f"Nombre: {i['nombre']} {i['apellido']}")
            print(f"ID: {i['ID']}")
            print(f"Estado: {i['estado']}")
            print(f"Direccion: {i['direccion']}")
            print(f"Acudiente: {i['acudiente']}")
            print(f"Celular: {i['celular']}")
            print(f"Jornada: {"Mañana (6am-2pm)" if i.get("jornada")=="1" else "Tarde(2pm-10pm)" }")
            break

def ver_info_trainer(ID):
    trainers=guardarLeerJSON.leerJSON("trainers.json")
    for i in trainers:
        if i["ID"]==ID:
            print("----- INFORMACIÓN PERSONAL TRAINER----")
            print(f"ID: {i['ID']}")
            print(f"Nombre: {i['nombre']}")
            print(f"Especialidad: {i['especialidad']}")
            print("Horario disponible:")
            for j in i["horario"]:
                if i["horario"][j][0] is None:
                    print(f"{i["horario"][j][1]}: No asignado")
                else:
                    print(f"{i["horario"][j][1]} asignado al grupo #{i["horario"][j][0]}")
        break
    

def ver_info_coordinacion(ID):
    coordinador=guardarLeerJSON.leerJSON("coordinador.json")
    for i in coordinador:
        if i["ID"]==ID:
            print("----INFORMACIÓN PERSONAL COORDINACIÓN----")
            print(f"Nombre: {i['nombre']}")
            print("Rol: Coordinador académico")
            break



