from random import choice

class RandomWalk():
    """Класс для генерирования случайных блужданий."""

    def __init__(self, num_points=5000):
        """Инициализирует атрибуты блуждания."""
        self.num_points = num_points

        # Все блуждания начинаются с точки (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Определяет направление и длину перемещения."""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance

    def fill_walk(self):
        """Вычисляет все точки блуждания."""

        # Шаги генерируются до достижения нужной длины.
        while len(self.x_values) < self.num_points:

            # Определение направления и длины перемещения.
            x_step = self.get_step()
            y_step = self.get_step()

            # Отклонение нулевых перемещений.
            if x_step == 0 and y_step == 0:
                continue

            # Вычисление следующих значений x и y.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
