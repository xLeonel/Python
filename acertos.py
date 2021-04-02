# Escreva um programa que corrija um teste de múltiplas escolhas, mostrando a quantidade de
# acertos, contendo três questões, cada questão possui 5 alternativas do tipo a, b, c, d e e. A
# resposta correta da primeira questão é “b”; da segunda, “a”; e da terceira, “d”. O programa
# conta um ponto a cada resposta correta. Considere a possibilidade do programa aceitar
# respostas com letra maiúsculas e minúsculas em todas as questões.

def primeira_questao():
    print('1. Quais o menor e o maior país do mundo?')
    print('A - Nauru e China')
    print('B - Vaticano e Rússia')
    print('C - Mônaco e Canadá')
    print('D - Malta e Estados Unidos')
    print('E - São Marino e Índia')
    print('')

def segunda_questao():
    print('2. De onde é a invenção do chuveiro elétrico?')
    print('A - Brasil')
    print('B - Inglaterra')
    print('C - França')
    print('D - Austrália')
    print('E - Itália')
    print('')

def terceira_questao():
    print('3. Qual a montanha mais alta do Brasil?')
    print('A - Pico Paraná')
    print('B - Monte Roraima')
    print('C - Pico da Bandeira')
    print('D - Pico da Neblina')
    print('E - Pico Maior de Friburgo')
    print('')

def validar_resposta(resposta):
    while(resposta.lower() != 'a' and resposta.lower() != 'b' and resposta.lower() != 'c' and resposta.lower() != 'd' and resposta.lower() != 'e'):
        print('Resposta Inválida. Por favor insira um valor entre [A-E]')
        resposta = input('Resposta: ')
        if not (resposta.lower() == 'a' and resposta.lower() == 'b' and resposta.lower() == 'c' and resposta.lower() == 'd' and resposta.lower() == 'e'):
            return resposta
    return resposta
      
acertos = 0

primeira_questao()
resposta = input('Resposta: ')

respostaValidada = validar_resposta(resposta)
if(respostaValidada.lower() == 'b'): ## resposta primeira
    acertos += 1

segunda_questao()
resposta = input('Resposta: ')

respostaValidada = validar_resposta(resposta)
if(respostaValidada.lower() == 'a'): ## resposta segunda
    acertos += 1

terceira_questao()
resposta = input('Resposta: ')

respostaValidada = validar_resposta(resposta)
if(respostaValidada.lower() == 'd'): ## resposta terceira
    acertos += 1

print('Voce acertou {} perguntas.'.format(acertos))








