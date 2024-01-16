faturamento = 1000
custo = 200

lucro = faturamento - custo

print(f'faturamento: {faturamento}, custo: {custo}, lucro: {lucro}')


email = 'exemplo@exemplo.com'
email1 = 'EXEMPLO@exemplo.com'

print(email1.lower())
print(email.find('@')) # localizar ou validr se o email tem um caracter 
print(email[7]) # pegar um item especifico 
print(email[7:]) #pegar da posição até o final
print(email[:8]) #pegar da posição ate o inicio 

posicao = email.find('@') # determina posição
servidor = email[posicao+1:] # pula 1 caracter '@'
print(servidor) # imprimi

tamanho = len(email) # tamanho de um texto  
print(tamanho)

# substituir um pedaco do email
novo_email = email.replace('exemplo.com','hotmail.com')
print(novo_email)

nome = 'bruno coelho'
print(nome.capitalize()) # primeira letra da frase fica maiuscula
print(nome.title()) # primeira letra de cada palavra fica maiuscula
print(nome.lower()) # texto tdod minusculo
print(nome.upper()) # texto todo maiusculo 

# formatação numerica 

print(f'faturamento: R$ {faturamento:,.2f}, custo: R$ {custo:,.2f}, lucro: R$ {lucro:,.2f}')
