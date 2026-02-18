import guardarLeerJSON

def actualizarAprobarInscritos():
    campers=guardarLeerJSON.leerJSON("campers.json")
    listaCampers=[i for i in campers if i["estado"]=="inscrito"]
    if listaCampers:
        print("los campers que actualmente se encuentran en estado 'inscrito' son: \n")
        print(f"{"nombre":<20}|{"ID":15}|{"nota teorica":<15}|{"nota practica":<15}|{"nota definitiva":<15}")
        for i in listaCampers:
            print(f"{i["nombre"]+" "+i["apellido"]:<20}|{i["ID"]:15}|{i["pruebaInicial"]["teorica"]:<15}|{i["pruebaInicial"]["practica"]:<15}|{((i["pruebaInicial"]["teorica"] + i["pruebaInicial"]["practica"])/2):<15}")
        print(f"la nota minima para aprobar a los camper es de 60.")
        opcion=input("""Escoja una de las siguientes opciones:
        1) auto-actualizar los estados de todos los campers segun la nota definitiva
            Aprobado si la nota total >=60
            Reprobado si la nota total <60
        2) actualizar el estado, la nota teorica, la nota practica y la nota definitiva de un camper particular por ID.
        respuesta: """)
        if (opcion=="1"):
            for i in campers:
                if i["estado"]=="inscrito":
                    notaDefinitiva=(i["pruebaInicial"]["teorica"]+i["pruebaInicial"]["practica"])/2
                    i["pruebaInicial"]["definitiva"]=notaDefinitiva
                    if notaDefinitiva >= 60:
                        i["estado"]="aprobado"
                    else:
                        i["estado"]="reprobado"
        elif (opcion=="2"):
            ID = input("Digite el ID del camper: ")
            encontrado = False
            
            for i in campers:
                if i["ID"] == ID and i["estado"]=="inscrito":
                    encontrado = True
                    print(f"\nCamper encontrado: {i['nombre']} {i['apellido']}")
                    
                    while(True):
                        try:
                            nuevaTeorica = int(input("Ingrese la nueva nota teórica (10-100): "))
                            nuevaPractica = int(input("Ingrese la nueva nota práctica (10-100): "))
                            if not (10<=nuevaTeorica<=100 and 10<=nuevaPractica<=100):
                                print("las notas deben ser entre 10 y 100")
                                continue
                            break
                        except ValueError:
                            print("Error: Las notas deben ser números enteros.")

                    notaDefinitiva = (nuevaTeorica + nuevaPractica) / 2
                    
                    i["pruebaInicial"]["teorica"] = nuevaTeorica
                    i["pruebaInicial"]["practica"] = nuevaPractica
                    i["pruebaInicial"]["definitiva"] = notaDefinitiva
                    
                    while(True):
                        print(f"la nota definitiva del camper {i['nombre']} es: {notaDefinitiva}")
                        opcion=input("si desea aprobarlo digite 1\nsi desea reprobarlo digite 2\nsi desea salir digite 3\n respuesta: ")
                        if opcion=="1":
                            i["estado"] = "aprobado"
                            break
                        elif opcion=="2":
                            i["estado"] = "reprobado"
                            break
                        elif opcion=="3":
                            return
                        else:
                            print("opcion invalida")
                    
                    print(f"\nDatos actualizados.")
                    print(f"Nueva Definitiva: {notaDefinitiva} - Nuevo Estado: {i['estado']}")
                    break
            
            if not encontrado:
                print("El ID ingresado no coincide con ningún camper inscrito.")
        else:
            print("se ha equivoado de opcion, intentelo nuevamente")
            return
        guardarLeerJSON.guardarJSON("campers.json", campers)
    else:
        print("la lista de campers 'inscritos' esta vacia")
actualizarAprobarInscritos()