faturamento = 1000
custo = 200

novas_vendas = 500

faturamento = faturamento + novas_vendas
imposto = faturamento * 0.1
lucro_liquido = faturamento - custo - imposto
lucro = faturamento - custo 

margem_de_lucro = lucro / faturamento

print(faturamento)
print(imposto)
print(custo)
print(lucro)
print(lucro_liquido)
print(margem_de_lucro)
print()

# MOD -> RESTO DA DIVISÃO
print("resto da divisão 10/3 = ", 10%3)
print()

# calculo de anos 

tempo_em_meses = 160 
tempo_em_anos = tempo_em_meses / 12
tempo_em_anos_int = int(tempo_em_meses / 12)

print(tempo_em_meses, 'meses')
print('conversão de meses para anos e meses:')
print(tempo_em_anos,'anos normal')
print(tempo_em_anos_int, 'anos int')
print(tempo_em_meses % 12, 'meses')

# arredondar um numero 
numero = 173.60
print(round(numero))

# edição visual para '_'

nuemro2 = 15_918_600_00
print(nuemro2) #numero completo

