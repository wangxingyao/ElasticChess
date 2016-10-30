# -*- coding: utf-8 -*-

import pygame
import sys
import math
import random
import traceback
import playerClass
import arrowClass
import boundaryClass
import buttonClass



def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    target.blit(temp, location)

def main():
    # 初始化
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    size = 1024, 576    # 490 542
    fullsize = pygame.display.list_modes()[0]   # 获得全屏尺寸
    fullsize = 1366, 1024
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    pygame.display.set_caption("Star War  -- Wxy")
    
    # *****************************************************************************************
    # 加载背景图片
    # 菜单背景图片
    backgroundMenuImage = pygame.image.load(r"..\pic\background\backgroundMenu1.png").convert_alpha()
    # 游戏运行时背景图片 
    backgroundGameImage = pygame.image.load(r"..\pic\background\backgroundEarth.png").convert_alpha()
    chessboardImage = pygame.image.load("..\\pic\\background\\CLOUDS.png").convert_alpha()
    # chessboardLineImage = pygame.image.load(r"..\pic\background\background.png").convert_alpha()
    chessboardSize = 490, 542
    chessboardPosition = [(fullsize[0]-chessboardSize[0])/2, (fullsize[1]-chessboardSize[1])/2]       # chessboard的左上角顶点位置
    quitButtonOff = buttonClass.QuitButton("quitButtonOff", (1300, 60))
    quitButtonOn  = buttonClass.QuitButton("quitButtonOn", (1300, 60))
    
    
    # ******************************************************************************************
    # 加载音乐音效
    collisionSound = pygame.mixer.Sound(r"..\music\Collision.wav")
    
    
    
    
    
    # *****************************************************************************************
    # 创建各种对象  and 对应精灵组
    # 创建星星         and 精灵组
    textCenter = (500, 217)
    buttonStarGroup = pygame.sprite.Group()
    buttonStar0Sun     = buttonClass.StarButton("Sun"    , (1024,  0))
    buttonStar0Sun.create_text("Quit", textCenter)
    buttonStar1Mercury = buttonClass.StarButton("Mercury", ( 830, 45))
    buttonStar2Venus   = buttonClass.StarButton("Venus"  , ( 720, 45))
    buttonStar3Earth   = buttonClass.StarButton("Earth"  , ( 610, 45))
    buttonStar3Earth.create_text("Play", textCenter)
    buttonStar4Mars    = buttonClass.StarButton("Mars"   , ( 500, 45))
    buttonStar5Jupiter = buttonClass.StarButton("Jupiter", ( 390, 45))
    buttonStar6Saturn  = buttonClass.StarButton("Saturn" , ( 280, 45))
    buttonStar7Uranus  = buttonClass.StarButton("Uranus" , ( 170, 45))
    buttonStar8Neptune = buttonClass.StarButton("Neptune", (  60, 45))
    buttonStarGroup.add(buttonStar0Sun)
    buttonStarGroup.add(buttonStar1Mercury)
    buttonStarGroup.add(buttonStar2Venus)
    buttonStarGroup.add(buttonStar3Earth)
    buttonStarGroup.add(buttonStar4Mars)
    buttonStarGroup.add(buttonStar5Jupiter)
    buttonStarGroup.add(buttonStar6Saturn)
    buttonStarGroup.add(buttonStar7Uranus)
    buttonStarGroup.add(buttonStar8Neptune)
    
    
    
    # 创建金属矩形边缘   and 精灵组
    rectBoundaryGroup = pygame.sprite.Group()
    rectBoundary8 = boundaryClass.Boundary(r"..\pic\border\rectangleBoundary8.png", [ 46 + chessboardPosition[0], -18 + chessboardPosition[1]])
    rectBoundary2 = boundaryClass.Boundary(r"..\pic\border\rectangleBoundary2.png", [ 46 + chessboardPosition[0], 542 + chessboardPosition[1]])
    rectBoundary4 = boundaryClass.Boundary(r"..\pic\border\rectangleBoundary4.png", [-19 + chessboardPosition[0],  47 + chessboardPosition[1]])
    rectBoundary6 = boundaryClass.Boundary(r"..\pic\border\rectangleBoundary6.png", [490 + chessboardPosition[0],  47 + chessboardPosition[1]])
    rectBoundaryGroup.add(rectBoundary8)
    rectBoundaryGroup.add(rectBoundary2)
    rectBoundaryGroup.add(rectBoundary4)
    rectBoundaryGroup.add(rectBoundary6)
    
    
    # 创建球形边缘     (逆时针) 数字为小键盘中的位置   and 精灵组
    ballBoundaryGroup = pygame.sprite.Group()
    ballBoundaryCoordinate = (( 46, -10), ( -10, 47), (-10, 224), (-10, 318), \
                              (-10, 495), ( 46, 552), (443, 552), (500, 495), \
                              (500, 318), (500, 224), (500,  47), (443, -10))
    for eachCoordinate in ballBoundaryCoordinate:
        ballBoundary = playerClass.Ball(chessboardPosition, "graySmaBallBoundary", (eachCoordinate[0] + chessboardPosition[0], eachCoordinate[1] + chessboardPosition[1]))
        ballBoundaryGroup.add(ballBoundary)
    
    
    # 创建弓箭
    arrow = arrowClass.Arrow()
    
    
    
    
    # 创建棋子  and belowBall精灵组   player1  and  player2
    player1 = playerClass.Player()
    player2 = playerClass.Player()
    allBallGroup = pygame.sprite.Group()
    
    starList = ["Ceres", "Earth", "Eris", "Jupiter", "Mars", \
                "Mercury", "Moon", "Neptune", "Pluto", "Venus"]
    player1.starName = random.choice(starList)
    player2.starName = random.choice(starList)
    while player2.starName == player1.starName:
        player2.starName = random.choice(starList)
    
    # 创建player1棋子 and player1Ball精灵组
    player1BallCooridinate = ([245, 453, "Big"], [ 37, 505, "Mid"], [ 89, 505, "Mid"], [141, 505, "Mid"], \
                              [193, 505, "Mid"], [297, 505, "Mid"], [349, 505, "Mid"], [401, 505, "Mid"], \
                              [453, 505, "Mid"], [ 89, 401, "Mid"], [401, 401, "Mid"], [ 37, 349, "Sma"], \
                              [141, 349, "Sma"], [245, 349, "Sma"], [349, 349, "Sma"], [453, 349, "Sma"])
    for eachCoordinate in player1BallCooridinate:
        player1Ball = playerClass.Ball(chessboardPosition, player1.starName + str(eachCoordinate[2]) + "Ball", \
                                       (eachCoordinate[0] + chessboardPosition[0], eachCoordinate[1] + chessboardPosition[1]))
        player1.ballGroup.add(player1Ball)
        
    # 创建player2棋子 and player2Ball精灵组
    player2BallCooridinate = ([245,  89, "Big"], [ 37,  37, "Mid"], [ 89,  37, "Mid"], [141,  37, "Mid"], \
                              [193,  37, "Mid"], [297,  37, "Mid"], [349,  37, "Mid"], [401,  37, "Mid"], \
                              [453,  37, "Mid"], [ 89, 141, "Mid"], [401, 141, "Mid"], [ 37, 193, "Sma"], \
                              [141, 193, "Sma"], [245, 193, "Sma"], [349, 193, "Sma"], [453, 193, "Sma"])
    for eachCoordinate in player2BallCooridinate:
        player2Ball = playerClass.Ball(chessboardPosition, player2.starName + str(eachCoordinate[2]) + "Ball", \
                                       (eachCoordinate[0] + chessboardPosition[0], eachCoordinate[1] + chessboardPosition[1]))
        player2.ballGroup.add(player2Ball)
        
    # 创建  allBall 精灵组
    allBallGroup.add(player1.ballGroup)
    allBallGroup.add(player2.ballGroup)
    
    # 创建  player1  player2 的IDcard and skillCard
    player1.idCard = playerClass.IDCard(player1.starName, "..\\pic\\others\\whiteCardLeft.png", (210, 558))   # (1156, 539)
    player2.idCard = playerClass.IDCard(player2.starName, "..\\pic\\others\\whiteCardLeft.png", (210, 229))
    player1.skillCard = playerClass.SkillCard(player1.starName, "..\\pic\\others\\whiteCardRight.png", (1156, 558))
    player2.skillCard = playerClass.SkillCard(player2.starName, "..\\pic\\others\\whiteCardRight.png", (1156, 229))
    
    
    # ********************************************************************************************
    skillBallSelect = None                      # 选择   要使用技能的  Ball
    skillBallHover = None                       # 悬停   要使用技能的  Ball
    showSkillWarning = False                    # 显示技能禁用的警告信息
    winner = None
    player = player1
    allBallsEkPower = 0
    quitableGameScene = False                   # 游戏中退出按钮是否被选中
    isCollisionSoundPlay = False                # 碰撞音效是否播放
    scene = "menuScene"                         # 切换场景
    fullscreen = False                          # 是否全屏
    mousePositionStop = 0                       # 提前定义
    clock = pygame.time.Clock()
    running = True                              # while循环判定
    while running:
        # 事件循环
        for event in pygame.event.get():
            # 退出游戏
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_c and pygame.KMOD_CTRL:
                    pygame.quit()
                    sys.exit()
                    
                # 切换场景  空格键用于测试
                if event.key == pygame.K_SPACE:
                    #if scene == "menuScene":
                    #    scene = "gameScene"
                    #else:
                    #    scene = "menuScene"
                    ##### pass 当前回合
                    player.idCard.reset_MP(20)  # 当前玩家魔法增加20
                    if player == player1:
                        player = player2
                    else:
                        player = player1
                    player.idCard.reset_MP(5)   # 另一玩家魔法增加5
                


                if event.key == pygame.K_F11:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode(fullsize, pygame.FULLSCREEN | pygame.HWSURFACE)
                    else:
                        screen = pygame.display.set_mode(size, pygame.RESIZABLE)
                    
                
                
                
                
                
            # 鼠标   移动   事件
            if event.type == pygame.MOUSEMOTION:
                if scene == "menuScene":
                    for eachStar in buttonStarGroup:
                        if eachStar.rect.collidepoint(event.pos):
                            eachStar.opacity = 255
                            eachStar.displayText = True
                        else:
                            eachStar.opacity = 110
                            eachStar.displayText = False
                elif scene == "gameScene":
                    # 退出按钮
                    if quitButtonOff.rect.collidepoint(event.pos):
                        quitableGameScene = True
                    else:
                        quitableGameScene = False
                    # 游戏中技能选择
                    for eachButton in player.skillCard.skillButtonGroup:
                        if eachButton.rect.collidepoint(event.pos):
                            eachButton.hover = True
                        else:
                            eachButton.hover = False
                    
                 
                 
                 
                 
                 
            # 鼠标    DOWN   事件
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and scene == "gameScene":
                    arrow.life = True
                    mousePositionStart = list(pygame.mouse.get_pos())
                    arrow.rect.left = mousePositionStart[0]
                    arrow.rect.top  = mousePositionStart[1]
                    selectBall = pygame.sprite.spritecollide(arrow, player.ballGroup, False, pygame.sprite.collide_circle)
                    if selectBall and selectBall[0].life and allBallsEkPower < 1:
                        isCollisionSoundPlay = False     # 是否播放碰撞音效 置为 否
                        selectBall = selectBall[0]
                        mousePositionStart[0] = selectBall.rect.left + selectBall.rect.width // 2
                        mousePositionStart[1] = selectBall.rect.top  + selectBall.rect.height // 2
                    else:
                        arrow.life = False
                
                
                
                
                
                
            
            # 鼠标     UP   事件
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and scene == "menuScene":
                    if buttonStar3Earth.rect.collidepoint(event.pos):
                        scene = "gameScene"
                        fullscreen = True
                        screen = pygame.display.set_mode(fullsize, pygame.FULLSCREEN | pygame.HWSURFACE)
                    if buttonStar0Sun.rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                if event.button == 1 and scene == "gameScene":
                    # 技能按钮
                    for eachButton in player.skillCard.skillButtonGroup:
                        if eachButton.rect.collidepoint(event.pos):
                            if player.idCard.MP >= eachButton.consumeMP:
                                player.skillCard.select_button(eachButton)
                                break
                            else:
                                showSkillWarning = True
                                
                    # pass 当前回合
                    if player.idCard.starImageRect.collidepoint(event.pos) and allBallsEkPower < 1:
                        player.idCard.reset_MP(20)  # 当前玩家魔法增加20
                        if player == player1:
                            player = player2
                        else:
                            player = player1
                        player.idCard.reset_MP(5)   # 另一玩家魔法增加5
                    # 退出按钮
                    if quitButtonOn.rect.collidepoint(event.pos):
                        scene = "menuScene"
                        fullscreen = False
                        screen = pygame.display.set_mode(size, pygame.RESIZABLE)
                        # 重新初始化棋子
                        allBallGroup.empty()
                        player1.starName = random.choice(starList)
                        player2.starName = random.choice(starList)
                        while player2.starName == player1.starName:
                            player2.starName = random.choice(starList)
                            
                        # 创建下方棋子 and player1.ballGroup精灵组
                        player1.ballGroup.empty()
                        player1.idCard.reset_IDCard(player1.starName)
                        player1.skillCard.reset_skillCard(player1.starName)
                        for eachCoordinate in player1BallCooridinate:
                            player1Ball = playerClass.Ball(chessboardPosition, player1.starName + str(eachCoordinate[2]) + "Ball", \
                                                           (eachCoordinate[0] + chessboardPosition[0], eachCoordinate[1] + chessboardPosition[1]))
                            player1.ballGroup.add(player1Ball)
                            
                        # 创建上方棋子 and player2.ballGroup精灵组
                        player2.ballGroup.empty()
                        player2.idCard.reset_IDCard(player2.starName)
                        player2.skillCard.reset_skillCard(player2.starName)
                        for eachCoordinate in player2BallCooridinate:
                            player2Ball = playerClass.Ball(chessboardPosition, player2.starName + str(eachCoordinate[2]) + "Ball", \
                                                           (eachCoordinate[0] + chessboardPosition[0], eachCoordinate[1] + chessboardPosition[1]))
                            player2.ballGroup.add(player2Ball)
                            
                        allBallGroup.add(player1.ballGroup)
                        allBallGroup.add(player2.ballGroup)
                
                    # 发射小球
                    if arrow.life and arrow.length > arrow.minLength:
                        # 给予小球初始角度，速度
                        selectBall.set_angle(mousePositionStart, mousePositionStop)
                        selectBall.set_velocity(arrow.length)
                        allBallsEkPower = 0.5 * selectBall.mass * (selectBall.velocity ** 2)
                        if selectBall.string[-7] == "B":
                            magnification = 1
                        elif selectBall.string[-7] == "M":
                            magnification = 2
                        elif selectBall.string[-7] == "S":
                            magnification = 4
                        # 导航技能消耗 10 点魔法
                        if player.skillCard.skill1Button.select:
                            player.idCard.reset_MP(-10)
                        player.skillCard.empty_allButtonSelect()
                        # 切换玩家
                        if player == player1:
                            player = player2
                        else:
                            player = player1
                        player.idCard.MP += 10
                    arrow.life = False
                
                    ###  左键  选中   要使用技能的   Ball
                    if player.skillCard.skill4Button.select and skillBallHover:
                        skillBallSelect = skillBallHover
                    else:
                        skillBallSelect = None
                    
                ### 鼠标     UP   事件
                ### 右键  使用  skill 技能
                if event.button == 3 and scene == "gameScene":
                    # 使用技能 2   使  Ball 缩小
                    if player.skillCard.skill2Button.select and skillBallHover:
                        addHP = skillBallHover.narrow_ball()
                        if addHP:
                            if skillBallHover in player1.ballGroup:
                                player1.idCard.reset_HP(addHP)
                            else:
                                player2.idCard.reset_HP(addHP)
                            player.idCard.reset_MP(-40)
                            player.skillCard.skill2Button.select = False
                            # 切换玩家
                            if player == player1:
                                player = player2
                            else:
                                player = player1
                            player.idCard.MP += 10
                    # 使用技能3    使 Ball  变大
                    if player.skillCard.skill3Button.select and skillBallHover:
                        addHP = skillBallHover.enlarge_ball()
                        if addHP:
                            if skillBallHover in player1.ballGroup:
                                player1.idCard.reset_HP(addHP)
                            else:
                                player2.idCard.reset_HP(addHP)
                            player.idCard.reset_MP(-40)
                            player.skillCard.skill3Button.select = False
                            # 切换玩家
                            if player == player1:
                                player = player2
                            else:
                                player = player1
                            player.idCard.MP += 10
                    # 使用技能4    使  Ball  重定位
                    if player.skillCard.skill4Button.select and skillBallSelect:
                        skillBallSelect.relocate_ball(event.pos)
                        player.idCard.reset_MP(-60)
                        player.skillCard.skill4Button.select = False
                        if player == player1:
                            player = player2
                        else:
                            player = player1
                        player.idCard.MP += 10
                    
    
        # **************************************************************************************
        # 绘制菜单场景
        if scene == "menuScene":
            # 绘制背景 和 按钮
            screen.blit(backgroundMenuImage, (0, 0))
            blit_alpha(screen, buttonStar0Sun.image    , buttonStar0Sun.rect    , buttonStar0Sun.opacity)
            blit_alpha(screen, buttonStar1Mercury.image, buttonStar1Mercury.rect, buttonStar1Mercury.opacity)
            blit_alpha(screen, buttonStar2Venus.image  , buttonStar2Venus.rect  , buttonStar2Venus.opacity)
            blit_alpha(screen, buttonStar3Earth.image  , buttonStar3Earth.rect  , buttonStar3Earth.opacity)
            blit_alpha(screen, buttonStar4Mars.image   , buttonStar4Mars.rect   , buttonStar4Mars.opacity)
            blit_alpha(screen, buttonStar5Jupiter.image, buttonStar5Jupiter.rect, buttonStar5Jupiter.opacity)
            blit_alpha(screen, buttonStar6Saturn.image , buttonStar6Saturn.rect , buttonStar6Saturn.opacity)
            blit_alpha(screen, buttonStar7Uranus.image , buttonStar7Uranus.rect , buttonStar7Uranus.opacity)
            blit_alpha(screen, buttonStar8Neptune.image, buttonStar8Neptune.rect, buttonStar8Neptune.opacity)
            # 绘制中央文字
            for eachStar in buttonStarGroup:
                if eachStar.displayText:
                    try:
                        screen.blit(eachStar.textImage, eachStar.textRect)
                    except:
                        pass
            
        # **************************************************************************************
        # 绘制游戏规则背景
        
        
        # *************************************************************************************
        # 绘制游戏制作背景    
        
        
        # *************************************************************************************        
        # 绘制游戏场景
        if scene == "gameScene":                  
            # 绘制背景
            screen.blit(backgroundGameImage, (chessboardPosition[0] + chessboardSize[0]/2 - fullsize[0]/2, chessboardPosition[1] + chessboardSize[1]/2 - fullsize[1]/2))
            blit_alpha(screen, chessboardImage, chessboardPosition, 180)
            # screen.blit(chessboardLineImage, chessboardPosition)
            # 绘制Ball
            for eachBall in allBallGroup:
                eachBall.move()
                blit_alpha(screen, eachBall.image, eachBall.rect, eachBall.opacity)
            # 绘制  IDCard
            blit_alpha(screen, player1.idCard.IDImage,   player1.idCard.rect, 160)
            blit_alpha(screen, player2.idCard.IDImage,   player2.idCard.rect, 160)
            if player == player1 and allBallsEkPower < 1:
                player.idCard.reset_IDCard()
                blit_alpha(screen, player1.idCard.starImage, player1.idCard.starImageRect, 255)
                blit_alpha(screen, player2.idCard.starImage, player2.idCard.starImageRect, 50)
            elif player == player2 and allBallsEkPower < 1:
                player.idCard.reset_IDCard()
                blit_alpha(screen, player1.idCard.starImage, player1.idCard.starImageRect, 50)
                blit_alpha(screen, player2.idCard.starImage, player2.idCard.starImageRect, 255)
            else:
                blit_alpha(screen, player1.idCard.starImage, player1.idCard.starImageRect, 50)
                blit_alpha(screen, player2.idCard.starImage, player2.idCard.starImageRect, 50)
            
            screen.blit(player1.idCard.nameTextImage,  player1.idCard.nameTextRect)
            screen.blit(player1.idCard.scoreTextImage, player1.idCard.scoreTextRect)
            screen.blit(player1.idCard.HPImage,        player1.idCard.HPRect)
            screen.blit(player1.idCard.HPTextImage,    player1.idCard.HPTextRect)
            screen.blit(player1.idCard.MPImage,        player1.idCard.MPRect)
            screen.blit(player1.idCard.MPTextImage,    player1.idCard.MPTextRect)
            
            screen.blit(player2.idCard.nameTextImage,  player2.idCard.nameTextRect)
            screen.blit(player2.idCard.scoreTextImage, player2.idCard.scoreTextRect)
            screen.blit(player2.idCard.HPImage,        player2.idCard.HPRect)
            screen.blit(player2.idCard.HPTextImage,    player2.idCard.HPTextRect)
            screen.blit(player2.idCard.MPImage,        player2.idCard.MPRect)
            screen.blit(player2.idCard.MPTextImage,    player2.idCard.MPTextRect)
            
            # 绘制  skillCard
            blit_alpha(screen, player1.skillCard.skillCardImage, player1.skillCard.rect, 160)
            blit_alpha(screen, player2.skillCard.skillCardImage, player2.skillCard.rect, 160)
            # 绘制  skillCard  按钮 显示
            for eachButton in player1.skillCard.skillButtonGroup:
                if eachButton.consumeMP > player1.idCard.MP:
                    pass
                elif eachButton.hover or eachButton.select:
                    blit_alpha(screen, eachButton.image, eachButton.rect, 255)
                else:
                    blit_alpha(screen, eachButton.image, eachButton.rect, 50)
                screen.blit(eachButton.textImage, eachButton.textRect)
            for eachButton in player2.skillCard.skillButtonGroup:
                if eachButton.consumeMP > player2.idCard.MP:
                    pass
                elif eachButton.hover or eachButton.select:
                    blit_alpha(screen, eachButton.image, eachButton.rect, 255)
                else:
                    blit_alpha(screen, eachButton.image, eachButton.rect, 50)
                screen.blit(eachButton.textImage, eachButton.textRect)
            
            # 绘制退出按钮
            screen.blit(quitButtonOff.image, quitButtonOff.rect)
            if quitableGameScene:
                screen.blit(quitButtonOn.image, quitButtonOn.rect)
            # 绘制矩形边界
            rectBoundaryGroup.draw(screen)
            # 绘制球形边界
            ballBoundaryGroup.draw(screen)
            # 绘制 使用技能的效果
            mousePosition = pygame.mouse.get_pos()
            if player.skillCard.skill2Button.select:
                # 绘制第2个技能
                for eachBall in allBallGroup:
                    if eachBall.rect.collidepoint(mousePosition):
                        skillBallHover = eachBall
                        if eachBall.string[-7] == "B":
                            player.skillCard.skill2Button.specialBigRect.center = mousePosition
                            player.skillCard.skill2Button.specialBigRect.center = eachBall.rect.center
                            if eachBall in player.ballGroup:
                                screen.blit(player.skillCard.skill2Button.specialBigBlackImage, player.skillCard.skill2Button.specialBigRect)
                            else:
                                screen.blit(player.skillCard.skill2Button.specialBigRedImage, player.skillCard.skill2Button.specialBigRect)
                        elif eachBall.string[-7] == "M":
                            player.skillCard.skill2Button.specialMidRect.center = mousePosition
                            player.skillCard.skill2Button.specialMidRect.center = eachBall.rect.center
                            if eachBall in player.ballGroup:
                                screen.blit(player.skillCard.skill2Button.specialMidBlackImage, player.skillCard.skill2Button.specialMidRect)
                            else:
                                screen.blit(player.skillCard.skill2Button.specialMidRedImage, player.skillCard.skill2Button.specialMidRect)
                        
            elif player.skillCard.skill3Button.select:
                # 绘制第3个技能
                for eachBall in allBallGroup:
                    if eachBall.rect.collidepoint(mousePosition):
                        skillBallHover = eachBall
                        if eachBall.string[-7] == "M":
                            player.skillCard.skill3Button.specialMidRect.center = mousePosition
                            player.skillCard.skill3Button.specialMidRect.center = eachBall.rect.center
                            if eachBall in player.ballGroup:
                                screen.blit(player.skillCard.skill3Button.specialMidBlackImage, player.skillCard.skill3Button.specialMidRect)
                            else:
                                screen.blit(player.skillCard.skill3Button.specialMidRedImage, player.skillCard.skill3Button.specialMidRect)
                        elif eachBall.string[-7] == "S":
                            player.skillCard.skill3Button.specialSmaRect.center = mousePosition
                            player.skillCard.skill3Button.specialSmaRect.center = eachBall.rect.center
                            if eachBall in player.ballGroup:
                                screen.blit(player.skillCard.skill3Button.specialSmaBlackImage, player.skillCard.skill3Button.specialSmaRect)
                            else:
                                screen.blit(player.skillCard.skill3Button.specialSmaRedImage, player.skillCard.skill3Button.specialSmaRect)
            
            # 绘制第4个技能        
            elif player.skillCard.skill4Button.select:
                # 绘制已选择Ball的效果
                if skillBallSelect and skillBallSelect.string[-7] == "B":
                    player.skillCard.skill4Button.specialBigRect.center = skillBallSelect.rect.center
                    if skillBallSelect in player.ballGroup:
                        screen.blit(player.skillCard.skill4Button.specialBigBlackImage, player.skillCard.skill4Button.specialBigRect)
                    else:
                        screen.blit(player.skillCard.skill4Button.specialBigRedImage, player.skillCard.skill4Button.specialBigRect)
                elif skillBallSelect and skillBallSelect.string[-7] == "B":
                    player.skillCard.skill4Button.specialBigRect.center = skillBallSelect.rect.center
                    if skillBallSelect in player.ballGroup:
                        screen.blit(player.skillCard.skill4Button.specialBigBlackImage, player.skillCard.skill4Button.specialBigRect)
                    else:
                        screen.blit(player.skillCard.skill4Button.specialBigRedImage, player.skillCard.skill4Button.specialBigRect)
                elif skillBallSelect and skillBallSelect.string[-7] == "B":
                    player.skillCard.skill4Button.specialBigRect.center = skillBallSelect.rect.center
                    if skillBallSelect in player.ballGroup:
                        screen.blit(player.skillCard.skill4Button.specialBigBlackImage, player.skillCard.skill4Button.specialBigRect)
                    else:
                        screen.blit(player.skillCard.skill4Button.specialBigRedImage, player.skillCard.skill4Button.specialBigRect)
                # 绘制悬停效果
                for eachBall in allBallGroup:
                    if eachBall.rect.collidepoint(mousePosition):
                        skillBallHover = eachBall
                        if eachBall.string[-7] == "B":
                            player.skillCard.skill4Button.specialBigRect.center = mousePosition
                            player.skillCard.skill4Button.specialBigRect.center = eachBall.rect.center
                            if eachBall in player.ballGroup:
                                screen.blit(player.skillCard.skill4Button.specialBigBlackImage, player.skillCard.skill4Button.specialBigRect)
                            else:
                                screen.blit(player.skillCard.skill4Button.specialBigRedImage, player.skillCard.skill4Button.specialBigRect)
                        elif eachBall.string[-7] == "M":
                            player.skillCard.skill4Button.specialMidRect.center = mousePosition
                            player.skillCard.skill4Button.specialMidRect.center = eachBall.rect.center
                            if eachBall in player.ballGroup:
                                screen.blit(player.skillCard.skill4Button.specialMidBlackImage, player.skillCard.skill4Button.specialMidRect)
                            else:
                                screen.blit(player.skillCard.skill4Button.specialMidRedImage, player.skillCard.skill4Button.specialMidRect)
                        elif eachBall.string[-7] == "S":
                            player.skillCard.skill4Button.specialSmaRect.center = mousePosition
                            player.skillCard.skill4Button.specialSmaRect.center = eachBall.rect.center
                            if eachBall in player.ballGroup:
                                screen.blit(player.skillCard.skill4Button.specialSmaBlackImage, player.skillCard.skill4Button.specialSmaRect)
                            else:
                                screen.blit(player.skillCard.skill4Button.specialSmaRedImage, player.skillCard.skill4Button.specialSmaRect)
                    

            
                                
            # 绘制弓箭
            if arrow.life:
                mousePositionStop = list(pygame.mouse.get_pos())
                # 计算弓箭半长度    创建旋转后的箭头箭尾图    计算箭头箭尾的位置    绘制弓箭
                arrow.calc_length(mousePositionStart, mousePositionStop)
                # 弓箭最大长度限制
                if arrow.length > arrow.maxLength:
                    arrow.x = mousePositionStart[0] - mousePositionStop[0]
                    arrow.y = mousePositionStart[1]  - mousePositionStop[1]
                    arrow.x = (arrow.maxLength / arrow.length) * arrow.x
                    arrow.y = (arrow.maxLength / arrow.length) * arrow.y
                    mousePositionStop[0] = mousePositionStart[0] - arrow.x
                    mousePositionStop[1] = mousePositionStart[1] - arrow.y
                    arrow.length = arrow.maxLength
                arrow.create_rotatedImage(mousePositionStart, mousePositionStop)
                arrow.calc_tailRotatedRect(mousePositionStart, mousePositionStop)
                arrow.calc_headRotatedRect(mousePositionStart, mousePositionStop)
                # 弓箭最短长度限制
                if arrow.length > arrow.minLength:
                    # 绘制  skiil1 导航线
                    x = mousePositionStop[0] - mousePositionStart[0]
                    y = mousePositionStop[1] - mousePositionStart[1]
                    if player.skillCard.skill1Button.select:
                        pygame.draw.aaline(screen, (255, 0, 0), selectBall.rect.center, \
                            (selectBall.rect.center[0] - 4*x, selectBall.rect.center[1] - 4*y), 1)    
                    # 绘制弓箭
                    screen.blit(arrow.tailRotatedImage, arrow.tailRotatedRect)
                    screen.blit(arrow.headRotatedImage, arrow.headRotatedRect)
            
            # --------------------------------------------------------------------------------------
            # 碰撞检测
            # 棋子间碰撞
            for eachBall in allBallGroup:
                allBallGroup.remove(eachBall)
                collideBall = pygame.sprite.spritecollide(eachBall, allBallGroup, False, pygame.sprite.collide_circle)
                if collideBall:
                    collideBall = collideBall[0]
                    if not eachBall.isCollide and eachBall.opacity == 255:
                        if not isCollisionSoundPlay:
                            collisionSound.play()
                            isCollisionSoundPlay = True
                        eachBall.collide(collideBall, True)
                allBallGroup.add(eachBall)
            for eachBall in allBallGroup:
                eachBall.isCollide = False
            # 棋子与矩形边界碰撞
            for eachBall in allBallGroup:
                if pygame.sprite.collide_rect(eachBall, rectBoundary8):
                    eachBall.isCollide = True
                    if eachBall.onChessboard:
                        eachBall.centerPosition[1] = chessboardPosition[1] + eachBall.rect.height / 2
                    else:
                        eachBall.centerPosition[1] = chessboardPosition[1] - eachBall.rect.height / 2 - rectBoundary8.rect.height
                    eachBall.rect.center = eachBall.centerPosition
                    eachBall.angle = -eachBall.angle
                elif pygame.sprite.collide_rect(eachBall, rectBoundary2):
                    eachBall.isCollide = True
                    if eachBall.onChessboard:
                        eachBall.centerPosition[1] = chessboardPosition[1] - eachBall.rect.height / 2 + eachBall.chessboardSize[1]
                    else:
                        eachBall.centerPosition[1] = chessboardPosition[1] + eachBall.rect.height / 2 + eachBall.chessboardSize[1] + rectBoundary2.rect.height
                    eachBall.rect.center = eachBall.centerPosition
                    eachBall.angle = -eachBall.angle
                elif pygame.sprite.collide_mask(eachBall, rectBoundary4):
                    eachBall.isCollide = True
                    if eachBall.onChessboard:
                        eachBall.centerPosition[0] = chessboardPosition[0] + eachBall.rect.width / 2
                    else:
                        eachBall.centerPosition[0] = chessboardPosition[0] - eachBall.rect.width / 2 - rectBoundary4.rect.width
                    eachBall.rect.center = eachBall.centerPosition
                    if eachBall.angle >= 0:
                        eachBall.angle = math.pi - eachBall.angle
                    elif eachBall.angle < 0:
                        eachBall.angle = -math.pi - eachBall.angle
                elif pygame.sprite.collide_mask(eachBall, rectBoundary6):
                    eachBall.isCollide = True
                    if eachBall.onChessboard:
                        eachBall.centerPosition[0] = chessboardPosition[0] - eachBall.rect.width / 2 + eachBall.chessboardSize[0]
                    else:
                        eachBall.centerPosition[0] = chessboardPosition[0] + eachBall.rect.width / 2 + eachBall.chessboardSize[0] + rectBoundary6.rect.width
                    eachBall.rect.center = eachBall.centerPosition
                    if eachBall.angle >= 0:
                        eachBall.angle = math.pi - eachBall.angle
                    elif eachBall.angle < 0:
                        eachBall.angle = -math.pi - eachBall.angle
            # 棋子与小球边界碰撞
            for eachBall in allBallGroup:
                if not eachBall.isCollide:
                    collideBall = pygame.sprite.spritecollide(eachBall, ballBoundaryGroup, False, pygame.sprite.collide_circle)
                    if collideBall:
                        collideBall = collideBall[0]
                        if not eachBall.isCollide:
                            eachBall.collide(collideBall, False)
            for eachBall in allBallGroup:
                eachBall.isCollide = False
            
            
            
            # 计算动能 两个玩家所有球的动能
            player1.ballsEkPower = 0
            for eachBall in player1.ballGroup:
                player1.ballsEkPower += 0.5 * eachBall.mass * (eachBall.velocity ** 2)
            player2.ballsEkPower = 0
            for eachBall in player2.ballGroup:
                player2.ballsEkPower += 0.5 * eachBall.mass * (eachBall.velocity ** 2)
            allBallsEkPower = player1.ballsEkPower + player2.ballsEkPower
          
            # 计算并绘画导向轴
            # for eachBall in allBallGroup:
            #     pygame.draw.aaline(screen, (255, 0, 0), eachBall.rect.center, \
            #         (eachBall.rect.center[0] + eachBall.velocity_x * 40, eachBall.rect.center[1] + eachBall.velocity_y * 40), 1)    
            
            
            # 出局判定
            for eachBall in allBallGroup:
                if not eachBall.life:
                    if eachBall in player1.ballGroup:
                        player1.ballGroup.remove(eachBall)
                        if not player1.ballGroup:
                            winner = player2
                        if eachBall.string[-7] == "B":
                            player1.idCard.HP    -= 15
                            player2.idCard.score += 400 * magnification
                        elif eachBall.string[-7] == "M":
                            player1.idCard.HP    -= 7
                            player2.idCard.score += 200 * magnification
                        elif eachBall.string[-7] == "S":
                            player1.idCard.HP    -= 3
                            player2.idCard.score += 100 * magnification
                    elif eachBall in player2.ballGroup:
                        player2.ballGroup.remove(eachBall)
                        if not player2.ballGroup:
                            winner = player1
                        if eachBall.string[-7] == "B":
                            player2.idCard.HP    -= 15
                            player1.idCard.score += 400 * magnification
                        elif eachBall.string[-7] == "M":
                            player2.idCard.HP    -= 7
                            player1.idCard.score += 200 * magnification
                        elif eachBall.string[-7] == "S":
                            player2.idCard.HP    -= 3
                            player1.idCard.score += 100 * magnification
                    
                    # 更新 IDcard 信息
                    player1.idCard.reset_HP()
                    player2.idCard.reset_HP()
            
                    
                    # 棋子出局渐变效果
                    eachBall.opacity -= 2
                    eachBall.image = pygame.transform.smoothscale(eachBall.oimage, \
                                             (int(eachBall.rect.width * eachBall.opacity / 255), \
                                              int(eachBall.rect.height * eachBall.opacity / 255)))
                    eachBall.rect.center = eachBall.centerPosition
                    eachBall.velocity *= 0.97
                    if eachBall.opacity < 10:
                        allBallGroup.remove(eachBall)
             
            # 判断胜者
            if winner:
                print(winner.starName)
        
        
        
        # 刷新画布
        pygame.display.update()
        clock.tick(60)
    

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
    
