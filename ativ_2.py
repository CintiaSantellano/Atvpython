class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b
    
    def mudar_lados(self, novo_lado_a, novo_lado_b):
        self.lado_a = novo_lado_a
        self.lado_b = novo_lado_b
    
    def retornar_lados(self):
        return self.lado_a, self.lado_b
    
    def calcular_area(self):
        return self.lado_a * self.lado_b
    
    def calcular_perimetro(self):
        return 2 * (self.lado_a + self.lado_b)

# Criar uma instância da classe Retangulo
meu_retangulo = Retangulo(5, 3)

# Retornar os valores dos lados do retângulo
print(meu_retangulo.retornar_lados())  

# Mudar os valores dos lados do retângulo
meu_retangulo.mudar_lados(7, 4)

# Retornar os novos valores dos lados do retângulo
print(meu_retangulo.retornar_lados())  

# Calcular a área do retângulo
area = meu_retangulo.calcular_area()
print(area)  

# Calcular o perímetro do retângulo
perimetro = meu_retangulo.calcular_perimetro()
print(perimetro)  

# Crie um programa que utilize esta classe. Ele deve pedir as medidas de um local.
# Depois,deve-se criar um objeto com as medidas e calcular a quantidade (em m2) de pisos (1 x 1 m2)
# e de rodapés necessários para o local.

class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b
    
    def mudar_lados(self, novo_lado_a, novo_lado_b):
        self.lado_a = novo_lado_a
        self.lado_b = novo_lado_b
    
    def retornar_lados(self):
        return self.lado_a, self.lado_b
    
    def calcular_area(self):
        return self.lado_a * self.lado_b
    
    def calcular_perimetro(self):
        return 2 * (self.lado_a + self.lado_b)


# Solicitar as medidas do local ao usuário
comprimento = float(input("Informe o comprimento do local em metros: "))
largura = float(input("Informe a largura do local em metros: "))

# Criar um objeto com as medidas informadas
local = Retangulo(comprimento, largura)

# Calcular a quantidade de pisos necessários (área do local)
area_local = local.calcular_area()
quantidade_pisos = area_local

# Calcular a quantidade de rodapés necessários (perímetro do local)
perimetro_local = local.calcular_perimetro()
quantidade_rodapes = perimetro_local

# Exibir os resultados
print(f"Quantidade de pisos necessários: {quantidade_pisos} m²")
print(f"Quantidade de rodapés necessários: {quantidade_rodapes} metros")
