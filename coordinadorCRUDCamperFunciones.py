import guardarLeerJSON
def aprobarInscritos():
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

def modificarCamper():
    campers = guardarLeerJSON.leerJSON("campers.json")
    idBuscar = input(f"\nIngrese el ID del camper a modificar: ")
    encontrado = False
    
    for i in campers:
        if i["ID"] == idBuscar:
            encontrado = True
            print(f"--- Camper encontrado: {i['nombre']} {i['apellido']} ---")
            print("""
1. Nombre
2. Apellido
3. ID (Documento)
4. Dirección
5. Acudiente
6. Celular
7. Fijo
8. Jornada
9. Estado
10. ID Grupo
11. Riesgo
12. Rendimiento
13. Nota Teórica
14. Nota Práctica
15. Nota Definitiva
16. Clave
17.regresar""")
            while True:
                opcion = input(f"\nSeleccione el número del dato a modificar: ")
                try:
                    if opcion == "1":
                        valor = input("Nuevo Nombre (solo letras): ")
                        if not valor.replace(" ", "").isalpha(): 
                            raise ValueError("Solo letras.")
                        i["nombre"] = valor
                    
                    elif opcion == "2":
                        valor = input("Nuevo Apellido (solo letras): ")
                        if not valor.replace(" ", "").isalpha(): 
                            raise ValueError("Solo letras.")
                        i["apellido"] = valor
                    
                    elif opcion == "3":
                        valor = input("Nuevo ID (solo números): ")
                        if not valor.isdigit(): 
                            raise ValueError("Solo números.")
                        i["ID"] = valor
                    
                    elif opcion == "4":
                        i["direccion"] = input("Nueva Dirección: ")
                    
                    elif opcion == "5":
                        valor = input("Nuevo Acudiente (solo letras): ")
                        if not valor.replace(" ", "").isalpha(): 
                            raise ValueError("Solo letras.")
                        i["acudiente"] = valor
                    
                    elif opcion == "6":
                        valor = input("Nuevo Celular: ")
                        if not valor.isdigit(): 
                            raise ValueError("Solo números.")
                        i["celular"] = valor
                    
                    elif opcion == "7":
                        valor = input("Nuevo Fijo: ")
                        if not valor.isdigit(): 
                            raise ValueError("Solo números.")
                        i["fijo"] = valor
                    
                    elif opcion == "8":
                        valor = input("Nueva Jornada (1: Mañana, 2: Tarde): ")
                        if valor not in ["1", "2"]: 
                            raise ValueError("Debe ser 1 o 2.")
                        i["jornada"] = valor
                    
                    elif opcion == "9":
                        validos = ["En proceso de ingreso", "Inscrito", "Aprobado", "reprobado", "Cursando", "Graduado", "Expulsado", "Retirado"]
                        print(f"Opciones válidas: {validos}")
                        valor = input("Nuevo Estado: ")
                        if valor not in validos: 
                            raise ValueError("Estado no válido.")
                        i["estado"] = valor
                    
                    elif opcion == "10":
                        valor = input("Nuevo ID Grupo (solo números): ")
                        if not valor.isdigit(): 
                            raise ValueError("Solo números.")
                        i["IDgrupo"] = valor
                    
                    elif opcion == "11":
                        niveles = ["bajo", "medio", "alto"]
                        valor = input(f"Nuevo Riesgo ({niveles}): ").lower()
                        if valor not in niveles: 
                            raise ValueError("Opción inválida.")
                        i["riesgo"] = valor
                    
                    elif opcion == "12":
                        niveles = ["bajo", "medio", "alto"]
                        valor = input(f"Nuevo Rendimiento ({niveles}): ").lower()
                        if valor not in niveles: 
                            raise ValueError("Opción inválida.")
                        i["rendimiento"] = valor
                    
                    elif opcion == "13" or opcion == "14":
                        valor = int(input("Nueva Nota (0-100): "))
                        if not (0 <= valor <= 100): 
                            raise ValueError("Rango 0-100.")
                        if opcion=="13":
                            i["pruebaInicial"]["teorica"] = valor
                        else:
                            i["pruebaInicial"]["practica"] = valor
                        i["pruebaInicial"]["definitiva"]=(i["pruebaInicial"]["practica"]+i["pruebaInicial"]["teorica"])/2
                    
                    elif opcion == "15":
                        valor = float(input("Nueva Nota Definitiva (0-100): "))
                        if not (0 <= valor <= 100): 
                            raise ValueError("Rango 0-100.")
                        i["pruebaInicial"]["definitiva"] = valor
                    
                    elif opcion == "16":
                        i["clave"] = input("Nueva Clave (alfanumérica): ")
                    
                    elif opcion== "17":
                        return
                    else:
                        print("Opción inválida.")
                        continue
                    
                    guardarLeerJSON.guardarJSON("campers.json", campers)
                    print(f"\n¡Información actualizada exitosamente!")
                    break

                except ValueError:
                    print(f"\n Por favor, ingrese el dato correctamente.")
            
            break 
            
    if not encontrado:
        print("No se encontró un camper con ese ID.")
        