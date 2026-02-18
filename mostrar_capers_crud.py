
import guardarLeerJSON

def mostrar_campers():
    campers = guardarLeerJSON.leerJSON("campers.json")

    if not campers:
        print("No hay campers registrados")
        return

    print("\n-------- LISTA DE CAMPERS --------")

    for c in campers:
        print("\n-------------------------------")
        print("ID:", c.get("ID"))
        print("Nombre:", c.get("nombre"), c.get("apellido"))
        print("Estado:", c.get("estado"))
        print("Jornada:", c.get("jornada"))
        print("Celular:", c.get("celular"))
        print("Acudiente:", c.get("acudiente"))

        print("ID Grupo:", c.get("IDgrupo"))
        print("Riesgo:", c.get("riesgo"))
        print("Rendimiento:", c.get("rendimiento"))

        print("Prueba Inicial:")
        prueba = c.get("pruebaInicial", {})
        print("  Teórica:", prueba.get("teorica"))
        print("  Práctica:", prueba.get("practica"))
        print("  Definitiva:", prueba.get("definitiva"))

mostrar_campers()