import pygame
import sys
import random
from pygame.locals import *
import pygame_menu
from pygame_menu.widgets import Image

WINDOWWIDTH = 400
WINDOWHEIGHT = 600

X_MARGIN = 80
LANEWIDTH = 60

CARWIDTH = 40
CARHEIGHT = 60
CARSPEED = 3
CARIMG = pygame.image.load('img/1.png')
CARIMG2 = pygame.image.load('img/2.png')
CARIMG3 = pygame.image.load('img/3.png')
CARIMG4 = pygame.image.load('img/4.png')
CARIMG5 = pygame.image.load('img/5.png')
CARIMG6 = pygame.image.load('img/6.png')
CARIMG7 = pygame.image.load('img/7.png')
CARIMG8 = pygame.image.load('img/8.png')
CARIMG9 = pygame.image.load('img/9.png')
CARIMG10 = pygame.image.load('img/10.png')

DISTANCE = 200
OBSTACLESSPEED = 3
OBSTACLESSPEED_2 = 4
CHANGESPEED = 0.001
OBSTACLESIMG = pygame.image.load('img/ob3.png')
OBSTACLESIMG1 = pygame.image.load('img/ob4.png')
OBSTACLESIMG2 = pygame.image.load('img/bomb100.png')
OBSTACLESIMG3 = pygame.image.load('img/ob2.png')

BGSPEED = 1.5
BGIMG = pygame.image.load('img/background.png')
BGIMG2 = pygame.image.load('img/background.png')
BGIMG3 = pygame.image.load('img/background.png')

explosion_img = pygame.image.load("img/Break 100x120.png")

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('ĐUA XE ỤN ỤN')

def sound_game_start():
    pygame.mixer.music.stop()
    pygame.mixer.init()
    pygame.mixer.music.load('sound/Mission-Impossible.mp3')
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play(-1)

def sound_game_running():
    pygame.mixer.music.stop()
    pygame.mixer.init()
    pygame.mixer.music.load('sound/Mission-Impossible.mp3')
    pygame.mixer.music.play(-1)

def sound_game_score():
    pygame.mixer.music.stop()
    pygame.mixer.init()
    pygame.mixer.music.load('sound/mixkit-game-treasure-coin-2038.wav')
    pygame.mixer.music.play()

def sound_game_stop():
    pygame.mixer.music.stop()
    pygame.mixer.init()
    pygame.mixer.music.load('sound/Tieng-xe-cap-cuu-chay-tren-duong-pho-www_tiengdong_com.mp3')
    pygame.mixer.music.play()

sound_game_start()

class BG:
    def __init__(self, speed, img):
        self.x = 0
        self.y = 0
        self.speed = speed
        self.img = img
        self.width = self.img.get_width()
        self.height = self.img.get_height()

    def draw(self):
        DISPLAYSURF.blit(self.img, (int(self.x), int(self.y)))
        DISPLAYSURF.blit(self.img, (int(self.x), int(self.y - self.height)))

    def update(self):
        self.y += self.speed
        if self.y > self.height:
            self.y -= self.height

class Background(BG):
    def __init__(self):
        super().__init__(BGSPEED, BGIMG)

class Background_2(BG):
    def __init__(self):
        super().__init__(BGSPEED * 2, BGIMG2)

class Background_3(BG):
    def __init__(self):
        super().__init__(BGSPEED * 3, BGIMG3)

'''OBSTACLES FOR LEVEL 1'''
class Obstacles():
    def __init__(self):
        self.width = CARWIDTH
        self.height = CARHEIGHT
        self.distance = DISTANCE
        self.speed = OBSTACLESSPEED
        self.changeSpeed = CHANGESPEED
        self.ls = []
        for i in range(5):
            y = -CARHEIGHT - i * self.distance
            lane = random.randint(0, 3)
            self.ls.append([lane, y])

    def draw(self):
        for i in range(5):
            x = int(X_MARGIN + self.ls[i][0] * LANEWIDTH + (LANEWIDTH - self.width) / 2)
            y = int(self.ls[i][1])
            DISPLAYSURF.blit(OBSTACLESIMG, (x, y))

    def update(self):
        for i in range(5):
            self.ls[i][1] += self.speed
        self.speed += self.changeSpeed
        if self.ls[0][1] > WINDOWHEIGHT:
            self.ls.pop(0)
            y = self.ls[3][1] - self.distance
            lane = random.randint(0, 3)
            self.ls.append([lane, y])

'''OBSTACLES FOR LEVEL 2'''
class Obstacles_2():
    def __init__(self):
        self.width = CARWIDTH
        self.height = CARHEIGHT
        self.distance = DISTANCE
        self.speed = OBSTACLESSPEED
        self.changeSpeed = CHANGESPEED
        self.ls = []
        for i in range(5):
            if i < 3:
                y = -CARHEIGHT - i * self.distance
                lane = random.randint(0, 3)
                obstacle_img = OBSTACLESIMG
                self.ls.append([lane, y, obstacle_img])
            elif i == 3:
                y = -CARHEIGHT - i * self.distance
                lane = random.randint(0, 3)
                obstacle_img = OBSTACLESIMG1
                self.ls.append([lane, y, obstacle_img])
            elif i == 4:
                y = -CARHEIGHT - i * (3 / 2) * self.distance
                lane = random.randint(0, 3)
                obstacle_img = random.choice([OBSTACLESIMG, OBSTACLESIMG1, OBSTACLESIMG2, OBSTACLESIMG3])
                self.ls.append([lane, y, obstacle_img])

    def draw(self):
        for i in range(5):
            x = int(X_MARGIN + self.ls[i][0] * LANEWIDTH + (LANEWIDTH - self.width) / 2)
            y = int(self.ls[i][1])
            obstacle_img = self.ls[i][2]
            DISPLAYSURF.blit(obstacle_img, (x, y))

    def update(self):
        for i in range(5):
            self.ls[i][1] += self.speed
        self.speed += self.changeSpeed
        if self.ls[0][1] > WINDOWHEIGHT:
            self.ls.pop(0)
            y = self.ls[3][1] - self.distance
            lane = random.randint(0, 3)
            obstacle_img = random.choice([OBSTACLESIMG, OBSTACLESIMG1, OBSTACLESIMG2, OBSTACLESIMG3])
            self.ls.append([lane, y, obstacle_img])

'''OBSTACLES FOR LEVEL 3'''
class Obstacles_3():
    def __init__(self):
        self.width = CARWIDTH
        self.height = CARHEIGHT
        self.distance = DISTANCE
        self.speed = OBSTACLESSPEED_2
        self.changeSpeed = CHANGESPEED
        self.ls = []
        for i in range(5):
            if i < 3:
                y = -CARHEIGHT - i * self.distance
                lane = random.randint(0, 3)
                obstacle_img = OBSTACLESIMG
                self.ls.append([lane, y, obstacle_img])
            elif i == 3:
                y = -CARHEIGHT - i * self.distance
                lane = random.randint(0, 3)
                obstacle_img = OBSTACLESIMG1
                self.ls.append([lane, y, obstacle_img])
            elif i == 4:
                y = -CARHEIGHT - i * (3 / 2) * self.distance
                lane = random.randint(0, 3)
                obstacle_img = OBSTACLESIMG3
                self.ls.append([lane, y, obstacle_img])

    def draw(self):
        for i in range(5):
            x = int(X_MARGIN + self.ls[i][0] * LANEWIDTH + (LANEWIDTH - self.width) / 2)
            y = int(self.ls[i][1])
            obstacle_img = self.ls[i][2]
            DISPLAYSURF.blit(obstacle_img, (x, y))

    def update(self):
        for i in range(5):
            self.ls[i][1] += self.speed
        self.speed += self.changeSpeed
        if self.ls[0][1] > WINDOWHEIGHT:
            self.ls.pop(0)
            y = self.ls[3][1] - self.distance
            lane = random.randint(0, 3)
            obstacle_img = random.choice([OBSTACLESIMG, OBSTACLESIMG1, OBSTACLESIMG3])
            if obstacle_img == OBSTACLESIMG3:
                self.ls.append([0, y, obstacle_img])
                self.ls.append([1, y, obstacle_img])
                self.ls.append([2, y, obstacle_img])
                self.ls.append([3, y, obstacle_img])
            else:
                self.ls.append([lane, y, obstacle_img])

class Car:
    def __init__(self, image):
        self.width = CARWIDTH
        self.height = CARHEIGHT
        self.x = (WINDOWWIDTH - self.width) / 2
        self.y = (WINDOWHEIGHT - self.height) / 2
        self.speed = CARSPEED
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill((255, 255, 255))
        self.original_image = image

    def draw(self):
        car_img = pygame.transform.scale(self.original_image, (self.width, self.height))
        DISPLAYSURF.blit(car_img, (int(self.x), int(self.y)))

    def update(self, moveLeft, moveRight, moveUp, moveDown):
        if moveLeft:
            self.x -= self.speed
        if moveRight:
            self.x += self.speed
        if moveUp:
            self.y -= self.speed
        if moveDown:
            self.y += self.speed

        if self.x < X_MARGIN:
            self.x = X_MARGIN
        if self.x + self.width > WINDOWWIDTH - X_MARGIN:
            self.x = WINDOWWIDTH - X_MARGIN - self.width
        if self.y < 0:
            self.y = 0
        if self.y + self.height > WINDOWHEIGHT:
            self.y = WINDOWHEIGHT - self.height

class Car1(Car):
    def __init__(self):
        super().__init__(CARIMG)
class Car2(Car):
    def __init__(self):
        super().__init__(CARIMG2)
class Car3(Car):
    def __init__(self):
        super().__init__(CARIMG3)
class Car4(Car):
    def __init__(self):
        super().__init__(CARIMG4)
class Car5(Car):
    def __init__(self):
        super().__init__(CARIMG5)
class Car6(Car):
    def __init__(self):
        super().__init__(CARIMG6)
class Car7(Car):
    def __init__(self):
        super().__init__(CARIMG7)
class Car8(Car):
    def __init__(self):
        super().__init__(CARIMG8)
class Car9(Car):
    def __init__(self):
        super().__init__(CARIMG9)
class Car10(Car):
    def __init__(self):
        super().__init__(CARIMG10)

class Score:
    def __init__(self):
        self.score = 0

    def draw(self):
        font = pygame.font.SysFont('consolas', 30)
        scoreSurface = font.render('Score: ' + str(int(self.score)), True, (0, 0, 0))
        DISPLAYSURF.blit(scoreSurface, (10, 10))

    def update(self):
        self.score += 0.02
        sound_game_score()

def rectCollision(rect1, rect2):
    if (rect1[0] <= rect2[0] + rect2[2] and rect2[0] <= rect1[0] + rect1[2]
            and rect1[1] <= rect2[1] + rect2[3] and rect2[1] <= rect1[1] + rect1[3]):
        return True
    return False

def isGameover(car, obstacles):
    global explosion_x, explosion_y
    carRect = [car.x, car.y, car.width, car.height]
    for i in range(5):
        x = int(X_MARGIN + obstacles.ls[i][0] * LANEWIDTH + (LANEWIDTH - obstacles.width) / 2)
        y = int(obstacles.ls[i][1])
        obstaclesRect = [x, y, obstacles.width, obstacles.height]
        if rectCollision(carRect, obstaclesRect) == True:
            explosion_x = ((car.x + obstaclesRect[0]) // 2.5) + (obstacles.width + car.width) // 10
            explosion_y = ((car.y + obstaclesRect[1]) // 2.5) + (obstacles.height + car.height) // 10
            return True

    return False

def gameStart(bg):
    bg.__init__()
    font = pygame.font.SysFont('consolas', 20)
    commentSurface1 = font.render('Institute of Intelligent', True, (0, 0, 0))
    commentSize1 = commentSurface1.get_size()

    font = pygame.font.SysFont('consolas', 20)
    commentSurface2 = font.render('and Interactive Technologies', True, (0, 0, 0))
    commentSize2 = commentSurface2.get_size()

    font = pygame.font.SysFont('consolas', 60)
    headingSurface = font.render('ĐUA XE ỤN ỤN', True, (255, 0, 0))
    headingSize = headingSurface.get_size()

    font = pygame.font.SysFont('consolas', 20)
    commentSurface = font.render('Press "Enter" to play', True, (0, 0, 0))
    commentSize = commentSurface.get_size()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == K_RETURN:
                    return
        bg.draw()
        DISPLAYSURF.blit(commentSurface1, (int((WINDOWWIDTH - commentSize1[0]) / 2), 40))
        DISPLAYSURF.blit(commentSurface2, (int((WINDOWWIDTH - commentSize2[0]) / 2), 65))
        DISPLAYSURF.blit(headingSurface, (int((WINDOWWIDTH - headingSize[0]) / 2), 100))
        DISPLAYSURF.blit(commentSurface, (int((WINDOWWIDTH - commentSize[0]) / 2), 400))
        pygame.display.update()
        fpsClock.tick(FPS)

def gamePlay(bg, car, obstacles, score):
    car.__init__()
    obstacles.__init__()
    bg.__init__()
    score.__init__()
    moveLeft = False
    moveRight = False
    moveUp = False
    moveDown = False
    sound_game_running()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    moveLeft = True
                if event.key == K_RIGHT:
                    moveRight = True
                if event.key == K_DOWN:
                    moveDown = True
                if event.key == K_UP:
                    moveUp = True

            if event.type == KEYUP:
                if event.key == K_LEFT:
                    moveLeft = False
                if event.key == K_RIGHT:
                    moveRight = False
                if event.key == K_DOWN:
                    moveDown = False
                if event.key == K_UP:
                    moveUp = False

        if isGameover(car, obstacles):
            return

        bg.draw()
        bg.update()
        obstacles.draw()
        obstacles.update()
        car.draw()
        car.update(moveLeft, moveRight, moveUp, moveDown)
        score.draw()
        score.update()

        pygame.display.update()
        fpsClock.tick(FPS)

def gamePlay2(bg, car, car2, obstacles, score):
    car.__init__()
    car2.__init__()
    obstacles.__init__()
    bg.__init__()
    score.__init__()
    moveLeft1 = False
    moveRight1 = False
    moveUp1 = False
    moveDown1 = False

    moveLeft2 = False
    moveRight2 = False
    moveUp2 = False
    moveDown2 = False

    sound_game_running()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    moveLeft1 = True
                if event.key == K_RIGHT:
                    moveRight1 = True
                if event.key == K_DOWN:
                    moveDown1 = True
                if event.key == K_UP:
                    moveUp1 = True

                if event.key == K_a:
                    moveLeft2 = True
                if event.key == K_d:
                    moveRight2 = True
                if event.key == K_s:
                    moveDown2 = True
                if event.key == K_w:
                    moveUp2 = True

            if event.type == KEYUP:
                if event.key == K_LEFT:
                    moveLeft1 = False
                if event.key == K_RIGHT:
                    moveRight1 = False
                if event.key == K_DOWN:
                    moveDown1 = False
                if event.key == K_UP:
                    moveUp1 = False

                if event.key == K_a:
                    moveLeft2 = False
                if event.key == K_d:
                    moveRight2 = False
                if event.key == K_s:
                    moveDown2 = False
                if event.key == K_w:
                    moveUp2 = False

        if isGameover(car, obstacles) or isGameover(car2, obstacles):
            return

        bg.draw()
        bg.update()
        obstacles.draw()
        obstacles.update()
        car.draw()
        car.update(moveLeft1, moveRight1, moveUp1, moveDown1)

        car2.draw()
        car2.update(moveLeft2, moveRight2, moveUp2, moveDown2)

        score.draw()
        score.update()

        pygame.display.update()
        fpsClock.tick(FPS)

def gameOver(bg, car, obstacles, score, highscore):
    sound_game_stop()

    font = pygame.font.SysFont('consolas', 60)
    headingSuface = font.render('Lêu lêu!', True, (255, 0, 0))
    headingSize = headingSuface.get_size()

    font = pygame.font.SysFont('consolas', 60)
    headingSuface1 = font.render('Bạn thua rồi', True, (255, 0, 0))
    headingSize1 = headingSuface1.get_size()

    font = pygame.font.SysFont('consolas', 20)
    commentSuface = font.render('Press "space" to replay', True, (0, 0, 0))
    commentSize = commentSuface.get_size()

    font = pygame.font.SysFont('consolas', 20)
    commentSuface1 = font.render('Press "esc" to mainmenu', True, (0, 0, 0))
    commentSize1 = commentSuface1.get_size()

    font = pygame.font.SysFont('consolas', 30)
    scoreSuface = font.render('Score: ' + str(int(score.score)), True, (0, 0, 0))
    scoreSize = scoreSuface.get_size()

    if score.score > highscore:
        highscore = score.score
    font = pygame.font.SysFont('consolas', 30)
    highscoreSuface = font.render('Highscore: ' + str(int(highscore)), True, (255, 0, 3))
    highscoreSize = highscoreSuface.get_size()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key == K_SPACE:
                    return highscore
                elif event.key == K_ESCAPE:
                    main_menu()

        bg.draw()
        obstacles.draw()
        car.draw()
        score.draw()
        DISPLAYSURF.blit(headingSuface, (int((WINDOWWIDTH - headingSize[0]) / 2), 80))
        DISPLAYSURF.blit(headingSuface1, (int((WINDOWWIDTH - headingSize1[0]) / 2), 130))
        DISPLAYSURF.blit(commentSuface, (int((WINDOWWIDTH - commentSize[0]) / 2), 450))
        DISPLAYSURF.blit(commentSuface1, (int((WINDOWWIDTH - commentSize1[0]) / 2), 475))
        DISPLAYSURF.blit(scoreSuface, (int((WINDOWWIDTH - scoreSize[0]) / 2), 220))
        DISPLAYSURF.blit(highscoreSuface, (int((WINDOWWIDTH - highscoreSize[0]) / 2), 250))
        DISPLAYSURF.blit(explosion_img, (explosion_x, explosion_y))

        pygame.display.update()
        fpsClock.tick(FPS)

selected_car = None
selected_level = None
selected_mode = None

custom_theme = pygame_menu.themes.Theme(
    background_color=(0, 95, 105),
    title_font_color=(242, 111, 51),
    widget_font_color=(242, 111, 51),
    selection_color=(50, 50, 50),
)

def main_menu():
    sound_game_start()
    menu = pygame_menu.Menu('Main', WINDOWWIDTH, WINDOWHEIGHT, theme=custom_theme)
    menu.add.button('Chọn Mode', choose_mode_menu)
    menu.add.button('Thoát', pygame_menu.events.EXIT)
    menu.mainloop(DISPLAYSURF)

def choose_mode_menu():
    global selected_mode

    menu = pygame_menu.Menu('Chọn Mode', WINDOWWIDTH, WINDOWHEIGHT, theme=custom_theme)

    menu.add.button('Thân ai nấy lo', choose_level_menu, 1)
    menu.add.button('Đồng cam cộng khổ', choose_level_menu, 2)

    menu.add.button('Quay lại', main_menu)

    menu.mainloop(DISPLAYSURF)

def choose_level_menu(mode):
    global selected_level, selected_mode

    selected_mode = mode

    menu = pygame_menu.Menu('Chọn Level', WINDOWWIDTH, WINDOWHEIGHT, theme=custom_theme)

    menu.add.button('Level 1', start_game, 1)
    menu.add.button('Level 2', start_game, 2)
    menu.add.button('Level 3', start_game, 3)

    menu.add.button('Quay lại', choose_mode_menu)

    menu.mainloop(DISPLAYSURF)

def select_car(car):
    global selected_car
    if car == 1:
        selected_car = "Car1"
    elif car == 2:
        selected_car = "Car2"
    elif car == 3:
        selected_car = "Car3"
    elif car == 4:
        selected_car = "Car4"
    elif car == 5:
        selected_car = "Car5"
    elif car == 6:
        selected_car = "Car6"
    elif car == 7:
        selected_car = "Car7"
    elif car == 8:
        selected_car = "Car8"
    elif car == 9:
        selected_car = "Car9"
    elif car == 10:
        selected_car = "Car10"

def start_game(level):
    global selected_car, selected_level, selected_mode
    selected_level = level
    choose_car_menu()

def choose_car_menu():
    global selected_car, selected_level

    menu = pygame_menu.Menu('Chọn Xe', WINDOWWIDTH, WINDOWHEIGHT, theme=custom_theme)

    car1_image_path = 'img/1.png'
    menu.add.button('Xe 1', select_car, 1)
    menu.add.generic_widget(pygame_menu.widgets.Image(image_path=car1_image_path, angle=0, scale=(0.1, 0.1)))

    car2_image_path = 'img/2.png'
    menu.add.button('Xe 2', select_car, 2)
    menu.add.generic_widget(pygame_menu.widgets.Image(image_path=car2_image_path, angle=0, scale=(0.1, 0.1)))

    car3_image_path = 'img/3.png'
    menu.add.button('Xe 3', select_car, 3)
    menu.add.generic_widget(pygame_menu.widgets.Image(image_path=car3_image_path, angle=0, scale=(0.1, 0.1)))

    car4_image_path = 'img/4.png'
    menu.add.button('Xe 4', select_car, 4)
    menu.add.generic_widget(pygame_menu.widgets.Image(image_path=car4_image_path, angle=0, scale=(0.1, 0.1)))

    car5_image_path = 'img/5.png'
    menu.add.button('Xe 5', select_car, 5)
    menu.add.generic_widget(pygame_menu.widgets.Image(image_path=car5_image_path, angle=0, scale=(0.1, 0.1)))

    car6_image_path = 'img/6.png'
    menu.add.button('Xe 6', select_car, 6)
    menu.add.generic_widget(pygame_menu.widgets.Image(image_path=car6_image_path, angle=0, scale=(0.1, 0.1)))

    car7_image_path = 'img/7.png'
    menu.add.button('Xe 7', select_car, 7)
    menu.add.generic_widget(pygame_menu.widgets.Image(image_path=car7_image_path, angle=0, scale=(0.1, 0.1)))

    car8_image_path = 'img/8.png'
    menu.add.button('Xe 8', select_car, 8)
    menu.add.generic_widget(pygame_menu.widgets.Image(image_path=car8_image_path, angle=0, scale=(0.1, 0.1)))

    car9_image_path = 'img/9.png'
    menu.add.button('Xe 9', select_car, 9)
    menu.add.generic_widget(pygame_menu.widgets.Image(image_path=car9_image_path, angle=0, scale=(0.1, 0.1)))

    car10_image_path = 'img/10.png'
    menu.add.button('Xe 10', select_car, 10)
    menu.add.generic_widget(pygame_menu.widgets.Image(image_path=car10_image_path, angle=0, scale=(0.1, 0.1)))

    menu.add.button('Bắt đầu', start_game_logic)
    menu.add.button('Quay lại', choose_level_menu)

    menu.mainloop(DISPLAYSURF)


def start_game_logic():
    highscore = 0
    global selected_car, selected_level, selected_mode

    if selected_car is not None and selected_level is not None and selected_mode is not None:
        if selected_car == "Car1":

            if selected_level == 1:
                if selected_mode == 1:
                    bg = Background()
                    car = Car1()
                    obstacles = Obstacles()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay(bg, car, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)
                if selected_mode == 2:
                    bg = Background()
                    car = Car1()
                    car2 = Car2()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay2(bg, car, car2, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)

            if selected_level == 2:
                if selected_mode == 1:
                    bg = Background()
                    car = Car1()
                    obstacles = Obstacles_2()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay(bg, car, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)
                if selected_mode == 2:
                    bg = Background()
                    car = Car1()
                    car2 = Car2()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay2(bg, car, car2, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)

            if selected_level == 3:
                if selected_mode == 1:
                    bg = Background()
                    car = Car1()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay(bg, car, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)
                if selected_mode == 2:
                    bg = Background()
                    car = Car1()
                    car2 = Car2()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay2(bg, car, car2, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)

        if selected_car == "Car2":

            if selected_level == 1:
                if selected_mode == 1:
                    bg = Background()
                    car = Car2()
                    obstacles = Obstacles()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay(bg, car, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)
                if selected_mode == 2:
                    bg = Background()
                    car = Car2()
                    car2 = Car3()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay2(bg, car, car2, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)

            if selected_level == 2:
                if selected_mode == 1:
                    bg = Background()
                    car = Car2()
                    obstacles = Obstacles_2()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay(bg, car, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)
                if selected_mode == 2:
                    bg = Background()
                    car = Car2()
                    car2 = Car3()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay2(bg, car, car2, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)

            if selected_level == 3:
                if selected_mode == 1:
                    bg = Background()
                    car = Car2()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay(bg, car, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)
                if selected_mode == 2:
                    bg = Background()
                    car = Car2()
                    car2 = Car3()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay2(bg, car, car2, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)

        if selected_car == "Car3":

            if selected_level == 1:
                if selected_mode == 1:
                    bg = Background()
                    car = Car3()
                    obstacles = Obstacles()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay(bg, car, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)
                if selected_mode == 2:
                    bg = Background()
                    car = Car3()
                    car2 = Car4()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay2(bg, car, car2, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)

            if selected_level == 2:
                if selected_mode == 1:
                    bg = Background()
                    car = Car3()
                    obstacles = Obstacles_2()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay(bg, car, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)
                if selected_mode == 2:
                    bg = Background()
                    car = Car3()
                    car2 = Car4()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay2(bg, car, car2, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)

            if selected_level == 3:
                if selected_mode == 1:
                    bg = Background()
                    car = Car3()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay(bg, car, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)
                if selected_mode == 2:
                    bg = Background()
                    car = Car3()
                    car2 = Car4()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay2(bg, car, car2, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)

        if selected_car == "Car4":

            if selected_level == 1:
                if selected_mode == 1:
                    bg = Background()
                    car = Car4()
                    obstacles = Obstacles()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay(bg, car, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)
                if selected_mode == 2:
                    bg = Background()
                    car = Car4()
                    car2 = Car1()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay2(bg, car, car2, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)

            if selected_level == 2:
                if selected_mode == 1:
                    bg = Background()
                    car = Car4()
                    obstacles = Obstacles_2()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay(bg, car, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)
                if selected_mode == 2:
                    bg = Background()
                    car = Car4()
                    car2 = Car1()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay2(bg, car, car2, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)

            if selected_level == 3:
                if selected_mode == 1:
                    bg = Background()
                    car = Car4()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay(bg, car, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)
                if selected_mode == 2:
                    bg = Background()
                    car = Car4()
                    car2 = Car5()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay2(bg, car, car2, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)

        if selected_car == "Car5":

            if selected_level == 1:
                if selected_mode == 1:
                    bg = Background()
                    car = Car5()
                    obstacles = Obstacles()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay(bg, car, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)
                if selected_mode == 2:
                    bg = Background()
                    car = Car5()
                    car2 = Car6()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay2(bg, car, car2, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)

            if selected_level == 2:
                if selected_mode == 1:
                    bg = Background()
                    car = Car5()
                    obstacles = Obstacles_2()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay(bg, car, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)
                if selected_mode == 2:
                    bg = Background()
                    car = Car5()
                    car2 = Car6()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay2(bg, car, car2, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)

            if selected_level == 3:
                if selected_mode == 1:
                    bg = Background()
                    car = Car5()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay(bg, car, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)
                if selected_mode == 2:
                    bg = Background()
                    car = Car5()
                    car2 = Car6()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay2(bg, car, car2, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)

        if selected_car == "Car6":

            if selected_level == 1:
                if selected_mode == 1:
                    bg = Background()
                    car = Car6()
                    obstacles = Obstacles()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay(bg, car, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)
                if selected_mode == 2:
                    bg = Background()
                    car = Car6()
                    car2 = Car7()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay2(bg, car, car2, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)

            if selected_level == 2:
                if selected_mode == 1:
                    bg = Background()
                    car = Car6()
                    obstacles = Obstacles_2()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay(bg, car, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)
                if selected_mode == 2:
                    bg = Background()
                    car = Car6()
                    car2 = Car7()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay2(bg, car, car2, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)

            if selected_level == 3:
                if selected_mode == 1:
                    bg = Background()
                    car = Car6()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay(bg, car, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)
                if selected_mode == 2:
                    bg = Background()
                    car = Car6()
                    car2 = Car7()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay2(bg, car, car2, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)

        if selected_car == "Car7":

            if selected_level == 1:
                if selected_mode == 1:
                    bg = Background()
                    car = Car7()
                    obstacles = Obstacles()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay(bg, car, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)
                if selected_mode == 2:
                    bg = Background()
                    car = Car7()
                    car2 = Car8()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay2(bg, car, car2, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)

            if selected_level == 2:
                if selected_mode == 1:
                    bg = Background()
                    car = Car7()
                    obstacles = Obstacles_2()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay(bg, car, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)
                if selected_mode == 2:
                    bg = Background()
                    car = Car7()
                    car2 = Car8()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay2(bg, car, car2, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)

            if selected_level == 3:
                if selected_mode == 1:
                    bg = Background()
                    car = Car7()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay(bg, car, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)
                if selected_mode == 2:
                    bg = Background()
                    car = Car7()
                    car2 = Car8()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay2(bg, car, car2, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)

        if selected_car == "Car8":

            if selected_level == 1:
                if selected_mode == 1:
                    bg = Background()
                    car = Car8()
                    obstacles = Obstacles()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay(bg, car, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)
                if selected_mode == 2:
                    bg = Background()
                    car = Car8()
                    car2 = Car9()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay2(bg, car, car2, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)

            if selected_level == 2:
                if selected_mode == 1:
                    bg = Background()
                    car = Car8()
                    obstacles = Obstacles_2()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay(bg, car, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)
                if selected_mode == 2:
                    bg = Background()
                    car = Car8()
                    car2 = Car9()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay2(bg, car, car2, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)

            if selected_level == 3:
                if selected_mode == 1:
                    bg = Background()
                    car = Car8()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay(bg, car, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)
                if selected_mode == 2:
                    bg = Background()
                    car = Car8()
                    car2 = Car9()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay2(bg, car, car2, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)

        if selected_car == "Car9":

            if selected_level == 1:
                if selected_mode == 1:
                    bg = Background()
                    car = Car9()
                    obstacles = Obstacles()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay(bg, car, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)
                if selected_mode == 2:
                    bg = Background()
                    car = Car9()
                    car2 = Car10()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay2(bg, car, car2, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)

            if selected_level == 2:
                if selected_mode == 1:
                    bg = Background()
                    car = Car9()
                    obstacles = Obstacles_2()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay(bg, car, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)
                if selected_mode == 2:
                    bg = Background()
                    car = Car9()
                    car2 = Car10()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay2(bg, car, car2, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)

            if selected_level == 3:
                if selected_mode == 1:
                    bg = Background()
                    car = Car9()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay(bg, car, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)
                if selected_mode == 2:
                    bg = Background()
                    car = Car9()
                    car2 = Car10()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay2(bg, car, car2, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)

        if selected_car == "Car10":

            if selected_level == 1:
                if selected_mode == 1:
                    bg = Background()
                    car = Car10()
                    obstacles = Obstacles()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay(bg, car, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)
                if selected_mode == 2:
                    bg = Background()
                    car = Car10()
                    car2 = Car1()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay2(bg, car, car2, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)

            if selected_level == 2:
                if selected_mode == 1:
                    bg = Background()
                    car = Car10()
                    obstacles = Obstacles_2()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay(bg, car, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)
                if selected_mode == 2:
                    bg = Background()
                    car = Car10()
                    car2 = Car1()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay2(bg, car, car2, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)

            if selected_level == 3:
                if selected_mode == 1:
                    bg = Background()
                    car = Car10()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay(bg, car, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)
                if selected_mode == 2:
                    bg = Background()
                    car = Car10()
                    car2 = Car1()
                    obstacles = Obstacles_3()
                    score = Score()
                    while True:
                        gameStart(bg)
                        gamePlay2(bg, car, car2, obstacles, score)
                        highscore = gameOver(bg, car, obstacles, score, highscore)
def main():
    while True:
        main_menu()

if __name__ == '__main__':
    main()