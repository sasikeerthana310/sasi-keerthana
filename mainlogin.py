import pygame


# initialize game engine
pygame.init()

window_width=1000
window_height=667
black = 0,0,0

clock_tick_rate=20

# Open a window
size = (window_width, window_height)
screen = pygame.display.set_mode(size)

# Set title to the window
pygame.display.set_caption("Welcome To Banking")

dead=False

clock = pygame.time.Clock()
background_image = pygame.image.load("background.png").convert()
user = pygame.image.load("user.png").convert()
user = pygame.transform.scale(user, (150,200))
userpos  = pygame.draw.rect(screen,black,(300,200,300,200))
admin = pygame.image.load("admin.png").convert()
admin = pygame.transform.scale(admin, (150,200))
adminpos  = pygame.draw.rect(screen,black,(600,200,600,200))
font = pygame.font.SysFont("comicsansms", 40)
text = font.render("User", True, (250, 80, 37))
lev = pygame.draw.rect(screen,black,(300,400,100,50))
text1 = font.render("admin", True, (250, 80, 37))
lev1 = pygame.draw.rect(screen,black,(600,400,100,50))

while(dead==False):
    pos = pygame.mouse.get_pos()
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if userpos.collidepoint(pos) and pressed1 or pressed2:
             import us_log
        if adminpos.collidepoint(pos) and pressed1 or pressed2:
            import ad_log
            pygame.quit()

        if event.type == pygame.QUIT:
            dead = True
    screen.blit(background_image, [0, 0])
    screen.blit(user,userpos)
    screen.blit(admin,adminpos)
    screen.blit(text,lev)
    screen.blit(text1,lev1)
    pygame.display.flip()
    clock.tick(clock_tick_rate)
