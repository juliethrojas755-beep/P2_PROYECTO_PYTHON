# Citacion
# Crea la fecha del examen (maximo la semana siguiente de la fecha actual).
# Inicialmente solicita el ID y los busca en camper:

# si lo encuentra: la fecha debe ser de lunes a viernes y se debe guardar en la info del camper.
# sino se encuentra: imprimir que no esta registrado en la base de datos
import guardarLeerJSON
from datetime import date, timedelta

def citacion():
    
    print("-"*80)
    print(f"\t***Bienvenido a Campuslands. Gracias por confiar en nosotros***")
    print("-"*80)
    print("Para asignar la cita de presentacion de la prueba inicial, por favor siga los siguientes pasos:"+f"\n\n")
    while (True):
        ID=input("por favor ingrese su documento de identidad (ID)")
        if not ID.isdigit(): 
            print("debe digitar unicamente numeros")
            continue
        if not 8<=len(ID)<=10:
            print("el ID debe ser contener entre 8 y 10 numeros")
            continue
        break
    campers=guardarLeerJSON.leerJSON("campers.json")
    ids=[i["IDcamper"] for i in campers]
    if ID not in ids:
        print("Usted no se encuentra registrado dentro de la base de datos de campers.")
        print("Por favor, primero realice el registro")
    else:
        fechaActual=date.today()
        fechaCita=fechaActual+timedelta(days=2)
        if fechaActual.weekday()==5:
            fechaCita=fechaActual+timedelta(days=2)
        elif fechaActual.weekday()==6:
            fechaCita=fechaActual+timedelta(days=1)
        fechaCita=fechaCita.strftime("%d-%m-%Y")
        for i in campers:
            if i["ID"]==ID:
                if i["fechaInicial"]!= None:
                    print("usted ya tiene asignada la fecha de presentacion de la prueba inicial")
                    print(f"La fecha es: {i["fechaInicial"]}")
                    break
                i["fechaInicial"]=fechaCita
                i["estado"]="inscrito"
                print("El proceso de asignacion de la cita ha sido exitoso.")
                print(f"Su cita es la siguiente: {i["fechaInicial"]}")
                guardarLeerJSON.guardarJSON("campers.json",campers)
                break