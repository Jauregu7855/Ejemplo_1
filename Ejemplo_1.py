# Ejemplo 1

print("-----INICIO-------")

class Mayor:

    def Numeros(self):

        A = []
        for i in range(1, 6):
            Numero = int(input("Ingresa un Numero: "))
            A.append(Numero)

        # Numero Mayor
        B = A[0]
        for i in A:
            if i > B:
                B = i
        print("El numero Mayor es: " + str(B))

        # Numero Menor
        C = A[0]
        for i in A:
            if i < C:
                C = i
        print("El numero Menor es: " + str(C))

    def Ejemplo(self):

        print("-----------2--------------")
        float_list = [i * j for i in range(1, 10) for j in range(1, 10)]
        print(float_list)


Mayor_F = Mayor()
Mayor_F.Numeros()
Mayor_F.Ejemplo()

print("------FIN-------")
