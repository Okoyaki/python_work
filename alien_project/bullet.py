import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Класс для управления снарядами, выпущенными кораблём."""

    def __init__(self, ai_game):
        """Создает объект снарядов в текущей позиции корабля."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Создание снаряда в позиции (0, 0) и назначение правильной позиции.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Позиция снаряда хранится в вещественном формате.
        self.y = float(self.rect.y)
        self.enemy = False

    def update(self):
        """Перемещает снаряд вверх по экрану."""
        # Обновление позиции снаряда в вещественном формате.
        if self.enemy:
            self.y += self.settings.enemy_bullet_speed_factor
        else:
            self.y -= self.settings.bullet_speed_factor
        # Обновление позиции прямоугольника.
        self.rect.y = self.y

    """def update_enemy(self):
        # Перемещает снаряд вниз по экрану.
        # Обновление позиции снаряда в вещественном формате.
        self.y += self.settings.enemy_bullet_speed_factor
        # Обновление позиции прямоугольника.
        self.rect.y = self.y"""

    def set_enemy_bullet(self, alien_rect):
        """Изменение позиции пули врагов."""
        self.rect.midbottom = alien_rect.midbottom
        self.y = float(self.rect.y)
        self.enemy = True

    def draw_bullet(self):
        """Вывод снаряда на экран."""
        pygame.draw.rect(self.screen, self.color, self.rect)
