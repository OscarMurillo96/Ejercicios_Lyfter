"""
Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.
"""

class Runner:
    def __init__(self, speed):
        self.speed = speed


    def run(self):
        print(f"Running at {self.speed} km/h")


class Jumper:
    def __init__(self, jump_height):
        self.jump_height = jump_height


    def jump(self):
        print(f"jumping to a height of {self.jump_height}")


class GameCharacter(Runner, Jumper): #Multiple inheritance
    def __init__(self, speed, jump_height):
        Runner.__init__(self, speed)
        Jumper.__init__(self, jump_height)


character = GameCharacter(20, 2)
character.run()
character.jump()

