def Retiro(ID):
    import guardarLeerJSON

    print("-"*80)
    print(f"\t***Modulo de solicitudes***")
    print("-"*80)

    valor=input("Ha seleccionado la opcion de retiro voluntario.\nSi desea continuar digite 1, de lo contrario, digite cualquier otra tecla: ")
    if valor=="1":
        campers=guardarLeerJSON.leerJSON("campers.json")
        camper=[i for i in campers if i["ID"]==ID]
        camper[0]["estado"]="retirado"
        print("la solicitud se ha realizado con exito")
        guardarLeerJSON.guardarJSON("campers.json",campers)