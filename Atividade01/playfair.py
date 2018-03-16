# coding=utf-8

#FUNCOES#

def matrix(key):
    matrix = []
    for e in key.upper():
        if e not in matrix:
            matrix.append(e)
    alfa = "ABCDEFGHIJLMNOPQRSTUVXZWY"

    for e in alfa:
        if e not in matrix:
            matrix.append(e)
    matrix_montada = []

    for e in range(5):
        matrix_montada.append('')

    matrix_montada[0] = matrix[0:5]
    matrix_montada[1] = matrix[5:10]
    matrix_montada[2] = matrix[10:15]
    matrix_montada[3] = matrix[15:20]
    matrix_montada[4] = matrix[20:25]

    return matrix_montada

def separar_duplas(message):
    mens = []

    for i in message:
        if i != " ":
            mens.append(i)
    p = 0
    for e in range(len(mens) / 2):
        if mens[p] == mens[p+1] and mens[p] == "X":
            mens.insert(p + 1, "Z")
        elif mens[p] == mens[p+1] and mens[p] != "X":
            mens.insert(p + 1, "X")
        p += 2

    if len(mens) % 2 != 0:
        if mens[len(mens) - 1] == "X":
            mens.append("Z")
        else:
            mens.append("X")
    duplas = []
    for i in range(0, len(mens), 2):
        duplas.append(mens[i:i + 2])
    return duplas

def posicao(matrix, letra):
    x = 0
    y = 0
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letra:
                x = i
                y = j
    return x, y

def cifrar(messege):
    mensagem = separar_duplas(message)
    mtx = matrix(key)
    mensagem_cifrada = []

    for i in mensagem:
        lin1, col1 = posicao(mtx, i[0])
        lin2, col2 = posicao(mtx, i[1])
        if lin1 == lin2:
            if col1 == 4:
                col1 = -1
            if col2 == 4:
                col2 = -1
            mensagem_cifrada.append(mtx[lin1][col1 + 1])
            mensagem_cifrada.append(mtx[lin1][col2 + 1])
        elif col1 == col2:
            if lin1 == 4:
                lin1 = -1
            if lin2 == 4:
                lin2 = -1
            mensagem_cifrada.append(mtx[lin1 + 1][col1])
            mensagem_cifrada.append(mtx[lin2 + 1][col2])
        else:
            mensagem_cifrada.append(mtx[lin1][col2])
            mensagem_cifrada.append(mtx[lin2][col1])

    msg = "".join(mensagem_cifrada)

    return msg

def decifrar(messege):
    mensagem = separar_duplas(messege)
    mtx = matrix(key)
    mensagem_decifrada = []

    for i in mensagem:
        lin1, col1 = posicao(mtx, i[0])
        lin2, col2 = posicao(mtx, i[1])
        if lin1 == lin2:
            if col1 == 4:
                col1 = -1
            if col2 == 4:
                col2 = -1
            mensagem_decifrada.append(mtx[lin1][col1 - 1])
            mensagem_decifrada.append(mtx[lin1][col2 - 1])
        elif col1 == col2:
            if lin1 == 4:
                lin1 = -1
            if lin2 == 4:
                lin2 = -1
            mensagem_decifrada.append(mtx[lin1 - 1][col1])
            mensagem_decifrada.append(mtx[lin2 - 1][col2])
        else:
            mensagem_decifrada.append(mtx[lin1][col2])
            mensagem_decifrada.append(mtx[lin2][col1])

    msg = "".join(mensagem_decifrada)

    return msg

#++++++++MAIN++++++++#

loop = True
while loop:

    print "╔══════════════════════════╗"
    print "║      Cifra Playfair      ║"
    print "╚══════════════════════════╝"
    escolha = input("ESCOLHA: \n1 - Cifrar \n2 - Decifrar\n3 - Sair\n" )

    if escolha == 1:
        key = raw_input("Chave : ")
        message = raw_input("Mensagem : ").upper()

        print "Matrix: "
        for k in matrix(key):
            for j in k:
                print j,
            print
        print "Mensagem cifrada: "
        print cifrar(message)

    elif escolha == 2:
        key = raw_input("Chave : ")
        mgs_decifrada = raw_input("Mensagem Cifrada:: ").upper()

        print "Matrix: "
        for k in matrix(key):
            for j in k:
                print j,
            print

        print "Mensagem decifrada: "
        print decifrar(mgs_decifrada)
    elif escolha == 3:
        loop = False
    else:
        print "Exception"