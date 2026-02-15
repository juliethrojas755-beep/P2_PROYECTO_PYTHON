<<<<<<< HEAD
def menu_principal ():
    while True:
      print ("=======CAMPUSLANDS===========")
      print ("1. Camper")
      print ("2. Trainer ")
      print ("3. Coordinador")

      opcion = input("Seleccione una opcion:")  

      match opcion:
         
         case 1:
            print("Entrando al menu del camper")
         case 2: 
            print("Entrando al menu del trainer ")
         case 3:
            print("Entrando al menu del coordinador")

def  menu_camper ():
=======
#=================================
#=== MENU INSCRIPCION CAMPER=====
#=================================

def  menu_inscripcion ():
>>>>>>> 72a1455 (Submenu inscripcion del camper)
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

def menu_trainer ():
  while True:
     print ("n|=============MENU TRAINER=============")
     print("1. Ver ruta asignada")
     print ("2. Registrar notas")
     print ("3. Ver campers asignados")    
     print ("4. Volver")
   
     opcion = input ("Seleccione una opcion:")
    
     match opcion:
        case 1:
<<<<<<< HEAD
         print
       #sfsfsdfs
>>>>>>> d90d2eb264fa678a03541df21feb29e2bd5545f4
=======
         print ("Esta es tu ruta asignada ")
        case 2:
         print ("Registro de notas...")
        case 3: 
         print ("Campers asignados")
        case 4:
         break
        case _:
         print ("Opcion invalida")
             
       
>>>>>>> 72a1455 (Submenu inscripcion del camper)
