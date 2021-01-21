import pygame#导入游戏模块
from pygame.sprite import Group

from settings import Settings#导入setting类
from game_stats import GameStats
from scoreboard import Scoreboard
from button_play import Button
from ship import Ship
import game_functions as gf
from record_db import DB
def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()#创建对象
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("飞机大战_by:徐广超")
    
    # 设置开始按钮
    play_button = Button(ai_settings, screen, "START")
    choose_button= Button(ai_settings, screen, "START")
    
    # 创建存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    ship = Ship(ai_settings, screen)#创建飞机
    bullets = Group()#子弹
    aliens = Group()#飞机
    
    # 创建一群飞机
    gf.create_fleet(ai_settings, screen, ship, aliens)

    pygame.mixer.music.load("resource/bg.mp3")  # 载入音效
    pygame.mixer.music.set_volume(1)  # 设置音量为 1
    pygame.mixer.music.play()  # 播放音效
    #开始游戏主循环
    while True:
        pygame.mixer.music.set_volume(0.5)  # 设置音量为 1
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
            aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
            bullets, play_button)
run_game()
