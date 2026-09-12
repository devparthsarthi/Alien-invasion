import os


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.high_score_file = "high_score.txt"
        self.high_score = self._load_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _load_high_score(self):
        """Load the all-time high score from a file."""
        if os.path.exists(self.high_score_file):
            try:
                with open(self.high_score_file, "r", encoding="utf-8") as f:
                    return int(f.read().strip())
            except (ValueError, OSError):
                return 0
        return 0

    def save_high_score(self):
        """Save the high score to a file."""
        try:
            with open(self.high_score_file, "w", encoding="utf-8") as f:
                f.write(str(self.high_score))
        except OSError:
            pass
