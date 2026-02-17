
import guardarLeerJSON
from datetime import date, timedelta
import random

def citacion():
# Citacion
# Crea la fecha del examen (maximo la semana siguiente de la fecha actual).
# Inicialmente solicita el ID y los busca en camper:

# si lo encuentra: la fecha debe ser de lunes a viernes y se debe guardar en la info del camper.
# sino se encuentra: imprimir que no esta registrado en la base de datos
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
    ids=[i["ID"] for i in campers]
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
                print("El proceso de asignacion de la cita ha sido exitoso.")
                print(f"Su cita es la siguiente: {i["fechaInicial"]}")
                guardarLeerJSON.guardarJSON("campers.json",campers)
                break


def revisarCitacion():
# revision de la citacion:
# Se debe imprimir la fecha de citacion si el ID esta registrado.
# sino, decir que no esta registrado
    print("-"*80)
    print(f"\t***Bienvenido a Campuslands. Gracias por confiar en nosotros***")
    print("-"*80)
    while (True):
        ID=input("Para revisar la fecha asignada de la prueba inicial, por favor digite su ID: ")
        if not ID.isdigit(): 
            print("debe digitar unicamente numeros")
            continue
        if not 8<=len(ID)<=10:
            print("el ID debe ser contener entre 8 y 10 numeros")
            continue
        break
    campers=guardarLeerJSON.leerJSON("campers.json")
    ids=[i["ID"] for i in campers]
    if ID not in ids:
        print("\nUsted no se encuentra registrado dentro de la base de datos de campers.")
        print("Por favor, primero realice el registro")
    else:
        for i in campers:
            if i["ID"]==ID:
                if i["fechaInicial"]==None :
                    print("\nusted se encuentra registrado pero no ha solicitado la cita para la prueba.")
                    break
                else:
                    print(f"\nLa fecha de la cita para la presentacion de la prueba es el {i["fechaInicial"]}")
  
def realizacionPrueba(ID): 
    campers=guardarLeerJSON.leerJSON("campers.json")
    camper=[i for i in campers if i["ID"]==ID]
    if camper[0]["pruebaInicial"]["teorica"] is None:
        camper[0]["pruebaInicial"]["teorica"]=random.randint(10,100)
        camper[0]["pruebaInicial"]["practica"]=random.randint(10,100)
        camper[0]["estado"]="inscrito"
        print("""Felicitaciones por terminar el examen, ahora espera a que el coordinador revise tu examen""")
        guardarLeerJSON.guardarJSON("campers.json",campers)
    else:
        print("ya tienes regristrada la nota de la prueba. Contactate con el coordinador ")
# Realizacion de la prueba:

# Primero debe haber ingresado previamente con sus credenciales (ID y clave).LISTO
# Al momento de ingresar a esta opcion se genera automaticamente la nota de la 
# prueba teorica Y la prueba practica.
# Inmediatamebte despues a lo anterior se cambia el estado del camper a "inscrito".

# MODIFICACION
# El calculo de la nota final con el promedio de las dos notas de la prueba se deja 
# para el momento en que el coordinador vaya a pasar al estudiante del estado de registrado a aprobado.