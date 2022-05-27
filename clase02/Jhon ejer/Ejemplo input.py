
"""


print ("ingrese su nombre")
nombre = input()
apellido = input("ingrese su apellido: ")
print("sunombre completo es:", nombre, apellido)
print(2)
print(type(nombre))
print(type(apellido))
print(type(2))
"""
def CDT(usuario: str, capital: int, tiempo:int):
    porcentage_interes = 0.03
    porcentage_a_perder = 0.02
    valor_intereses_ganados = (capital * porcentage_interes * tiempo) / 12
   
    
    if tiempo > 2 : 
         valor_total = valor_intereses_ganados + capital
         return "Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}" .format (usuario, capital, tiempo, valor_total)
    else:
         if tiempo < 3 : 
             valor_a_perder = capital * porcentage_a_perder
             valor_total_perdida = capital - valor_a_perder
            
             return "Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}" .format (usuario, capital, tiempo, valor_total_perdida)    



usuario = str (input ("ingrese nombre: "))
capita = int (input ("ingrese cantidad de dinero "))
tiempo = int (input ("tiempo CDT "))

print (CDT(usuario, capita, tiempo))

            




 
    





    



