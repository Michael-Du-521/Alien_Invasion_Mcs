class Settings:
    """Store all the classes of settings in Alien Invension"""

    def __init__(self):
        """Initialize the settings of the game"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        # fleet_direction = 1 means moving right, otherwise fleet_direction =-1 means moving left
        self.fleet_direction = 1

        self.bullet_speed = 1.5
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (255, 60, 60)
        self.bullet_allowed = 3
