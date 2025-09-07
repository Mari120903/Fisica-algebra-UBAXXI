#Problema 1. Un ciclista parte del reposo y se desplaza en línea recta. A los 30 s alcanza una velocidad de 10 m/s. Si su aceleración es constante, determinar su aceleración y la distancia recorrida en ese lapso.

""" Lógica y código
Identifica las variables:

Velocidad inicial (v_i) = 0 m/s (parte del reposo)

Velocidad final (v_f) = 10 m/s

Tiempo (t) = 30 s

Aceleración (a) = ?

Distancia (x) = ?

Elige las fórmulas:

Para la aceleración: a=(v_f−v_i)/t

Para la distancia: x=v_it+1/2at 
2 """

# Problema 1 del parcial de Física: Movimiento Rectilíneo Uniformemente Variado (MRUV)

# Variables dadas
velocidad_inicial = 0.0  # en m/s (parte del reposo)
velocidad_final = 10.0   # en m/s
tiempo = 30.0            # en segundos

# 1. Calcular la aceleración (a = (vf - vi) / t)
aceleracion = (velocidad_final - velocidad_inicial) / tiempo

# 2. Calcular la distancia recorrida (x = vi*t + 1/2*a*t^2)
distancia = (velocidad_inicial * tiempo) + (0.5 * aceleracion * (tiempo**2))

# Mostrar los resultados
print(f"La aceleración del ciclista es: {aceleracion:.2f} m/s²")
print(f"La distancia recorrida es: {distancia:.2f} m")
