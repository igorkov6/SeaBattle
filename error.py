# error.py
# =========================================
#               Игорь Ковалев igorkov6@gmail.com
# SkillFactory: FPW-2.0
# Модуль:       C2 Продолжение ООП
#               ИТОГОВОЕ ЗАДАНИЕ 2.5 (HW-02)
# project:      игра морской бой
# interpreter:  Python 3.8
# ide:          PyCharm 2021.3.2
# =========================================

# -------------------------------------------
# классы исключений
# -------------------------------------------

# лимит попыток исчерпан
class TryLimit(Exception):
    pass


# ошибка размещения корабля
class Placement(Exception):
    pass


# выстрел уже был
class AlreadyShot(Exception):
    pass


# выстрел за пределами поля
class OutOfBoard(Exception):
    pass


# выстрел мимо
class ShotPast(Exception):
    pass


# удачный выстрел
class ShotOk(Exception):
    pass


# не цифровой символ
class NotDigit(Exception):
    pass


# игра окончена
class GameOver(Exception):
    pass
