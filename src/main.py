import pygame, os, copy, random
import player
import invader
import resource_loader

def main():
    FPS = 60
    MAX_BULLETS = 10
    MAX_INVADERS = 5
    game_loop = True
    input_type = True
    
    pygame.init()
    
    clock = pygame.time.Clock()
    size = width , height = 600 , 468
    screen = pygame.display.set_mode(size)
    
    icon = pygame.image.load('../gfx/icon.png')
    
    invader1_images = resource_loader.load_sprite_images('invader1.png',32)
    invader2_images = resource_loader.load_sprite_images('invader2.png',32)
    
    bullet = pygame.image.load('../gfx/bullet1.png').convert()
    
    #this background should be replaced by the background image
    background = pygame.surface.Surface(screen.get_size()).convert()
    background.fill((0,0,0))
    
    screen.blit(background,background.get_rect())
    
    pygame.display.set_icon(icon)
    pygame.display.set_caption('PyInvaders')
    pygame.mouse.set_visible(0)
    
    bullets = []
    for i in range(MAX_BULLETS):
        bullets.append(copy.deepcopy(bullet))
        
    invaders = []
    for i in range(MAX_INVADERS):
        invaders.append(invader.Invader(invader1_images))
        invaders.append(invader.Invader(invader2_images))
    
    p = player.Player()
    
    
    objects = []
    #objects.append(p)
    objects.extend(invaders)
    all_sprites = pygame.sprite.RenderPlain(objects)

    #init the font module and load the font
    if pygame.font:        
        pygame.font.init()
        font = pygame.font.Font('../gfx/04b_25__.ttf', 12)
    
    while game_loop:       
        
        #clearing screen
        screen.blit(background,p.rect)
        for s in objects:
            screen.blit(background, s.rect)
        
        #watching for key events   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop = not game_loop            
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_loop = not game_loop
                    
                #start activating invaders  
                if event.key == pygame.K_p:
                    for i in invaders:
                        i.active = not i.active
                        #i.rect.top = random.randint(0, (height - 64) / 32) * 32
                        #i.rect.left = -32

                #switching betweent keyboard and mouse
                if event.key == pygame.K_k:
                    input_type = not input_type
                    
                    
        # hints and shortcuts to be printed
        screen.blit(font.render("Press k to switch input", 0, ((255, 206, 0))), (460, 5))

        if input_type is True:
            screen.blit(font.render("current input: " + "keyboard", 0, ((255, 0, 0))), (465, 20))
        
        else:
            screen.blit(font.render("current input: " + "mouse", 0, ((255, 0, 0))), (465, 20))
            

        p.update(input_type)
        screen.blit(p.image,p.rect)

        all_sprites.update()
        all_sprites.draw(screen)
                
        clock.tick(FPS)
        pygame.display.flip()
        
    pygame.quit()
    
    

if __name__ == '__main__':
    main()
