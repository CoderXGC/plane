class Settings():
    """设置类，包括窗口大小，背景颜色"""

    def __init__(self):
        """开始开屏幕的大小"""
        self.screen_width = 1200#宽
        self.screen_height = 800#高
        self.bg_color = (195, 200, 201)#设置背景颜色


        # 飞机设置.
        self.ship_limit = 1
            
        # 子弹设置.

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
        # 飞机下落速度
        self.fleet_drop_speed = 10
            
        # 游戏速度
        self.speedup_scale = 1.1
        # 飞船速度
        self.score_scale = 1.5
    
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        
        # 一个飞船50分
        self.alien_points = 50
    
        # fleet_direction为1表示向右；为-1表示向左
        self.fleet_direction = 1
        
    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
