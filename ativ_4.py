class Tamagotchi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
    
    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
    
    def alterar_fome(self, nova_fome):
        self.fome = nova_fome
    
    def alterar_saude(self, nova_saude):
        self.saude = nova_saude
    
    def alterar_idade(self, nova_idade):
        self.idade = nova_idade
    
    def retornar_nome(self):
        return self.nome
    
    def retornar_fome(self):
        return self.fome
    
    def retornar_saude(self):
        return self.saude
    
    def retornar_idade(self):
        return self.idade

# Criar uma instância da classe Tamagotchi
meu_tamagotchi = Tamagotchi("Tama", 5, 8, 2)

# Alterar o nome do Tamagotchi
meu_tamagotchi.alterar_nome("Tammy")

# Alterar o nível de fome do Tamagotchi
meu_tamagotchi.alterar_fome(3)

# Alterar o nível de saúde do Tamagotchi
meu_tamagotchi.alterar_saude(10)

# Alterar a idade do Tamagotchi
meu_tamagotchi.alterar_idade(3)

# Obter o nome atual do Tamagotchi
nome = meu_tamagotchi.retornar_nome()

# Obter o nível de fome atual do Tamagotchi
fome = meu_tamagotchi.retornar_fome()

# Obter o nível de saúde atual do Tamagotchi
saude = meu_tamagotchi.retornar_saude()

# Obter a idade atual do Tamagotchi
idade = meu_tamagotchi.retornar_idade()

# Exibir informações do Tamagotchi
print("Nome:", nome)
print("Fome:", fome)
print("Saúde:", saude)
print("Idade:", idade)
