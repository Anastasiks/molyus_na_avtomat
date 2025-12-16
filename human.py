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
        enemy.take_damage(self.damage)
        log.write(f"{self.name} ударил врага на {self.damage} урона\n")
