class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0
    
    def andar(self, distancia):
        combustivel_necessario = distancia / self.consumo
        if combustivel_necessario <= self.combustivel:
            self.combustivel -= combustivel_necessario
            print(f"O carro percorreu {distancia} km.")
        else:
            print("Não há combustível suficiente para percorrer essa distância.")
    
    def obter_gasolina(self):
        return self.combustivel
    
    def adicionar_gasolina(self, quantidade):
        self.combustivel += quantidade
        print(f"Foram adicionados {quantidade} litros de gasolina.")


# Criar uma instância da classe Carro
meu_carro = Carro(10)  # Consumo de 10 km/l

# Obter o nível de combustível atual
nivel_combustivel = meu_carro.obter_gasolina()
print(f"Nível de combustível: {nivel_combustivel} litros.")

# Abastecer o tanque com 50 litros de gasolina
meu_carro.adicionar_gasolina(50)

# Obter o novo nível de combustível
nivel_combustivel = meu_carro.obter_gasolina()
print(f"Nível de combustível: {nivel_combustivel} litros.")

# Dirigir o carro por 200 km
meu_carro.andar(200)

# Obter o nível de combustível após a viagem
nivel_combustivel = meu_carro.obter_gasolina()
print(f"Nível de combustível: {nivel_combustivel} litros.")
