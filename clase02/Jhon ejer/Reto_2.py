def cliente ( informacion:dict)-> dict:
  
  apto=True
  if informacion["edad"] > 18:
    atraccion = "X-Treme" 
    total_boleta = 20000
    if informacion["primer_ingreso"] == True:
      total_boleta = 20000*0.95
  elif informacion["edad"] >= 15 and informacion["edad"] <= 18:
    atraccion = "Carros chocones"
    total_boleta = 5000
    if informacion["primer_ingreso"] == True:
      total_boleta = 5000*0.93
  elif informacion["edad"] >= 7 and informacion["edad"] < 15:
    atraccion = "Sillas voladoras"
    total_boleta = 10000
    if informacion["primer_ingreso"] == True:
      total_boleta = 10000*0.95
  
  elif informacion["edad"] < 7 :
    atraccion ="N/A"
    total_boleta ="N/A"
    apto=False
  
  reporte = {}
  reporte["nombre"]=informacion["nombre"] 
  reporte["edad"]=informacion["edad"] 
  reporte["atraccion"]=atraccion 
  reporte["apto"]=apto 
  reporte["primer_ingreso"]=informacion["primer_ingreso"]
  reporte["total_boleta"]=total_boleta
  return reporte


	
informacion = {
    'id_cliente': 1,
    'nombre': 'Johana Fernandez',
    'edad': 20,
    'primer_ingreso': False
}
print(cliente(informacion))


help(cliente)