
import guardarLeerJSON

def eliminar_trainer():
    trainers = guardarLeerJSON.leerJSON("trainers.json")

    if not trainers:
        print("No hay trainers registrados")
        return

    ID = input("Ingrese el ID del trainer a eliminar: ")
    trainer_encontrado = None

    for i in trainers:
        if i.get("ID") == ID:
            trainer_encontrado = i
            break
    if trainer_encontrado is None:
        print ("No existe un trainer con ese ID")  
        return

    print ("---ADVERTENCIA-----")
    print("Esta acción eliminará el trainer PERMANENTEMENTE")
    print("ID:", trainer_encontrado.get("ID"))
    print("Nombre:", trainer_encontrado.get("nombre"))
    print("Especialidad:", trainer_encontrado.get("especialidad"))

    confirmacion = input("---¿Está seguro de eliminarlo? (si/no): ").lower()

    match confirmacion:
        case "si":
            trainers.remove(trainer_encontrado)
            guardarLeerJSON.guardarJSON("trainers.json", trainers)
            print ("Treiner eliminado correctamente")
        case "no":
            print ("Elimnacion cancelada")
        case "_":
            print ("Opcion invalida, eliminacion cancelada")

            guardarLeerJSON.guardarJSON ("trainers.json", trainers)


