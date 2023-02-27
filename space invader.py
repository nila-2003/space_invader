import pygame
import random
import math
from pygame import mixer

#initializing pygame

pygame.init()

#creating gaming window
screen= pygame.display.set_mode((800,600))
background=pygame.image.load("C:/Users/nilas/Downloads/spacebackground.jpg")



#logo and title
pygame.display.set_caption("Space Invaders")
icon= pygame.image.load("C:/Users/nilas/Downloads/spaceship.png")
pygame.display.set_icon(icon)

#background sound
mixer.music.load('C:/Users/nilas/AppData/Local/Temp/Rar$DRa8988.16661/Space-Invaders-Pygame-master/background.wav')
mixer.music.play(-1)  #loop

#adding image 
playerimg= pygame.image.load("C:/Users/nilas/Downloads/icons8-space-fighter-50.png")
playerX= 370
playerY=480
playerX_change=0

#adding Enemy
enemyimg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
numofenemies=6
for i in range(numofenemies):
    enemyimg.append(pygame.image.load("C:/Users/nilas/Downloads/icons8-alien-50.png"))
    enemyX.append(random.randint(0,750))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.8)
    enemyY_change.append(40)

#bullet
bulletimg=pygame.image.load("C:/Users/nilas/Downloads/icons8-bullet-64.png")
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=3
bullet_state="ready"

#score
score_value=0

font=pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10

#game over text
over_font=pygame.font.Font('freesansbold.ttf',64)

def game_over_text():
    over_text=over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))

def show_score(x,y):
    score=font.render("Score: "+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def player(x,y):
    screen.blit(playerimg,(x,y))
    
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))
    
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletimg,(x-2,y+10))
    
def iscollision(enemyX,enemyY,bulletX,bulletY):
    distance= math.sqrt((math.pow(enemyX-bulletX,2))+ (math.pow(enemyY-bulletY,2)))
    if distance<27:
        return True
    else:
        return False

#game loop
running=True
while running:
    #background colour
    screen.fill((0,0,0))
    #background
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running=False
            
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change-=0.5
            if event.key==pygame.K_RIGHT:
                playerX_change+=0.5
            if event.key==pygame.K_SPACE:
                if bullet_state=="ready":
                    bullet_sound= mixer.Sound('C:/Users/nilas/AppData/Local/Temp/Rar$DRa8988.19704/Space-Invaders-Pygame-master/laser.wav')
                    bullet_sound.play()
                    bulletX=playerX
                    fire_bullet(bulletX,bulletY)
                
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0

    playerX+=playerX_change
    if playerX<=0:
        playerX=0
    elif playerX>=750:
        playerX=750
        
    #enemies
    for i in range(numofenemies):    
        #game over
        if enemyY[i]>440:
            for j in range(numofenemies):
                enemyY[j]=2000
            game_over_text()
            break
        enemyX[i]+=enemyX_change[i]
        if enemyX[i]<=0:
            enemyX_change[i]=0.8
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i]>=750:
            enemyX_change[i]=-0.8
            enemyY[i]+=enemyY_change[i]
            
         #collision
        collision=iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound=mixer.Sound('C:/Users/nilas/AppData/Local/Temp/Rar$DRa8988.23499/Space-Invaders-Pygame-master/explosion.wav')
            explosion_sound.play()
            bulletY=480
            bullet_state="ready"
            score_value+=1
            enemyX[i]=random.randint(0,750)
            enemyY[i]=random.randint(50,150)
        enemy(enemyX[i],enemyY[i],i)
        
        
    #bullet movement
    if bulletY<=0:
        bulletY=480
        bullet_state="ready"
        
    if bullet_state=="fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change
        
   
        
        
    #Calling the function        
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()
    
        