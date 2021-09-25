import pygame, random
from pygame.locals import *

def on_grid_random(PX_L):
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x//PX_L * PX_L, y//PX_L * PX_L)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

PX_L = 10

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Consolas', 20)

screen_h = 600
screen_w = 1000

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('Snake')
my_direction = LEFT

qtd_block_w = screen_w // (3 * PX_L)
qtd_block_h = screen_h // (3 * PX_L)
block_pos = []
bd_range = 60
for i in range(qtd_block_w):
    if (PX_L *i + bd_range, bd_range) not in block_pos:
        block_pos.append((PX_L *i + bd_range, bd_range))
    if (screen_w - PX_L *i - bd_range - PX_L, bd_range) not in block_pos:
        block_pos.append((screen_w - PX_L *i - bd_range - PX_L, bd_range))
    if (PX_L *i + bd_range, screen_h - PX_L - bd_range ) not in block_pos:
        block_pos.append((PX_L *i + bd_range, screen_h - PX_L - bd_range))
    if (screen_w - PX_L *i - bd_range - PX_L, screen_h - PX_L - bd_range ) not in block_pos:
        block_pos.append((screen_w - PX_L *i - bd_range - PX_L, screen_h - PX_L - bd_range ))

for i in range(qtd_block_h):
    if (bd_range, PX_L *i + bd_range) not in block_pos:
        block_pos.append((bd_range, PX_L *i + bd_range))
    if (bd_range, screen_h - PX_L *i - bd_range - PX_L) not in block_pos:
        block_pos.append((bd_range, screen_h - PX_L *i - bd_range - PX_L))
    if (screen_w - PX_L - bd_range , PX_L *i + bd_range) not in block_pos:
        block_pos.append((screen_w - PX_L - bd_range , PX_L *i + bd_range))
    if (screen_w - PX_L - bd_range , screen_h - PX_L *i - bd_range - PX_L) not in block_pos:
        block_pos.append((screen_w - PX_L - bd_range , screen_h - PX_L *i - bd_range - PX_L))

block = pygame.Surface((10, 10))
block.fill((40, 40, 40))

snake = [(200, 200), (200, 210), (200, 220)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((0, 255, 0))

fruit_pos = (on_grid_random(PX_L))
cg_apple_color = 0

clock = pygame.time.Clock()

snake_body = pygame.image.load(r'C:\Users\amate\Desktop\Python\pygame\pysnake\themes\default\img\snake_body.png','')
# snake_tail = pygame.image.load(r'C:\Users\amate\Desktop\Python\pygame\pysnake\themes\default\img\snake_tail.png','')
fruit      = pygame.image.load(r'C:\Users\amate\Desktop\Python\pygame\pysnake\themes\default\img\fruit.png','')
floor      = pygame.image.load(r'C:\Users\amate\Desktop\Python\pygame\pysnake\themes\default\img\floor.png','')


end          = False
apple_et     = 0
snake_len    = 0
cg_direction = False

first_rend = True

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
    
        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
                cg_direction = True
            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT
                cg_direction = True
            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
                cg_direction = True
            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT
                cg_direction = True

    if collision(snake[0], fruit_pos):
        fruit_pos = on_grid_random(PX_L)
        while fruit_pos in block_pos:
            fruit_pos = on_grid_random(PX_L)
        snake.append((0, 0))
        apple_et += 1

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
        if snake[0][1] < 0:
            snake[0] = (snake[0][0], snake[0][1] + screen_h)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
        if snake[0][1] > screen_h:
            snake[0] = (snake[0][0], snake[0][1] - screen_h)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
        if snake[0][0] > screen_w:
            snake[0] = (snake[0][0] - screen_w - 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
        if snake[0][0] < 0:
            snake[0] = (snake[0][0] + screen_w, snake[0][1])

    if not end:
        screen.fill((0, 0, 0))
        # Draws the floor
        for i in range(screen_w // 50):
            for j in range(screen_h // 50):
                screen.blit(floor, (0 + i * 50,0 + j * 50))
        
        # Draws the fruit
        screen.blit(fruit, fruit_pos)

        ang = 0
        if first_rend:
            portal_1_pos = [(screen_w//5, screen_h//3), (screen_w - screen_w//5, screen_h//3)]
            portal_2_pos = [(screen_w//5, screen_h - screen_h//3), (screen_w - screen_w//5, screen_h - screen_h//3)]
            # portal_2_pos = [on_grid_random(PX_L), on_grid_random(PX_L)]
            first_rend = False
        for m in range(2):
            portal_1   = pygame.image.load(r'C:\Users\amate\Desktop\Python\pygame\pysnake\themes\default\img\portal_1.png','')
            for i in range(2):
                for j in range(2):
                    portal_1 = pygame.transform.rotate(portal_1, ang)
                    screen.blit(portal_1, (portal_1_pos[m][0] + i * 10, portal_1_pos[m][1] + j * 10))
                    ang += 90
        ang = 0
        for m in range(2):
            portal_2  = pygame.image.load(r'C:\Users\amate\Desktop\Python\pygame\pysnake\themes\default\img\portal_2.png','')
            for i in range(2):
                for j in range(2):
                    portal_2 = pygame.transform.rotate(portal_2, ang)
                    screen.blit(portal_2, (portal_2_pos[m][0] + i * 10, portal_2_pos[m][1] + j * 10))
                    ang += 90

        crashed = False
        for w in range(len(portal_1_pos)):
            for i in range(2):
                for j in range(2):
                    if collision(snake[0], (portal_1_pos[w][0] + i * 10, portal_1_pos[w][1] + j * 10)):
                        if w == 0 and not crashed:
                            if my_direction == UP:
                                if i == 0 and j == 0:
                                    snake[0] = (portal_1_pos[1][0], portal_1_pos[1][1] - 10)
                                elif i == 0 and j == 1:
                                    snake[0] = (portal_1_pos[1][0], portal_1_pos[1][1] - 10)
                                elif i == 1 and j == 0:
                                    snake[0] = (portal_1_pos[1][0], portal_1_pos[1][1] - 20)
                                elif i == 1 and j == 1:
                                    snake[0] = (portal_1_pos[1][0], portal_1_pos[1][1] - 20)
    
                            elif my_direction == DOWN:
                                if i == 0 and j == 0:
                                    snake[0] = (portal_1_pos[1][0], portal_1_pos[1][1] + 10)
                                elif i == 0 and j == 1:
                                    snake[0] = (portal_1_pos[1][0], portal_1_pos[1][1] + 10)
                                elif i == 1 and j == 0:
                                    snake[0] = (portal_1_pos[1][0], portal_1_pos[1][1] + 20)
                                elif i == 1 and j == 1:
                                    snake[0] = (portal_1_pos[1][0], portal_1_pos[1][1] + 20)
    
                            elif my_direction == LEFT:
                                if i == 0 and j == 0:
                                    snake[0] = (portal_1_pos[1][0] - 10, portal_1_pos[1][1])
                                elif i == 0 and j == 1:
                                    snake[0] = (portal_1_pos[1][0] - 10, portal_1_pos[1][1])
                                elif i == 1 and j == 0:
                                    snake[0] = (portal_1_pos[1][0] - 20, portal_1_pos[1][1])
                                elif i == 1 and j == 1:
                                    snake[0] = (portal_1_pos[1][0] - 20, portal_1_pos[1][1])
    
                            elif my_direction == RIGHT:
                                if i == 0 and j == 0:
                                    snake[0] = (portal_1_pos[1][0] + 10, portal_1_pos[1][1])
                                elif i == 0 and j == 1:
                                    snake[0] = (portal_1_pos[1][0] + 10, portal_1_pos[1][1])
                                elif i == 1 and j == 0:
                                    snake[0] = (portal_1_pos[1][0] + 20, portal_1_pos[1][1])
                                elif i == 1 and j == 1:
                                    snake[0] = (portal_1_pos[1][0] + 20, portal_1_pos[1][1])

                            crashed = True
                        elif w == 1 and not crashed:
                            if my_direction == UP:
                                if i == 0 and j == 0:
                                    snake[0] = (portal_1_pos[0][0], portal_1_pos[0][1] - 10)
                                elif i == 0 and j == 1:
                                    snake[0] = (portal_1_pos[0][0], portal_1_pos[0][1] - 10)
                                elif i == 1 and j == 0:
                                    snake[0] = (portal_1_pos[0][0], portal_1_pos[0][1] - 20)
                                elif i == 1 and j == 1:
                                    snake[0] = (portal_1_pos[0][0], portal_1_pos[0][1] - 20)

                            elif my_direction == DOWN:
                                if i == 0 and j == 0:
                                    snake[0] = (portal_1_pos[0][0], portal_1_pos[0][1] + 10)
                                elif i == 0 and j == 1:
                                    snake[0] = (portal_1_pos[0][0], portal_1_pos[0][1] + 10)
                                elif i == 1 and j == 0:
                                    snake[0] = (portal_1_pos[0][0], portal_1_pos[0][1] + 20)
                                elif i == 1 and j == 1:
                                    snake[0] = (portal_1_pos[0][0], portal_1_pos[0][1] + 20)

                            elif my_direction == LEFT:
                                if i == 0 and j == 0:
                                    snake[0] = (portal_1_pos[0][0] - 10, portal_1_pos[0][1])
                                elif i == 0 and j == 1:
                                    snake[0] = (portal_1_pos[0][0] - 10, portal_1_pos[0][1])
                                elif i == 1 and j == 0:
                                    snake[0] = (portal_1_pos[0][0] - 20, portal_1_pos[0][1])
                                elif i == 1 and j == 1:
                                    snake[0] = (portal_1_pos[0][0] - 20, portal_1_pos[0][1])

                            elif my_direction == RIGHT:
                                if i == 0 and j == 0:
                                    snake[0] = (portal_1_pos[0][0] + 10, portal_1_pos[0][1])
                                elif i == 0 and j == 1:
                                    snake[0] = (portal_1_pos[0][0] + 10, portal_1_pos[0][1])
                                elif i == 1 and j == 0:
                                    snake[0] = (portal_1_pos[0][0] + 20, portal_1_pos[0][1])
                                elif i == 1 and j == 1:
                                    snake[0] = (portal_1_pos[0][0] + 20, portal_1_pos[0][1])
                            crashed = True

        crashed = False
        for w in range(len(portal_2_pos)):
            for i in range(2):
                for j in range(2):
                    if collision(snake[0], (portal_2_pos[w][0] + i * 10, portal_2_pos[w][1] + j * 10)):
                        if w == 0 and not crashed:
                            if my_direction == UP:
                                if i == 0 and j == 0:
                                    snake[0] = (portal_2_pos[1][0], portal_2_pos[1][1] - 10)
                                elif i == 0 and j == 1:
                                    snake[0] = (portal_2_pos[1][0], portal_2_pos[1][1] - 10)
                                elif i == 1 and j == 0:
                                    snake[0] = (portal_2_pos[1][0], portal_2_pos[1][1] - 20)
                                elif i == 1 and j == 1:
                                    snake[0] = (portal_2_pos[1][0], portal_2_pos[1][1] - 20)
    
                            elif my_direction == DOWN:
                                if i == 0 and j == 0:
                                    snake[0] = (portal_2_pos[1][0], portal_2_pos[1][1] + 10)
                                elif i == 0 and j == 1:
                                    snake[0] = (portal_2_pos[1][0], portal_2_pos[1][1] + 10)
                                elif i == 1 and j == 0:
                                    snake[0] = (portal_2_pos[1][0], portal_2_pos[1][1] + 20)
                                elif i == 1 and j == 1:
                                    snake[0] = (portal_2_pos[1][0], portal_2_pos[1][1] + 20)
    
                            elif my_direction == LEFT:
                                if i == 0 and j == 0:
                                    snake[0] = (portal_2_pos[1][0] - 10, portal_2_pos[1][1])
                                elif i == 0 and j == 1:
                                    snake[0] = (portal_2_pos[1][0] - 10, portal_2_pos[1][1])
                                elif i == 1 and j == 0:
                                    snake[0] = (portal_2_pos[1][0] - 20, portal_2_pos[1][1])
                                elif i == 1 and j == 1:
                                    snake[0] = (portal_2_pos[1][0] - 20, portal_2_pos[1][1])
    
                            elif my_direction == RIGHT:
                                if i == 0 and j == 0:
                                    snake[0] = (portal_2_pos[1][0] + 10, portal_2_pos[1][1])
                                elif i == 0 and j == 1:
                                    snake[0] = (portal_2_pos[1][0] + 10, portal_2_pos[1][1])
                                elif i == 1 and j == 0:
                                    snake[0] = (portal_2_pos[1][0] + 20, portal_2_pos[1][1])
                                elif i == 1 and j == 1:
                                    snake[0] = (portal_2_pos[1][0] + 20, portal_2_pos[1][1])

                            crashed = True
                        elif w == 1 and not crashed:
                            if my_direction == UP:
                                if i == 0 and j == 0:
                                    snake[0] = (portal_2_pos[0][0], portal_2_pos[0][1] - 10)
                                elif i == 0 and j == 1:
                                    snake[0] = (portal_2_pos[0][0], portal_2_pos[0][1] - 10)
                                elif i == 1 and j == 0:
                                    snake[0] = (portal_2_pos[0][0], portal_2_pos[0][1] - 20)
                                elif i == 1 and j == 1:
                                    snake[0] = (portal_2_pos[0][0], portal_2_pos[0][1] - 20)

                            elif my_direction == DOWN:
                                if i == 0 and j == 0:
                                    snake[0] = (portal_2_pos[0][0], portal_2_pos[0][1] + 10)
                                elif i == 0 and j == 1:
                                    snake[0] = (portal_2_pos[0][0], portal_2_pos[0][1] + 10)
                                elif i == 1 and j == 0:
                                    snake[0] = (portal_2_pos[0][0], portal_2_pos[0][1] + 20)
                                elif i == 1 and j == 1:
                                    snake[0] = (portal_2_pos[0][0], portal_2_pos[0][1] + 20)

                            elif my_direction == LEFT:
                                if i == 0 and j == 0:
                                    snake[0] = (portal_2_pos[0][0] - 10, portal_2_pos[0][1])
                                elif i == 0 and j == 1:
                                    snake[0] = (portal_2_pos[0][0] - 10, portal_2_pos[0][1])
                                elif i == 1 and j == 0:
                                    snake[0] = (portal_2_pos[0][0] - 20, portal_2_pos[0][1])
                                elif i == 1 and j == 1:
                                    snake[0] = (portal_2_pos[0][0] - 20, portal_2_pos[0][1])

                            elif my_direction == RIGHT:
                                if i == 0 and j == 0:
                                    snake[0] = (portal_2_pos[0][0] + 10, portal_2_pos[0][1])
                                elif i == 0 and j == 1:
                                    snake[0] = (portal_2_pos[0][0] + 10, portal_2_pos[0][1])
                                elif i == 1 and j == 0:
                                    snake[0] = (portal_2_pos[0][0] + 20, portal_2_pos[0][1])
                                elif i == 1 and j == 1:
                                    snake[0] = (portal_2_pos[0][0] + 20, portal_2_pos[0][1])
                            crashed = True
    
        cg_apple_color += 1

        block = pygame.image.load(r'C:\Users\amate\Desktop\Python\pygame\pysnake\themes\default\img\bush.png','')
        for pos in block_pos:
            screen.blit(block, pos)
            if collision(snake[0], pos):
                end = True

        snake_head = pygame.image.load(r'C:\Users\amate\Desktop\Python\pygame\pysnake\themes\default\img\snake_head.png','')
        if my_direction == RIGHT:
            snake_head = pygame.transform.rotate(snake_head, 270)
        elif my_direction == DOWN:
            snake_head = pygame.transform.rotate(snake_head, 180)
        elif my_direction == LEFT:
            snake_head = pygame.transform.rotate(snake_head, 90)
        screen.blit(snake_head, snake[0])

        for pos in snake[1:]:
            screen.blit(snake_body, pos)

        
    else:
        screen.fill((0, 0, 0))
        texts = []
        texts.append(myfont.render('You Lose!', False, (255, 255, 255)))
        texts.append(myfont.render(f'Score: {apple_et} pts', False, (255, 255, 255)))
        
        plus_pos = 0
        for text in texts:
            screen.blit(text, (int(screen_w/2),int(screen_h/2) + plus_pos))
            plus_pos += 22

    pygame.display.update()