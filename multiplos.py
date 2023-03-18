def contar_multiplos():
    numeros = []
    for i in range(20):
        num = int(input("Ingrese un número entero: "))
        numeros.append(num)
    
    mult_2 = 0
    mult_3 = 0
    mult_2_3 = 0
    
    for num in numeros:
        if num % 2 == 0:
            mult_2 += 1
        if num % 3 == 0:
            mult_3 += 1
        if num % 2 == 0 and num % 3 == 0:
            mult_2_3 += 1
    
    print("Resultados:")
    print(f"Cantidad de números múltiplos de 2: {mult_2}")
    print(f"Cantidad de números múltiplos de 3: {mult_3}")
    print(f"Cantidad de números múltiplos de 2 y 3: {mult_2_3}")

contar_multiplos()