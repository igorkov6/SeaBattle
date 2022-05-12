# dot.py
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
# класс точки
# -------------------------------------------

class Dot:
    
    # -------------------------------------------
    # инициализация точки
    # -------------------------------------------
    
    def __init__(self, x=0, y=0):
        
        self.x = x
        self.y = y

    # -------------------------------------------
    # сравнение точек
    # -------------------------------------------
    
    def __eq__(self, other):
        
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    # -------------------------------------------
    # сложение точек
    # -------------------------------------------
    
    def __add__(self, other):
        
        return Dot(self.x + other.x, self.y + other.y)