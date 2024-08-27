import math
import random
import time
import pygame

pygame.init()

WIDTH,HEIGHT = 800,600

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Aim Trainer")

TARGET_INCREMENT = 400 #(mini sec between targets appearing)
TARGET_EVENT = pygame.USEREVENT

TARGET_PADDING = 30

FRAMES = 120 #more frames faster the targets

BG_COLOR = (0,25,40) #rgb values *green *red *blue
LIVES = 3
TOP_BAR_HEIGHT = 50

TARGET_HIT_SOUND = "D:/Codes/Image recongn/sounds/tanmay.mp3"
TARGET_HIT_SOUND = "D:/Codes/Image recongn/sounds/target_hit.mp3"
MISCLICK_SOUND = "D:/Codes/Image recongn/sounds/misclick.mp3"
FAIL_TARGET_SOUND = "D:/Codes/Image recongn/sounds/fail_target.mp3"

LABEL_FONT = pygame.font.SysFont("comicsans",24)

class Target:
    MAX_SIZE = 30
    GROWTH_RATE = 0.2
    COLOR = "red"
    SECOND_COLOR = "yellow"

    THIRD_COLOR = "cyan"

    def __init__(self,x,y): #targeted contructor
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True
    
    def update(self):
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False
        if self.grow:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE

    def draw(self,win):

        pygame.draw.circle(win,self.COLOR,(self.x,self.y),self.size)
        pygame.draw.circle(win,self.THIRD_COLOR,(self.x,self.y),self.size * 0.8)
        pygame.draw.circle(win,self.COLOR,(self.x,self.y),self.size * 0.6)
        pygame.draw.circle(win,self.SECOND_COLOR,(self.x,self.y),self.size * 0.4)
        #need to print like this so that smaller circles can overlap on each other

    def collide(self , x , y):
        dis = math.sqrt((self.x - x)**2 + (self.y -y)**2) #sqaure root
        return dis <= self.size


def draw(win,targets):
    win.fill(BG_COLOR)

    for target in targets:
        target.draw(win)


def format_time(sec):
    milli = math.floor(int(sec*1000 % 1000) / 100) #give us the number of miniseconds
    seconds = int(round(sec % 60 , 1))
    minutes = int(sec // 60)

    return f"{minutes:02d}:{seconds:02d}.{milli}"

def draw_top_bar(win,elapsed_time , targets_pressed , misses):

    pygame.draw.rect(win,"grey",(0,0,WIDTH,TOP_BAR_HEIGHT))
    time_label = LABEL_FONT.render(f"Time: {format_time(elapsed_time)}",1,"black")

    speed = round(targets_pressed/elapsed_time , 1)
    speed_label = LABEL_FONT.render(f"Speed: {speed} t/s",1,"black")

    hits_label = LABEL_FONT.render(f"Hits: {targets_pressed}",1,"black")

    lives_label = LABEL_FONT.render(f"Lives: {LIVES - misses}",1,"black")

    win.blit(time_label , (5,5))
    win.blit(speed_label , (200,5))
    win.blit(hits_label , (450,5))
    win.blit(lives_label , (650,5))

def end_screen(win,elapsed_time,targets_pressed,clicks):
    win.fill(BG_COLOR)
    
    # time_label = LABEL_FONT.render(f"Time: {format_time(elapsed_time)}",1,"white")
    time_label = LABEL_FONT.render(f"Target: {(targets_pressed)}",1,"white")

    speed = round(targets_pressed/elapsed_time , 1)
    speed_label = LABEL_FONT.render(f"Speed: {speed} t/s",1,"white")
    hits_label = LABEL_FONT.render(f"Hits: {targets_pressed}",1,"white")

    accuracy = round((targets_pressed/clicks) * 100 ,1)
    acc_label = LABEL_FONT.render(f"Accuracy: {accuracy}%",1,"white")

    clicks_label = LABEL_FONT.render(f"Clicks: {clicks}",1,"white")

    win.blit(time_label , (get_middle(time_label),100))
    win.blit(speed_label , (get_middle(speed_label),200))
    win.blit(hits_label , (get_middle(hits_label),300))
    win.blit(acc_label , (get_middle(acc_label),400))
    win.blit(clicks_label , (get_middle(clicks_label),500))

    pygame.display.update()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                quit()

def get_middle(surface):
    return WIDTH/2 - surface.get_width()/2

def main():
    # time.sleep(10)
    run = True
    targets = []
    clock = pygame.time.Clock()

    target_pressed = 0
    clicks = 0
    misses = 0
    start_time = time.time()

    pygame.time.set_timer(TARGET_EVENT,TARGET_INCREMENT)

    while run:
        clock.tick(FRAMES) #franes per second
        click = False
        mouse_pos = pygame.mouse.get_pos() #give mouse position
        elapsed_time = time.time() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == TARGET_EVENT:
                x=random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y=random.randint(TARGET_PADDING + TOP_BAR_HEIGHT, HEIGHT - TARGET_PADDING)
                target = Target(x,y)
                targets.append(target)

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1
              
        for target in targets:
            target.update()

            if target.size <= 0:
                targets.remove(target)
                misses += 1
                pygame.mixer.music.load(FAIL_TARGET_SOUND)
                pygame.mixer.music.play()

            if click and target.collide(*mouse_pos): #'*' splat operators for tuple (same as mouse_pos[0],mouse_pos[1])
                targets.remove(target)
                # print(target.collide(*mouse_pos))
                target_pressed += 1
                pygame.mixer.music.load(TARGET_HIT_SOUND)
                pygame.mixer.music.play()
            # elif target.collide(*mouse_pos) == False and click != True:
            #     pygame.mixer.music.load(MISCLICK_SOUND)
            #     pygame.mixer.music.play()

        if misses >= LIVES:
            end_screen(WIN,elapsed_time,target_pressed,clicks)

        draw(WIN,targets)
        draw_top_bar(WIN,elapsed_time,target_pressed,misses)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()

    
