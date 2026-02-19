#casos base
#1) que se hayan alcanzado el numero maximo de grupos de la mañana y de la tarde. que estos esten llenos 
#2) que haya menos de 25 campers aprobados, que los grupos sean menos del numero maximo pero esten llenos

#casos recursivos
#1)si #aprobados >=25 abre grupos (pasan a estado cursando)
#2)sino si hay grupos abiertos, agrega campers hasta 35

import guardarLeerJSON, random
from datetime import datetime, timedelta
trainers=guardarLeerJSON.leerJSON("trainers.json")
def formarGrupo(jornada):
    grupos=guardarLeerJSON.leerJSON("grupos.json")
    campers=guardarLeerJSON.leerJSON("campers.json")
    trainers=guardarLeerJSON.leerJSON("trainers.json")
    aulas=guardarLeerJSON.leerJSON("aulaDisponibilidad.json")

    #separacion de grupos por jornada
    if jornada=="1":
        maximo=6
        grupo=[i for i in grupos if i["horario"] in ["1","2"] ]
        grupocampers=[i for i in campers if i["jornada"] == "1" ]
        trainersjornada=[]
        for i in trainers:
            llavesHorario=i["horario"].keys()
            for k in llavesHorario:
                if k in ["1","2"]:
                    trainersjornada.append(i)
                    break
    elif jornada=="2":
        maximo=4
        grupo=[i for i in grupos if i["horario"] in ["3","4"]]
        grupocampers=[i for i in campers if i["jornada"] == "2" ]
        trainersjornada=[]
        for i in trainers:
            listatrainers=i["horario"].keys()
            for k in listatrainers:
                if k in ["3","4"]:
                    trainersjornada.append(i)
                    break
        
    if grupos:
        #caso base #1
        contador=0
        for i in grupo:
            if i["estado"]=="cerrado":
                contador+=1
        if jornada=="1" and contador==maximo:
            print("se han alcanzado el numero maximo de grupos de la mañana")
            print(f"el numero de campers aprobados de la jornada de la mañana que quedaron sin grupo es: {len([i for i in grupocampers if i['estado']=='aprobado'])}")
            return
        else:
            if jornada=="2" and contador==maximo:
                print("se han alcanzado el numero maximo de grupos de la tarde")
                print(f"el numero de campers aprobados de la jornada de la tarde que quedaron sin grupo es: {len([i for i in grupocampers if i['estado']=='aprobado'])}")
                return
        
        #caso base #2
        aprobados=[i for i in grupocampers if i["estado"]=="aprobado"]
        numeroGruposAbiertos=len([i for i in grupos if i["estado"]=="abierto"])
        if len(aprobados)<aulas[0]["capacidad"]["minimo"] and numeroGruposAbiertos==0:
            print("hay menos de 25 campers aprobados, los grupos son menos del numero maximo pero estan llenos")
            print(f"el numero de campers aprobados en esta jornada que quedaron sin grupo es: {len([i for i in grupocampers if i['estado']=='aprobado'])}")
            return
    
    aprobados=[i for i in grupocampers if i["estado"]=="aprobado"]
    #caso base #3
    if len(aprobados)==0:
        print("no quedan mas campers aprobados para formar grupos, se han formado todos los grupos posibles o inicialmente no habia campers aprobados")
        return
    # caso recursivo
    #1)si #aprobados >=25 abre grupos (pasan a estado cursando)
    if len(aprobados)>=aulas[0]["capacidad"]["minimo"] and len(grupo)<4:
        #ruta
        listaRuta=[]
        for i in trainersjornada:
            for j in i["especialidad"]:
                if j not in listaRuta:
                    listaRuta.append(j)
        ruta=random.choice(listaRuta)

        #horario, aula, nombre del grupo, fecha de inicio y fecha de finalizacion
        if not grupos:
            ID=100
        else:
            ID=100
            for i in grupos:
                if int(i["ID"])==ID:
                    ID+=1
                else:
                    break
        salonAsignado=False
        for i in aulas[1]["aulas"]:
            if jornada=="1":
                for j in ["1","2"]:
                    if i["horario"][j] == None:
                        i["horario"][j]=str(ID)
                        horario=j
                        nombreAula=i["nombre"]
                        salonAsignado=True 
                        break
                if salonAsignado==True:
                    break
            else:
                for j in ["3","4"]:
                    if i["horario"][j] == None:
                        if j=="4" and aulas[1]["aulas"][0]["horario"]["4"]!=None:
                            break
                        i["horario"][j]=str(ID)
                        horario=j
                        nombreAula=i["nombre"]
                        salonAsignado=True   
                        break
                if salonAsignado==True:
                    break
        #trainer
        listaTrainerPrimera=[]
        for i in trainersjornada:
            if ruta in i["especialidad"]:
                for j in i["horario"]:
                    if j==horario and i["horario"][j][0] == None:
                        listaTrainerPrimera.append(i)
                        break
        trainerasignado=random.choice(listaTrainerPrimera)
        trainerasignado["horario"][horario][0]=str(ID)
        #nombre del grupo
        nombre=trainerasignado["nombre"][0:1]+horario
        #fecha de inicio
        fechas=[datetime.strptime(i["fechaInicial"], "%d-%m-%Y").date() for i in grupocampers]
        fechaInicio=max(fechas)+timedelta(days=6)
        if fechaInicio.weekday()==5:
            fechaInicio+=timedelta(days=2)
        elif fechaInicio.weekday()==6:
            fechaInicio+=timedelta(days=1)  
        #fecha de finalizacion
        fechaFinal=fechaInicio + timedelta(weeks=40)
        if fechaFinal.weekday()==5:
            fechaFinal+=timedelta(days=2)
        elif fechaFinal.weekday()==6:
            fechaFinal+=timedelta(days=1) 
        fechaFinal=fechaFinal.strftime("%d-%m-%Y")
        fechaInicio=fechaInicio.strftime("%d-%m-%Y")
        
        #cambio de estado a cursando y lista de ID campers que estan en el grupo
        for i in range(0,aulas[0]["capacidad"]["minimo"]):
            aprobados[i]["estado"]="cursando"
            aprobados[i]["IDgrupo"]=str(ID)
        listaAprobados=[i["ID"] for i in aprobados[:aulas[0]["capacidad"]["minimo"]]]
        
        
        #creacion del grupo
        grupo={
            "ID":str(ID),
            "jornada":"6am-2pm" if jornada=="1" else "2pm-10pm",
            "horario":horario,
            "nombre":nombre,
            "estado":"abierto",
            "campers":listaAprobados,   
            "IDtrainer":trainerasignado["ID"],
            "ruta":ruta,
            "salon":nombreAula,
            "numeroDeCampers":len(listaAprobados),
            "FechaInicio": fechaInicio,
            "FechaFinal": fechaFinal
            }           
        
        grupos.append(grupo)
        print("se ha creado exitosamente el grupo "+nombre)
        guardarLeerJSON.guardarJSON("grupos.json", grupos)
        guardarLeerJSON.guardarJSON("aulaDisponibilidad.json", aulas)
        guardarLeerJSON.guardarJSON("trainers.json", trainers)
        guardarLeerJSON.guardarJSON("campers.json", campers)
        formarGrupo(jornada)
        
        
        #2)sino si hay grupos abiertos, agrega campers hasta 35 
    else:
            gruposAbiertos=[i for i in grupo if i["estado"]=="abierto"]
            if gruposAbiertos:
                for i in gruposAbiertos:
                    
                    while i["numeroDeCampers"]<aulas[0]["capacidad"]["maximo"] and len(aprobados)>0:
                        i["campers"].append(aprobados[0]["ID"])
                        aprobados[0]["estado"]="cursando"
                        aprobados[0]["IDgrupo"]=i["ID"]
                        aprobados.pop(0)
                        i["numeroDeCampers"]+=1
                    if i["numeroDeCampers"]==aulas[0]["capacidad"]["maximo"]:
                        i["estado"]="cerrado"
                guardarLeerJSON.guardarJSON("grupos.json", grupos)
                guardarLeerJSON.guardarJSON("campers.json", campers)
                formarGrupo(jornada)
