print("Hecho por: Nieto Alonso Yarei Alelhí")
print("Serie de Fibonacci")
def fibonacci_n_terms(n):
    if n <= 0:
        print("El número de términos debe ser mayor a 0.")
    else:
        a, b = 0, 1
        print(a, end=" ")
        for _ in range(1, n):
            print(b, end=" ") 
            a, b = b, a + b 
        print()  
num_terms = int(input("Introduce el número de términos: "))
fibonacci_n_terms(num_terms)
