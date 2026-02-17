



def buscar_camper_por_id(ID):
    campers = leerJSON("campers.json")
    for c in campers:
        if c["ID"] == ID:
            return c
    return None

def menu_ver_notas(id_camper):
    camper = buscar_camper_por_id(ID)

    if camper is None:
        print(" Camper no encontrado")
        return

    estado = camper["estado"].lower()

    
    if estado in ["en proceso de ingreso", "inscrito", "aprobado"]:
        print(" Aún no tiene notas. Su proceso formativo no ha iniciado.")
        return

    if estado in ["expulsado", "retirado"]:
        print(" Comuníquese con CampusLands: 018000-CAMPUS")
        return

    if estado not in ["cursando", "graduado"]:
        print(" Estado no válido")
        return

    while True:
        print("---- VER NOTAS ----")
        print("1. Notas generales")
        print("2. Notas por módulo")
        print("3. Regresar")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
             ver_notas_generales("camper")
        
            case "2":
                ver_notas_por_modulo("camper")
            case "3":
                break
            case  _:
                print("opcion invalida")



def ver_notas_generales(camper):
    print("\n NOTAS GENERALES")
    for modulo, notas in camper["modulos"].items():
        print(f"\n {modulo}")
        for  tipo,valor in notas.items():
            print(f"  {tipo}: {valor}")

def ver_notas_por_modulo(camper):
    modulo = input("Ingrese el módulo: ").lower()
    modulos = camper.get ("modulos",{})
    if modulo in modulos:
        print(f"\n {modulo}")
        for tipo, valor in modulos[modulo].items():
            print(f"  {tipo}: {valor}")
    else:
        print(" Módulo no encontrado")



  
    