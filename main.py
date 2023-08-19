import pygame
import random


#Starting pygame
pygame.init()

#Colours
bianco = (255, 255, 255)
black = (1, 1, 1)

#Creating game window
larghezza_finestra = 800
altezza_finestra = 600

finestra = pygame.display.set_mode((larghezza_finestra, altezza_finestra))
pygame.display.set_caption("pong")


#Control of fps
clock = pygame.time.Clock()
fps = 60

#Creating rachets
larghezza_racchetta = 15
altezza_racchetta = 100
velocita_racchetta = 5


racchetta_destra = pygame.Rect(larghezza_finestra - 50 - larghezza_racchetta,
                                 altezza_finestra // 2 - altezza_racchetta // 2,
                                 larghezza_racchetta, altezza_racchetta)


racchetta_sinistra = pygame.Rect(50, altezza_finestra // 2 - altezza_racchetta // 2,
                                 larghezza_racchetta, altezza_racchetta)


#Creating the ball
dimensione_palla = 20
velocita_palla_x = 5
velocita_palla_y = 5

palla = pygame.Rect(larghezza_finestra // 2 - dimensione_palla // 2,
                    altezza_finestra // 2 - dimensione_palla // 2,
                    dimensione_palla,
                    dimensione_palla)



#Score
punteggio1 = 0
punteggio2 = 0
font = pygame.font.SysFont("Calibri", 60, bold=True, italic=False)


 
#drawing objects
def disegna_oggetti():
    finestra.fill(black)
    pygame.draw.rect(finestra, bianco, racchetta_sinistra)
    pygame.draw.rect(finestra, bianco, racchetta_destra)
    pygame.draw.ellipse(finestra, bianco, palla)


    testo = font.render(str(punteggio1), True, bianco)
    finestra.blit(testo, (larghezza_finestra // 2 - testo.get_width() // 2 - 50, 60))
    testo = font.render(str(punteggio2), True, bianco)
    finestra.blit(testo, (larghezza_finestra // 2 - testo.get_width() // 2 + 50, 60))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
    disegna_oggetti()

    pygame.display.update()
    clock.tick(fps)

    #Objects movement
    tasti = pygame.key.get_pressed()
    if tasti[pygame.K_w]:
        racchetta_sinistra.y -= velocita_racchetta
    
    if tasti[pygame.K_s]:
         racchetta_sinistra.y += velocita_racchetta

    if tasti[pygame.K_UP]:
        racchetta_destra.y -= velocita_racchetta
    
    if tasti[pygame.K_DOWN]:
        racchetta_destra.y += velocita_racchetta


    #Ball movement
    palla.x += velocita_palla_x
    palla.y += velocita_palla_y
        
    #top and bottom
    if palla.top <= 0 or palla.bottom >= altezza_finestra:
        velocita_palla_y = -velocita_palla_y

    #right and left
    if palla.left <= 0:
        #Player lost
        palla.x = larghezza_finestra // 2 - dimensione_palla // 2
        palla.y = altezza_finestra // 2 - dimensione_palla // 2
        punteggio2 += 1
        
        velocita_palla_x = random.choice([-5, 5])
        velocita_palla_y = random.choice([-5, 5])

        

    if palla.right >= larghezza_finestra:
        palla.x = larghezza_finestra // 2 - dimensione_palla // 2
        palla.y = altezza_finestra // 2 - dimensione_palla // 2
        punteggio1 += 1
        
        velocita_palla_x = random.choice([-5, 5])
        velocita_palla_y = random.choice([-5, 5])

        

    #Rachet collision
    if palla.colliderect(racchetta_sinistra) or palla.colliderect(racchetta_destra):
        velocita_palla_x = -velocita_palla_x
        