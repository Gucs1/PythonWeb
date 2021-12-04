
# nome = "Gustavo"

# anno_nsc = 2002

# idade = 2021 - 2002

# print("Seu nome é: "+ nome + " e sua idade é: "+str(idade))


## --------- OUTRO EXERCICIO -----------


# nome = "Gustavo"

# nota_mat = 10 
# nota_mat2 = 6
# nota_mat3 = 4

# media = (nota_mat+nota_mat2+nota_mat3)/3 

# if(media >= 7):
#     print('Voce passou do ano!!')
# elif(media >=5):        
#     print('Voce esta de recuperação!!')
# else:
#     print('Voce reprovou de ano!!')


## ------------ OUTRA FORMA DE FAZER  ---------------------

# nome = "Gustavo"
# nota_mat = 5 
# nota_mat2 = 5
# nota_mat3 = 5
# media = (nota_mat+nota_mat2+nota_mat3)/3 

# print (nome + " Possui: "+str(media) + " de media")

# list_med = [7,5,4]
# list_result = ["passou","recuperação","reprovou"]

# cont = 0
# for x in list_med:
#     if media >= int(x):
#         print(list_result[cont])
#         break
#     cont = cont +1


## ------------ OUTRA FORMA DE FAZER  ---------------------

# print('*'*10, 'Descubra sua Média', '*'*10)
# print('\n')

# nome = input('Digite o seu nome: ')
# nota_um = int(input('Digite sua peimeira nota: '))
# nota_dois = int(input('Digite sua segunda nota: '))
# nota_tres = int(input('Digite sua terceira nota: '))

# media =  (nota_um+nota_dois+nota_tres)/3

# if(media >= 7):
#     print('Você passou do ano!!')
# elif(media  >=5):
#     print('Você esta de recuperação!!')
# else:
#     print('Você reprovou de ano!!')

    ## ------------ OUTRO EXERCICIO ---------------------

Dict_turma = {}
qt_alunos = int(input("Digite a quantidade de alunos: \n"))
qt_notas =  int(input("Digite a quantidade de notas: \n"))

cont = 0
cont2 = 0
notas = []

while cont != qt_alunos:
    cont = cont + 1
    nome = input("Digite o nome do Aluno"+str(cont)+ ": ")
    cont2 = 0
    notas = []
while cont2 != qt_notas:
    cont2 = cont2 + 1
    nota = float(input("Digite a nota "+str(cont2)+ ": "))
    notas.append(nota)

    

media = (sum(notas)) / qt_notas
Dict_turma[nome] = media

print(Dict_turma)



## ------------ OUTRO EXERCICIO ---------------------

   

