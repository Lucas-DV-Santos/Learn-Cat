print('=====Canais/Professores para estudos=====')
sistema = True

while sistema:
    print('1-Continuar para ver canais de estudos\n2- Sair ')
    escolha = int(input(': '))
    if escolha == 1:
        print('Escolha a matéria\n1 - Biologia\n2 - Filosofia\n3 - Sociologia\n4 - Física\n5 - Geografia\n6 - História\n7 - Inglês\n8 - Matemática\n9 - Português\n10 - Redação\n11 - Química')
        escolhaMateria = int(input(': '))
        match escolhaMateria:
            case 1:
                print('')
            case 2:
                print('')
            case 3:
                print('')
            case 4:
                print('')
    else:
        sistema = False
