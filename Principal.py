def conengrafo(TP, n):
    A, i = [[0] * n for _ in range(n)], 0
    for y in TP:
        i += 1
        j = 0
        for x in y:
            j += 1
            if x != -1 and x != 0:
                A[i][j] = 1
    return A


def busca(grafo, inicio, encontrar):
    lista = []

    pila = [[inicio]]

    while pila:
        ruta = pila.pop()
        nodo = ruta[-1]

        vecinos = []
        contador = 0
        for w in grafo[int(nodo)]:
            contador += 1
            if w == 1:
                vecinos.append(str(contador - 1))

        for siguiente in set(vecinos) - set(ruta):
            if siguiente == encontrar:
                lista.append(ruta + [siguiente])
            else:
                pila.append(ruta + [siguiente])

    return lista, len(lista)


if __name__ == '__main__':
    n = int(input("Deme el numero de nodos"))
    TP = [[0] * n for _ in range(n)]
    print("deme la matriz")
    for i in range(n):
        TP[i] = [int(j) for j in input().split(" ")]
    grafo = conengrafo(TP, n + 1)

    for i in range(1, n + 1):
        print()
        for j in range(1, n + 1):
            caminos = busca(grafo, str(i), str(j))
            print("De " + str(i) + " a " + str(j) + " hay " + str(caminos[1]) + " caminos y son:", caminos[0])
