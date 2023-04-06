import pygame
from pygame.sprite import Sprite


class Target(Sprite):
    """Класс для управления снарядами, выпущенными кораблём."""

    def __init__(self, ai_game):
        """Создает объект мишеней."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.target_color

        # Создание мишени в позиции (0, 0) и назначение правильной позиции.
        self.rect = pygame.Rect(self.settings.screen_width - self.settings.target_width - 10,
                                10, self.settings.target_width,
                                self.settings.target_height)

        # Позиция мишени хранится в вещественном формате.
        self.y = float(self.rect.y)

    def check_edges(self):
        """Возвращает True, если пришелец находится у края экрана."""
        screen_rect = self.screen.get_rect()
        if self.rect.top <= 0 or self.rect.bottom >= screen_rect.bottom:
            return True

    def update(self):
        """Перемещает снаряд вверх по экрану."""
        # Обновление позиции мишени в вещественном формате.
        self.y += (self.settings.target_speed_factor *
                        self.settings.target_direction)
        # Обновление позиции прямоугольника.
        self.rect.y = self.y

    def place_reset(self):
        """Возвращает мишень на начальное место."""
        self.rect.x = self.settings.screen_width - self.settings.target_width - 10
        self.rect.y = 10
        self.y = float(self.rect.y)

    def draw_target(self):
        """Вывод снаряда на экран."""
        pygame.draw.rect(self.screen, self.color, self.rect)
