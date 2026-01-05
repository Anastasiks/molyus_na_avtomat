from human import Human
from enemy import Enemy
from battle import Battle
from artifacts import ArtifactStorage
import os


def save_game(player, login, password):
    """Сохраняет игру в файл."""
    with open("save.txt", "w", encoding="utf-8") as f:
        f.write(login + "\n")
        f.write(password + "\n")
        f.write(player.name + "\n")
        f.write(str(player.hp) + "\n")
        f.write(str(player.damage) + "\n")
        f.write(",".join(player.artifacts))
    print("💾 Игра сохранена")


def check_save_credentials(login, password):
    """Проверяет, совпадают ли логин и пароль с сохраненными."""
    if not os.path.exists("save.txt"):
        return False
    with open("save.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines()]
        if len(lines) < 2:
            return False

        saved_login = lines[0]
        saved_password = lines[1]

        return saved_login == login and saved_password == password


def load_game(login, password):
    """Загружает игру из файла для указанного пользователя."""
    if not os.path.exists("save.txt"):
        return None

    with open("save.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines()]
        if len(lines) < 4:
            return None

        saved_login = lines[0]
        saved_password = lines[1]

        # Проверка логина и пароля
        if saved_login != login or saved_password != password:
            return None

        name = lines[2]

        if len(lines) >= 6:
            hp = int(lines[3])
            damage = int(lines[4])
            artifacts = lines[5].split(",") if lines[5] else []

        player = Human(name)
        player.hp = hp
        player.damage = damage
        player.artifacts = artifacts

        return player


def show_menu():
    """Отображает главное меню игры."""
    print("\n" + "=" * 40)
    print("ГЛАВНОЕ МЕНЮ")
    print("=" * 40)
    print("1 — Пойти в лес")
    print("2 — Пойти в пещеру")
    print("3 — Остаться в деревне")
    print("4 — Выход из игры")
    print("=" * 40)


def main():
    # Запрашиваем логин и пароль
    login = input("Логин: ")
    password = input("Пароль: ")

    # Проверяем, есть ли сохранение для этого пользователя
    if check_save_credentials(login, password):
        print("💾 Найдено сохранение для этого пользователя!")
        load_choice = input("Загрузить сохранение? (y/n): ")
        if load_choice.lower() == "y":
            player = load_game(login, password)
            if player:
                print(f"✅ Игра загружена!")
                print(f"👤 Игрок: {player.name}")
                print(f"💚 Здоровье: {player.hp}")
                print(f"⚔️ Урон: {player.damage}")
                print(f"📦 Артефакты: {', '.join(player.artifacts) if player.artifacts else 'нет'}")
            else:
                print("❌ Ошибка загрузки. Начинаем новую игру.")
                player = Human("Герой")
        else:
            player = Human("Герой")
    else:
        if os.path.exists("save.txt"):
            print("⚠️ Сохранение найдено, но логин или пароль не совпадают.")
            print("Начинаем новую игру.")
        player = Human("Герой")

    storage = ArtifactStorage()

    while True:
        show_menu()
        choice = input("Ваш выбор: ")

        if choice == "1":
            print("\n🌲 Лес. На вас напали!")
            win = Battle(player, Enemy()).start()
            if win:
                artifact = storage.take_artifact()
                player.artifacts.append(artifact)
                print(f"✨ Вы получили артефакт: {artifact}")
            else:
                print("💀 Вы проиграли...")
                break
            print(f"\n💚 Ваше здоровье: {player.hp}")
            print(f"📦 Артефакты: {', '.join(player.artifacts) if player.artifacts else 'нет'}")

        elif choice == "2":
            print("\n🕳 Пещера. Сильный враг!")
            win = Battle(player, Enemy()).start()
            if win:
                artifact = storage.take_artifact()
                player.artifacts.append(artifact)
                print(f"✨ Вы получили артефакт: {artifact}")
            else:
                print("💀 Вы проиграли...")
                break
            print(f"\n💚 Ваше здоровье: {player.hp}")
            print(f"📦 Артефакты: {', '.join(player.artifacts) if player.artifacts else 'нет'}")

        elif choice == "3":
            print("\n🏠 Вы отдохнули в деревне")
            player.hp = min(100, player.hp + 20)  # Восстановление здоровья
            print(f"💚 Ваше здоровье восстановлено до {player.hp}")
            print(f"📦 Артефакты: {', '.join(player.artifacts) if player.artifacts else 'нет'}")

        elif choice == "4":
            print("\n👋 Выход из игры...")
            save = input("Сохранить игру перед выходом? (y/n): ")
            if save.lower() == "y":
                save_game(player, login, password)
            else:
                print("❌ Игра не сохранена")
            print("До свидания!")
            break

        else:
            print("❌ Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()