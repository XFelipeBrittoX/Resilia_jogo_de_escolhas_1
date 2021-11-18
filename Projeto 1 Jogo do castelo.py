#prints de boas vindas ao jogo.
def boas_vindas():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('    Bem vindo à AVENTURA NO CASTELO ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    print('     ESCOLHA O SEU JOGADOR    ')

    print('Escolha um dos 3 personagens abaixo:' )
    print('''[1] Leon
[2] Trevor
[3] Strahd''')


#logica de escolhas
def escolha_jogador():
    jogador = int(input('Escolha o numero das opçoes: \n'))
    while jogador > 3 or jogador < 1:
        jogador = int(input('Escolha o numero das opçoes: \n'))
    return jogador


#parte do personagem Leon
def fase_1_leon():
    print('''Você se encontra no meio de um nevoeiro a procura do castelo Ravenloft, depois
De horas procurando você se depara com um grande porta…sim é ela mesmo, a entrada do castelo…
O que você faz?
[1] Bate na porta
[2] Procura uma nova entrada
[3] ir embora''')
    escolha = escolha_jogador()
    if escolha == 2:
        fase_2_leon()
    elif escolha == 1:
        print('No momento que voce encosta na porta, ela simplesmente despenca na usa direção, nao a tempo de correr, parace que é o Fim...')
    else:
        print('Game Over')


def fase_2_leon():
    print('''Você procura outra entrada e vê que parte de trás do castelo existe outro caminho que leva ao um bosque
e também o que parece ser outra entrada para o castelo…
[1] Seguir em direção ao bosque.
[2] Abrir a porta e entrar.
[3] Ir embora.''')
    escolha = escolha_jogador()
    if escolha == 2:
        fase_3_leon()
    elif escolha == 1:
        print('''Voce segue em direção ao bosque e caminha até que derrempente o barulho de bater de asas ecoando pelas arvores e
inumeros morcegos saem da escuridão e começam a dilacerar a sua carne, parece que esse é o seu Fim...''')
    else:
        print('Game Over')


def fase_3_leon():
    print('''Você entra no castelo e vai caminhando pelos cômodos até que um grito escolha pelas
Paredes do enorme castelo, tentando identificar a direção você segue e vê dois caminhos
Um que leva até uma porta antiga e ornamentada e um uma grande escadaria que segua para a
Parte superior do castelo.


[1] Subir as escadas.
[2] Seguir pela porta ornamentada.
[3] Ir embora.''')
    escolha = escolha_jogador()
    if escolha == 1:
        fase_4_leon()
    elif escolha == 2:
        print('''Voce segue pela porta ornamentada, a mesma da em direção a um correndor com inumeras armaduras, sem perceber voce pisa
em um mecanismo no chão ativando uma armadilha de dardos perfurantes q saem das paredes, nao há para aonde correr parecc que é o seu Fim...''')
    else:
        print('Game Over')

def fase_4_leon():
    print('''Subindo as escadas você se depara com duas figuras que se parecem com dois homens
um deles está de pé segurando em suas mãos manchadas do que se parece ser sangue um 
Longo objeto pontiagudo também coberto de sangue, enquanto o outro se encontra no chão 
Com uma possa de sangue que se espalha por todos o chão…

[1] Ataque rapidamente com sua espada
[2] Pergunte “o que estava acontecendo aqui?”
[3] Ir embora.''')
    escolha = escolha_jogador()
    if escolha == 2:
        print('''O homem olha em sua direção rapidamente e ameaça em partir em sua direção até que ele percebe o que realmente é voce e diz:
"Eu poderia imaginar que existiriam outros vampiros aqui, mas olhando bem pra voce acredito que voce nao seja um deles,
Meu nome é Trevor e eu vim aqui acabar com a tirania do Conde Strahd,Esse vampiro que mantem essa região presa nesse 
nevoeiro, e como pode ver eu consegui!!!''')
    elif escolha == 1:
        print('''Voce parte em direção o homem que se encontra de pé e desferam um golpe contra ele, porem o seu golpe passa pelo vazio devido ao
rapido movimento do homem que desfere um golpe mortal em voce, sua visão aos poucos começa a falhar so enchergando o frio da escuridão...parece que é o seu Fim.''')
    else:
        print('Game Over')

#Parte do Personagem Trevor

def fase_1_trevor():
    print('''Já é noite e você esta perseguindo o que supostamente esta aterrorizando essa região, a perseguição segue por floresta a dentro enquanto você e a pessoa que esta sendo perseguida se deparam com muitos caminhos tortuosos, ele faz um rápido movimento puxa a sela do cavalo dele para a direita indo em direção a outro caminho… o que você faz?

[1] Faz o mesmo movimento que ele.
[2] Segue para a direita mas com cuidado.
[3] ir embora.''')
    escolha = escolha_jogador()
    if escolha == 2:
        fase_2_trevor()
    elif escolha == 1:
        print('''Você faz o mesmo movimento rápido que ele fez, com isso você acaba batendo com a cabeça com violência em um galho de árvore perfurando sua garganta… parece que esse é seu fim.''')
    else:
        print('Game Over')


def fase_2_trevor():
    print('''Você segue na mesma direção que ele e seus instintos de ir com mais cuidado falaram mais alto, a
 pessoa ja não esta tao próxima mais ainda possível ver que ela seguiu em direção ao castelo que
 esta logo em sua frente, de longe é possível ver que a porta está fechando… o que você faz?

[1] Segue em direção a porta mas com cuidado.
[2] Segue em direção a porta o mais rápido possível.
[3] ir embora''')
    escolha = escolha_jogador()
    if escolha == 2:
        fase_3_trevor()
    elif escolha == 1:
        print('''Indo em direção a porta com cuidado, você examina a porta que ja eta fechada quando de repente 
ela começa a cair em sua direção, não é possível sair a tempo…parece que esse é seu fim''')
    else:
        print('Game Over')


def fase_3_trevor():
    print(''' Com um movimento rápido você incita o seu cavalo a correr mais do que nunca enquanto a porta
 levadiça está se fechando… o que você faz?


[1] Continua a fazer o cavalo correr o mais rápido possível.
[2] Tenta salta do cavalo em direção da porta.
[3] ir embora''')
    escolha = escolha_jogador()
    if escolha == 2:
        fase_4_trevor()
    elif escolha == 1:
        print('''O cavalo começa a correr ainda mais rapido mais ao perceber que o caminho será obstruído ele para
 de repente arremessando você em direção ao portao que fecha sobre sua costa o esmagando…
parece que esse é seu fim''')
    else:
        print('Game Over')


def fase_4_trevor():
    print(''' Com um movimento rápido, você dá um grande impulso do seu cavalo, saltando em direção a porta
 levadiça, no momento que o seu pé fazem contato com o chão voce faz um rolamento e desliza
 passado pela porta centímetros antes dela se fechar por completo, no momento que se é possível
 notar ao seu redor a pessoa que você persegue está nas escadas a usa frente, um homem pálido e de 
 aparência um tanto sinistra e com uma expressão de frustração ao ver o seu êxito diz:

“Foi um erro vir até aqui caçador!!”

O que você faz?


[1] Não diz nada e arremessa uma de suas estacas nele.
[2] Diz que “Você morrerá hoje vampiro!”
[3] ir embora.''')
    escolha = escolha_jogador()
    if escolha == 1:
        print('''Você arremessa com precisão sua estaca que acerta em cheio o coração do vampiro, ele agonizando
 sobe as escadas pra o próximo andar, você o segue e vê ele no chão ainda agonizando, então você
 desfere o golpe final assim eliminando ele de vez.''')
    elif escolha == 2:
        print(''' No momento que você diz a sua ameça ao fundo você escuta alguém batendo na porta, no mesmo
 instante o vampiro na escada aciona um mecanismo na parede que ativa uma armadilha, do teto
 começa a cair inúmeras pedras encima de você… parece que esse é seu fim.''')
    else:
        print('Game Over 2')



#Parte do Personagem Strahd


def fase_1_strahd():
    escolha = escolha_jogador()
    if escolha == 1:
        fase_2_strahd()
    elif escolha == 2:
        print('Game Over 1')
    else:
        print('Game Over 2')


def fase_2_strahd():
    escolha = escolha_jogador()
    if escolha == 2:
        fase_3_strahd()
    elif escolha == 1:
        print('Game Over 1')
    else:
        print('Game Over 2')


def fase_3_strahd():
    escolha = escolha_jogador()
    if escolha == 1:
        fase_4_trevor()
    elif escolha == 2:
        print('Game Over 1')
    else:
        print('Game Over 2')


def fase_4_strahd():
    escolha = escolha_jogador()
    if escolha == 2:
        print('Final 1')
    elif escolha == 1:
        print('Final 2')
    else:
        print('Game Over 2')



#Sequencia de fases do jogo.
boas_vindas()
personagem = escolha_jogador()
if personagem == 1:
    fase_1_leon()
elif personagem == 2:
    fase_1_trevor()
elif personagem == 3:
    fase_1_strahd()