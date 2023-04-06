class GameStats():
    """Отслеживание статистики для игры Alien Invasion."""

    def __init__(self, ai_game):
        """Инициализирует статистику."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Рекорд не должен сбрасываться.
        self.high_score = 0

        # Игра Alien Invasion запускается в неактивном состоянии.
        self.game_active = False

        # Параметр для определения находится ли игрок в режиме выбора сложности.
        self.choosing_dif = False

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1