
import json

def leer_campers():
    try:
        with open("campers.json", "r") as f:
            return json.load(f)
    except:
        return []

def buscar_camper(id_camper):
    for c in leer_campers():
        if c["IDcamper"] == id_camper:
            return c
    return None

def menu_ver_notas(id_camper):
    camper = buscar_camper(id_camper)

    if camper is None:
        print(" Camper no encontrado")
        return

    estado = camper["estado"].lower()

    
    if estado in ["en proceso de ingreso", "inscrito", "aprobado"]:
        print("⚠️ Aún no tiene notas. Su proceso formativo no ha iniciado.")
        return

    if estado in ["expulsado", "retirado"]:
        print(" Comuníquese con CampusLands: 018000-CAMPUS")
        return

    if estado not in ["cursando", "graduado"]:
        print(" Estado no válido")
        return

    while True:
        print("\n---- VER NOTAS ----")
        print("1. Notas generales")
        print("2. Notas por módulo")
        print("3. Regresar")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ver_notas_generales(camper)

        elif opcion == "2":
            ver_notas_por_modulo(camper)

        elif opcion == "3":
            break

        else:
            print(" Opción inválida")

def ver_notas_generales(camper):
    print("\n NOTAS GENERALES")
    for modulo, notas in camper["modulos"].items():
        print(f"\n {modulo}")
        for k, v in notas.items():
            print(f"  {k}: {v}")

def ver_notas_por_modulo(camper):
    modulo = input("Ingrese el módulo: ").lower()

    if modulo in camper["modulos"]:
        print(f"\n {modulo}")
        for k, v in camper["modulos"][modulo].items():
            print(f"  {k}: {v}")
    else:
        print(" Módulo no encontrado")



  
    