
import guardarLeerJSON

def mostrar_trainer ():
    trainers= guardarLeerJSON.leerJSON("trainers.json")

    if not trainers:
        print ("No hay trainers registrados")
        return
    
    while True:
        print ("----------MOSTRAR TRAINER---------")
        print ("1. Ver todos los trainers")
        print ("2. Ver trainer por ID")
        print ("3. Regresar")

        opcion= input ("Seleccione una opcion:  ")

        match opcion:
            case "1":
                print ("-----LISTA DE TRAINERS------")
                for i in trainers:
                    print ("ID:", i ["ID"])
                    print ("Nombre:", i ["nombre"])
                    print ("Especialidad:", i ["especialidad"])
                    print ("Estado:", i.get( "estado", "No definido "))
            case "2":
                ID= input ("Ingrese el ID del trainer: ")
                encontrado= False

                for i in trainers:
                   if i ["ID"]==ID:
                       print ("------TRAINER ENCONTRADO----")
                       print ("ID:", i ["ID"])
                       print ("Nombre:", i ["nombre" ])
                       print ("Especialidad:", i ["especialidad"])
                       print ("Estado:", i.get ( "estado", "No definido"))
                       encontrado= True
                       break
                   if not encontrado:
                      print ("No existe un trainer con ese ID")

            case "3":
                break
            case "_":
                print ("Opcion invalida")

    guardarLeerJSON.guardarJSON("traners.json", trainers)

mostrar_trainer()
    