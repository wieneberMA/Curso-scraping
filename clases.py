class Soldado:
    # Constructor de la clase Soldado
    def __init__(self, nivel):
        self.nivel = nivel  # Nivel del soldado, influye en sus atributos
        self.vida = 50 + (nivel * 10)  # Vida inicial basada en el nivel
        self.ataque = nivel * 5  # Poder de ataque basado en el nivel
        self.defensa = nivel + 1  # Poder de defensa basado en el nivel
        self.velocidad = 15  # Velocidad de movimiento del soldado
        self.vuela = False  # Capacidad de volar (False para todos los soldados en este diseño)

# Creación de instancias de Soldado con diferentes niveles
tropa1 = Soldado(10)
tropa2 = Soldado(15)

def calcular_vida_post_ataque(defensor, atacante):
    # Calcula la vida restante del defensor después de recibir un ataque
    vida_restante = defensor.vida - (atacante.ataque - defensor.defensa)
    vida_restante = max(0, vida_restante)  # Asegura que la vida no sea negativa
    return vida_restante

# Ejemplo de uso de las funciones e instancias
print("Tropa 1:", tropa1.nivel)
print("Tropa 2:", tropa2.nivel)

# Simulación de un ataque y muestra de resultados
vida_post_ataque = calcular_vida_post_ataque(tropa1, tropa2)
print(f"Tropa {tropa1.nivel} ataca a Tropa {tropa2.nivel} donde queda con un total de {vida_post_ataque} Vida")
