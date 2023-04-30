from pygame import *

WIDTH = 1200
HEIGHT = 700

FPS = 60

clock = time.Clock()
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("")
display.set_icon(image.load("Images/sprite1.png"))

background = transform.scale(image.load("Images/bg.jpg"), (WIDTH, HEIGHT))

sprite1 = transform.scale(image.load("Images/sprite1.png"), (100, 100))
sprite2 = transform.scale(image.load("images/sprite2.png"), (100, 100))

sprite1_x = WIDTH // 12
sprite1_y = (HEIGHT - 100) // 2

sprite2_x = WIDTH - WIDTH // 12 - 100
sprite2_y= (HEIGHT - 100) // 2

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                game = False

    keys_pressed = key.get_pressed()

    if keys_pressed[K_w] and sprite1_y > 5:
        sprite1_y -= 10
    if keys_pressed[K_s] and sprite1_y < HEIGHT - 100:
        sprite1_y += 10
    if keys_pressed[K_a] and sprite1_x > 5:
        sprite1_x -= 10
    if keys_pressed[K_d] and sprite1_x < WIDTH - 100:
        sprite1_x += 10

    if keys_pressed[K_UP] and sprite2_y > 5:
        sprite2_y -= 10
    if keys_pressed[K_DOWN] and sprite2_y < HEIGHT - 100:
        sprite2_y += 10
    if keys_pressed[K_LEFT] and sprite2_x > 5:
        sprite2_x -= 10
    if keys_pressed[K_RIGHT] and sprite2_x < WIDTH - 100:
        sprite2_x += 10

    if keys_pressed[K_UP] and sprite2_y > 5:
        sprite2_y -= 10
    if keys_pressed[K_DOWN] and sprite2_y < HEIGHT - 100:
        sprite2_y += 10
    if keys_pressed[K_LEFT] and sprite2_x > 5:
        sprite2_x -= 10
    if keys_pressed[K_RIGHT] and sprite2_x < WIDTH - 100:
        sprite2_x += 10

    window.blit(background, (0, 0))

    window.blit(sprite1, (sprite1_x, sprite1_y))
    window.blit(sprite2, (sprite2_x, sprite2_y))

    display.update()
    clock.tick(FPS)
