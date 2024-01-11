car = 50
motorista = 5
espaco_car = 2.

motoristas_carro = motorista
carros_livres = car - motorista
capacidade = motorista * espaco_car
motoristas_livres = motorista - car

resutado = 0

if motoristas_livres <= 0:
    resutado = 0
else: resutado =  motoristas_livres

print("Motoristas contratados", motoristas_carro)
print("veiculos livres", carros_livres)
print("motoristas livres", resutado)
print("capacidade do veiculo", capacidade)