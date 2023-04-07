import sys
from time import sleep
import sched, time
from random import randint

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
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

        # Создание экземпляров для хранения статистики
        # и панели результатов.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()

        self.initialize_fire_event()

        self._create_fleet()

        # Создание кнопки Play.
        self.play_button = Button(self, "Play")

        # Создание кнопок сложностей.
        self.button_easy = Button(self, "Easy", self.settings.x_off_easy)
        self.button_medium = Button(self, "Medium")
        self.button_hard = Button(self, "Hard", self.settings.x_off_hard)
        self.dif_buttons = [self.button_easy, self.button_medium, self.button_hard]

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_enemy_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stats.save_highscore()
                sys.exit()
            elif event.type == self.FIREEVENT:
                self._fire_enemy_bullet()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.stats.choosing_dif:
                    self._check_dif_button(mouse_pos)
                else:
                    self._check_play_button(mouse_pos)

    def start_game(self):
        """Запускает новую игру."""
        # Обновление статистики и инициализация параметров.
        self._reset_and_prep()
        self.settings.initialize_dynamic_settings()

        # Очистка списков пришельцев и снарядов.
        self.aliens.empty()
        self.bullets.empty()
        self.enemy_bullets.empty()

        # Создание нового флота и размещение корабля в центре.
        self._create_fleet()
        self.ship.center_ship()

        # Указатель мыши скрывается.
        pygame.mouse.set_visible(False)

    def _check_play_button(self, mouse_pos):
        """Запускает новую игру при нажатии кнопки Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active and not self.stats.choosing_dif:
            # Сброс игровых настроек.
            self.stats.choosing_dif = True

    def _check_dif_button(self, mouse_pos):
        """Меняет множитель сложности игры."""
        for button in self.dif_buttons:
            button_clicked = button.rect.collidepoint(mouse_pos)
            if button_clicked and not self.stats.game_active and self.stats.choosing_dif:
                if button == self.button_easy:
                    self.settings.difficulty_multiplier = 0.5
                elif button == self.button_medium:
                    self.settings.difficulty_multiplier = 1.0
                elif button == self.button_hard:
                    self.settings.difficulty_multiplier = 1.5
                self.start_game()

    def initialize_fire_event(self):
        """Инициализирует событие выстрела врагом снаряда."""
        self.FIREEVENT = pygame.USEREVENT + 0
        self.fire_int = 1000
        pygame.time.set_timer(self.FIREEVENT, self.fire_int)

    def _reset_and_prep(self):
        """Сбрасывает статистику и выводит её на экран."""
        # Сброс статистики.
        self.stats.reset_stats()
        self.stats.game_active = True
        self.stats.choosing_dif = False

        # Вывод статистики на экран.
        self.sb.prep_images()

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавишы."""
        if event.key == pygame.K_p and not self.stats.game_active:
            self.stats.choosing_dif = True
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            self.stats.save_highscore()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif self.stats.choosing_dif:
            if event.key == pygame.K_e:
                self.settings.difficulty_multiplier = 0.5
            elif event.key == pygame.K_m:
                self.settings.difficulty_multiplier = 1.0
            elif event.key == pygame.K_h:
                self.settings.difficulty_multiplier = 1.5
            self.start_game()

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавишы."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _create_fleet(self):
        """Создание флота вторжения."""
        # Создание пришельца и вычисление количества пришельцев в ряду
        # Интервал между соседними пришельцами равен ширине пришельца.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        """Определяет количество рядов, помещающихся на экране."""
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Создание флота вторжения.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Создание приешльца и размещение его в ряду."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Реагирует на достижение пришельцем края экрана."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Опускает весь флот и меняет направление флота."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _fire_enemy_bullet(self):
        """Создание нового вражеского снаряда и включение его в группу alien_bullets."""
        if len(self.enemy_bullets) < self.settings.enemy_bullets_allowed:
            new_enemy_bullet = Bullet(self)
            rand_alien = randint(0, len(self.aliens.sprites()) - 1)
            new_enemy_bullet.set_enemy_bullet(self.aliens.sprites()[rand_alien].rect)
            self.enemy_bullets.add(new_enemy_bullet)

    def _update_aliens(self):
        """Обновляет позиции всех пришельцев во флоте."""
        self._check_fleet_edges()
        self.aliens.update()

        # Проверка коллизий "пришелец - корабль".
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Проверить, добрались ли пришельцы до нижнего края экрана.
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Обрабатывает столкновение корабля с пришельцем."""
        if self.stats.ships_left > 0:
            # Уменьшение ships_left.
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Очистка списков пришельцев и снарядов.
            self.aliens.empty()
            self.bullets.empty()
            self.enemy_bullets.empty()

            # Создание нового флота и размещение корабля в центре.
            self._create_fleet()
            self.ship.center_ship()

            # Пауза.
            sleep(0.5)
        else:
            # self.stats.reset_stats()
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Проверяет, добрались ли пришельцы до нижнего края экрана."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Происходит то же самое, что при столкновении с кораблем.
                self._ship_hit()
                break

    def _update_bullets(self):
        """Обновление позиции снарядов и уничтожение старых снарядов."""
        # Обновление позиций снарядов.
        self.bullets.update()

        # Удаление снарядов, вышедших за край экрана.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _update_enemy_bullets(self):
        """Обновление позиции снарядов и уничтожение старых снарядов."""
        # Обновление позиций снарядов.
        self.enemy_bullets.update()

        # Удаление снарядов, вышедших за край экрана.
        for enemy_bullet in self.enemy_bullets.copy():
            if enemy_bullet.rect.top > self.settings.screen_height:
                self.enemy_bullets.remove(enemy_bullet)

        if pygame.sprite.spritecollideany(self.ship, self.enemy_bullets):
            self._ship_hit()

    def _check_bullet_alien_collisions(self):
        """Обработка коллизий снарядов с пришельцами."""
        # Удаление снарядов и пришельцев, участвующих в коллизиях.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            self.start_new_level()

    def start_new_level(self):
        """Запуск нового уровня."""
        # Уничтожение существующих снарядов и создание нового флота
        self.bullets.empty()
        self.enemy_bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()

        # Увеличение уровня.
        self.stats.level += 1
        self.sb.prep_level()

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for enemy_bullet in self.enemy_bullets.sprites():
            enemy_bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Вывод информации о счете.
        self.sb.show_score()

        # Кнопка Play отображается в том случае, если игра неактивна.
        if not self.stats.game_active:
            if not self.stats.choosing_dif:
                self.play_button.draw_button()
            else:
                for button in self.dif_buttons:
                    button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
