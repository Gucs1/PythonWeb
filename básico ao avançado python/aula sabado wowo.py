#Exercicio 5

# print('*'*10, 'Digite sua nota', '*'*10)
# print('\n')

# while(True):
#   note = int(input('Digite uma nota de  0 a 10: '))
#   if note > 10:
#     print("Valor inválido \n")
#   elif note < 0:
#     print("Valor inválido \n")
#   else:
#     print("Valor correto")
#     break


#Exercicio 7

def redigite(campo):
    return input("Digite novamente o(a): " + campo + " \n")

def validacao(qt_letras_nome,idade):
    if qt_letras_nome <=3:
        print("Nome muito curto")
        nome = redigite("Nome")
        qt_letras_nome = len(nome)
        validacao(qt_letras_nome,idade)
    if idade < 0:
        print("Valor para idade incorreto")
        idade = int(redigite("Idade"))
        validacao(qt_letras_nome,idade)
    elif idade > 150:
        print("Valor para idade incorreto")
        idade = int(redigite("Idade"))
        validacao(qt_letras_nome,idade)

    return
    
tps_sexo = "mf"
tps_est_civ = "scvd"

nome = input("Digite o Nome: ")
idade = int(input("Digite a Idade: "))

qt_letras_nome = len(nome)


validacao(qt_letras_nome,idade)

sexo = input ("Digite o Sexo: \n"+
                "m - masculino \n" +
                "f - feminino \n")
salario = float(input("Digite o Salario: "))

est_civ = input ("Digite o Estado Civil: \n"+
                "s- solteiroo \n" +
                "c - casado \n"+
                " v - viuvo \n"+
                "d - divorciado \n")




if salario <=0:
    print("Salario invalido")

if sexo  not in tps_sexo:
    print(" Sexo invalido")

if est_civ not in tps_est_civ:
    print ("Estado civil invalido")


for l in letra:
    cont += 1

if cont >1:
    print("Você Digitou Mais de uMa Letra")

else:
    if (letra not in vogais) and (letra not in n_pode):
        print("Letra é uma consoante")
    elif (letra  not in cons) and (letra not in n_pode):
        print("Letra é uma Vogal")
    else:
        print("Isto Não é Uma Letra")





     
