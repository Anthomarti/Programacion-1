from datetime import datetime

# Fechas
fecha1 = datetime(2002, 5, 28)
fecha2 = datetime(2024, 5, 28)

# Calcular la diferencia en días
diferencia_dias = (fecha2 - fecha1).days

# Calcular la diferencia en años
diferencia_anos = fecha2.year - fecha1.year

# Calcular la diferencia en meses
diferencia_meses = (fecha2.year - fecha1.year) * 12 + (fecha2.month - fecha1.month)

# Ajustar si el día del mes de la fecha inicial es mayor que el de la fecha final
if fecha2.day < fecha1.day:
    diferencia_meses -= 1

print(f"Diferencia entre las fechas: {diferencia_anos} años, {diferencia_meses} meses y {diferencia_dias} días")