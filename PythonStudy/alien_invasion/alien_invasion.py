# coding=gbk
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # ��ʼ����Ϸ������һ����Ļ����
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("����������")  # ���ñ���
    # ����һ�ҷɴ�
    ship = Ship(ai_settings,screen)

    # ��ʼ��Ϸ����ѭ��
    while True:
        # �������̺�����¼�
        gf.check_events(ship)
        ship.update()
        # ÿ��ѭ��ʱ�ػ���Ļ
        # ��������Ƶ���Ļ�ɼ�
        gf.update_screen(ai_settings,screen,ship)

run_game()
