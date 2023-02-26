import random

# Вибір рівня складності та псевдоніму гравця
level = input("Виберіть рівень складності (легкий або середній): ")
name = input("Введіть свій псевдонім: ")

# Встановлюємо розмір поля в залежності від рівня складності
if level == "легкий":
    size = 5
else:
    size = 10

# Генеруємо випадкову позицію скарбу
treasure_row = random.randint(0, size-1)
treasure_col = random.randint(0, size-1)

# Головний цикл гри
moves = 0
while True:
    # Виводимо інформацію про стан гри
    print("Ходів: ", moves)
    for row in range(size):
        for col in range(size):
            if row == treasure_row and col == treasure_col:
                # Скарб знаходиться в цій клітинці
                print("X", end=" ")
            else:
                # Порожні клітинки позначаємо крапкою
                print(".", end=" ")
        print()

    # Гравець вводить координати руху
    move_row = int(input("Введіть рядок (0-{}): ".format(size-1)))
    move_col = int(input("Введіть стовпець (0-{}): ".format(size-1)))

    # Збільшуємо лічильник ходів
    moves += 1

    # Перевіряємо, чи знайшов гравець скарб
    if move_row == treasure_row and move_col == treasure_col:
        print("Вітаю, {}! Ви знайшли скарб за {} ходів!".format(name, moves))
        break