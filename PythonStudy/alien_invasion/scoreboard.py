# coding=gbk
import json

import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreborad():
    """��ʾ�÷���Ϣ��"""

    def __init__(self, ai_settings, screen, stats):
        """��ʼ����ʾ�÷��漰������"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #��ʾ�÷���Ϣʱʹ�õ���������
        self.text_color = ( 30, 30, 30 )
        # ��None�ĳ�����"simsunnsimsun"������������ʾ���ģ�
        # print(pygame.font.get_fonts())�鿴���������б�
        self.font = pygame.font.SysFont("None",40)


        # ׼��������ߵ÷ֺ͵�ǰ�÷ֵ�ͼ��
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """���÷�ת��Ϊһ����Ⱦ��ͼ��"""
        rounded_score = round(self.stats.score,-1) #Բ����10�ı���
        score_str = "{:,}".format(rounded_score)
        #�ı�ת����ͼ�񣬷��ص���surface
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)

        #���÷ַ�����Ļ���Ͻ�
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_level(self):
        """���ȼ�ת��Ϊ��Ⱦ��ͼ��"""
        level_str = "Level: "+ str(self.stats.level)
        self.level_image =  self.font.render( level_str,True,self.text_color,self.ai_settings.bg_color)

        # ���ȼ����ڵ÷��·�
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.left - 180
        self.level_rect.top = self.score_rect.top

    def show_score(self):
        """����Ļ����ʾ�÷�"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        #���Ʒɴ�
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """����ߵ÷�ת��Ϊ��Ⱦ��ͼ��"""
        high_score = round(self.stats.high_score,-1)
        high_score_str = "High Score: "+"{:,}".format(high_score)
        #�ı�ת����ͼ��,���ص���surface
        self.high_score_image = self.font.render(high_score_str,True,
             self.text_color,self.ai_settings.bg_color)

        #����ߵ÷ַ�����Ļ��������
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = self.screen_rect.left + 380
        self.high_score_rect.top = self.score_rect.top

    def prep_ships(self):
        """��ʾ�����¶����ҷɴ�"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings , self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def save_score(self,high_score):
        """������߷�"""
        filename = 'HighScore.json'
        with open(filename,'w') as f_obj:
            json.dump(high_score,f_obj)
