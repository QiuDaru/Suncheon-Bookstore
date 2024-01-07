import pygame

pygame.init()
screen= pygame.display.set_mode((700,700))

run = True
while run :
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            run = False
    pygame.display.set_caption('小恐龍')
# 清除畫面並填滿背景色
    screen.fill((255, 255, 255))

            
           
            
           
pygame.quit()
        