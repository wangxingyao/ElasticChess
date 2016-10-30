# -*- coding: utf-8 -*-
import pygame
import math
import copy
import buttonClass




class Player():
    idCard = None
    starName = None
    skillCard = None
                
    def __init__(self):
        self.ballGroup = pygame.sprite.Group()
        self.ballsEkPower = 0    











class SkillCard():
    def __init__(self, starName, cardImagePath, center):
        self.skillCardImage = pygame.image.load(cardImagePath).convert_alpha()
        self.rect = self.skillCardImage.get_rect()
        self.rect.center = center
        self.starName = starName
        self.opacity = 180
        
        self.arrowheadImage = pygame.image.load(r"..\pic\others\triangularArrowhead.png").convert_alpha()
        self.arrowheadRect  = self.arrowheadImage.get_rect()
        
        self.skill1Button = buttonClass.SkillButton(self.starName, "Guide", 10, (self.rect.center[0], self.rect.center[1] - 45))
        self.skill2Button = buttonClass.SkillButton(self.starName, "Narrow", 40, (self.rect.center[0], self.rect.center[1] - 15))
        self.skill3Button = buttonClass.SkillButton(self.starName, "Enlarge", 40, (self.rect.center[0], self.rect.center[1] + 15))
        self.skill4Button = buttonClass.SkillButton(self.starName, "Relocate", 60, (self.rect.center[0], self.rect.center[1] + 45))
        
        self.skillButtonGroup = pygame.sprite.Group()
        self.skillButtonGroup.add(self.skill1Button, self.skill2Button, self.skill3Button, self.skill4Button)
        
        
    def reset_skillCard(self, starName):
        self.starName = starName
        self.skill1Button.reset_starImage(self.starName)
        self.skill2Button.reset_starImage(self.starName)
        self.skill3Button.reset_starImage(self.starName)
        self.skill4Button.reset_starImage(self.starName)
        
    def select_button(self, selectButton):
        self.skillButtonGroup.remove(selectButton)
        for eachButton in self.skillButtonGroup:
            eachButton.select = False
        self.skillButtonGroup.add(selectButton)
        selectButton.select = not selectButton.select
    
    def empty_allButtonSelect(self):
        for eachButton in self.skillButtonGroup:
            eachButton.select = False
        
    
    
    
    
    
    
    
    
    
    
    
    
class IDCard():
    def __init__(self, starName, cardImagePath, center):
        self.IDImage = pygame.image.load(cardImagePath).convert_alpha()
        self.rect = self.IDImage.get_rect()
        self.rect.center = center
        self.starName = starName
        self.score = 0
        self.HP = 100
        self.MP = 100
        self.opacity = 180
        
        self.font = pygame.font.FontType(r"..\font\minijianshaoer.ttf", 20)      # 字体
        self.starImage = pygame.image.load("..\\pic\\solarSystem\\" + self.starName + "BigBall.png").convert_alpha()
        self.starImageRect  = self.starImage.get_rect()
        self.starImageRect.center  = self.rect.center[0] + 70, self.rect.center[1] - 30
        
        self.nameText  = "name: " + starName
        self.nameTextImage  = self.font.render(self.nameText,  True, (0, 0, 0))
        self.nameTextRect   = self.nameTextImage.get_rect()
        self.nameTextRect   = self.rect.center[0] - 95, self.rect.center[1] - 45 - 10
        
        self.scoreText = "score: " + str(self.score)
        self.scoreTextImage = self.font.render(self.scoreText, True, (0, 0, 0))
        self.scoreTextRect  = self.scoreTextImage.get_rect()
        self.scoreTextRect   = self.rect.center[0] - 95, self.rect.center[1] - 15 -10
        
        self.HPText    = "HP:          " + str(self.HP) + "%"
        self.HPTextImage       = self.font.render(self.HPText,    True, (0, 0, 0))
        self.HPTextRect        = self.HPTextImage.get_rect()
        self.HPTextRect   = self.rect.center[0] - 95, self.rect.center[1] + 15 - 10
        
        self.HPBaseImage   = pygame.image.load(r"..\pic\others\base.png").convert_alpha()
        self.HPBaseRect    = self.HPBaseImage.get_rect()
        self.HPBaseRect    = self.rect.center[0], self.rect.center[1]
        self.HPPurpleImage = pygame.image.load(r"..\pic\others\purpleHP.png").convert_alpha()
        self.HPGreenImage  = pygame.image.load(r"..\pic\others\greenHP.png").convert_alpha()
        self.HPRedImage    = pygame.image.load(r"..\pic\others\redHP.png").convert_alpha()
        self.HPImage       = self.HPGreenImage
        self.HPRect        = self.HPImage.get_rect()
        self.HPRect        = self.rect.center[0] - 55, self.rect.center[1] + 15 - 2
        
        
        self.MPText    = "MP:          " + str(self.MP) + "%"
        self.MPTextImage    = self.font.render(self.MPText,    True, (0, 0, 0))
        self.MPTextRect     = self.MPTextImage.get_rect()
        self.MPTextRect   = self.rect.center[0] - 95, self.rect.center[1] + 45 - 10
        self.MPBlueImage  = pygame.image.load(r"..\pic\others\blueMP.png").convert_alpha()
        self.MPImage      = self.MPBlueImage
        self.MPRect       = self.MPImage.get_rect()
        self.MPRect       = self.rect.center[0] - 55, self.rect.center[1] + 45 - 2
        
    
    def blit_screen(self, screen):
        screen.blit(self.nameTextImage, self.nameTextRect)
        screen.blit(self.nameTextImage, self.nameTextRect)
        screen.blit(self.scoreTextImage, self.scoreTextRect)
        screen.blit(self.HPTextImage, self.HPTextRect)
        screen.blit(self.nameTextImage, self.nameTextRect)
        screen.blit(self.scoreTextImage, self.scoreTextRect)
        screen.blit(self.HPTextImage, self.HPTextRect)


    def reset_HP(self, addHP = 0):  # 增加HP
        self.HP += addHP
        self.HPText    = "HP:          " + str(self.HP) + "%"
        self.HPTextImage    = self.font.render(self.HPText,    True, (0, 0, 0))
        if self.HP <= 30:
            self.HPImage = self.HPRedImage.subsurface((0, 0), (1.5 * self.HP, 10))
        elif self.HP <= 100:
            self.HPImage = self.HPGreenImage.subsurface((0, 0), (1.5 * self.HP, 10))
        else:
            self.HPImage = self.HPPurpleImage
        
        self.scoreText = "score: " + str(self.score)
        self.scoreTextImage = self.font.render(self.scoreText, True, (0, 0, 0))
       
    def reset_MP(self, addMP = 0):  # 增加MP
        self.MP += addMP
        if self.MP > 100:
            self.MP = 100
        self.MPText    = "MP:          " + str(self.MP) + "%"
        self.MPTextImage    = self.font.render(self.MPText,    True, (0, 0, 0))
        self.MPImage     = self.MPBlueImage.subsurface((0, 0), (1.5 * self.MP, 10))
    
    
    
    def reset_IDCard(self, starName=None):
        if starName:
            self.starName = starName
            self.score = 0
            self.HP = 100
            self.MP = 100
            self.starImage = pygame.image.load("..\\pic\\solarSystem\\" + self.starName + "BigBall.png").convert_alpha()
            self.nameText  = "name: " + starName
            self.nameTextImage  = self.font.render(self.nameText,  True, (0, 0, 0))
            self.HPImage = self.HPGreenImage
        
        
        self.scoreText = "score: " + str(self.score)
        self.scoreTextImage = self.font.render(self.scoreText, True, (0, 0, 0))
        self.HPText    = "HP:          " + str(self.HP) + "%"
        self.HPTextImage    = self.font.render(self.HPText,    True, (0, 0, 0))
        # HP  MP  检测
        if self.MP > 100:
            self.MP = 100
        self.MPText    = "MP:          " + str(self.MP) + "%"
        self.MPTextImage    = self.font.render(self.MPText,    True, (0, 0, 0))
        
        if self.HP <= 30:
            self.HPImage = self.HPRedImage.subsurface((0, 0), (1.5 * self.HP, 10))
        elif self.HP <= 100:
            self.HPImage = self.HPGreenImage.subsurface((0, 0), (1.5 * self.HP, 10))
        else:
            self.HPImage = self.HPPurpleImage
        self.MPImage     = self.MPBlueImage.subsurface((0, 0), (1.5 * self.MP, 10))
    











class Ball(pygame.sprite.Sprite):
    def __init__(self, chessboardRect, string, center):
        pygame.sprite.Sprite.__init__(self)
        
        #文件记录    self.fileName = "..\\collideRecord\\" + string + "_" + str(number) + ".txt"
        self.string = string
        self.oimage = pygame.image.load("..\\pic\\ball\\" + string + ".png").convert_alpha()
        self.image = self.oimage
        self.rect = self.image.get_rect()
        self.rect.center = center
        
        # 半径   质量   角度   速率    能量
        self.radius = self.rect.width // 2
        if string[-7] == 'B':
            self.mass = 0.3025
        elif string[-7] == 'M':
            self.mass = 0.1600
        elif string[-7] == 'S':
            self.mass = 0.0625
        elif string[-8:] == "Boundary":
            self.mass = 999999999999999
            
        self.angle = 0                          # 棋子速度的角度
        self.velocity = 0                       # 棋子速度
        self.velocity_x = 0                     # 棋子X轴分速度
        self.velocity_y = 0                     # 棋子Y轴分速度
        self.opacity = 255                      # 棋子透明度
        self.isCollide = False                  # 棋子是否碰撞
        self.centerPosition = list(center)      # 棋子中心坐标
        # 文件记录    self.count = 0                 # 文件记录
        self.life = True                        # 棋子生命,若棋子与棋盘有接触则有生命，否则无生命
        self.onChessboard = True                # 棋子中心是否在棋盘上
        self.chessboardSize = 490, 542          # 棋盘尺寸
        self.chessboardRect = chessboardRect    # 棋盘坐标
 
 
    # 技能   放大棋子
    def enlarge_ball(self):
        if self.string[-7] == "B":
            return False
        elif self.string[-7] == "M":
            self.string = self.string[:-7] + "Big" + self.string[-4:]
        elif self.string[-7] == "S":
            self.string = self.string[:-7] + "Mid" + self.string[-4:]    
            
        self.oimage = pygame.image.load("..\\pic\\ball\\" + self.string + ".png").convert_alpha()
        self.image = self.oimage
        self.rect  = self.image.get_rect()
        self.rect.center = self.centerPosition
        # 半径   质量   角度   速率    能量
        self.radius = self.rect.width // 2
        if self.string[-7] == 'B':
            self.mass = 0.3025
            return 8
        elif self.string[-7] == 'M':
            self.mass = 0.1600
            return 4
        

    def relocate_ball(self, center):
        self.centerPosition = list(center)
 
 
    # 技能   缩小棋子
    def narrow_ball(self):
        if self.string[-7] == "B":
            self.string = self.string[:-7] + "Mid" + self.string[-4:]
        elif self.string[-7] == "M":
            self.string = self.string[:-7] + "Sma" + self.string[-4:]    
        elif self.string[-7] == "S":
            return False
            
        self.oimage = pygame.image.load("..\\pic\\ball\\" + self.string + ".png").convert_alpha()
        self.image = self.oimage
        self.rect  = self.image.get_rect()
        self.rect.center = self.centerPosition
        # 半径   质量   角度   速率    能量
        self.radius = self.rect.width // 2
        if self.string[-7] == 'M':
            self.mass = 0.1600
            return -8
        elif self.string[-7] == 'S':
            self.mass = 0.0625
            return -4
        
    
    def set_angle(self, positionStart, positionStop):
        # A 为 start,B 为 Stop,计算的是 BA 角度
        # x,y为start相对stop的坐标(直角坐标系)
        self.x = positionStart[0] - positionStop[0]
        self.y = positionStop[1]  - positionStart[1]
        length = math.sqrt(self.x ** 2 + self.y ** 2)
        if self.y != 0:
            self.angle = math.acos(self.x / length) * self.y / math.fabs(self.y)
        elif self.x > 0:
            self.angle = 0
        else:
            self.angle = math.pi
            
    
    # 碰撞函数
    def collide(self, collideBall, isChessman):
        # 第0步：转换变量名
        B = copy.copy(self)
        A = copy.copy(collideBall)
        
        angleB = B.angle
        VB     = B.velocity
        # VBX    = B.velocity_x
        # VBY    = -B.velocity_y
        MB     = B.mass
        angleA = A.angle
        VA     = A.velocity
        # VAX    = A.velocity_x
        # VAY    = -A.velocity_y
        MA     = A.mass
    
        # 第1步：求 XAB 轴的角度，即 B 相对于 A 的角度
        positionA = collideBall.rect.left + collideBall.rect.width / 2, collideBall.rect.top  + collideBall.rect.height / 2 
        positionB = self.rect.left + self.rect.width / 2, self.rect.top  + self.rect.height / 2
        x = positionB[0] - positionA[0]
        y = positionA[1] - positionB[1]
        if x == 0 and y == 0:
            print("错误120:两球发生重叠!")
            angleAB = 0
        elif y != 0:
            angleAB = math.acos(  x  / math.sqrt(x ** 2 + y ** 2)) *   y  / math.fabs( y)
            # angleBA = math.acos((-x) / math.sqrt(x ** 2 + y ** 2)) * (-y) / math.fabs(-y)
        else:
            angleAB = math.acos(  x  / math.sqrt(x ** 2 + y ** 2))
            # angleBA = math.acos((-x) / math.sqrt(x ** 2 + y ** 2))
        
        
        # 第1.5步：为防止粘连现象，调整小球位置
        actualCenterDistance       = math.sqrt((self.rect.center[0] - collideBall.rect.center[0]) ** 2 + (self.rect.center[1] - collideBall.rect.center[1]) ** 2)
        idealCenterDistance        = self.radius + collideBall.radius
        oneBallNeedMoveDistance    = (idealCenterDistance - actualCenterDistance) / 2
        selfBallNeedMoveDistance_x = oneBallNeedMoveDistance * math.cos(angleAB)
        selfBallNeedMoveDistance_y = oneBallNeedMoveDistance * math.sin(angleAB)
        self.centerPosition[0] += selfBallNeedMoveDistance_x * 2
        self.centerPosition[1] -= selfBallNeedMoveDistance_y * 2
        self.rect.center = self.centerPosition
        if isChessman:
            collideBall.centerPosition[0] -= selfBallNeedMoveDistance_x
            collideBall.centerPosition[1]+= selfBallNeedMoveDistance_y
            collideBall.rect.center = collideBall.centerPosition
        else:
            self.centerPosition[0] += selfBallNeedMoveDistance_x * 2
            self.centerPosition[1] -= selfBallNeedMoveDistance_y * 2
            self.rect.center = self.centerPosition
            
    
        
        
        # 第2步：记录 XAB 坐标系中 VB VA 的角度
        #       并求出 XAB 坐标系中 X Y 轴的分速度
        angleNB = angleB - angleAB
        ##if angleNB <= -math.pi:
        ##    angleNB += 2 * math.pi
        VNB  = VB
        VNBX = VNB * math.cos(angleNB)
        VNBY = VNB * math.sin(angleNB)
        
        angleNA = angleA - angleAB
        ##if angleNA <= -math.pi:
        ##    angleNA += 2 * math.pi
        VNA  = VA
        VNAX = VNA * math.cos(angleNA)
        VNAY = VNA * math.sin(angleNA)
        
        # 第3步：XAB( 坐标系中，Y 轴速度不变，X 轴速度满足完全弹性正碰
        #       计算 X 轴上碰撞后的新速度
        VPNBX = ((MB - MA) * VNBX + 2 * MA * VNAX) / (MA + MB)
        VPNBY = VNBY
        
        VPNAX = ((MA - MB) * VNAX + 2 * MB * VNBX) / (MA + MB)
        VPNAY = VNAY
        
        # 第4步：合成碰撞后的新速度，并计算 XAB中的新角度
        VPNB = math.sqrt(VPNBX ** 2 + VPNBY ** 2)
        if VPNBX == 0 and VPNBY == 0:
            #print("错误121:碰撞后B新速度为0")
            anglePNB = 0
        elif VPNBY != 0:
            anglePNB = math.acos(VPNBX / VPNB) * VPNBY / math.fabs(VPNBY)
        else:
            anglePNB = math.acos(VPNBX / VPNB)
        
        VPNA = math.sqrt(VPNAX ** 2 + VPNAY ** 2)
        if VPNAX == 0 and VPNAY == 0:
            #print("错误122:碰撞后A新速度为0")
            anglePNA = 0
        elif VPNAY != 0:
            anglePNA = math.acos(VPNAX / VPNA) * VPNAY / math.fabs(VPNAY)
        else:
            anglePNA = math.acos(VPNAX / VPNA)
            
        # 第5步：将 XAB 坐标系转化为 XB XA 坐标系中的速度和角度
        angleZB = anglePNB + angleAB
        ##if angleZB > math.pi:
        ##    angleZB -= 2 * math.pi
        VZB  = VPNB
        VZBX = VZB * math.cos(angleZB)
        VZBY = VZB * math.sin(angleZB)
        
        angleZA = anglePNA + angleAB
        ##if angleZA > math.pi:
        ##    angleZA -= 2 * math.pi
        VZA  = VPNA
        VZAX = VZA * math.cos(angleZA)
        VZAY = VZA * math.sin(angleZA)
        
        # 第5.9步：检测角度范围，调整到(-pi, pi]
        if angleZA > math.pi:
            angleZA -= 2 * math.pi
        elif angleZA <= -math.pi:
            angleZA += 2 * math.pi
        if angleZB > math.pi:
            angleZB -= 2 * math.pi
        elif angleZB <= -math.pi:
            angleZB += 2 * math.pi
        
        # 第6步：赋值操作
        self.angle      = angleZB
        self.velocity   = VZB
        self.velocity_x = VZBX
        self.velocity_y = -VZBY
        self.isCollide  = True
    
        if isChessman:
            collideBall.angle      = angleZA
            collideBall.velocity   = VZA
            collideBall.velocity_x = VZAX
            collideBall.velocity_y = -VZAY
            collideBall.isCollide  = True
    
        
        # 文件记录
        '''
        if self.count == 0:
            # 计算动能
            EkA   = 1/2 * MA * VA * VA
            EkNA  = 1/2 * MA * VNA * VNA
            EKPNA = 1/2 * MA * VPNA * VPNA
            EKZA  = 1/2 * MA * VZA * VZA
            
            EkB   = 1/2 * MB * VB * VB
            EkNB  = 1/2 * MB * VNB * VNB
            EKPNB = 1/2 * MB * VPNB * VPNB
            EKZB  = 1/2 * MB * VZB * VZB
            
            string0 = "angleA = %6.2f" % angleA  + "   angleNA = %6.2f" % angleNA + "   anglePNA = %6.2f" % anglePNA + "   angleZA = %6.2f" % angleZA + "   angleAB = %6.2f \n" % angleAB
            string1 = "VA     = %6.2f" % VA      + "   VNA     = %6.2f" % VNA     + "   VPNA     = %6.2f" % VPNA     + "   VZA     = %6.2f" % VZA     + "\n"    
            string2 = "VAX    = %6.2f" % VAX     + "   VNAX    = %6.2f" % VNAX    + "   VPNAX    = %6.2f" % VPNAX    + "   VZAX    = %6.2f" % VZAX    + "\n"
            string3 = "VAY    = %6.2f" % VAY     + "   VNAY    = %6.2f" % VNAY    + "   VPNAY    = %6.2f" % VPNAY    + "   VZAY    = %6.2f" % VZAY    + "\n"
            string4 = "EkA    = %6.2f" % EkA     + "   EkNA    = %6.2f" % EkNA    + "   EkPNA    = %6.2f" % EKPNA    + "   EkZA    = %6.2f" % EKZA    + "\n\n"
             
            string5 = "angleB = %6.2f" % angleB  + "   angleNB = %6.2f" % angleNB + "   anglePNB = %6.2f" % anglePNB + "   angleZB = %6.2f" % angleZB + "   angleAB = %6.2f \n" % angleAB
            string6 = "VB     = %6.2f" % VB      + "   VNB     = %6.2f" % VNB     + "   VPNB     = %6.2f" % VPNB     + "   VZB     = %6.2f" % VZB     + "\n"    
            string7 = "VBX    = %6.2f" % VBX     + "   VNBX    = %6.2f" % VNBX    + "   VPNBX    = %6.2f" % VPNBX    + "   VZBX    = %6.2f" % VZBX    + "\n"
            string8 = "VBY    = %6.2f" % VBY     + "   VNBY    = %6.2f" % VNBY    + "   VPNBY    = %6.2f" % VPNBY    + "   VZBY    = %6.2f" % VZBY    + "\n"
            string9 = "EkB    = %6.2f" % EkB     + "   EkNB    = %6.2f" % EkNB    + "   EkPNB    = %6.2f" % EKPNB    + "   EkZB    = %6.2f" % EKZB    + "\n"
            
            f = open(self.fileName, "w")
            f.write( string0 )
            f.write( string1 )
            f.write( string2 )
            f.write( string3 )
            f.write( string4 )
            f.write( string5 )
            f.write( string6 )
            f.write( string7 )
            f.write( string8 )
            f.write( string9 )
            f.close()
            self.count += 1
        ''' 
              
        
    
     
    
    # 蓄力弓箭
    def set_velocity(self, velocity):
        self.velocity = (velocity - 25) / 10
        self.velocity_x =  self.velocity * math.cos(self.angle)
        self.velocity_y = -self.velocity * math.sin(self.angle)
       
    
    def move(self):
        # 默认重力加速度为0.5，摩擦因数0.1
        if self.onChessboard:
            self.velocity -= 0.5 * 0.1
            pass
        else:
            # self.velocity -= 0.5 * 0.1
            pass
            '''
            self.velocity_x = self.velocity * math.cos(self.angle)
            self.velocity_y = self.velocity * math.sin(self.angle)
            self.velocity_y -= 0.5
            self.velocity = math.sqrt(self.velocity_x ** 2 + self.velocity_y ** 2)
            if self.velocity_y == 0:
                self.angle = math.acos(self.velocity_x / self.velocity)
            else:
                self.angle = math.acos(self.velocity_x / self.velocity) * self.velocity_y / math.fabs(self.velocity_y)
            self.velocity -= 0.5 * 0.1
            '''
                
        if self.velocity < 0:
            self.velocity = 0    
        self.velocity_x =  self.velocity * math.cos(self.angle)
        self.velocity_y = -self.velocity * math.sin(self.angle)
        self.centerPosition[0] += self.velocity_x
        self.centerPosition[1] += self.velocity_y
        self.rect.center = self.centerPosition
    
        # 棋子中心是否在棋盘上
        if self.centerPosition[0] > self.chessboardRect[0] and \
            self.centerPosition[0] < self.chessboardRect[0] + self.chessboardSize[0] and \
            self.centerPosition[1] > self.chessboardRect[1] and \
            self.centerPosition[1] < self.chessboardRect[1] + self.chessboardSize[1]:
            self.onChessboard = True
        else:
            self.onChessboard = False
        
        # 棋子是否与棋盘接触
        if self.centerPosition[0] > self.chessboardRect[0] - self.rect.width / 2 and \
            self.centerPosition[0] < self.chessboardRect[0] + self.chessboardSize[0] + self.rect.width / 2and \
            self.centerPosition[1] > self.chessboardRect[1] - self.rect.height / 2 and \
            self.centerPosition[1] < self.chessboardRect[1] + self.chessboardSize[1] + self.rect.height / 2:
            self.life = True
        else:
            self.life = False
        
        