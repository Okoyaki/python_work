class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует статические настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Настройки корабля
        self.ship_limit = 1

        # Сдвиг позиций кнопок по горизонтали
        self.x_off_easy = -1
        self.x_off_hard = 1

        # Параметры снаряда
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.enemy_bullets_allowed = 1

        # Настройки пришельцев
        self.fleet_drop_speed = 3

        # Темп ускорения игры
        self.speedup_scale = 1.1
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5

        self.difficulty_multiplier = 1.0

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed_factor = 1.5 * self.difficulty_multiplier
        self.bullet_speed_factor = 3.0 * self.difficulty_multiplier
        self.alien_speed_factor = 1.0 * self.difficulty_multiplier
        self.enemy_bullet_speed_factor = 1.5 * self.difficulty_multiplier

        # Подсчет очков
        self.alien_points = 50

        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимость пришельцев."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

