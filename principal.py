import inicioSesion, ingresoDatosCamper, pruebaInicial,solicitud,informacion_personal
#capa 1
def menu_principal():
   while True:
     print ("--------CAMPUSLANDS------")
     print("1. Camper")
     print ("2. Trainer")
     print ("3. Coordinacion")
     print ("4. Salir")

     opcion=input ("Seleccione una opcion: ")

     match opcion:
       
       case "1":
         menu_camper(opcion)
       case "2":
         validacion,ID=inicioSesion.iniciarSesion(opcion)
         if validacion:
          menu_trainer(ID)
         else: 
           print("Ingreso denegado. Intentelo nuevamente")
       case "3":
         validacion,ID=inicioSesion.iniciarSesion(opcion)
         if validacion:
          menu_coordinacion(ID)
         else: 
           print("Ingreso denegado. Intentelo nuevamente")
       case "4": 
         print ("Saliendo del sistema....")
         break
       case _:
         print ("Opcion invalida")

#CAMPER
def menu_camper(opcionAnterior):
  while True:
    print("------MENU CAMPER------")
    print ("1. Inscripcion")
    print ("2. Ver informacion personal")
    print ("3. Iniciar sesion")
    print ("4. Regresar")

    opcion = input ("Seleccione una opcion: ")

    match opcion:
      case "1":
        menu_inscripcion()
      case "2":
        informacion_personal.ver_info_camper()
      case "3":
        validacion,ID=inicioSesion.iniciarSesion(opcionAnterior)
        if validacion:
          menu_sesion_camper (ID)
        else: 
           print("Ingreso denegado. Intentelo nuevamente")
      case "4":
        break
      case _:
        print ("Opcion invalida")
        
#submenu de camper.inscripcion (opcion=1)
def  menu_inscripcion ():

   while True:
      print ("=======INSCRIPCION============")
      print ("1.Ingreso de identidad ")
      print ("2.Agendar prueba inicial")
      print ("3.Revisar fecha prueba inical")
      print ("4.Regresar")
      opcion = input ("Seleccione una opcion: ")
      match opcion:
       case "1":
        ingresoDatosCamper.registrarCamper()
       case "2":
        pruebaInicial.citacion()
       case "3": 
        pruebaInicial.revisarCitacion()
       case "4":
         break
       case _:
         print ("Opcion invalida")

#submenu Camper.iniciarSesion (Camper opcion=3 )
def menu_sesion_camper(ID):
  while True:
    print ("----SESION CAMPER-----")
    print ("1.Realizar prueba inicial")
    print ("2.Ver horario ")
    print ("3.Ver notas")
    print("4.Solicitar retiro voluntario")
    print ("5.Regresar")

    opcion = input ("Seleccione una opcion: ")

    match opcion:
      case "1":
        pruebaInicial.realizacionPrueba(ID)
      case "2":
        print ("Horario (:)")
      case "3": 
        menu_ver_notas(ID)
      case "4":
        solicitud.Retiro(ID)
      case "5":
        break
      case _:
        print ("Opcion invalida")

def menu_ver_notas(ID):
   while True:
      print ("----VER NOTAS----")
      print ("1. General ")
      print ("2. Por modulo")
      print ("3. Regresar")
      opcion = input ("Seleccione una opcion:")

      match opcion:
        case "1":
          print("Notas generales (:)")
        case "2":
          print ("Notas por modulo (:)")
        case "3":
          break
        case _:
          print ("Opcion invalida")

def menu_modulos ():
  while True:
    print ("""-----SELECCIONE MODULO
           
1. Fundamentos de programación
2. Programación Web
3. Programación formal
4. Bases de datos
5. Backend
6. Regresar""")
    opcion = input ("Seleccione una opcion: ")
    match opcion :
      case "1":
        print ("Fundamentos de programación")
      case "2": 
        print ("Programación Webo")
      case "3":
        print ("Programación formal ")
      case "4":
        print("Bases de datos")
      case "5":
        print("Backend")
      case "6":
        break
      case _:
        print ("Opcion invalida")

def menu_registrar_notas():
  while True:
    print ("---REGISTRAR CALIFICACIONES-----")
    print ("1.Por camper")
    print ("2.Por grupo")
    print ("3.Regresar")

    opcion= input ("Seleccione una opcion:")
    match opcion:
     case "1":
        menu_modulos()
     case "2":
        menu_modulos()
     case "3":
        break
     case _:
        print ("Opcion invalida")

def menu_modulo_academico():
  while True:
    print ("----MODULO ACADEMICO-----")
    print ("1. Ver campers con nota por grupo")
    print ("2. Registrar calificaciones ")
    print ("3. Regresar")

    opcion= input ("Seleccione una opcion: ")

    match opcion:
      case "1":
        print ("Lista de campers por grupo ()")
      case "2":
        menu_registrar_notas()
      case "3":
        break
      case _:
        print ("Opcion invalida")
#TRAINER
def menu_trainer(ID):
  while True:
    print ("------MENU TRAINER-----")
    print ("1. Informacion personal")
    print ("2. Modulo academico")
    print ("3. Regresar")

    opcion=input ("Seleccione una opcion:")
    match opcion:
      case "1":
        informacion_personal.ver_info_trainer(ID)
      case "2":
        menu_modulo_academico ()
      case "3":
        break
      case _:
        print("Opcion invalida")
#COORDINADOR
def menu_coordinacion(ID):
  while True:
    print ("------MENU COORDINACION-----")
    print ("1. Trainer (CRUD)")
    print ("2.Camper (CRUD)")
    print ("3.Modulo Reportes")
    print ("4.Modulo de matricula")
    print ("5. Agregar ruta")
    print ("6. informacion personal")
    print ("7. Salir")

    opcion= input ("Seleccione una opcion: ")

    match opcion:
      case "1":
        print ("Crud trainer ()")
      case "2":
        coordinadorCRUDCamper()
      case "3": 
        print("Modulo de reportes")
      case "4":
        print ("Modulo de matricula")
      case "5":
        print ("Agregando ruta")
      case "6":
        informacion_personal.ver_info_coordinacion(ID)
      case "7":
        break
      case _:
        print ("Opcion invalida")
        
def coordinadorCRUDCamper():
  while(True):
    print("-"*60)
    print("\t*** Espacio CRUD del camper ***")
    print("-"*60)
    
    print("""\nDigite una de las siguientes opciones 
          1.crear camper
          2.mostrar camper
          3.actualizar camper
          4.eliminar camper
          5.regresar""")
    
    opcion=input("escriba la respuesta aqui:")
    
    match opcion:
      case "1":
        print("crear")
      case "2":
        print("mostrar")
      case "3":
        print("actualizar")
      case "4":
        print("eliminar")
      case "5":
        break
      case _:
        print("te equivocaste, vuelve a intentarlo")
    
def coordinadorCRUDCamperActualizar():
  while(True):
    print("-"*60)
    print("\t*** Espacio para actualizar el camper ***")
    print("-"*60)
    
    print("""\nDigite una de las siguientes opciones 
1.Modificar cualquier dato de un camper. Dicho camper se busca por ID.
2.Rendimiento y riesgo acumulado despues de que salga la nota de cada modulo
3.Aprobar los inscritos que pasaron la prueba
4.regresar""")
    
    opcion=input("escriba la respuesta aqui:")
    
    match opcion:
      case "1":
        print("Modificar cualquier dato de un camper. Dicho camper se busca por ID")
      case "2":
        print("Rendimiento y riesgo acumulado despues de que salga la nota de cada modulo")
      case "3":
        print("Aprobar los inscritos que pasaron la prueba")
      case "4":
        break
      case _:
        print("te equivocaste, vuelve a intentarlo")
    
menu_principal()
        
