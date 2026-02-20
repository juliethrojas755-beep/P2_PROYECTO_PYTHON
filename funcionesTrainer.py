# Editar notas por camper(ingresar notas y cambiarlas) segun el modulo.

# se especifica el modulo y el tipo de nota que se va a cambiar o editar.
# puede dejar el espacio sin llenar si decide no calificar
# el camper se identifica con ID
# el trainer solo puede cambiar las notas de los campers que esten en alguno de los grupos que dirije

import guardarLeerJSON

print("-"*90)
print("\t**-----Bienvenido al modulo de calificaciones para trainers-----**\naqui podra registrar o cambiar las calificaciones de los campers que esten en alguno de los grupos que dirije.")
print("-"*90)
grupos = guardarLeerJSON.leerJSON("grupos.json")
campers = guardarLeerJSON.leerJSON("campers.json")
trainers = guardarLeerJSON.leerJSON("trainers.json")
seccionAcademica = guardarLeerJSON.leerJSON("seccionAcademica.json")

def registrarCambiarCalificacion(ID):
    gruposAsignados=[]
    for trainer in trainers:
        #no se pone else porque el trainer autenticó sus credenciales con su ID
        if trainer["ID"]==ID:
            for i in trainer["horario"]:
                if trainer["horario"][i][0]!=None:
                    #en gruposAsignados se guardan los grupos que el trainer tiene asignados, 
                    # para luego mostrarle solo esos grupos y que pueda elegir a cual de ellos 
                    # quiere cambiarle la calificacion a un camper
                    gruposAsignados.append(trainer["horario"][i][0])
            break
    #caso en el que el trainer no tiene grupos asignados
    if len(gruposAsignados)==0:
        print("No hay grupos asignados a este trainer.")
        return
    #el trainer tiene grupos asignados.
    else:
        #se garantiza la integridad del dato IDcamper
        while(True):
            IDcamper=input("Ingrese el ID del camper al que desea asignarle o cambiarle la calificacion: ").strip()
            if not IDcamper.isdigit():
                print("digite unicamente numeros ")
                continue
            if not 8<=len(IDcamper)<=10:
                print("El ID debe tener entre 8 y 10 numeros")
                continue
            break
        #se verifica que el ID del camper exista en la lista de campers
        camperExiste=False
        registrarCalificacion=False
        for i in campers:
            if i["ID"]==IDcamper:
                #se verifica que el camper este cursando en alguno de los grupos
                if i["estado"]=="cursando":
                    for k in grupos:
                        #se verifica que estemos en uno de los grupos asignados al trainer
                        if k["ID"] in gruposAsignados:
                            for j in k["campers"]:
                                #se verifica que el camper esté en el grupo
                                if j==IDcamper:
                                    #encontramos al camper
                                    camperExiste=True
                                    while(True):
                                        #menu de ingreso o cambio de nota
                                        opcionModulo=input("""Ingrese el numero de uno de los siguientes modulos segun donde quiera agregar o cambiar una nota:
1. Fundamentos
2. Web
3. formal
4. BasesDeDatos
5. Backend
6. regresar
:""").strip()
                                        if opcionModulo.isdigit():
                                            break
                                        else:
                                            print("Digite unicamente numeros")
                                            continue
                                    modulos=["Fundamentos","Web","formal","BasesDeDatos","Backend"]
                                    if opcionModulo=="6":
                                        return
                                    while(True):
                                        
                                        nota={  "ID":IDcamper,
                                                "IDgrupo":k["ID"],
                                                "notaTeorica":int(input("Ingrese la nota teorica: ")),
                                                "notaPractica":int(input("Ingrese la nota practica: ")),
                                                "notaActividades":int(input("Ingrese la nota actividades: ")),
                                            }
                                        nota["notaFinal"]=(nota["notaTeorica"]*0.3 + nota["notaPractica"]*0.6 + nota["notaActividades"]*0.1)
                                        nota["estado"] = "aprobado" if nota["notaFinal"]>=60 else "reprobado"
                                        seccionAcademica[1]["modulos"][int(opcionModulo)-1]["notas"].append(nota)
                                        registrarCalificacion=True
                                        break
                                        
    print(registrarCalificacion)                                  
                                            
    if camperExiste==False:
        print("El ID del camper no existe o el camper no esta cursando en ninguno de los grupos asignados a este trainer.") 
        return
    if registrarCalificacion==True:
        guardarLeerJSON.guardarJSON("seccionAcademica.json",seccionAcademica)
        print("Calificacion registrada o cambiada exitosamente.")
    else:
        print("No se pudo registrar o cambiar la calificacion.")

registrarCambiarCalificacion("91256838")