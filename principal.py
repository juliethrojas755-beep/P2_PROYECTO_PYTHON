

def  menu_inscripcion ():

   while True:
      print ("n|=======INSCRIPCION============")
      print ("1. Ingreso de identidad ")
      print ("2.Agendar prueba iniciial")
      print ("3.Revisar fecha prueba inical")
      print ("4.Salir")


      opcion = input ("Seleccione una opcion: ")

      match opcion:

       case 1:
        print("Ingreso de identidad (:) ")
        
       case 2:
        print("Agendar prueba inicial (:)")
      
       case 3: 
        print ("Revisar fecha prueba inicial (:)")
       case 4:
         break
       case _:
         print ("Opcion invalida")
         
def menu_ver_notas():
   while True:
      print ("|n----VER NOTAS----")
      print ("1.General ")
      print ("2. Por modulo")
      print ("3. Regresar")
      opcion = input ("Seleccione una opcion:")

      match opcion:
        case 1:
          print("Notas generales (:)")

        case 2:
          print ("Notas por modulo (:)")
        case 3:
          break
        case _:
          print ("Opcion invalida")

def menu_sesion_camper():
  while True:
    print ("n|----SESION CAMPER-----")
    print ("1.Realizar prueba inicial")
    print ("3.Ver notas ")
    print ("4. Solicitar retiro volutanrio")
    print("5. Regresar")

    opcion = input ("Seleccione una opcion: ")

    match opcion:
      case 1:
        print ("Prueba inicial (:)")
      case 2:
        print ("Horario (:)")
      case 3: 
        menu_ver_notas
      case 4:
        print ("Retiro voluntario solicitado (:)")
      case 5:
        break
      case _:
        print ("Opcion invalida")

def menu_camper():
  while True:
    print("|n------MENU CAMPER------")
    print ("1. Inscripcion")
    print ("2. Ver informacion personal")
    print ("3. Iniciar sesion")
    print ("4. Regresar")

    opcion = input ("Seleccione una opcion: ")

    match opcion:
      case 1:
        menu_inscripcion ()
      case 2:
        print ("Imformacion personal")
      case 3:
        menu_sesion_camper ()
      case 4:
        break
      case _:
        print ("Opcion invalida")

def menu_modulos ():
  while True:
    print ("|n-----SELECCIONE MODULO")
    print ("1. Introduccion a la programacion")
    print ("2. Bakend")
    print ("3.Bases de datos")
    print ("4. Regresar")

    opcion = input ("Seleccione una opcion: ")
    match opcion :
       case 1  | 2 | 3 :
        print ("Registrar notas")
        print ("-Examen practico")
        print ("Examen teorico ")
        print ("-Actividades")
       case 4:
        break
       case _:
        print ("Opcion invalida")




