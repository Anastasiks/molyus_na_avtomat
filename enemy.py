
import random
import time
import sys
import random

def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        # небольшая вариативность, чтобы текст "дышал"
        time.sleep(delay + random.uniform(0, 0.02))
class Enemy:
    def __init__(self, name):
        self.name = name
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
        log.write(f"{self.name} ударил {human.name}а на {dam} урона\n")
        slow_print(f"{self.name} ударил {human.name}а на {dam} урона\n", 0.035)