import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """子弹管理的类"""

    def __init__(self, ai_settings, screen, ship):
        """在飞机所在处创建子弹"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.image = pygame.image.load('resource/bullet_2.png')
        self.rect = self.image.get_rect()
       # self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # self.rect = self.image.get_rect()
        # self.screen_rect = screen.get_rect()  # 获取外接矩形


        #存储用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
       #更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
