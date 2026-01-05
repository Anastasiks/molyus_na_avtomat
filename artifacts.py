import random

class ArtifactStorage:
    def __init__(self):
        self.all_artifacts = ["Кольцо", "Амулет", "Клинок"]

    def generate_new(self):
        print("⚡ Все артефакты собраны! Генерация новых...")
        self.all_artifacts = [
            f"Артефакт_{random.randint(100,999)}"
            for _ in range(3)
        ]

    def take_artifact(self):
        if not self.all_artifacts:
            self.generate_new()
        return self.all_artifacts.pop()