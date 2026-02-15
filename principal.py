

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

def menu_trainer ():
  while True:
     print ("n|=============MENU TRAINER=============")
     print("1. Ver ruta asignada")
     print ("2. Registrar notas")
     print ("3. Ver campers asignados")    
     print ("4. Volver")
   
     opcion = input ("Seleccione una opcion:")
     
