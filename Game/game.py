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
        self.knightImgL = pygame.image.load('Sprites/stand_lft.png')
        self.display = display
        self.speed = 0
        self.maxSpeed = 7
        self.anim = 0
        self.attackStance = 0
        self.knightWidth = 60
        self.which = 0

        self.image = pygame.image.load('Sprites/stand.png')

        self.isAttacking = False;
        self.isRight = True;

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

        self.arrayAttackR = []
        self.arrayAttackR.append(pygame.image.load('Sprites/swing_r_1.png'))
        self.arrayAttackR.append(pygame.image.load('Sprites/swing_r_2.png'))
        self.arrayAttackR.append(pygame.image.load('Sprites/swing_r_3.png'))
        self.arrayAttackR.append(pygame.image.load('Sprites/swing_r_4.png'))
        self.arrayAttackR.append(pygame.image.load('Sprites/swing_r_5.png'))

        self.arrayAttackL = []
        self.arrayAttackL.append(pygame.image.load('Sprites/swing_l_1.png'))
        self.arrayAttackL.append(pygame.image.load('Sprites/swing_l_2.png'))
        self.arrayAttackL.append(pygame.image.load('Sprites/swing_l_3.png'))
        self.arrayAttackL.append(pygame.image.load('Sprites/swing_l_4.png'))
        self.arrayAttackL.append(pygame.image.load('Sprites/swing_l_5.png'))



    def drawKnight(self):

        self.speed = 0
        if self.isRight == True:
            self.image = self.knightImg
            self.display.blit(self.image, (self.x, self.y))
        else:
            self.image = self.knightImgL
            self.display.blit(self.image, (self.x, self.y))

        self.anim = 0
        self.rect = self.image.get_rect()

        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)

        return True


    def moveRight(self):
        self.speed += 1
        self.isRight = True
        if self.speed >= self.maxSpeed:
            self.speed = +self.maxSpeed

        self.image = self.arrayR[self.anim]
        self.display.blit(self.image, (self.x, self.y))




        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)

        self.rect = self.image.get_rect()
        

        return True



    def moveLeft(self):
        self.speed -= 1
        self.isRight = False
        if self.speed <= -self.maxSpeed:
            self.speed = -self.maxSpeed


        self.image = self.arrayL[self.anim]
        self.display.blit(self.image, (self.x, self.y))
        self.rect = self.image.get_rect()
        

        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + 50 + self.image_w, self.y + self.image_h)

        return True

    



    def attack(self):


        if self.isRight == True:
            self.speed += 1
            if self.speed >= self.maxSpeed:
                self.speed = +self.maxSpeed


            self.image = self.arrayAttackR[self.attackStance]
            self.display.blit(self.image, (self.x, self.y))

            self.rect = self.image.get_rect()
            

            self.rect.move(self.x, self.y)
            self.rect.topleft = (self.x, self.y)
            self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)

            

        else:
            self.speed -= 1
            if self.speed >= self.maxSpeed:
                self.speed = +self.maxSpeed

            self.image = self.arrayAttackL[self.attackStance]

            self.display.blit(self.image, (self.x, self.y))
            
            self.rect = self.image.get_rect()
            self.rect.move(self.x, self.y)
            self.rect.topleft = (self.x, self.y)
            self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)

        return True

    def chooseAnim(self, chosen):
        self.which = chosen


    def makeAnim(self):

        if (self.which == 1):
            self.drawKnight()
        elif(self.which == 2):
            self.moveRight()
        elif(self.which == 3):
            self.moveLeft()
        elif(self.which == 4):
            self.attack()
        else:
            self.drawKnight()

        
        


class Bat(pygame.sprite.Sprite):

    def __init__(self, display, x, y):

        pygame.sprite.Sprite.__init__(self)

        self.display = display
        self.x = x
        self.y = y
        self.isAlive = True
        self.speedX = 0

        self.batWidth = 50

        self.image = pygame.image.load('Sprites/zoltadupa.png')

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

    def randSpeed(self):
        
        self.speedX = random.randint(-30, 30)

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

        self.shit_startx = random.randrange(0, self.display_width-50)
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

        

        self.points = 5;

        self.bat1 = Bat(self.gameDisplay, self.shit_startx, self.shit_starty)

        #self.all = pygame.sprite.RenderUpdates((self.knight, self.bat1))

        pygame.key.set_repeat(10,80)
        
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

    def pointsDisplay(self, text, disW, disH, display):
        largeText = pygame.font.SysFont('freesandbold.ttf', 50)
        TextSurf, TextRect = self.text_objects(text, largeText)
        TextRect.center = (disW/5, disH/5)
        display.blit(TextSurf, TextRect)


    def crash(self):
        self.message_display("You died")

    def redrawBackground(self):
        self.gameDisplay.fill(Colors.black)
        self.gameDisplay.blit(self.clouds,(200, self.cloud_y))
        self.gameDisplay.blit(self.background, (200,300))


    def gameLoop(self):

        while not self.gameExit:   

            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.gameExit = True


                
                if self.event.type == pygame.KEYDOWN:
                    if self.event.key == pygame.K_LEFT:

                        self.knight.chooseAnim(3)
                    

                        if self.knight.anim < 7:
                            self.knight.anim += 1
                            print(self.knight.anim)
                        else:
                            self.knight.anim = 0

                        
                    elif self.event.key == pygame.K_RIGHT:

                        self.knight.chooseAnim(2)

                        if self.knight.anim < 7:
                            self.knight.anim += 1
                            print(self.knight.anim)
                        else:
                            self.knight.anim = 0

                    elif self.event.key == pygame.K_SPACE:
                       
                        self.knight.chooseAnim(4)
                        self.knight.isAttacking = True;
                

                        if self.knight.attackStance < 4:
                            self.knight.attackStance += 1
                            print(self.knight.attackStance)
                        else:
                            self.knight.attackStance = 0

                        
                    elif self.event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

                if self.event.type == pygame.KEYUP:
                    if self.event.key == pygame.K_LEFT or self.event.key == pygame.K_RIGHT or self.event.key == pygame.K_SPACE:
                        self.knight.chooseAnim(1)

                        
                
                print(self.event)

            if self.knight.x > self.display_width - self.knight.knightWidth:
                self.knight.x = self.display_width - self.knight.knightWidth
            elif self.knight.x < 0:
                self.knight.x = 0
            else:
                self.knight.x += self.knight.speed       

            
            if self.bat1.y >= self.display_height * 0.8:
                self.bat1.y = self.display_height * 0.8

                self.bat1.x += self.bat1.speedX

            if self.bat1.x > self.display_width - self.bat1.batWidth:
                self.bat1.x = self.display_width - self.bat1.batWidth
            if self.bat1.x < 0:
                self.bat1.x = 0

            else:
                self.bat1.y += 5

            

            self.redrawBackground()
            self.knight.makeAnim()
            self.bat1.drawRect()
            self.pointsDisplay(str(self.points), self.display_width, self.display_height, self.gameDisplay)


            if pygame.sprite.collide_rect(self.knight, self.bat1):
                if self.knight.isAttacking == True:
                    self.points += 10
                    self.bat1.y = 100
                    self.bat1.x = random.randrange(0, self.display_width-50)
                    self.bat1.randSpeed()
                    self.knight.isAttacking = False

                

                else:
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


