import math

class Asteroide:
    def __init__(self, nombre, x, y, velocidad_x, velocidad_y):
        self.nombre = nombre
        self.x = x
        self.y = y
        self.velocidad_x = velocidad_x
        self.velocidad_y = velocidad_y

class SistemaAlertaAsteroides:
    def __init__(self):
        self.asteroides = []

    def agregar_asteroide(self, asteroide):
        self.asteroides.append(asteroide)

    def calcular_distancia_entre_puntos(self, x1, y1, x2, y2):
        """
        Calcula la distancia entre dos puntos en un plano cartesiano.
        """
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    def calcular_distancia_tierra_asteroide(self, x_asteroide, y_asteroide):
        """
        Calcula la distancia entre la Tierra (punto en el origen) y un asteroide dado su posición en el plano cartesiano.
        """
        return self.calcular_distancia_entre_puntos(0, 0, x_asteroide, y_asteroide)
    
    def generar_alerta(self, distancia_minima_aceptable, distancia_tierra_asteroide):
        """
        Genera una alerta si la distancia del asteroide a la Tierra es menor a la distancia mínima aceptable.
        """
        return distancia_tierra_asteroide < distancia_minima_aceptable
    
    def buscar_asteroides_cercanos(self, distancia_minima_aceptable):
        """
        Busca asteroides cercanos a la Tierra y genera alertas en caso necesario.
        """

        for asteroide in self.asteroides:
            distancia_tierra_asteroide = self.calcular_distancia_tierra_asteroide(asteroide.x, asteroide.y)
            if self.generar_alerta(distancia_minima_aceptable, distancia_tierra_asteroide):
                print(f"ALERTA: El asteroide {asteroide.nombre} está demasiado cerca de la Tierra!")

if __name__ == "__main__":
    sistema_alerta = SistemaAlertaAsteroides()

    # Agregar asteroides a la lista del sistema de alerta
    asteroide1 = Asteroide("2023ABC", 100, 200, 10, 5)
    asteroide2 = Asteroide("2023XYZ", -50, 300, 7, -3)
    sistema_alerta.agregar_asteroide(asteroide1)
    sistema_alerta.agregar_asteroide(asteroide2)

    # Distancia mínima aceptable para generar una alerta (en kilómetros)
    distancia_minima_aceptable = 500000

    # Buscar asteroides cercanos y generar alertas si es necesario
    sistema_alerta.buscar_asteroides_cercanos(distancia_minima_aceptable)
