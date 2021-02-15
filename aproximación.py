objetivo = int(input('Escoge un entero: '))
epsilon = 0.001
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontró la raíz cuadrada del {objetivo}')
else:
    print(f'La raíz cuadrada del objetivo es {respuesta}')
