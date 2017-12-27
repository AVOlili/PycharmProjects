import pygame

class Ship():
    def __init__(self,screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect() #pygame通过Rect对象存储和操作矩形区域
        self.screen_rect = screen.get_rect()

        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #移动标志
        self.moving_right = False  #默认false，即不移动（有按键操作时才移动）
        self.moving_left = False
    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right:
            self.rect.centerx += 1 #如果为真就向右移动一个像素点
        if self.moving_left:
            self.rect.centerx -= 1 #如果为真就向左移动一个像素点

    def blitme(self):
        """
        在指定位置绘制飞船，
        self.screen是一个surface对象，
        将self.image图片复制到rect矩形区域
        """
        self.screen.blit(self.image,self.rect)