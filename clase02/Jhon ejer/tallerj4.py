#queremos que todas y cada una de ellas consuman la misma cantidad de refrescos ¿Cuántas latas de refresco sobrarán?

cajas_de_refresco = 9
contenido_de_una_caja_en_latas = 24
personas_invitadas = 56

contenido_total_de_latas_en_todas_las_cajas = cajas_de_refresco*contenido_de_una_caja_en_latas
total_de_latas_que_le_corresponde_a_persona = contenido_total_de_latas_en_todas_las_cajas/personas_invitadas

print(round(total_de_latas_que_le_corresponde_a_persona%1*personas_invitadas))

