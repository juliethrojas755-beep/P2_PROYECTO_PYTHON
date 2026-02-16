import guardarLeerJSON
def validacion(datos):
           
    while (True):
        ID=input("por favor ingrese su documento de identidad (ID)")
        if not ID.isdigit(): 
            print("debe digitar unicamente numeros")
            continue
        break
    while(True):
        clave=input("digite el numero de la clave") 
        if not clave.isdigit(): 
            print("debe digitar unicamente numeros")
            continue
        break 
    for i in datos:
        if ID==i["ID"] and clave==i["clave"]:
            print("ingreso autorizado")
            return True
    return False


def iniciarSesion(opcion):
    print("-"*80)
    print(f"\t***Informacion personal registrada en el sistema***")
    print("-"*80+f"\n\n")
    if opcion==1:
        datos=guardarLeerJSON.leerJSON("campers.json") 
        return validacion(datos)
        
    elif opcion==2:
        datos=guardarLeerJSON.leerJSON("trainers.json")
    elif opcion==3:
        datos=guardarLeerJSON.leerJSON("trainers.json")