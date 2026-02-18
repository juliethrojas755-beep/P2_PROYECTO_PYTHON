
import guardarLeerJSON

def eliminar_camper():
    campers = guardarLeerJSON.leerJSON("campers.json")

    if not campers:
        print("No hay campers registrados")
        return

    ID = input("Ingrese el ID del camper a eliminar: ")
    camper_encontrado = None

    for i in campers:
        if i.get("ID") == ID:
            camper_encontrado = i
            break
        if camper_encontrado is None:
          print("No existe un camper con ese ID")
        return

    print("----ADVERTENCIA----")
    print("Esta acción eliminará al camper PERMANENTEMENTE")
    print("ID:", camper_encontrado.get("ID"))
    print("Nombre:", camper_encontrado.get("nombre"), camper_encontrado.get("apellido"))
    print("Estado:", camper_encontrado.get("estado"))

    confirmacion = input("---¿Está seguro de eliminarlo?-- (si/no): ").lower()

    match confirmacion:
        case "si":
            campers.remove(camper_encontrado)
            guardarLeerJSON.guardarJSON("campers.json", campers)
            print("Camper eliminado correctamente")
        case "no":
            print(" Eliminación cancelada")
        case _:
            print(" Opción inválida, eliminación cancelada")
eliminar_camper()