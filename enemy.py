
import random
class Enemy:
    def __init__(self):
        self.hp = random.randint(20, 80)
        self.damage = 15

    @property
    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

    def attack(self, human, log):
        dam = (random.randint(0, self.damage))
        human.take_damage(dam)
        log.write(f"Враг ударил {human.name} на {dam} урона\n")
        print(f"Враг ударил {human.name} на {dam} урона\n")