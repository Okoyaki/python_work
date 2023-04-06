class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Настройки корабля
        self.ship_limit = 3

        # Параметры снаряда
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        self.miss_limit = 3

        # Параметры мишени
        self.target_speed = 0.5
        self.target_width = 30
        self.target_height = 80
        self.target_color = (60, 60, 60)

        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.target_speed_factor = 1.0

        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.target_direction = 1

    def increase_target_speed(self):
        """Увеличивает настройки скорости."""
        self.target_speed_factor *= self.speedup_scale
