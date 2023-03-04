import pygame

class Character():
    """Класс, определяющий игрового персонажа."""

    def __init__(self, game):
        """Инициализация персонажа и задание его начальной позиции."""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Загрузка изображения персонажа и получение прямоугольника
        self.image = pygame.image.load('images/character.bmp')
        self.rect = self.image.get_rect()
        # Каждый новый персонаж появляется у нижнего края
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Рисует персонажа в текущей позиции."""
        self.screen.blit(self.image, self.rect)