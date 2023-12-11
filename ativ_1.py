class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def troca_cor(self, nova_cor):
        self.cor = nova_cor
    
    def mostra_cor(self):
        return self.cor

# Criar uma classe que modele a Bola
minha_bola = Bola("vermelho", 13, "couro")

# Mostrar a cor atual da bola
print(minha_bola.mostra_cor())  

# Trocar a cor da bola
minha_bola.troca_cor("verde")

# Mostrar a nova cor da bola
print(minha_bola.mostra_cor())  

