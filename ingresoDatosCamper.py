import guardarLeerJSON

def registrarCamper():

    #lee la base de datos de campers.json
    campers=guardarLeerJSON.leerJSON("Campers.json")

    print("-"*70)
    print(f"\t\t***¡Bienvenido a Campusland!***")
    print("Por favor ingrese los siguientes datos para crear su cuenta como Camper")
    print("-"*70+f"\n\n")
    camper={}

    #nombre
    while(True):
        camper["nombre"]=input("digite su nombre (sin apellidos): ").strip()
        if camper["nombre"].replace(" ","").isalpha():
            break
        else:
            print("digite unicamente letras ")

    #apellido
    while(True):
        camper["apellido"]=input("digite su apellido: ").strip()
        if camper["apellido"].replace(" ","").isalpha():
            break
        else:
            print("digite unicamente letras ")

    #ID
    while(True):
        bandera=1
        camper["ID"]=input("digite su numero de ID: ").strip()
        if not camper["ID"].isdigit():
            print("digite unicamente numeros ")
            continue
        if not 8<=len(camper["ID"])<=10:
            print("El ID debe tener entre 8 y 10 numeros")
            continue
        if campers:#mira si la lista está vacia
            IDs=[i["ID"] for i in campers]#Lista de todos los ID de los campers
            for i in IDs:
                if camper["ID"]==i:
                    print("este numero de ID ya está registrado en el sistema. intentelo nuevamente")
                    bandera=0
                    break
        if bandera:
                break
    #Direccion
    camper["direccion"]=input("digite su direccion de residencia: ")

    #acudiente
    while(True):
        camper["acudiente"]=input("digite el nombre de su acudiente: ").strip()
        if camper["acudiente"].replace(" ","").isalpha():
            break
        else:
            print("digite unicamente letras ")

    #numero celular
    while(True):
        camper["celular"]=input("digite su numero de celular: ").strip()
        if camper["celular"].isdigit() and len(camper["celular"])==10 and camper["celular"][0]=="3":
            break
        else:
            print(f"Algo salió mal,intentelo nuevamente.\n Recuerde que:\n-debe digitar unicamente numeros\n-el celular debe tener 10 numeros\n-el primer numero debe ser 3 ")
            
    #numero fijo
    while(True):
        camper["fijo"]=input("digite su numero fijo, si no tiene, digite 0: ").strip()
        if ((camper["fijo"].isdigit() and len(camper["fijo"])==7) or camper["fijo"]=="0"):
            break
        else:
            print(f"Algo salió mal,intentelo nuevamente.\nRecuerde que:\n-digite unicamente numeros\n-deben ser 7 numeros\n-digite 0 si no tiene numero fijo ")

    #jornada
    while(True):
        print("Campusland cuenta con 2 jornadas, las cuales son:")
        print(f"1. Mañana (6am-2pm)\n2.Tarde(2pm-10pm)")
        camper["jornada"]=input(f"Digite el numero de la jornada que le interesa.\ndigite 0 en caso de que ambas jornadas le sirvan: ")
        if camper["jornada"] in ["0","1","2"]:
            break
        else:
            print("ERROR:Digitó una opcion invalida. Intentelo de nuevo")
    
    #----------LLAVES CON VALOR NULO (none):

    #estado
    camper["estado"]="en proceso de ingreso"  
    
    #grupo
    camper["IDgrupo"]=None
    
    #llamada de atencion
    camper["llamadaAtencion"]=[]
    
    #riesgo
    camper["riesgo"]=None

    #rendimiento
    camper["rendimiento"]=None

    #fecha de prueba inicial
    camper["fechaInicial"]=None

    #Prueba inicial
    camper["pruebaInicial"]={"teorica":None,"practica":None, "definitiva":None}

    #Clave
    camper["clave"]="123456789"

    #ingreso del estudiante a la base de datos
    campers.append(camper)

    print(campers)

    #actualizar la base de datos de campers
    guardarLeerJSON.guardarJSON("campers.json",campers)
    
registrarCamper()