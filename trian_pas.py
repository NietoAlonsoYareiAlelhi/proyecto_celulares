print("Hecho por: NIETO ALONSO YAREI ALELHÍ Y OLIMAN SORIANO FRANCISCO PAUL")
print("Realizar el programa del triángulo de pascal en Python")
def generar_imprimir_triangulo_pascal(n):
    triangulo = [[1]]  
    for i in range(1, n):
        fila_anterior = triangulo[i - 1]
        fila = [1] 
        for j in range(1, i):
            fila += [fila_anterior[j - 1] + fila_anterior[j]]
        fila += [1] 
        triangulo += [fila] 
    for i in range(len(triangulo)):
        espacios = " " * (n - i - 1) 
        print(espacios) 
        for numero in triangulo[i]:
            print(numero, " ", sep="", end="") 
        print() 
filas = int(input("Ingrese el número de filas para el Triángulo de Pascal: "))
generar_imprimir_triangulo_pascal(filas)

