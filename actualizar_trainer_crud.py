
import guardarLeerJSON

def actualizar_trainer ():
    trainers= guardarLeerJSON.leerJSON ("trainers.json")

    id_buscar= input ("Ingrese el ID del trainer a modificar: ")

    for trainer in trainers:
        if trainer ["ID"]== id_buscar:

            print ("---TRAINER ENCONTRADO----")
            print ("1. Nombre:", trainer.get ("nombre", "no definido"))
            print ("2. Apellido:", trainer.get ("apellido", "no definido"))
            print ("3. Celular:", trainer.get ("celular", "no definido"))
            print ("4. Especialidad:", trainer.get ("especialidad", "no definido"))
            print ("5. Estado:", trainer.get ("estado", "no definido"))
            print ("6. Clave:", trainer.get ("clave", "no definido"))
            
            print ("---¿Que dato desea mmodificar?----")
            print ("1. Nombre")
            print ("2. Apellido")
            print ("3. Celular")
            print ("4. Especialidad")
            print ("5. Estado")
            print ("6. Clave")

            opcion= input ("Sleccione una opccion: ")

            match opcion:
                case "1":
                    trainer ["nombre"]= input ("Nuevo nombre: ")
                case "2":
                    trainer ["apellido"]= input ("Nuevo apellido: ")
                case "3":
                    trainer ["celular"]= input ("NUevo celular:")
                case "4":
                    trainer ["especialidad"]= input ("Nueva especialidad: ")
                case "5":
                    trainer ["estado"]= input ("Nuevo estado: ")
                case "6":
                    trainer ["clave"]= input ("Nueva clave: ")
                case "_":
                    print ("Opcion invalida")
                    return
    guardarLeerJSON.guardarJSON("trainers.json", trainers)
    print ("Modifcacion exitosa")

