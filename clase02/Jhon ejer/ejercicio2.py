peso_producto_en_gramo = 100
precio_producto = 5.95
peso_kilo_en_gramo =  1000

precio_pro_gramo = precio_producto / peso_producto_en_gramo
precio_por_kilo = precio_pro_gramo * peso_kilo_en_gramo
precio_por_kilo = round(precio_por_kilo, 2)

print(round(precio_por_kilo))

