import numpy as np

def f(x):
    return x**2 * np.exp(x)

h = 0.01
x0 = 1.2

def diferencia_adelante(f, x0, h):
    return (f(x0 + h) - f(x0)) / h

def extremo_tres_puntos(f, x0, h):
    return (-3*f(x0) + 4*f(x0 + h) - f(x0 + 2*h)) / (2*h)

def punto_medio_tres_puntos(f, x0, h):
    return (f(x0 + h) - f(x0 - h)) / (2*h)

def cinco_puntos_extremo(f, x0, h):
    return (-25*f(x0) + 48*f(x0 + h) - 36*f(x0 + 2*h) + 16*f(x0 + 3*h) - 3*f(x0 + 4*h)) / (12*h)

def cinco_puntos_medio(f, x0, h):
    return (f(x0 - 2*h) - 8*f(x0 - h) + 8*f(x0 + h) - f(x0 + 2*h)) / (12*h)

adelante = diferencia_adelante(f, x0, h)
extremo_tres = extremo_tres_puntos(f, x0, h)
punto_medio = punto_medio_tres_puntos(f, x0, h)
cinco_puntos_ext = cinco_puntos_extremo(f, x0, h)
cinco_puntos_med = cinco_puntos_medio(f, x0, h)

# print de resultados
print(f"Diferencias hacia adelante: {adelante}")
print(f"Extremo de tres puntos: {extremo_tres}")
print(f"Punto medio tres puntos: {punto_medio}")
print(f"Cinco puntos en el extremo: {cinco_puntos_ext}")
print(f"Cinco puntos en el medio: {cinco_puntos_med}")
