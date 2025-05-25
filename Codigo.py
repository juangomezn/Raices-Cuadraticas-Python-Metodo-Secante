from math import sqrt

a = float(input("Ingrese Valor de a: "))
b = float(input("Ingrese Valor de b: "))
c = float(input("Ingrese Valor de c: "))

if a == 0:
    print("No es una ecuación cuadrática (a ≠ 0)")

else:
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        print("Sin solución real")
    else:

        x1 = (-b - sqrt(discriminante)) / (2 * a)
        print(f"X1 (Fórmula Cuadrática) = {x1}")

        iteraciones = 0
        tolerancia = 0.0001
        error = 1

        xPrevio = -0.6
        xActual = -0.5

        while error > tolerancia and iteraciones < 1000:
            fPrevio = a * xPrevio**2 + b * xPrevio + c
            fActual = a * xActual**2 + b * xActual + c

            siguiente = xActual - fActual * (xActual - xPrevio) / (fActual - fPrevio)
            error = abs(siguiente - xActual)

            xPrevio = xActual
            xActual = siguiente
            iteraciones += 1

        x2 = xActual
        print(f"X2 (Secante) = {x2}")
        print(f"Iteraciones: {iteraciones}")