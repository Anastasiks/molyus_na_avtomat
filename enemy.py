class Enemy:
    def __init__(self):
        self.hp = 80
        self.damage = 15

    @property
    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

    def attack(self, human, log):
        human.take_damage(self.damage)
        log.write(f"Враг ударил {human.name} на {self.damage} урона\n")
