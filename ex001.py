# mensagens de boas vindas
print ("Olá, bem vindo a loja Renan Oliveira Bueno Capolupo")

#Variáveis
valor = float(input("Qual o valor do produto? (EM REAIS): "))
quantidade = int(input("Qual a quantidade do produto? "))
preco = valor * quantidade

if quantidade < 200: #Código para produto sem desconto
    print ("O Valor sem desconto é ${}".format(preco))
    print ("A quantidade mínima para o desconto não foi exigido")
elif quantidade >= 200 and quantidade <= 1000: #Código para desconto de 5%
    print ("O Valor sem desconto é ${:2f}".format(preco))
    print ("O Valor com desconto é ${:.2f}".format(preco - (5 * preco / 100 )))
elif quantidade >= 1000 and quantidade <= 2000: #Código para desconto de 10%
    print ("O Valor sem desconto é ${:.2f}".format(preco))
    print ("O Valor com desconto é ${:.2f}".format(preco - (10 * preco / 100 )))
else : #Código para desconto de 15%
    print ("O Valor sem desconto é $ {:.2f}".format(preco))
    print ("O Valor com desconto é $ {:.2f}".format(preco - (15 * preco / 100 )))






