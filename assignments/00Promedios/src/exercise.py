def main():
    #escribe tu código abajo de esta línea
    print("Promedio de 10 numeros")

    s = 0
    cp = 0
    ci = 0

    for i in range(10):
        n = int(input("Dame un numero:"))

        if n % 2 == 0:
            cp = cp + 1
        else:
            ci = ci + 1
        
        s = s + n
    
    promedio = s / 10

    print(f"El promedio de los valores capturados es: {promedio}")
    print(f"El total de valores pares fue: {cp}")
    print(f"El total de valores impares fuer: {ci}")

if __name__=='__main__':
    main()
