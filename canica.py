import random

colors = ['rojo', 'blanco', 'verde', 'morado']
canicas = 100
canicas_colores = {color: 0 for color in colors}

# Asignamos un color aleatorio a cada canica
for i in range(canicas):
    color = random.choice(colors)
    canicas_colores[color] += 1

print("Canicas por color:", canicas_colores)

# Calculamos la probabilidad de obtener una canica de cada color
probabilidades = {color: count / canicas for color, count in canicas_colores.items()}

print("Probabilidades:", probabilidades)

# Preguntamos al usuario por un color específico
buscado = input("¿Qué color quieres buscar?: ")

# Buscamos la probabilidad de obtener una canica de ese color
probabilidad = probabilidades.get(buscado, 0)

print("La probabilidad de obtener una canica de color", buscado, "es", probabilidad)