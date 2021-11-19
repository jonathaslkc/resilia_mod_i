from time import sleep
import sys


def digit(txt, seg=0.2):
    # Funcao para o programa 'digitar' letra por letra de um texto informado (txt) nos segundos desejado (seg).
    for letras in txt:
        print(letras, end='')
        sleep(seg)
    print()


def pula():
    print('\n' * 40)


def valida_entrada(selecao, opcs):
    saida_laco = True
    while saida_laco:
        if not selecao.isdigit():
            print('Opcoes: ', end='')
            for opc in range(1, opcs + 1):
                print(f'[{opc}] ', end='')
            print()
            selecao = input('Por favor, digite um número válido: ')
        else:
            selecao = int(selecao)
            if selecao <= 0:
                print('Opcoes: ', end='')
                for opc in range(1, opcs + 1):
                    print(f'[{opc}] ', end='')
                print()
                selecao = input('Digite uma das opcao presentes: ')
            elif selecao > opcs:
                print('Opcoes: ', end='')
                for opc in range(1, opcs + 1):
                    print(f'[{opc}] ', end='')
                print()
                selecao = input('Digite uma das opcao presentes: ')
            else:
                saida_laco = False
    return selecao


def inicio():
    # OPCOES PARA INÍCIO DO GAME/CONTAR UM POUCO DA HISTÓRIA/SAIR
    selecao_menu = menu()
    if selecao_menu == 1:
        # Início do jogo, segue para tela de selecao do personagem
        selecao_inicio = campanha()
        # Após select do personagem, retorna e segue com a história do personagem (incluir aqui os demais projetos).
        missao_personagens(selecao_inicio)
    elif selecao_menu == 2:
        historia()
    elif selecao_menu == 3:
        print('Carregando...')
        # fim()


def menu():
    pula()
    print('=' * 20)
    print(f'{cor["fazul"]}{"- MENU -":^20}{cor["limpa"]}')
    print('''    [1] Campanha
    [2] História
    [3] Sair''')
    print('=' * 20)
    print()
    selecao = input('Digite o número da opcao desejada [1, 2 ou 3]: ')
    #retorno = valida_entrada(selecao, opcs=3)
    retorno = valida_entrada(selecao, 3)
    return retorno


def historia():
    pula()
    history = '''   - History

        Em um mundo sombrio, ardiloso e selvagem, onde jáz somente o tech e o "qi", surge uma luz nas profundezas 
        dos 'stage' que apresenta-se imponente e altivo, mas sobre um caminho misterioso e cheio de desafios.

        Um grupo de jovens inquietos, preocupado com o porvir e ansiosos por desafios, a caminhar pelas estradas 
        desse mundo, veem um senhor de longa barba branca, escondendo-se nas pregas de um trampo miserável, sen-
        tado sobre uma rocha, coberto sobre a sombra de um lindo Carvalho com o que mais se parecia um alpendre, 
        a observar todos que alí perambulavam. O grupo, incitado pela curiosidade, fazem perguntas que o levam 
        para uma verdadeira aventura.

        Vá até o End-Game, vença Pitão com bom senso, capacidade de lidar com as respostas e uma atitude positiva 
        e flexível, busque o Tesouro Perdido!

        #RunAndGetThereFirst!'''
    digit(history, 0.01)
    print('''
    References: 
    Mit Technology Review
    https://mittechreview.com.br/a-importancia-das-soft-skills-e-porque-nunca-foram-prioridade/
    https://ead.ucs.br/blog/soft-skills
    https://www.voitto.com.br/blog/artigo/pilares-da-inteligencia-emocional
    https://blog.solides.com.br/guest-post-soft-skills/
    https://www.digitalhouse.com/br/blog/descubra-como-uma-maior-capacidade-analitica-ajuda-no-seu-trabalho-como-lider''')
    sleep(0.7)
    print('=' * 40)
    input('<< Pressione ENTER para voltar >>')
    inicio()


def campanha():
    pula()
    # Funcao que apresenta os personagems e dá opcao para selecao para seguir campanha
    print('=' * 20)
    print(f'{"- SELECAO DE PERSONAGENS -":^20}')
    sleep(0.5)
    print(f'{cor["fverm"]}{" [1] Elesis":<20}{cor["limpa"]}')
    print(f'''{cor["negrito"]}      - rompe com o esteriótipo de garota fraca e inocente. Para Elesis, missao dada é
    missao cumprida! Mas sua identidade antiética, sem espírito de equipe e agressiva pode atrapalhá-lá.''')
    sleep(0.5)
    print(f'{cor["fverd"]}{" [2] Ryan":<20}   {cor["limpa"]}')
    print(f'''{cor["negrito"]}      - Sempre a frente, falastrao e a todo momento empolgado com aventuras, e agora com
    energia na busca por Pitao. Mas as vezes tem medo e nao observa todos os pontos para tomar decisoes.''')
    sleep(0.5)
    print(f'{cor["fazul"]}{" [3] Zero":<20}   {cor["limpa"]}')
    print(f'''{cor["negrito"]}      - Analítico, se inteirar de tudo antes de agir, nao deixa os pontos negativos 
    sobressair. Mas nao se comunica com os amigos para falar o que sabe, observou. Quieto e introvertido.''')
    sleep(0.5)
    print()
    print(f'{cor["negrito"]}{" [4] VOLTAR":<20}   {cor["limpa"]}')
    print('=' * 20)
    selecao = input('Digite o número da opcao desejada [1, 2, 3 ou 4]: ')
    retorno = valida_entrada(selecao, 4)
    return retorno


def missao_personagens(select):
    # Seta para o projeto dos demais colegdas do nosso grupo
    if select == 1:
        # Seta para do personagem 1 (Elesis)
        elesis()
    elif select == 4:
        inicio()


def certo_errado(resp, correta, nivel):
    correto = True
    if resp == correta:
        if nivel == 1:
            pula()
            digit('Muito Bem! Próxima...', seg=0.05)
            print()
            return correto
        elif nivel == 2:
            pula()
            digit('Gostei de ver! Última...! <<< O DESAFIO PYTHON! >>>', seg=0.05)
            print()
            return correto
        elif nivel == 3:
            print()
            digit('NAAAAAOOOOOOOOO!!!! ', 4)
            digit('V v vvooc voce m me venceu....', 2)
            digit('.....', seg=0.5)
            print(' -- Misteriosamente o Guardiao sumiu...')
            sleep(4)
            print()
            correto = False
            return correto
    else:
        print()
        digit('VOCE ERROU!!!! HAHAHA VOLTE PARA TEU MESTRE E ESTUDE MAIS!', 0.01)
        sleep(1)
        correto = False
        return correto


def elesis():
    # Case de Elesis
    pula()
    print(f'{cor["fverm"]}- Campanha de Elesis -{cor["limpa"]}')
    sleep(1)
    print('Senhor de Barba Branca:')
    digit('Está pronto para comecar a campanha?')
    sleep(1)
    digit('Suponho que sim...')
    sleep(1)
    # copia texto
    digit('Tenho um desafio para você, Elesis...', 0.01)
    digit('Sua missão é atravessar para o outro lado da ilha e receber o Tesouro Perdido!', 0.01)
    digit('Nesta ilha há três caminhos. E você precisará atravessar um deles.', 0.01)
    digit('O seu caminho é pela Floresta da Humilhação.', 0.01)
    digit('Na última, vença o Desafio Pitão e ganhe a passagem para o tesouro perdido!', 0.01)
    digit('Você terá somente 1 chance e 3 fases... Dê o seu melhor!', 0.01)
    print()
    digit(' -- Após receber outras instruções... Caminha para a Floresta.......', 0.01)
    sleep(2)
    # Guardiao
    print('\n' * 2)
    digit('?? : Olá, Jovem!')
    digit('Eu sou o Guardian Gate Soft e tenho 3 desafios para você!', 0.01)
    digit('Complete-os e te deixei atravessar a Floresta da Humilhacao!', 0.01)
    digit('Os desafios consistem em conceitos e importâncias das soft skill,', 0.01)
    digit('HAHAHA! Espero que aprenda (a lição)...', 0.01)
    sleep(1)
    digit('Vamos lá....')
    print()
    print('   [1] Desafio da Ética')
    print('   [2] Desafio da Empatia')
    print('   [3] Desafio do Trabalho em Equipe')
    desafio = input('Escolha o desafio que deseja percorrer: ')
    resposta_desafio = valida_entrada(desafio, 3)
    print('\n' * 3)
    if resposta_desafio == 1:
        # Desafios
        # |1 Ética|
        # 1ª Pergunta
        digit('É uma palavra criada a partir do termo grego ethos. É um conjunto de valores morais de um grupo ', 0.01)
        digit('ou indivíduo e bem valorizada no mercado de trabalho. Estou falando de? ', 0.01)
        print('-=' * 20)
        print('''        1) Aquele Velho da barba branca encostado do INSS.
        2) Saia do meu caminho e deixe-me seguir com minha missao.
        3) Já sei! Vi o velho barbudo falar algo sobre... Ética!!! Estou certo!
        ''')
        resposta = input('Digite o número correspondente à resposta: ')
        resposta = valida_entrada(resposta, 3)
        resposta = certo_errado(resposta, 3, 1)
        if resposta:
            # 2ª Pergunta
            digit('São inúmeros casos de demissões em razão de atitudes que desvirtuam as condutas morais... ', 0.01)
            digit('E as empresas tem um espaço para tratar disso. Chama-se...?', 0.01)
            print('-=' * 20)
            print('''        1) Departamento de RH?
        2) Deve ser o Estacionamento.
        3) Conselho de Ética!
            ''')
            resposta = input('Digite o número correspondente à resposta: ')
            resposta = valida_entrada(resposta, 3)
            resposta = certo_errado(resposta, 3, 2)
            if resposta:
                # 3ª Pergunta
                digit('Quais características a Ética te beneficia?', 0.01)
                print('-=' * 20)
                print('''        1) Em montar um computador bonito? .
        2) Hummm... A credibilidade, a paz e a ordem no trabalho e também em casa! Pois é uma mão de via dupla!
        3) Saia da minha frente, paspalho!  Estou perdendo meu tempo com você!
                        ''')
                resposta = input('Digite o número correspondente à resposta: ')
                resposta = valida_entrada(resposta, 3)
                resposta = certo_errado(resposta, 2, 3)
                if not resposta:
                    gameover()
            else:
                gameover()
        else:
            gameover()
    elif resposta_desafio == 2:
        # Desafios
        # |2 Empatia|
        # 1ª Pergunta
        digit('Importante em qualquer ambiente que se tenha interação. Capacidade', 0.01)
        digit('de se colocar no lugar do outro. Estou falando de...?', 0.01)
        print('-=' * 20)
        print('''        1) Velho da lancha da barba branca.
        2) Deixa de bla bla bla saia da minha frente!
        3) Acho que lembro... o Velho nos contou. É a Empatia? Certo?
        ''')
        resposta = input('Digite o número correspondente à resposta: ')
        resposta = valida_entrada(resposta, 3)
        resposta = certo_errado(resposta, 3, 1)
        if resposta:
            # 2ª Pergunta
            digit('Sabendo que a empatia é a capacidade de se colocar no lugar do outro.', 0.01)
            digit('Mais onde ela tem destaque no âmbito profissional da empresa?', 0.01)
            print('-=' * 20)
            print('''        1) Deve ser na relação entre líderes e liderados. Ou melhor, onde há hierarquia!
        2) Eu não sei cara... tá me deixando furiosa!! Eu não quero saber dessas besteiras!
        3) Deve ser na tua casa! Já olhou lá? Ah... deixa de lorota e me deixa passar...
            ''')
            resposta = input('Digite o número correspondente à resposta: ')
            resposta = valida_entrada(resposta, 3)
            resposta = certo_errado(resposta, 1, 2)
            if resposta:
                # 3ª Pergunta
                digit('Agora falando do negócio em si. Ela é um ponto interessante até para o marketing.', 0.01)
                digit('Essa habilidade é essencial para?', 0.01)
                print('-=' * 20)
                print('''        1) Na relação empresa e cliente! Por que o empreendimento precisa 
           entender qual é a necessidade exata do consumidor.
        2) Aff cansei. Não quero mais te responder.
        3) Besteira...
                        ''')
                resposta = input('Digite o número correspondente à resposta: ')
                resposta = valida_entrada(resposta, 3)
                resposta = certo_errado(resposta, 1, 3)
                if not resposta:
                    gameover()
            else:
                gameover()
        else:
            gameover()
    elif resposta_desafio == 3:
        # Desafios
        # |3 Trabalho em Equipe|
        # 1ª Pergunta
        digit('Sabemos que mesmo que você trabalhe só, em algum momento precisara relacionar-se. ', 0.01)
        digit('É uma habilidade bem requisitada pelas empresas. Quem não tem essa habilidade, ', 0.01)
        digit('acaba mais tumultuando do que ajudando. Estou falando de...?', 0.01)
        print('-=' * 20)
        print('''         1) Habilidade de você sair do caminho! Não me atrapalha guri!
            2) Ah... odeio! Não tenho paciência... mas é o Trabalho em Equipe.
            3) Não lembro. Quando lembrar te digo.
                ''')
        resposta = input('Digite o número correspondente à resposta: ')
        resposta = valida_entrada(resposta, 3)
        resposta = certo_errado(resposta, 2, 1)
        if resposta:
            # 2ª Pergunta
            digit('O trabalho em equipe exige outras habilidades para que tenha uma consonância e bom desempenho.', 0.01)
            digit(' Quais seriam alguma dessas habilidades?', 0.01)
            print('-=' * 20)
            print('''        1) Deve ser Maturidade Emocional pq eu aguento a pressão! Não sei os outros... 
                   Ah, Empatia também e principalmente liderança.
            2) Deve ser a pancadaria e socos! Me deixa passar!
            3) Odeio aceitar opiniões contrárias às minhas! Não gosto de ninguém! Nem sei pq tenho amigos...
                    ''')
            resposta = input('Digite o número correspondente à resposta: ')
            resposta = valida_entrada(resposta, 3)
            resposta = certo_errado(resposta, 1, 2)
            if resposta:
                # 3ª Pergunta
                digit('Se fossemos uma equipe e eu te propusesse ser líder. Diz-me duas ', 0.01)
                digit('características que engloba a liderança e o Trabalho em Equipe.', 0.01)
                print('-=' * 20)
                print('''        1) Aff cansei. Não quero mais te responder. 
                2) Besteira...
                3) Desenvolver isso de liderança em toda equipe e manter esse espírito de trabalho em 
                   equipe, acredito que seria interessante.
                                ''')
                resposta = input('Digite o número correspondente à resposta: ')
                resposta = valida_entrada(resposta, 3)
                resposta = certo_errado(resposta, 1, 3)
                if not resposta:
                    gameover()
            else:
                gameover()
        else:
            gameover()


def gameover():
    pula()
    print('-=' * 40)
    print()
    print(f'{cor["fverm"]}{"------------":^80}{cor["limpa"]}')
    print(f'{cor["fverm"]}{" <<<<    GAME OVER     >>>>":^80}{cor["limpa"]}')
    print(f'{cor["fverm"]}{"------------":^80}{cor["limpa"]}')
    print()
    print('-=' * 40)
    print('\n' * 3)
    input(' <<Pressione ENTER para Voltar ao Início >>')
    inicio()



def fim():
    # Segue para últimas linhas para finalizar o jogo
    print('\n' * 4)
    sleep(0.5)
    print(f'{cor["fazul"]}<< GAME SENDO FINALIZADO >>{cor["limpa"]}')
    sleep(0.8)
    print('Aguarde', end='')
    digit('.....', seg=0.01)
    digit('Até logo!   =..( ', seg=0.01)
    # sys.exit(0)


cor = {
    'negrito': '\033[1m',
    'sublinhado': '\033[4m',
    'verde': '\033[1;32m',
    'vermelho': '\033[1;31m',
    'fverm': '\033[1;4;41m',
    'fverd': '\033[1;4;42m',
    'famar': '\033[1;4;43m',
    'fazul': '\033[1;4;44m',
    'limpa': '\033[0m'}

# INÍCIO DO GAME | TELA DE BEM-VINDO
print('-=' * 20)
print(f'{cor["fverd"]}{"B E M    V I N D O":^40}{cor["limpa"]}')
print(f'{"GAME":^40}')
print(f'{cor["sublinhado"]}{cor["negrito"]}{"-em busca do pitao-":^40}{cor["limpa"]}')
print('-=' * 20)
print()
input(f'{cor["fazul"]}{"<< Pressione ENTER para continuar >>":^40}{cor["limpa"]}')
print('\n' * 30)
# BLOCO DE INICIO
inicio()
# Quando sai do inicio(), ele finaliza o jogo
print('\n' * 4)
sleep(0.5)
print(f'{cor["famar"]}<< GAME SENDO FINALIZADO >>{cor["limpa"]}')
sleep(0.8)
print('Aguarde', end='')
digit('.....', seg=0.01)
digit('Até logo!   =..( ', seg=0.01)
