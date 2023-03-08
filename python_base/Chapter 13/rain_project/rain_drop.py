import sys
import pygame

from settings import Settings
from rain import Rain


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        self.raindrops = pygame.sprite.Group()
        self.rain_disap = False

        self._create_fleet()

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()
            self._update_raindrops()
            self._update_screen()

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавишы."""
        if event.key == pygame.K_q:
            sys.exit()

    def _create_fleet(self):
        """Создание флота вторжения."""
        # Создание пришельца и вычисление количества пришельцев в ряду
        # Интервал между соседними пришельцами равен ширине пришельца.
        raindrop = Rain(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        available_space_x = self.settings.screen_width - (2 * raindrop_width)
        number_raindrops_x = available_space_x // (2 * raindrop_width)

        """Определяет количество рядов, помещающихся на экране."""
        available_space_y = (self.settings.screen_height -
                             (2 * raindrop_height))
        number_rows = available_space_y // (2 * raindrop_height)

        # Создание флота вторжения.
        for row_number in range(number_rows):
            for raindrop_number in range(number_raindrops_x):
                self._create_raindrop(raindrop_number, row_number)

    def _create_raindrop(self, raindrop_number, row_number):
        """Создание приешльца и размещение его в ряду."""
        raindrop = Rain(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        raindrop.x = raindrop_width + 2 * raindrop_width * raindrop_number
        raindrop.rect.x = raindrop.x
        raindrop.rect.y = raindrop_height + 2 * raindrop_height * row_number
        self.raindrops.add(raindrop)

    def _update_raindrops(self):
        """Update raindrops position and delete old raindrops, create a row if deleted"""
        self.raindrops.update()

        for raindrop in self.raindrops.copy():
            if raindrop.rect.top > self.settings.screen_height:
                self.raindrops.remove(raindrop)
                self.rain_disap = True

        if self.rain_disap:
            self._create_fleet()
            self.rain_disap = False


    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
