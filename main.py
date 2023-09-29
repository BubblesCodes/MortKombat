import pygame
import os
import time
#got colours from other exerices
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
green = (0, 255, 0)
pink = (255, 0, 255)
orange = (255, 155, 0)
sky_blue = (70, 132, 219)
ground = (12, 201, 47)
sun = (237, 245, 15)
house_brown = (184, 149, 84)
house_red = (148, 53, 50)
gray1 = (235, 235, 235)
gray2 = (214, 214, 214)
gray3 = (200, 200, 200)

done = False


#initialize pygames windows
pygame.font.init()
pygame.init()
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Mort Combat')
#set framerate
clock = pygame.time.Clock()
FPS = 60


#load images
bg_image = pygame.image.load(os.path.join("assets", "fight-background.jpg")).convert_alpha()

player1_img = pygame.image.load(os.path.join("assets", "mort1.png")).convert_alpha()
player1_attack = pygame.image.load(os.path.join("assets","mort1_attack.png")).convert_alpha()

player2_img = pygame.image.load(os.path.join("assets", "mort2.png")).convert_alpha()
player2_attack = pygame.image.load(os.path.join("assets", "mort2_attack.png")).convert_alpha()

#drawing different functions on the screen
def draw_bg():
  scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
  screen.blit(scaled_bg.convert_alpha(), (0, 0))


def draw_pb():
  play_font = pygame.font.SysFont('comicsansms', 75)
  play_button = play_font.render('Play', True, (black))
  screen.blit(play_button, (876, 450))


def draw_quit():
  draw_font = pygame.font.SysFont('comicsansms', 75)
  quit_button = draw_font.render('Quit', True, (black))
  screen.blit(quit_button, (870, 850))


def draw_title():
  title_font = pygame.font.SysFont('comicsansms', 75)
  title_button = title_font.render('Mort Kombat', True, (black))
  screen.blit(title_button, (740, 250))


def draw_info():
  htp_font = pygame.font.SysFont('comicsansms', 75)
  htp_button = htp_font.render('Info', True, (black))
  screen.blit(htp_button, (870, 660))


def draw_esc():
  esc_font = pygame.font.SysFont('comicsansms', 35)
  esc_button = esc_font.render('Esc', True, (black))
  screen.blit(esc_button, (727, 407))
  
def draw_health_bar(health, x, y):
  ratio = health / 100
  pygame.draw.rect(screen, white, (x - 3, y - 3, 404, 34))
  pygame.draw.rect(screen, red, (x, y, 400, 30))
  pygame.draw.rect(screen, yellow, (x, y, 400 * ratio, 30))

    
over = False

#draw players postions and images


player1_health = 100
player2_health = 100

player1_x = 450
player1_y = 600

player2_x = 1400
player2_y = 600


player1_idle = pygame.transform.scale(player1_img, (216, 200))
player1_attack = pygame.transform.scale(player1_attack, (216, 200))


player2_idle = pygame.transform.scale(player2_img, (80, 200))
player2_attack = pygame.transform.scale(player2_attack, (80, 200))



#Main Loop
while not done:
  clock.tick(FPS)
  #creates the scenes and the backrounds
  scene_1 = False
  scene_2 = False
  screen.fill(gray3)
  pygame.draw.rect(screen, blue, [840, 470, 240, 90])
  draw_pb()
  pygame.draw.rect(screen, yellow, [840, 870, 240, 90])
  draw_quit()
  pygame.draw.rect(screen, orange, [840, 670, 240, 90])
  draw_info()
  draw_title()
  #screen.blit(mort_1,(0, 0))
  mouse_pos = pygame.mouse.get_pos()
  mouse_x = mouse_pos[0]
  mouse_y = mouse_pos[1]
  print(mouse_x," ", mouse_y)
  #left_mouse = event.type.get()
  #quit button and hover colour change
  if mouse_x in range(840, 1075) and mouse_y in range(870, 955):
    pygame.draw.rect(screen, (241, 235, 156), [840, 870, 240, 90])
    draw_quit()
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        left_mouse = pygame.mouse.get_pressed()
        if left_mouse[0]:
          pygame.quit()
          pygame.display.flip()

  #play button to jump into next scene
  if mouse_x in range(840, 1075) and mouse_y in range(470, 555):
    pygame.draw.rect(screen, sky_blue, [840, 470, 240, 90])
    draw_pb()
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        left_mouse = pygame.mouse.get_pressed()
        if left_mouse[0]:
          scene_1 = True
          pygame.display.flip()

  #draw how to play button
  if mouse_x in range(840, 1075) and mouse_y in range(670, 755):
    pygame.draw.rect(screen, (252, 182, 3), [840, 670, 240, 90])
    draw_info()
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        left_mouse = pygame.mouse.get_pressed()
        if left_mouse[0]:
          scene_2 = True

  #How to play scene
  while scene_2:
    
    mouse_pos = pygame.mouse.get_pos()
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
    print(mouse_x," ", mouse_y)
    pygame.draw.rect(screen, gray1, [710, 400, 500, 600])
    pygame.draw.rect(screen, gray2, [720, 415, 90, 40])
    draw_esc()
    #Draw some stuff
    key = pygame.key.get_pressed()
    if mouse_x in range(720, 800) and mouse_y in range(415, 450):
      pygame.draw.rect(screen, (249, 249, 249), [720, 415, 90, 40])
      draw_esc()
      if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_presses = pygame.mouse.get_pressed()
        if mouse_presses[0]:
          scene_2 = False
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
      pygame.draw.rect(screen, (249, 249, 249), [720, 415, 90, 40])
      draw_esc()
      scene_2 = False
      clock.tick(FPS)

    pygame.display.flip()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
  #game scene
  while scene_1:
    p1_attacking = False
    p2_attacking = False

    clock.tick(FPS)
    SPEED = 7
    key = pygame.key.get_pressed()
    draw_bg()
    DAMAGE = 0.5
    draw_health_bar(player1_health, 80, 50)
    draw_health_bar(player2_health, 1430, 50)
    
    player1 = player1_idle
    player2 = player2_idle

    #player 1 hitbox
    player1_hitbox = pygame.Rect(player1_x, player1_y, 216,200)
    #pygame.draw.rect(screen,red,[player1_x, player1_y, 216, 200], 3)
    
    #player 2 hitbox
    player2_hitbox = pygame.Rect(player2_x, player2_y, 80, 200)
    #pygame.draw.rect(screen, red,[player2_x, player2_y, 80, 200], 3)

    over_font = pygame.font.SysFont('comicsansms', 60)
    game_over = over_font.render('GAME OVER', True, (white))
    if player1_health <= 0 or player2_health <= 0:
      screen.blit(game_over, (800, 150))
      over = True

    if over == False:
    #attacking

      if key[pygame.K_w]:
        p1_attacking = True
        player1 = player1_attack
        p1_attack = pygame.Rect(player1_x, player1_y, 216, 200)
        #pygame.draw.rect(screen, green, p1_attack)
        if p1_attack.colliderect(player2_hitbox):
          player2_health -= DAMAGE
          



      if key[pygame.K_UP]:
        p2_attacking = True
        player2 = player2_attack
        p2_attack = pygame.Rect(player2_x, player2_y, 80, 200)
        #pygame.draw.rect(screen, green, p2_attack)
        if p2_attack.colliderect(player1_hitbox):
          player1_health -= DAMAGE


      screen.blit(player1.convert_alpha(), (player1_x, player1_y))
      screen.blit(player2.convert_alpha(), (player2_x, player2_y))

    

      #movement
      #player one portal radius

      if player1_x <= -220:
        player1_x = 1920
      
      elif player1_x >= 1920:
        player1_x = -220

      #player two portal radius
      if player2_x <= -100:
        player2_x = 1920
      
      elif player2_x >= 1920:
        player2_x = -100

      #player 1 controls
      if p1_attacking == False:
        if key[pygame.K_a]:
          player1_x -= SPEED

        if key[pygame.K_d]:
          player1_x += SPEED
        
      #player 2 controls
      if p2_attacking == False:
        if key[pygame.K_LEFT]:
          player2_x -= SPEED

        if key[pygame.K_RIGHT]:
          player2_x += SPEED
      




  

    pygame.display.flip()

    
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          scene_3 = True
          while scene_3:
            pygame.display.flip()
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = mouse_pos[0]
            mouse_y = mouse_pos[1]
            #print(mouse_x," ", mouse_y)
            #Pause menu
            pygame.draw.rect(screen, gray1, [710, 400, 500, 600])
            pygame.draw.rect(screen, gray2, [720, 415, 90, 40])
            draw_esc()
            if mouse_x in range(720, 800) and mouse_y in range(415, 450):
              pygame.draw.rect(screen, (249, 249, 249), [720, 415, 90, 40])
              draw_esc()
              if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    scene_3 = False
            pygame.draw.rect(screen, (yellow), [840, 870, 240, 90])          
            draw_quit()
            if mouse_x in range(840, 1075) and mouse_y in range(870, 955):
              pygame.draw.rect(screen, (241, 235, 156), [840, 870, 240, 90])
              draw_quit()
              for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                  left_mouse = pygame.mouse.get_pressed()
                  if left_mouse[0]:
                    pygame.quit()
                    pygame.display.flip()
            pygame.display.flip()

                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  pygame.quit()

        #pygame.draw.rect(screen, red, [450, 600, 117, 240])
        #pygame.draw.rect(screen, red, [1470, 600, 117, 240])


    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

  pygame.display.flip()

pygame.quit()
