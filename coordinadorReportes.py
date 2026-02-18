from guardarLeerJSON import leerJSON

def campersInscritos():
    campers = leerJSON("campers.json")
    
    print("====== CAMPERS EN ESTADO INSCRITO ======\n")
    encontrados = False
    for camper in campers:
        if camper["estado"] == "inscrito":
            encontrados = True
            print(f"Nombre: {camper['nombre']} {camper['apellido']}")
            print(f"ID: {camper['ID']}")
            print(f"Jornada: {camper['jornada']}")
            print("-" * 40)

    if not encontrados:
        print("No hay campers en estado inscrito.")

def campersAprobaronExamen():
    campers = leerJSON("campers.json")
    
    print("====== CAMPERS QUE APROBARON EL EXAMEN INICIAL ======")
    
    encontrados = False

    for camper in campers:
        pruebaInicial = camper.get("pruebaInicial", {})
        notaDefinitiva = pruebaInicial.get("definitiva")

        if notaDefinitiva is not None and notaDefinitiva >= 60:
            encontrados = True
            print(f"Nombre: {camper['nombre']} {camper['apellido']}")
            print(f"ID: {camper['ID']}")
            print(f"Nota Definitiva: {notaDefinitiva}")
            print("-" * 40)

    if not encontrados:
        print("No hay campers que hayan aprobado el examen inicial.")

def entrenadoresCampusLands():
    trainers = leerJSON("trainers.json")

    print("====== ENTRENADORES QUE TRABAJAN CON CAMPUSLANDS ======")

    if not trainers:
        print("No hay entrenadores registrados.")
        return

    for trainer in trainers:
        nombre = trainer["nombre"].strip()
        idTrainer = trainer.get("ID")
        especialidad = trainer.get("especialidad")

        print(f"Nombre: {nombre}")
        print(f"ID: {idTrainer}")
        print(f"Especialidad: {especialidad}")
        print("-" * 40)

def campersRendimientoBajo():
    campers = leerJSON("campers.json")
    
    print("====== CAMPERS CON BAJO RENDIMIENTO======\n")
    if not campers:
        print("la lista de campers esta vacia")
        return
    
    encontrados = False
    for camper in campers:
        if camper["rendimiento"] is not None and camper["rendimiento"]== "bajo":
            encontrados = True
            print(f"Nombre: {camper['nombre']} {camper['apellido']}")
            print(f"ID: {camper['ID']}")
            print(f"Jornada: {camper['jornada']}")
            print("-" * 40)

    if not encontrados:
        print("No hay campers con rendimiento")