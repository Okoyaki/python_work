class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Настройки корабля
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Настройки пришельцев
        self.alien_speed = 0.5
        self.fleet_approach_speed = 3

        # fleet_direction = 1 обозначает движение вверх; а -1 - вниз.
        self.fleet_direction = 1
