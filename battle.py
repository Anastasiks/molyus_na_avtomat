class Battle:
    def __init__(self, human, enemy):
        self.human = human
        self.enemy = enemy

    def start(self):
        with open("battle_log.txt", "a", encoding="utf-8") as log:
            log.write("=== НАЧАЛО БИТВЫ ===\n")


            while self.human.is_alive and self.enemy.is_alive:
                self.human.attack(self.enemy, log)
                if self.enemy.is_alive:
                    self.enemy.attack(self.human, log)

            if self.human.is_alive:
                log.write("Игрок победил!\n")
                return True
            else:
                log.write("Игрок проиграл!\n")
                return False
