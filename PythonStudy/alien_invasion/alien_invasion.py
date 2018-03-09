# coding=gbk

  ###
    #     
    # @Author AVOli  
    # @Date 2018/2/1 15:40
    # @Description   用pygame写的打飞机游戏
    #
    ###

import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import  Scoreborad
from button import Button
from ship import Ship
import game_functions as gf
      

def run_game():

    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('sound/bg_music.ogg')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("外星人入侵")  # 设置标题

    #创建Play按钮
    play_button = Button(ai_settings,screen,"Play")

    #创建一个用于存储游戏统计信息的实列,并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreborad( ai_settings, screen, stats)
    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings,screen)

    #创建一个用于存储子弹的编组
    bullets = Group()
    aliens = Group()

    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)

    # 开始游戏的主循环
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        #更新屏幕上的图像，并切换到新屏幕
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
run_game()
