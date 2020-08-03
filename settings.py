class Settings:
    """klasa u koju ćemo spremati postavke za najezdu svemiraca"""

    def __init__(self):
        """inicijalizira postavke igre"""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 500

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 50
        # fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # how quickly game speeds up
        self.speedup_scale = 1.1
        # how quickly alien point value increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and points value."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)