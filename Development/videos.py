def sistemaCanaisVideos():
    print('=====Canais/Professores para estudos=====')
    sistema = True
    while sistema:
        print('1-Continuar para ver canais de estudos\n2- Sair ')
        escolha = int(input('Escolha: '))
        if escolha == 1:
            print('Escolha a matéria\n1 - Biologia🧬\n2 - Filosofia🤔\n3 - Sociologia👥\n4 - Física⚛️\n5 - Geografia🌍\n6 - História📜\n7 - Inglês📚\n8 - Matemática➗\n9 - Português✍️\n10 - Redação✍️\n11 - Química🧪')
            escolhaMateria = int(input('Escolha: '))
            match escolhaMateria:
                case 1:
                    print('Biologia!')
                    print('Professor: Pido Biologia\nCanal: https://www.youtube.com/@pidobiologia')
                case 2:
                    print('Filosofia!')
                    print('Professor: Clóvis de Barros Filho\nCanal: https://www.youtube.com/@clovisdebarrosoficial/featured ')
                case 3:
                    print('Sociologia!')
                    print('Professor: Clóvis de Barros Filho\nCanal: https://www.youtube.com/@clovisdebarrosoficial/featured')
                case 4:
                    print('Física!')
                    print('Professor: Boaro\nCanal: https://www.youtube.com/@professorboaro/videos')
                case 5:
                    print('Geografia!')
                    print('Professor: Rodolfo Alves Pena\nCanal: https://www.youtube.com/@TerraNegra/videos')
                case 6:
                    print('História!')
                    print('Professor: Débora Aladim\nCanal: https://www.youtube.com/@deboraaladim')
                case 7:
                    print('Inglês!')
                    print('Professor: Teacher Kenny\nCanal: https://www.youtube.com/@PROFESSORKENNYOFICIAL')
                case 8:
                    print('Matemática!')
                    print('Professor: Sandro Curió\nCanal: https://www.youtube.com/@sandrocuriodicasdemat')
                case 9:
                    print('Português!')
                    print('Professor: Noslen Borges \nCanal: https://www.youtube.com/@ProfessorNoslen')
                case 10:
                    print('Redação!')
                    print('Professor: Noslen Borges\nCanal: https://www.youtube.com/@ProfessorNoslen')
                case 11:
                    print('Química!')
                    print('Professor: Paulo Valim\nCanal: https://www.youtube.com/@paulovalim')
                case _:
                    print('Opção inválida!')     
        else:
            sistema = False
sistemaCanaisVideos()
