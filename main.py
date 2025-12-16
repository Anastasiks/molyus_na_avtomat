from human import Human
from enemy import Enemy
from battle import Battle
from artifacts import ArtifactStorage

def save_game(player, login, password):
    with open("save.txt", "w", encoding="utf-8") as f:
        f.write(login + "\n")
        f.write(password + "\n")
        f.write(player.name + "\n")
        f.write(",".join(player.artifacts))
    print("💾 Игра сохранена")

def main():
    login = input("Логин: ")
    password = input("Пароль: ")

    player = Human("Герой")
    storage = ArtifactStorage()

    print("1 — Пойти в лес")
    print("2 — Пойти в пещеру")
    print("3 — Остаться в деревне")

    choice = input("Ваш выбор: ")

    if choice == "1":
        print("🌲 Лес. На вас напали!")
        win = Battle(player, Enemy()).start()
        if win:
            player.artifacts.append(storage.take_artifact())

    elif choice == "2":
        print("🕳 Пещера. Сильный враг!")
        win = Battle(player, Enemy()).start()
        if win:
            player.artifacts.append(storage.take_artifact())

    elif choice == "3":
        print("🏠 Вы отдохнули, но ничего не нашли")

    print("Артефакты:", player.artifacts)

    save = input("Сохранить игру? (y/n): ")
    if save == "y":
        save_game(player, login, password)
    else:
        print("❌ Прогресс сброшен, артефакты возвращены")

if __name__ == "__main__":
    main()
