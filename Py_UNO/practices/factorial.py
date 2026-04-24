def factorial():
        n = int(input("Ingrese el numero a sacar el factorial: "))

        factorial = 1
        for x in range(1, n+1):
            factorial = factorial*x

        return factorial

