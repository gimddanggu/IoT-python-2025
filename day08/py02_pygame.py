# py02_pygame.py
# PyGame 그래픽 표현(선, 사각형, 원..)
import pygame   # pygame 기본모듈 추가
from pygame.locals import QUIT # 종료처리 변수
from pygame.draw import *
import pygame.image as image
import sys      # 운영체제 시스템 명령


pygame.init()
Surface = pygame.display.set_mode((400, 400)) 
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption('Pygame Basic')
def main():
    # 이미지 로드
    snake = image.load('.\image\snake.png')

    # 텍스트 변수
    myfont = pygame.font.SysFont('Namugothic', 50) # antialias=True 계단현상
    message1 = myfont.render('This is my message', True, (255, 0, 255))
    message2 = myfont.render('This is Pygame', False, (255, 0, 255))

    while True:
        Surface.fill(color='black') # Surface.fill((0, 0, 0)) 
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                pygame.quit()   
                sys.exit()      
        # 화면 표현 start_pos=(x, y)
        # 격자무늬
        for x in range(10, 400, 10):
            line(Surface, 'white', (x,0), (x,400))
            line(Surface, 'white', (0,x), (400,x))
        # 선
        pygame.draw.line(Surface, color='red', start_pos=(30, 30), end_pos=(150, 30), width=3)
        line(Surface, (0, 255, 0), (30, 60), (150, 60), 5)
        line(Surface, (0, 0, 255), (30, 90), (150, 90), 7)

        # 사각형 (x, y, weight, height)
        pygame.draw.rect(Surface, 'white', (200, 30, 50, 50))
        pygame.draw.rect(Surface, color='red', rect=(200, 90, 100, 70), width=4)

        # 원 (중심을 시작점으로)
        # pygame.draw.circle(Surface, (255, 255, 0), (30, 160), 10)
        pygame.draw.circle(Surface, color=(255, 255, 0), center=(40, 160), radius=10)
        circle(Surface, (255, 255, 255), (80, 160), 20)
        # 타원
        pygame.draw.ellipse(Surface, (255, 112, 10), (120, 160, 50, 100))
        pygame.draw.ellipse(Surface, (255, 112, 150), (180, 180, 110, 70), 4)

        # polygon 다각형 (별..)

        # 이미지 flaticon.com
        Surface.blit(snake, (336,336))
        Surface.blit(snake, (0,336), (0, 0,32, 32))
        
        # 텍스트
        Surface.blit(message1, (30, 270))
        Surface.blit(message2, (30, 300))

        pygame.display.update() 
        FPSCLOCK.tick(30) 

if __name__ == '__main__':
    main()