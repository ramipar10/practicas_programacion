#lista de valores de produccion

produccion_diaria = [120, 85, 95 ,150, 110]

print("REPORTE DE PRODUCCION")

#Estructura elegida: Bucle for y condicional if/else
for cantidad in produccion_diaria:
    if cantidad >= 100:
        print(f"{cantidad} unidades producidas : Meta cumplida")
    else:
        print(f"{cantidad} unidades producidas : Produccion baja")
    