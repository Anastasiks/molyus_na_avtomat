import random
class Human:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.damage = 20
        self.artifacts = []

    @property
    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

    def attack(self, enemy, log):
        damag = (random.randint(0, self.damage))
        enemy.take_damage(damag)
        log.write(f"{self.name} ударил {enemy.name} на {damag} урона\n")
        print(f"{self.name} ударил {enemy.name} на {damag} урона\n")