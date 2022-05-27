

# datos de entrada 
def notas_de_la_clase_ej2(nota: int) -> str:
    #validando los parametros
    if not isinstance(nota, float) and not isinstance(nota, int):
        return "la nota debe ser con valor numerico."
    # proceso 
    # if not(nota >= 0.0 and nota <= 5.0):
    if nota < 0 or nota > 5: # -(p and q) --> -p or -q
           return " La nota ingresada no es valida. "
    if nota >= 3.0:
        mensaje = "Ganó la materia. ¡Felicitaciones!" 
    else:
        mensaje = "Perdio la materia." 
    # salida    
    return "Su nota es: {}. {} .". format ( nota , mensaje )


#nota = float (input("ingrese nota : "))
#print(notas_de_la_clase_ej2(nota))

# 1. Diseñe un algoritmo que permita solicitar tanto el nombre como la edad de una persona y 
# posteriormente indicar si es “Mayor de edad” o “Menor de edad” según la información ingresada. 
# Una persona se considera mayor de edad si tiene 18 años o más.

def nombre_edad_de_persona (nombre:str, edad:int) -> str : 
        
    if edad <= 18: 
        return " es mayor de edad. "
    else:
        return "ingrese nombre completo {} edad {}". format(nombre, edad) 

nombre = str (input("ingrese nombre: "))
edad = int (input("ingrese edad: "))
print(nombre_edad_de_persona(nombre, edad))

