usuarios = []
matriz = []

def login():
    print("\nSISTEMA DE LOGIN")

    nome = input("Digite o nome de usuário: ")
    senha = input("Digite sua senha: ")

    for u in usuarios:
        if u["nome"] == nome and u["senha"] == senha:
            print("USUÁRIO LOGADO")
            escolher_menu()
            return

    print("USUÁRIO OU SENHA INCORRETA")


def cadastro():
    print("\nSISTEMA DE CADASTRO")

    nome = input("Digite o nome de usuário: ")

    for u in usuarios:
        if u["nome"] == nome:
            print("USUÁRIO JÁ CADASTRADO")
            return

    senha = input("Digite sua senha: ")
    usuarios.append({"nome": nome, "senha": senha})
    print("Cadastro realizado!")


def sair():
    print("SAINDO...")


def MenuCadastro():
        while True:
            print("\n==== MENU DE CADASTRO ====\n")

            escolha = int(input("[1] - LOGIN\n[2] - CADASTRO\n[3] - SAIR\nEscolha: "
                 ))

            if escolha == 1:
                login()
                input("\nPressione ENTER para voltar ao menu...")

            elif escolha == 2:
                cadastro()
                input("\nPressione ENTER para voltar ao menu...")

            elif escolha == 3:
                sair()
                break

            else:
                print("Opção inválida")
                input("\nPressione ENTER para voltar ao menu...")

def sistemaCanaisVideos():

    print('\n=====Canais/Professores para estudos=====')
    sistema = True
    while sistema:
        print('\n[1]-Continuar para ver canais de estudos\n[2]- Sair ')
        escolha = int(input('Escolha: '))
        if escolha == 1:
            print('\nEscolha a matéria\n[1] - Biologia🧬\n[2] - Filosofia🤔\n[3] - Sociologia👥\n[4] - Física⚛️\n[5] - Geografia🌍\n[6] - História📜\n[7] - Inglês📚\n[8] - Matemática➗\n[9] - Português✍️\n[10] - Redação✍️\n[11] - Química🧪')
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
            print("\n" * 50)
            escolher_menu()

def quimica():
    print('\n🐱 LearnCat: Miau! Descubra como a matéria se transforma e entenda a química presente no nosso cotidiano.')
def biologia():
    print('\n🐱 LearnCat: Miau! Vamos estudar os seres vivos e seus processos. Faça exercícios para fixar o conteúdo e aprender mais rápido!')
def filosofia():
    print('\n🐱 LearnCat: Miau! Explore as ideias dos grandes pensadores e desenvolva seu senso crítico com reflexões e debates.')
def sociologia():
    print('\n🐱 LearnCat: Miau! Vamos entender como a sociedade funciona e como as pessoas interagem no mundo ao nosso redor.')
def fisica():
    print('\n🐱 LearnCat: Miau! Descubra as leis que explicam os fenômenos da natureza e pratique exercícios para dominar a matéria.')
def geografia():
    print('\n🐱 LearnCat: Miau! Conheça os lugares do mundo, os climas e a relação entre o ser humano e o meio ambiente.')
def historia():
    print('\n🐱 LearnCat: Miau! Viaje pelo passado e descubra como os acontecimentos históricos influenciam o presente.')
def ingles():
    print('\n🐱 LearnCat: Miau! Aprenda novas palavras, pratique a leitura e evolua no inglês um pouquinho a cada dia.')
def matematica():
    print('\n🐱 LearnCat: Miau! Treine seu raciocínio lógico resolvendo exercícios e aprendendo diferentes estratégias.')
def portugues():
    print('\n🐱 LearnCat: Miau! Aprimore sua escrita e interpretação estudando gramática e analisando textos.')
def redacao():
    print('\n🐱 LearnCat: Miau! Organize suas ideias e pratique a escrita para criar textos claros, criativos e bem estruturados.')


def modelosDeEstudo():
    print('\n=====Modelos de estudos=====')
    sistema = True
    while sistema:
        print('\n[1]-Continuar para modelos de estudos\n[2]- Sair ')
        escolha = int(input('Escolha: '))
        if escolha == 1:
            print('\nEscolha a matéria\n[1] - Biologia🧬\n[2] - Filosofia🤔\n[3] - Sociologia👥\n[4] - Física⚛️\n[5] - Geografia🌍\n[6] - História📜\n[7] - Inglês📚\n[8] - Matemática➗\n[9] - Português✍️\n[10] - Redação✍️\n[11] - Química🧪')
            escolhaMateria = int(input('Escolha: '))
            match escolhaMateria:
                case 1:
                    print('Biologia!')
                    biologia()
                case 2:
                    print('Filosofia!')
                    filosofia()
                case 3:
                    print('Sociologia!')
                    sociologia()
                case 4:
                    print('Física!')
                    fisica()
                case 5:
                    print('Geografia!')
                    geografia()
                case 6:
                    print('História!')
                    historia()
                case 7:
                    print('Inglês!')
                    ingles()
                case 8:
                    print('Matemática!')
                    matematica()
                case 9:
                    print('Português!')
                    portugues()
                case 10:
                    print('Redação!')
                    redacao()
                case 11:
                    print('Química!')
                    quimica()
                case _:
                    print('Opção inválida!')     
        else:
            sistema = False
            print("\n" * 50)
            escolher_menu()

def criar_questao():
    linha = []

    print("\n" * 50)

    print('Vamos adicionar uma questão!') 

    materia = str(input('\nDigite a Matéria: '))
    linha.append(materia)

    print('\n---------------')

    conteudo = str(input('\nDigite a Conteúdo: '))
    linha.append(conteudo)

    print('\n---------------')

    modelo = int(input('\nA questão é \n[1] Verdadeira ou falso\n[2] Alternativas\n DIGITE AQUI: '))
    
    if modelo == 1:
        enunciado = str(input('\nDigite o enunciado: '))
        linha.append(enunciado)
        print('---------------')
        # for i in linha:
        matriz.append(linha)
        verdadeiro = print('Verdadeiro')
        falso = print('Falso')
        linha.append(verdadeiro)
        linha.append(falso)
        escolher_menu()

    elif modelo == 2:
        vetor_alternativas = []
        enunciado = str(input('\nDigite o enunciado:'))
        linha.append(enunciado)
        print('\n',matriz)
        # for i in linha:
        matriz.append(linha)

        print('\n---------------')

        quantidade = int(input('\nAdicione a quantidade de alternativas: '))
        for i in range(quantidade):

            print('---------------')
            
            alternativa = str(input(f'\nDigite a {i+1}º alternativa: '))
            vetor_alternativas.append(alternativa)
        matriz.append(vetor_alternativas)
        escolher_menu()

def chat_learn():
    print("\n" * 50)
    print("LearnCat iniciado!")
    print("Pode conversar comigo sobre estudos")
    print("Digite 'sair' para voltar ao menu.\n")

    while True:
        msg = input("Você: ").lower()

        if msg == "sair":
            print("LearnCat: Voltando ao menu...\n")
            ("\n" * 50)
            escolher_menu()

        elif any(p in msg for p in ["cansado", "preguiça", "desanimado"]):
            print("LearnCat: Normal cansar, mas tenta começar com 10 minutos só. Já ajuda muito!")

        elif any(p in msg for p in ["estudar", "o que estudar"]):
            print("LearnCat: Que matéria você quer focar? Posso te ajudar a montar um plano.")

        elif any(p in msg for p in ["matemática", "matematica"]):
            print("LearnCat: Matemática é prática! Faz exercícios básicos e depois sobe o nível.")

        elif any(p in msg for p in ["física"]):
            print("LearnCat: Física = entender + treinar. Começa pela teoria e vai pros exercícios.")

        elif any(p in msg for p in ["prova", "teste"]):
            print("LearnCat: Revisão + exercícios é o melhor combo antes da prova. Resolver exercícios é a melhor forma de aprender.")

        elif any(p in msg for p in ["química"]):
            print("LearnCat: Assistir vídeos de química é a uma ótima forma de aprender. Acesse a função de ver vídeos e assista!!")

        elif any(p in msg for p in ["geografia", "mapa", "país", "continente", "clima"]):
            print("LearnCat: Geografia é sobre o mundo!")
            print("- Estude mapas e localização dos países")
            print("- Entenda clima (tropical, temperado, árido)")
            print("- Foque em relevo, rios e regiões do mundo")
            print("- Dica: use mapas mentais pra memorizar melhor")

        elif any(p in msg for p in ["distopia", "livro distopia", "ficção distópica"]):
            print("LearnCat: Livros de distopia para você:")
            print("- 1984 (George Orwell) → vigilância e controle")
            print("- Admirável Mundo Novo → sociedade controlada pelo prazer")
            print("- Fahrenheit 451 → livros proibidos e censura")
            print("- Jogos Vorazes → sobrevivência e controle político")
            print("- Divergente → sociedade dividida por facções")

        else:
            print("LearnCat: Não entendi muito bem, mas posso te ajudar a estudar melhor!")

def escolher_menu():
    while True:
        escolhas = int(input("Por onde vamos começar?! \n [1] Canais de professores \n [2] Adicionar Questões \n [3] Chat com Learn Cat \n [4] Modelos de Estudo \n [5] Ler questões \n [6] Sair \n DIGITE AQUI:"))
        print('\n----------MENU----------')
        print('Bem Vindo ao Learn Cat!!')
        print('===========😹===========')
        

        match escolhas:
            case 1:
                sistemaCanaisVideos()
                return 
            case 2: 
                criar_questao()
                return
            case 3:
                chat_learn()
                return
            case 4:
                modelosDeEstudo()
                return
            case 5:
                for linha in matriz:
                    print(linha)
            case 6:
                return
            case _:
                print('Opção indisponivel! TENTE NOVAMENTE!')
                return
    
MenuCadastro()
