#casos base
#1) que se hallan alcanzado el numero maximo de grupos de la mañana y de la tarde. que estos esten llenos 
#2) que haya menos de 25 campers aprobados, que los grupos sean menos del numero maximo pero esten llenos

#casos recursivos
#1)si #aprobados >=25 abre grupos (pasan a estado cursando)
#2)sino si hay grupos abiertos, agrega campers hasta 35

import guardarLeerJSON

grupos=guardarLeerJSON.leerJSON("grupos.json")
campers=guardarLeerJSON.leerJSON("campers.json")
trainers=guardarLeerJSON.leerJSON("trainers.json")
aulas=guardarLeerJSON.leerJSON("aulaDisponibilidad.json")

