class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def imprimir(self):
        print(f"({self.x}, {self.y})")


class Retangulo:
    def __init__(self, largura, altura, ponto_inicial):
        self.largura = largura
        self.altura = altura
        self.ponto_inicial = ponto_inicial
    
    def encontrar_centro(self):
        centro_x = self.ponto_inicial.x + self.largura / 2
        centro_y = self.ponto_inicial.y + self.altura / 2
        return Ponto(centro_x, centro_y)


# Criar objetos da classe Retangulo
ponto_inicial = Ponto(2, 3)
retangulo1 = Retangulo(5, 4, ponto_inicial)
retangulo2 = Retangulo(3, 6, ponto_inicial)

# Encontrar o centro do retangulo1
centro1 = retangulo1.encontrar_centro()
centro1.imprimir()

# Encontrar o centro do retangulo2
centro2 = retangulo2.encontrar_centro()
centro2.imprimir()

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def imprimir(self):
        print(f"({self.x}, {self.y})")


class Retangulo:
    def __init__(self, largura, altura, ponto_inicial):
        self.largura = largura
        self.altura = altura
        self.ponto_inicial = ponto_inicial
    
    def encontrar_centro(self):
        centro_x = self.ponto_inicial.x + self.largura / 2
        centro_y = self.ponto_inicial.y + self.altura / 2
        return Ponto(centro_x, centro_y)


# Criar objetos da classe Retangulo
ponto_inicial = Ponto(2, 3)
retangulo1 = Retangulo(5, 4, ponto_inicial)
retangulo2 = Retangulo(3, 6, ponto_inicial)

# Encontrar o centro do retangulo1
centro1 = retangulo1.encontrar_centro()
centro1.imprimir()

# Encontrar o centro do retangulo2
centro2 = retangulo2.encontrar_centro()
centro2.imprimir()
