from pygame import *
from Player import Player
from Ball import Ball

window = display.set_mode((700, 500))
display.set_caption("ping pong!!")

background = transform.scale(image.load("image.jpg"), (700, 500))
player = transform.scale(image.load('pngwing.com.png'), (100, 100))


mixer.init()
mixer.music.load('astronomia-negry-tancuyut-s-grobom-mp3.mp3')
mixer.music.play()

player_l = Player('pngwing.com.png ',80, 220 , 7, (70, 100), window)
player_r = Player('pngwing.com.png',550, 220 , 7, (70, 100), window)
ball = Ball('ball.png', 300, 220, 7, (30, 50),window)

FPS = 60
clock = time.Clock()

game = True
finish = False

speed_x = 3
speed_y = 3

font.init()
font1 = font.Font(None, 45)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))
font2 = font.Font(None, 45)
lose2 = font2.render('PLAYER 2 LOSE!', True, (180, 0, 0))

while game:
    clock.tick(FPS)

    for e in event.get():
        # обработай событие «клик по кнопке "Закрыть окно"»
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0, 0))
        player_l.reset()
        player_l.update_l()
        player_r.reset()
        player_r.update_r()
        ball.reset()
        ball.update()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > 500 - 50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(player_l, ball) or sprite.collide_rect(player_r, ball):
            speed_x *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (250, 250))

        if ball.rect.x > 700:
            finish = True
            window.blit(lose2, (250, 250))








    display.update()