from random import randint
from random import seed
from urllib import request

numero = None
amigos = None
grelha = None
jogadas = None
pontos = None
semente = None

def get_numero(linha):
    numero = linha[7:-1]
    
    print("numero = \"" + numero + "\"")

    return numero
def get_amigos(linha):

    amigos = linha[7:-1]

    print("amigos = \"" + amigos + "\"")
    # contar vírgulas
    n_virgulas = 0
    for letra in amigos:
        if letra == ",":
            n_virgulas = n_virgulas + 1

    n_amigos = n_virgulas + 1
    if (n_amigos < 2) or (n_amigos > 5):
        print("Número de amigos = " + str(n_amigos))
        print("O número de amigos é INVÁLIDO. Tem que estar entre 2 e 5.")
        print("A sua entrada no ranking vai ser REJEITADA.")

    return amigos

def le_identificacao():
    global numero
    global amigos

    ficheiro = open("identificacao.txt", "r")
    linha1 = ficheiro.readline()
    print(linha1)
    linha2 = ficheiro.readline()
    print(linha2)
    ficheiro.close()

    numero = get_numero(linha1)
    amigos = get_amigos(linha2)

def inicializa_semente(semente_a_usar):
    global semente
    if semente_a_usar == None:
        semente_a_usar = randint(1, 1000)
    seed(semente_a_usar)
    semente = semente_a_usar

def regista_grelha_inicial(g11, g12, g13, g14,
                           g21, g22, g23, g24,
                           g31, g32, g33, g34,
                           g41, g42, g43, g44):
    global grelha
    global jogadas
    global pontos
    grelha = [[g11, g12, g13, g14],
             [g21, g22, g23, g24],
             [g31, g32, g33, g34],
             [g41, g42, g43, g44]]
# inicialização das restantes variáveis globais
    jogadas = ""
    pontos = None
def regista_jogada(letra):

    global jogadas

    jogadas = jogadas + letra

def regista_pontos(p):

    global pontos

    pontos = p

def regista_ranking():
    mensagem = None
    try:
        url_string = "http://ec2-54-76-249-109.eu-west-1.compute.amazonaws.com/cgi-bin/submit_2048.py?numero=" + numero + "&amigos=" + amigos + "&jogadas=" + jogadas + "&pontos=" + str(pontos) + "&semente=" + str(semente)

        url = request.urlopen(url_string)
        mensagem = url.read().decode("utf-8")
    except Exception as err:
        mensagem = "Não foi possível registar a pontuação no ranking.\n"
        mensagem = mensagem + str(err)

    return mensagem
def escreve_registo():

    nome_ficheiro = numero + "." + str(pontos)

    ficheiro = open(nome_ficheiro, "w")

    ficheiro.write("numero=" + numero + "\n")
    ficheiro.write("amigos=" + amigos + "\n")
    ficheiro.write("grelha_inicial=" + str(grelha) + "\n")
    ficheiro.write("jogadas=" + jogadas + "\n")
    ficheiro.write("pontos=" + str(pontos) + "\n")
    ficheiro.write("semente=" + str(semente) + "\n")

    ficheiro.close()

    mensagem_cloud = regista_ranking()

    return mensagem_cloud

