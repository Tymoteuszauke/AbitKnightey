import pygame
import sys
import time
import random




class Knight(pygame.sprite.Sprite):
    
    def __init__(self, display, x, y):

        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.knightImg = pygame.image.load('Sprites/stand.png')
        self.display = display
        self.speed = 0
        self.maxSpeed = 7
        self.anim = 0
        self.knightWidth = 60

        self.rect = self.knightImg.get_rect()

        self.image_w, self.image_h = self.knightImg.get_size()
        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)      

        

        self.arrayR = []
        self.arrayR.append(pygame.image.load('Sprites/right1.png'))
        self.arrayR.append(pygame.image.load('Sprites/right2.png'))
        self.arrayR.append(pygame.image.load('Sprites/right3.png'))
        self.arrayR.append(pygame.image.load('Sprites/right4.png'))
        self.arrayR.append(pygame.image.load('Sprites/right5.png'))
        self.arrayR.append(pygame.image.load('Sprites/right6.png'))
        self.arrayR.append(pygame.image.load('Sprites/right7.png'))
        self.arrayR.append(pygame.image.load('Sprites/right8.png'))

        self.arrayL = []
        self.arrayL.append(pygame.image.load('Sprites/left1.png'))
        self.arrayL.append(pygame.image.load('Sprites/left2.png'))
        self.arrayL.append(pygame.image.load('Sprites/left3.png'))
        self.arrayL.append(pygame.image.load('Sprites/left4.png'))
        self.arrayL.append(pygame.image.load('Sprites/left5.png'))
        self.arrayL.append(pygame.image.load('Sprites/left6.png'))
        self.arrayL.append(pygame.image.load('Sprites/left7.png'))
        self.arrayL.append(pygame.image.load('Sprites/left8.png'))


    def drawKnight(self):

        self.speed = 0
        self.display.blit(self.knightImg, (self.x, self.y))
        self.anim = 0
        self.rect = self.knightImg.get_rect()

        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)


    def moveRight(self):
        self.speed += 1
        if self.speed >= self.maxSpeed:
            self.speed = +self.maxSpeed

        
        self.display.blit(self.arrayR[self.anim], (self.x, self.y))
        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)

        self.rect = self.arrayR[self.anim].get_rect()



    def moveLeft(self):
        self.speed -= 1
        if self.speed <= -self.maxSpeed:
            self.speed = -self.maxSpeed

        
        self.display.blit(self.arrayL[self.anim], (self.x, self.y))
        self.rect = self.arrayR[self.anim].get_rect()

        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + 50 + self.image_w, self.y + self.image_h)


    def jumpRight(self):
        self.speed += 2


class Shit(pygame.sprite.Sprite):

    def __init__(self, display, x, y):

        pygame.sprite.Sprite.__init__(self)

        self.display = display
        self.x = x
        self.y = y

        self.shit = pygame.image.load('Sprites/zoltadupa.png')
        self.rect = self.shit.get_rect()

        self.image_w, self.image_h = self.shit.get_size()
        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)

    def drawRect(self):
        self.display.blit(self.shit, (self.x, self.y))

        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)


class Colors:

    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)




class Engine:

    def __init__(self):
        
        pygame.display.set_caption('A bit Knightey')

        self.fps = 60
        self.display_width = 800
        self.display_height = 600
        
        self.x = self.display_width * 0.45
        self.y = self.display_height * 0.8

        self.shit_startx = random.randrange(0, self.display_width)
        self.shit_starty = 100

        self.clock = pygame.time.Clock()

        self.background = pygame.image.load('mountain.png')
        self.clouds = pygame.image.load('clouds.png')
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        
        self.knight = Knight(self.gameDisplay, self.x, self.y)

        self.gameExit = False

        self.gameDisplay.fill(Colors.black)
        self.gameDisplay.blit(self.clouds,(200, 1))
        self.gameDisplay.blit(self.background, (200,300))
        self.knight.drawKnight()

        self.cloud_y = 1
        self.cloud_down = False

        self.shit1 = Shit(self.gameDisplay, self.shit_startx, self.shit_starty)

        pygame.key.set_repeat(10,80)
        #message_display("NAKURWIAJ!!", display_width, display_height, gameDisplay)
        self.gameLoop()

    def text_objects(self, text, font):
        textSurface = font.render(text, True, Colors.red)
        return textSurface, textSurface.get_rect()

    def message_display(self, text, disW, disH, display):
        largeText = pygame.font.SysFont('freesandbold.ttf', 115)
        TextSurf, TextRect = self.text_objects(text, largeText)
        TextRect.center = (disW/2, disH/2)
        display.blit(TextSurf, TextRect)

        pygame.display.update()

        time.sleep(3)

    def crash(self):
        self.message_display("You died")

    def gameLoop(self):

        while not self.gameExit:   

            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.gameExit = True


                
                if self.event.type == pygame.KEYDOWN:
                    if self.event.key == pygame.K_LEFT:
                        self.gameDisplay.fill(Colors.black)
                        self.gameDisplay.blit(self.clouds,(200, self.cloud_y))
                        self.gameDisplay.blit(self.background, (200,300))
                        self.knight.moveLeft()

                        if self.knight.anim < 7:
                            self.knight.anim += 1
                            print(self.knight.anim)
                        else:
                            self.knight.anim = 0

                        
                    elif self.event.key == pygame.K_RIGHT:
                        self.gameDisplay.fill(Colors.black)
                        self.gameDisplay.blit(self.clouds,(200, self.cloud_y))
                        self.gameDisplay.blit(self.background, (200,300))
                        self.knight.moveRight()

                        if self.knight.anim < 7:
                            self.knight.anim += 1
                            print(self.knight.anim)
                        else:
                            self.knight.anim = 0


                        
                    elif self.event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

                if self.event.type == pygame.KEYUP:
                    if self.event.key == pygame.K_LEFT or self.event.key == pygame.K_RIGHT:
                        self.gameDisplay.fill(Colors.black)
                        self.gameDisplay.blit(self.clouds,(200, self.cloud_y))
                        self.gameDisplay.blit(self.background, (200,300))
                        self.knight.drawKnight()
                        


                print(self.event)

            if self.knight.x > self.display_width - self.knight.knightWidth:
                self.knight.x = self.display_width - self.knight.knightWidth
            elif self.knight.x < 0:
                self.knight.x = 0
            else:
                self.knight.x += self.knight.speed



            
            if self.shit1.y >= self.display_height * 0.8:
                self.shit1.y = self.display_height * 0.8
            else:
                self.shit1.y += 5

 
            self.shit1.drawRect()

            if pygame.sprite.collide_rect(self.knight, self.shit1):
                quit()

            pygame.display.update()

            self.clock.tick_busy_loop(self.fps)



def main(args):

    pygame.init()
    game = Engine()
    pygame.quit()
    quit()

if __name__ == '__main__':
    sys.exit(main(sys.argv))


    