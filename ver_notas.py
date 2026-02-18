
import guardarLeerJSON

def buscar_camper_por_id(ID):
    campers = guardarLeerJSON.leerJSON("campers.json")
    for c in campers:
        if c.get("ID") == ID:
            return c
    return None


def menu_ver_notas(ID):
    camper = buscar_camper_por_id(ID)

    if camper is None:
        print("Camper no encontrado")
        return

    estado = camper.get("estado", "").lower()

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
        print("n---- VER NOTAS ----")
        print("1. Notas generales")
        print("2. Notas por módulo")
        print("3. Regresar")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
              ver_notas_generales(camper)

            case "2":
                ver_notas_por_modulo(camper)

            case "3":
                break

            case _:
                print(" Opción inválida")
def ver_notas_generales(camper):
    modulos = camper.get("modulos", {})

    if not modulos:
        print(" No hay notas registradas")
        return

    print("--- NOTAS GENERALES-----")

    for modulo, notas in modulos.items():
        print(f"\nMódulo: {modulo}")
        for tipo, valor in notas.items():
            print(f"  {tipo}: {valor}")

def ver_notas_por_modulo(camper):
    modulos = camper.get("modulos", {})

    if not modulos:
        print(" No hay notas registradas")
        return

    modulo = input("Ingrese el nombre del módulo: ").lower()

    if modulo in modulos:
        print(f"\n Módulo: {modulo}")
        for tipo, valor in modulos[modulo].items():
            print(f"  {tipo}: {valor}")
    else:
        print("Módulo no encontrado")

