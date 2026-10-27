class SerVivo:
    def __init__(self, nombre_cientifico, energia, adn):
        self.nombre_cientifico = nombre_cientifico
        self.edad = 0
        self.energia = 100
        self.adn = adn

    def getter_adn(self):
        return self.adn

    def nacer(self):
        print("estoy naciendo...")
        self.energia = 100

    def morir(self):
        self.energia = 0
        print("el ser ha fallecido")

    def alimentarse(self):
        pass