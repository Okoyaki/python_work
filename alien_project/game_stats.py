import json


class GameStats():
    """Отслеживание статистики для игры Alien Invasion."""

    def __init__(self, ai_game):
        """Инициализирует статистику."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Рекорд не должен сбрасываться.
        self.highscore_file = 'saved_files/highscore.json'
        self.high_score = 0
        self._load_highscore()

        # Игра Alien Invasion запускается в неактивном состоянии.
        self.game_active = False

        # Параметр для определения находится ли игрок в режиме выбора сложности.
        self.choosing_dif = False

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _load_highscore(self):
        """Загружает рекорд из файла."""
        with open(self.highscore_file) as hs:
            self.high_score = json.load(hs)

    def save_highscore(self):
        """Сохраняет рекорд в файл."""
        with open(self.highscore_file, 'w') as hs:
            json.dump(self.high_score, hs)
