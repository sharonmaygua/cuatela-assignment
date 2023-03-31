def crear_tabla():
    tabla = [["-", "-", "-", "-"],
             ["-", "-", "-", "-"],
             ["-", "-", "-", "-"],
             ["-", "-", "-", "-"], ]
    return tabla


def mostrar_tabla(tabla):
    for fila in tabla:
        print(fila)


def formato_ficha(ficha):
    columna = int(ficha[0])
    fila = int(ficha[1])
    nombre_ficha = ficha[2]
    return [columna, fila, nombre_ficha]


def insertar_en_tabla(datos_ficha, tabla):
    columna = int(datos_ficha[0])

    fila = int(datos_ficha[1])
    ficha = datos_ficha[2]

    tabla[columna][fila] = ficha
    return tabla


def tabla_por_defecto(tabla, lista_Fichas):
    for ficha in lista_Fichas:
        tabla = insertar_en_tabla(ficha, tabla)
    return tabla


def mostrar_fichas_del_jugador(lista_fichas):
    contador = 1
    for ficha in lista_fichas:
        print(f"Ficha {contador}: ({ficha[0]},{ficha[1]})")
        contador += 1


def limite_matriz(fila, columna):
    if fila < 0 or fila > 3 or columna < 0 or columna > 3:
        return False
    else:
        return True


def mover_ficha(tabla, ficha, movimiento):
    nueva_ficha = ficha

    if (movimiento == "N"):  # Arriba
        nueva_ficha = [ficha[0], ficha[1], ficha[2]]
        pos_libres = 0
        for i in range(ficha[0] - 1, -1, -1):  # Revisa lugares hacia arriba
            if tabla[i][ficha[1]] == "-":
                nueva_ficha[0] = i
                pos_libres += 1
            else:
                break
        if pos_libres > 0:  # Si hay lugares libres hacia arriba
            tabla = insertar_en_tabla([ficha[0], ficha[1], "-"], tabla)  # Borra la ficha actual
            tabla = insertar_en_tabla(nueva_ficha, tabla)  # Inserta la ficha en la nueva posición encontrada
        else:
            print("Movimiento invalido")

    if (movimiento == "E"):  # Hacia la derecha
        nueva_ficha = [ficha[0], ficha[1], ficha[2]]
        pos_libres = 0
        for j in range(ficha[1] - 1, -1, -1):  # Revisa lugares hacia la derecha
            if limite_matriz(ficha[0], j) and tabla[ficha[0]][j] == "-":
                nueva_ficha[1] = j
                pos_libres += 1
            else:
                break
        if pos_libres > 0:  # Si hay lugares libres hacia la derecha
            tabla = insertar_en_tabla([ficha[0], ficha[1], "-"], tabla)  # Borra la ficha actual
            tabla = insertar_en_tabla(nueva_ficha, tabla)  # Inserta la ficha en la nueva posición encontrada
        else:
            print("Movimiento invalido")

    if (movimiento == "S"):  # Abajo
        nueva_ficha = [ficha[0], ficha[1], ficha[2]]
        pos_libres = 0
        for i in range(ficha[0] + 1, len(tabla)):  # Revisa lugares hacia abajo
            if tabla[i][ficha[1]] == "-":
                nueva_ficha[0] = i
                pos_libres += 1
            else:
                print("Movimiento invalido")
        if pos_libres > 0:  # Si hay lugares libres hacia abajo
            tabla = insertar_en_tabla([ficha[0], ficha[1], "-"], tabla)  # Borra la ficha actual
            tabla = insertar_en_tabla(nueva_ficha, tabla)  # Inserta la ficha en la nueva posición encontrada
        else:
            print("Movimiento invalido")

    if (movimiento == "O"):  # Hacia la izquierda
        nueva_ficha = [ficha[0], ficha[1], ficha[2]]
        pos_libres = 0
        for j in range(ficha[1] + 1, len(tabla[ficha[0]])):  # Revisa lugares hacia la izquierda
            if limite_matriz(ficha[0], j) and tabla[ficha[0]][j] == "-":
                nueva_ficha[1] = j
                pos_libres += 1
            else:
                break
        if pos_libres > 0:  # Si hay lugares libres hacia la izquierda
            tabla = insertar_en_tabla([ficha[0], ficha[1], "-"], tabla)  # Borra la ficha actual
            tabla = insertar_en_tabla(nueva_ficha, tabla)  # Inserta la ficha en la nueva posición encontrada
        else:
            print("Movimiento invalido")

    if (movimiento == "NE"):  # Diagonal hacia el noreste
        nueva_ficha = [ficha[0], ficha[1], ficha[2]]
        pos_libres = 0
        i = ficha[0] - 1
        j = ficha[1] + 1
        while limite_matriz(i, j):
            if tabla[i][j] == "-":
                nueva_ficha = [i, j, ficha[2]]
                pos_libres += 1
                i -= 1
                j += 1
            else:
                break
        if pos_libres > 0:  # Si hay lugares libres en la diagonal
            tabla = insertar_en_tabla([ficha[0], ficha[1], "-"], tabla)  # Borra la ficha actual
            tabla = insertar_en_tabla(nueva_ficha, tabla)  # Inserta la ficha en la nueva posición encontrada
        else:
            print("Movimiento invalido")

    if (movimiento == "SE"):  # Diagonal hacia el sureste
        nueva_ficha = [ficha[0], ficha[1], ficha[2]]
        pos_libres = 0
        i = ficha[0] + 1
        j = ficha[1] + 1
        while limite_matriz(i, j):
            if tabla[i][j] == "-":
                nueva_ficha = [i, j, ficha[2]]
                pos_libres += 1
                i += 1
                j += 1
            else:
                break
        if pos_libres > 0:  # Si hay lugares libres en la diagonal
            tabla = insertar_en_tabla([ficha[0], ficha[1], "-"], tabla)  # Borra la ficha actual
            tabla = insertar_en_tabla(nueva_ficha, tabla)  # Inserta la ficha en la nueva posición encontrada
        else:
            print("Movimiento invalido")

    if (movimiento == "SO"):  # Diagonal hacia el suroeste
        nueva_ficha = [ficha[0], ficha[1], ficha[2]]
        pos_libres = 0
        i = ficha[0] + 1
        j = ficha[1] - 1
        while limite_matriz(i, j):
            if tabla[i][j] == "-":
                nueva_ficha = [i, j, ficha[2]]
                pos_libres += 1
                i += 1
                j -= 1
            else:
                break
        if pos_libres > 0:  # Si hay lugares libres en la diagonal
            tabla = insertar_en_tabla([ficha[0], ficha[1], "-"], tabla)  # Borra la ficha actual
            tabla = insertar_en_tabla(nueva_ficha, tabla)  # Inserta la ficha en la nueva posición encontrada
        else:
            print("Movimiento invalido")

    if (movimiento == "NO"):  # Diagonal superior derecha
        nueva_ficha = [ficha[0], ficha[1], ficha[2]]
        pos_libres = 0
        i = ficha[0] - 1
        j = ficha[1] - 1
        while limite_matriz(i, j):
            if tabla[i][j] == "-":
                nueva_ficha = [i, j, ficha[2]]
                pos_libres += 1
                i -= 1
                j -= 1
            else:
                break
        if pos_libres > 0:
            tabla = insertar_en_tabla([ficha[0], ficha[1], "-"], tabla)  # Borra la ficha actual
            tabla = insertar_en_tabla(nueva_ficha, tabla)  # Inserta la ficha en la nueva posición encontrada
        else:
            print("Movimiento invalido")
    return nueva_ficha