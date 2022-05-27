def CDT(usuario: str, capital: int, tiempo:int):
    
    if tiempo > 2 : 
         valor_total = (capital * 0.03 * tiempo) / 12 + capital
         return "Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}" .format (usuario, capital, tiempo, valor_total)
    else:
         if tiempo < 3 :
             valor_a_perder = capital * 0.02
             valor_total_perdida = capital - valor_a_perder
             return "Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}" .format (usuario, capital, tiempo, valor_total_perdida)


usuario = str (input ("ingrese nombre: "))
capita = int (input ("ingrese cantidad de dinero "))
tiempo = int (input ("tiempo CDT "))

print (CDT(usuario, capita, tiempo))