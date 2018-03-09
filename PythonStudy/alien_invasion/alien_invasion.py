# coding=gbk

  ###
    #     
    # @Author AVOli  
    # @Date 2018/2/1 15:40
    # @Description   ��pygameд�Ĵ�ɻ���Ϸ
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

    # ��ʼ����Ϸ������һ����Ļ����
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('sound/bg_music.ogg')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("����������")  # ���ñ���

    #����Play��ť
    play_button = Button(ai_settings,screen,"Play")

    #����һ�����ڴ洢��Ϸͳ����Ϣ��ʵ��,�������Ƿ���
    stats = GameStats(ai_settings)
    sb = Scoreborad( ai_settings, screen, stats)
    # ����һ�ҷɴ���һ���ӵ������һ�������˱���
    ship = Ship(ai_settings,screen)

    #����һ�����ڴ洢�ӵ��ı���
    bullets = Group()
    aliens = Group()

    #����������Ⱥ
    gf.create_fleet(ai_settings,screen,ship,aliens)

    # ��ʼ��Ϸ����ѭ��
    while True:
        # �������̺�����¼�
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        #������Ļ�ϵ�ͼ�񣬲��л�������Ļ
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
run_game()
