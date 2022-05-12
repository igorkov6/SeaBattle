# main.py
# =========================================
#               Игорь Ковалев igorkov6@gmail.com
# SkillFactory: FPW-2.0
# Модуль:       C2 Продолжение ООП
#               ИТОГОВОЕ ЗАДАНИЕ 2.5 (HW-02)
# project:      игра морской бой
# interpreter:  Python 3.8
# ide:          PyCharm 2021.3.2
# =========================================
# release:      v1.01 14.04.2022
#   игрок играет с компьютером
#   игровая стратегия компьютера не реализована
#   компьютер делает случайный ход
#   размер игрового поля и набор кораблей
#   задаются в настройках игры
# =========================================

from game import Game

# -------------------------------------------
# настройки игры в задании
# -------------------------------------------

# размер игрового поля
BOARD_SIZE = 6

# набор кораблей (размер, количество)
SHIP_SET = [(3, 1), (2, 2), (1, 4)]

# -------------------------------------------
# настройки стандартной игры
# -------------------------------------------

# размер игрового поля
# BOARD_SIZE = 10

# набор кораблей (размер, количество)
# SHIP_SET = [(4, 1), (3, 2), (2, 3), (1, 4)]

# -------------------------------------------
# старт игры
# -------------------------------------------

game = Game(board_size=BOARD_SIZE,
            ship_set=SHIP_SET)
game.start()

# =========================================