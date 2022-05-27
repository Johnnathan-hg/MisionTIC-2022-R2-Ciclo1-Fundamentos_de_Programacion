
def numero_par_o_impa (numero) :
    if numero % 2 == 0 :
        mensaje = 'El numero es par.'
    else : 
        mensaje = 'El mumero es impar.'
    return mensaje

print (" ingrese el numero que se analizara para saber si es par o impar")
numero_texto = input ()
num = int (numero_texto)
resultado = numero_par_o_impa ( num )
print (resultado)




