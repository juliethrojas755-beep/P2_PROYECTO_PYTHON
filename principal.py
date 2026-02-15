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
   while True:
      print ("n|========MENU CAMPER============")
      print ("1.Ver mis datos ")
      print ("2.Ver estado academico ")
      print ("3.Ver Ruta")
      print ("4. Volver")
      


      opcion = input ("Seleccione una opcion: ")

      match opcion:

       case 1:
        print("Monstrando tus datos ")
        
       case 2:
        print("Mostrando tu estado academico")

       case 3:
        print ("Mostando tu ruta ")

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
         print
       #sfsfsdfs
>>>>>>> d90d2eb264fa678a03541df21feb29e2bd5545f4
