from clases import Suma, Resta, Multiplicacion

def main():
    a = 10
    b = 5

    suma = Suma()
    resta = Resta()
    multiplicacion = Multiplicacion()

    print(f"La suma de {a} y {b} es {suma.sumar(a, b)}")
    print(f"La resta de {a} y {b} es {resta.restar(a, b)}")
    print(f"La multiplicación de {a} y {b} es {multiplicacion.multiplicar(a, b)}")

if __name__ == "__main__":
    main()