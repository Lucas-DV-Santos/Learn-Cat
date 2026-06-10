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
            print("LearnCat: Normal cansar, mas tenta começar com 10 min só. Já ajuda muito!")

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

chat_learn()