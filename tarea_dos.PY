print("Bienvenido al programa para calcular el volumen de una arepa")

#Definir la conversion de tazas a cucharadas y cucharadas a cucharaditas
cucharada_a_cucharadita = 3
taza_a_cucharada = 16

# Pedir al usuario las cantidades de los ingredientes en tazas y cucharaditas
tazas_de_agua = float(input("Indique la cantidad de agua en tazas: "))
tazas_de_harina = float(input("Indique la cantidad de haria en tazas: "))
cdta_de_sal = float(input("Indique la cantidad de sal en cucharaditas: "))
cda_de_aceite = float(input("Indique la cantidad de aceite en cucharadas: "))

# Convertir las cantidades a cucharaditas
agua_uno = tazas_de_agua*taza_a_cucharada*cucharada_a_cucharadita 
harina_uno = tazas_de_harina*taza_a_cucharada*cucharada_a_cucharadita
sal_uno = cdta_de_sal
aceite_uno = cda_de_aceite*cucharada_a_cucharadita

# Convertir las cantidades a cucharadas
agua_dos = tazas_de_agua * taza_a_cucharada
harina_dos = tazas_de_harina * taza_a_cucharada
sal_dos = cdta_de_sal / 3
aceite_dos = cda_de_aceite

# calcular el volumen inicial en cucharadas y cucharaditas

volumen_inicial_cucharaditas = agua_uno + harina_uno + sal_uno + aceite_uno
volumen_inicial_cucharadas = agua_dos + harina_dos + sal_dos + aceite_dos

# calcular el volumen total en cucharadas y cucharaditas, considerando que el 10% se evapora

volumen_total_cucharaditas = volumen_inicial_cucharaditas * 0.9
volumen_total_cucharadas = volumen_inicial_cucharadas * 0.9

# Mostrar el resultado en cucharaditas y cucharadas

print(f"EL volumen final de la arepa en cucharaditas despues de la copcion es: {volumen_total_cucharaditas}")
print(f"EL volumen final de la arepa en cucharadas despues de la copcion es: {volumen_total_cucharadas}")