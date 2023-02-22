forma1 = input("Qual a forma?[O ou X]\n")
forma2 ='O' if 'X' == forma1 else 'X'
if forma1 =='X' or forma1 == 'O':
    a = ['a1', 'a2', 'a3']
    b = ['b1', 'b2', 'b3']
    c = ['c1', 'c2', 'c3']
    def mostarJogo():
        print(" %s | %s | %s " % (a[0], a[1], a[2]))
        print("----|----|----")
        print(" %s | %s | %s " % (b[0], b[1], b[2]))
        print("----|----|----")
        print(" %s | %s | %s " % (c[0], c[1], c[2]))

    def checarVitoria(forma):
        if a[0] == a[1] == a[2] or b[0] == b[1] == b[2] or c[0] == c[1] == c[2]:
            print('O "%s" venceu!!!' % forma)
            return True
        elif a[0] == b[1] == c[2] or c[0] == b[1] == a[2]:
            print('O "%s" venceu!!!' % forma)
            return True
        elif a[0] == b[0] == c[0] or a[1] == b[1] == c[1] or a[2] == b[2] == c[2]:
            print('O "%s" venceu!!!' % forma)
            return True
        else:
            return False

    def validarJogada(jogada):
        if len(jogada) < 1:
            print('Informe um espaco valido!')
            return False
        elif jogada[0] != 'a' and jogada[0] != 'b' and jogada[0] != 'c':
            print('Informe um espaco valido!')
            return False
        elif int(jogada[1]) > 3 or int(jogada[1]) < 1:
            print('Informe um espaco valido!')
            return False
        elif len(jogada) > 3:
            print('Informe um espaco valido!')
            return False
        else:
            t = True
            print(jogada[0])
            print(a[int(jogada[1])-1])
            print(a[int(jogada[1])-1]  == "O ")
            if jogada[0] == 'a' and (a[int(jogada[1])-1] == "X " or a[int(jogada[1])-1]  == "O "):
                t = False
                print('Informe um espaco valido!')
                return False
            if jogada[0] == 'b' and (b[int(jogada[1])-1] == "X " or b[int(jogada[1])-1]  == "O "):
                t = False
                print('Informe um espaco valido!')
                return False
            if jogada[0] == 'c' and (c[int(jogada[1])-1] == "X " or c[int(jogada[1])-1]  == "O "):
                t = False
                print('Informe um espaco valido!')
                return False
            if t == True:
                return True    
        
    mostarJogo()

    i= 0
    z= True
    while i < 9:
        while z == True:
            jogada = input("Qual a posicao jogador 1?\n").lower()
            if validarJogada(list(jogada)):
                if jogada[0] == 'a':
                    a[int(jogada[1])-1] = forma1 + " "
                if jogada[0] == 'b':
                    b[int(jogada[1])-1] = forma1 + " "
                if jogada[0] == 'c':
                    c[int(jogada[1])-1] = forma1 + " "
                break
            

        mostarJogo()
        if checarVitoria(forma1):
            break

        i+=1
        if i == 9:
            break

        while z == True:
            jogada = input("Qual a posicao jogador 2?\n").lower()
            if validarJogada(list(jogada)):
                if jogada[0] == 'a':
                    a[int(jogada[1])-1] = forma2 + " "
                if jogada[0] == 'b':
                    b[int(jogada[1])-1] = forma2 + " "
                if jogada[0] == 'c':
                    c[int(jogada[1])-1] = forma2 + " "
                break

        mostarJogo()
        if checarVitoria(forma2):
            break
        i+=1

    if i == 9:
        print("Empate!!!")

else:
    print("informe uma forma valida!")

