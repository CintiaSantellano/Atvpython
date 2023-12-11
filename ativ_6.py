class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel
    
    def abastecer_por_valor(self, valor_abastecido):
        litros_abastecidos = valor_abastecido / self.valor_litro
        if litros_abastecidos > self.quantidade_combustivel:
            litros_abastecidos = self.quantidade_combustivel
        self.quantidade_combustivel -= litros_abastecidos
        print(f"Foram abastecidos {litros_abastecidos:.2f} litros de {self.tipo_combustivel}.")
    
    def abastecer_por_litro(self, litros_abastecidos):
        valor_pagar = litros_abastecidos * self.valor_litro
        if litros_abastecidos > self.quantidade_combustivel:
            litros_abastecidos = self.quantidade_combustivel
            valor_pagar = litros_abastecidos * self.valor_litro
        self.quantidade_combustivel -= litros_abastecidos
        print(f"O valor a ser pago é R$ {valor_pagar:.2f}.")
    
    def alterar_valor(self, novo_valor_litro):
        self.valor_litro = novo_valor_litro
    
    def alterar_combustivel(self, novo_tipo_combustivel):
        self.tipo_combustivel = novo_tipo_combustivel
    
    def alterar_quantidade_combustivel(self, nova_quantidade_combustivel):
        self.quantidade_combustivel = nova_quantidade_combustivel


# Criar uma instância da classe BombaCombustivel
bomba = BombaCombustivel("Gasolina", 5.0, 1000)

# Exemplo de abastecimento por valor
bomba.abastecer_por_valor(50)

# Exemplo de abastecimento por litro
bomba.abastecer_por_litro(20)

# Alterar o valor do litro do combustível
bomba.alterar_valor(5.5)

# Alterar o tipo do combustível
bomba.alterar_combustivel("Etanol")

# Alterar a quantidade de combustível restante na bomba
bomba.alterar_quantidade_combustivel(500)
