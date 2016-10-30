# -*- coding: utf-8 -*- 

import pygame


class SkillButton(pygame.sprite.Sprite):
    def __init__(self, starName, text, consumeMP, center):
        pygame.sprite.Sprite.__init__(self)
        
        self.starName = starName
        
        self.select = False
        self.hover = False
        self.consumeMP = consumeMP
        
        self.image = pygame.image.load("..\\pic\\solarSystem\\" + self.starName + "SmaBall.png").convert_alpha()
        self.rect  = self.image.get_rect()
        self.rect.center = center[0] - 80, center[1]
          
        self.font = pygame.font.FontType(r"..\font\minijianshaoer.ttf", 20)      # 字体
        self.text = text
        self.textImage = self.font.render(self.text, True, (0, 0, 0))
        self.textRect  = self.textImage.get_rect()
        self.textRect.center = center[0], center[1]
        
        # 加载各技能特效图片      技能1目前没有特效图片  所有用try
        if self.text != "Guide":
            self.specialBigRedImage   = pygame.image.load("..\\pic\others\\red" + self.text + "Big.png").convert_alpha()
            self.specialMidRedImage   = pygame.image.load("..\\pic\others\\red" + self.text + "Mid.png").convert_alpha()
            self.specialSmaRedImage   = pygame.image.load("..\\pic\others\\red" + self.text + "Sma.png").convert_alpha()
            self.specialBigBlackImage = pygame.image.load("..\\pic\others\\black" + self.text + "Big.png").convert_alpha()
            self.specialMidBlackImage = pygame.image.load("..\\pic\others\\black" + self.text + "Mid.png").convert_alpha()
            self.specialSmaBlackImage = pygame.image.load("..\\pic\others\\black" + self.text + "Sma.png").convert_alpha()
            
            self.specialBigRect = self.specialBigRedImage.get_rect()
            self.specialMidRect = self.specialMidRedImage.get_rect()
            self.specialSmaRect = self.specialSmaRedImage.get_rect()
    
        
    def reset_starImage(self, starName):
        self.starName = starName
        self.image = pygame.image.load("..\\pic\\solarSystem\\" + self.starName + "SmaBall.png").convert_alpha()
        
        

class StarButton(pygame.sprite.Sprite):
    def __init__(self, name, center):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("..\\pic\\solarSystem\\" + name + "BigBall.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = center
        
        self.displayText = False
        self.opacity = 110
        
    def create_text(self, string, center):
        font = pygame.font.FontType(r"..\font\minijianshaoer.ttf", 56)      # 字体
        self.text = string
        self.textImage = font.render(self.text, True, (0, 0, 0))
        self.textRect = self.textImage.get_rect()
        self.textRect.center = center
        
        
class QuitButton(pygame.sprite.Sprite):
    def __init__(self, name, center):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("..\\pic\\others\\" + name + ".png").convert_alpha()
        self.rect  = self.image.get_rect()
        self.rect.center = center 
        
        
        