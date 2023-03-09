import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from target import Target
from bullet import Bullet


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.target = Target(self)

        # Создание кнопки Play.
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_target()

            self._update_screen()

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def start_game(self):
        """Запускает новую игру."""
        # Сброс игровой статистики.
        self.stats.reset_stats()
        self.stats.game_active = True

        # Очистка списков пришельцев и снарядов.
        self.bullets.empty()

        # Создание нового флота и размещение корабля в центре.
        self.target.place_reset()
        self.ship.center_ship()

        # Указатель мыши скрывается.
        pygame.mouse.set_visible(False)

    def _check_play_button(self, mouse_pos):
        """Запускает новую игру при нажатии кнопки Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.start_game()

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавишы."""
        if event.key == pygame.K_p and not self.stats.game_active:
            self.start_game()
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавишы."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_fleet_edges(self):
        """Реагирует на достижение пришельцем края экрана."""
        if self.target.check_edges():
            self.settings.target_direction *= -1

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_target(self):
        """Обновляет позиции всех пришельцев во флоте."""
        self._check_fleet_edges()
        self.target.update()

    def _update_bullets(self):
        """Обновление позиции снарядов и уничтожение старых снарядов."""
        # Обновление позиций снарядов.
        self.bullets.update()

        # Удаление снарядов, вышедших за край экрана.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.ship.screen_rect.right:
                self.bullets.remove(bullet)
                self.target_hit()

        self._check_bullet_collisions()

    def target_hit(self):
        """Обрабатывает столкновение снаряда с мишенью."""
        if self.stats.misses_left > 1:
            self.stats.misses_left -= 1
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_bullet_collisions(self):
        """Обработка коллизий снарядов с пришельцами."""
        # Удаление снарядов и пришельцев, участвующих в коллизиях.
        for bullet in self.bullets.copy():
            collisions = pygame.sprite.collide_rect(
                bullet, self.target
            )
            if collisions:
                # Уничтожение существующих снарядов и создание нового флота
                sleep(0.5)
                self.stats.game_active = False
                pygame.mouse.set_visible(True)

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.target.draw_target()

        # Кнопка Play отображается в том случае, если игра неактивна.
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
