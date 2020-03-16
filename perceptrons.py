# -*- coding: utf-8 -*-
# Aplicativo para verificar se o ser vivo eh quadrupede ou bipede
# quadrupede=1, bipede =-1
#cao =[-1,-1,1,1] | resposta = 1
#gato [1,1,1,1] | resposta = 1
#cavalo = [1,1,-1,1] | resposta = 1
#homem = [-1,-1,-1,1] | resposta =-1


#pesos(sinapses)
w =[0,0,0,0]

#entradas
entradas =[
    [-1,-1,1,1], 
    [1,1,1,1], 
    [1,1,-1,1],
    [-1,-1,-1,1]
   ]

#respostas esperadas
respostas_esperadas =[1,1,1,-1]

#bias (ajuste fino)
bias = 0

#saida
saida = 0

#numero máximo de interações
max_int =10

#taxa de aprendizado
taxa_aprendizado = 1

#soma
soma = 0

#threshold - Limite
threshold = 1

#nome do animal
animal =""

#resposta acerto ou falha
resposta = ""

#dicionario de dados
#cao =[-1,-1,1,1] | resposta = 1
#gato [1,1,1,1] | resposta = 1
#cavalo = [1,1,-1,1] | resposta = 1
#homem = [-1,-1,-1,1] | resposta =-1
dic = {'-1,-1,1,1':'cao',
     '1,1,1,1':'gato',
     '1,1,-1,1':'cavalo',
     '-1,-1,-1,1':'homem'
    }
print("Aprendizado com redes neurais artificiis - Perceptrons")
print("Treinando")

#função para converter listas em strings
def list_to_strings(list):
    s = str(list).strip('[]')
    s = s.replace(' ','')
    return s

#inicio do algoritimo
for k in range(1, max_int):
    acertos = 0 
    print ("Interacao " + str(k) + "------------------------")
    for i in range(0, len(entradas)):
        soma =0
        #pega o nome do animal no dicionario
        if dic.has_key(list_to_strings(entradas[i])):
            animal = dic[list_to_strings(entradas[i])]
        else:
            animal = ""
    
        # Para calcular a saida do perceptron, cada entrada de x eh multiplicada
        # pelo seu peso w correspondente
        for j in range(0, len(entradas[i])):
            soma += entradas[i][j] * w[j]

        #Saida eh igual a adição di bias com a soma anterior
        y_in = bias + soma

        #função de saída determinada pelo threshold
        if y_in > threshold:
            saida = 1
        elif y_in >= -threshold and y_in <= threshold:
            saida =0
        else:
            saida =-1

        #atualiza os pesos caso a saida nao corresponda ao valor esperado
        if saida == respostas_esperadas[i]:
            acertos +=1
            resposta = "acerto"
        else:
            for j in range(0, len(w)):
                w[j] = w[j] + (taxa_aprendizado * respostas_esperadas[i] * entradas[i][j])    
            bias = bias + taxa_aprendizado * respostas_esperadas[i]
            resposta = "Falha - Peso atualizado"
    
        #Imprime a resposta
        if saida == 1:
            print(animal + " = quadrupede = " + resposta)
        elif saida ==0:
            print(animal + " = padrão não identificado = " + resposta)
        elif saida ==-1:
            print(animal + " = bipede = " + resposta)
    
    if acertos == len(entradas):
        print("\nFuncionalidade com " + str(k) + " interações")
        break
    print("")
print("\nFinalizado com sucesso")
raw_input()


    






