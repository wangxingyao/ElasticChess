# -*- coding: utf-8 -*-
import pygame
import math


class Arrow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.centerImage = pygame.image.load(r"..\pic\ball\arrowCenter.png").convert_alpha()
        self.rect = self.centerImage.get_rect()
        
        self.image = pygame.image.load(r"..\pic\ball\arrow.png").convert_alpha()        
        self.length = 0
        self.minLength = 30
        self.maxLength = 145-20
        self.angle = 0
        self.life = False
        self.x = 0
        self.y = 0
        self.tailImage = self.image.subsurface((0, 0),(self.length, 12))
        self.tailRotatedImage = pygame.transform.rotate(self.tailImage, self.angle * (180 / math.pi))
        self.headImage = self.image.subsurface(((320-self.length), 0),(self.length, 12))
        self.headRotatedImage = pygame.transform.rotate(self.headImage, self.angle * (180 / math.pi))
    
    
    # 计算    弓箭半长度
    def calc_length(self, mousePositionStart, mousePositionStop):
        self.x = mousePositionStart[0] - mousePositionStop[0]
        self.y = mousePositionStop[1] - mousePositionStart[1]
        self.length = math.sqrt(self.x ** 2 + self.y ** 2)
        
            
    # 创建    旋转后的箭尾图
    def create_rotatedImage(self, mousePositionStart, mousePositionStop):
        # x,y为start相对stop的坐标(直角坐标系)
        self.x = mousePositionStart[0] - mousePositionStop[0]
        self.y = mousePositionStop[1]  - mousePositionStart[1]
        if self.length > 0 and self.y != 0:
            self.angle = math.acos(self.x / self.length) * self.y / math.fabs(self.y)
        if self.length <= 320:
            self.tailImage = self.image.subsurface((0, 0),(self.length, 12))
            self.headImage = self.image.subsurface(((320-self.length), 0),(self.length, 12))
        self.tailRotatedImage = pygame.transform.rotate(self.tailImage, self.angle * (180 / math.pi))
        self.headRotatedImage = pygame.transform.rotate(self.headImage, self.angle * (180 / math.pi))
       
       
    # 计算    箭尾旋转后的位置
    def calc_tailRotatedRect(self, mousePositionStart, mousePositionStop):
        self.tailRotatedRect = self.tailRotatedImage.get_rect()
        self.tailRotatedRect.left = (mousePositionStart[0] + mousePositionStop[0]) // 2 - self.tailRotatedRect.width // 2
        self.tailRotatedRect.top  = (mousePositionStart[1] + mousePositionStop[1]) // 2 - self.tailRotatedRect.height // 2
       
                
    # 计算    箭头旋转后的位置
    def calc_headRotatedRect(self, mousePositionStart, mousePositionStop):
        self.headRotatedRect = self.headRotatedImage.get_rect()
        self.headRotatedRect.left = 2 * mousePositionStart[0] - (mousePositionStart[0] + mousePositionStop[0]) // 2 - self.headRotatedRect.width // 2
        self.headRotatedRect.top  = 2 * mousePositionStart[1] - (mousePositionStart[1] + mousePositionStop[1]) // 2 - self.headRotatedRect.height // 2
        
            