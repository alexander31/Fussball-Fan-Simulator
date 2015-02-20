# -*- coding: utf-8 -*-
"""
003_static_blit_pretty.py
static blitting and drawing (pretty version)
url: http://thepythongamebook.com/en:part2:pygame:step003
author: horst.jens@spielend-programmieren.at
licence: gpl, see http://www.gnu.org/licenses/gpl.html

Blitting a surface on a static position
Drawing a filled circle into ballsurface.
Blitting this surface once.
introducing pygame draw methods
The ball's rectangular surface is black because the background
color of the ball's surface was never defined nor filled."""
#TODO:
#Fackel bessere 3D Berechnung
#Bessere Animationen
#Besseres Fackel Design
#Vanille

import pygame 
import random
import os



class Arm(pygame.sprite.Sprite):
    #Fanklasse abschreiben
    images=[]
    images.append(pygame.image.load("hand.png"))
    images.append(pygame.image.load("handwithmiddlefinger.png")) # 2.. with middlefinger
    images.append(pygame.image.load("hand001.png")) # 1 .. with pyro
    images.append(pygame.image.load("hand002.png"))
    images.append(pygame.image.load("hand003.png"))
    images.append(pygame.image.load("hand004.png"))
    images.append(pygame.image.load("hand005.png"))
    images.append(pygame.image.load("hand006.png"))
    images.append(pygame.image.load("hand007.png"))
    #images.append(pygame.image.load("me2.png"))
    #images.append(pygame.image.load("me3.png"))
    #images.append(pygame.image.load("me4.png"))
    #images.append(pygame.image.load("me5.png"))
    #images.append(pygame.image.load("fan2.png"))
    #image.convert_alpha()
    
    def __init__(self, x, y, zoom=1.0, image_index=0):
        """create a (black) surface and paint a blue ball on it"""
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.zoom = zoom
        self.i=image_index
        self.zoom = zoom     #self.background = background
        # create a rectangular surface for the ball 50x50
        #self.surface = pygame.Surface((2*self.radius,2*self.radius))    
        self.image1 = pygame.transform.rotozoom(Arm.images[self.i], 0 , zoom)
        self.image=self.image1
        #self.image1 = pygame.transform.rotozoom(Arm.images[self.i], 0 , zoom)
        self.rect = self.image1.get_rect()
        self.burning=False
        self.burntime=0.0
       
        
    def blit(self, background):
        """blit the Ball on the background"""
        background.blit(self.image1, ( self.x, self.y))
        
    def handwechsel(self):
        self.i+=1
        if self.i >= len (Arm.images):
            self.i=0
        if self.i>=2:
            self.burning=True
        else:
            self.burning=False
        
    def update(self, seconds, x, y):
        self.image1 = pygame.transform.rotozoom(Arm.images[self.i], 0 , self.zoom)
        self.image=self.image1
        self.rect = self.image1.get_rect()
        self.rect.centerx=x
        if y<160:
            y=160
        self.rect.centery=y
        if self.burning:
            self.burntime+=seconds
            if self.burntime>random.random():
                self.i+=1
                self.burntime+=0
                if self.i >= len (Arm.images):
                    self.i=2
            
        
        
        #------

class Flugobjekt(pygame.sprite.Sprite):
    images=[]
    #images.append(pygame.image.load("smokebomb.png"))
    images.append(pygame.image.load("fackel1.png"))
    images.append(pygame.image.load("fackel2.png"))
    images.append(pygame.image.load("fackel3.png"))
    images.append(pygame.image.load("fackel4.png"))
    images.append(pygame.image.load("fackel5.png"))
    images.append(pygame.image.load("fackel6.png"))
    images.append(pygame.image.load("fackel7.png"))
    images.append(pygame.image.load("fackel8.png"))
    images.append(pygame.image.load("fackel9.png"))
    
    
    
    def __init__(self, x, y, zoom=1.0, image_index=0):
        """Fliegende Fackel"""
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = 860 #y
        self.z = 1.0
        self.dx= -0.5+1*random.random()
        self.dy= -5.5-0.5*random.random()
        self.dz= -0.01 #  -0.007*random.random()
        self.gravity=0.05
        self.i=image_index
        self.zoom = 1.0    
        self.rotation = random.randint(1,360)
        self.dr = -5 + 10*random.random()
        self.image1 = pygame.transform.rotozoom(Flugobjekt.images[self.i], self.rotation , self.zoom)
        self.image = self.image1
        self.rect = self.image.get_rect()
        self.rect.centerx=x
        self.rect.centery=y
        
        self.maxburntime=180
        self.burntime=0
        #self.noburntime=random.randint(0,160)
        #self.maxnoburntime=10
       # self.burn=False
       
    def update (self, seconds, x, y):
        self.burntime+=seconds
        # flug
        self.x += self.dx
        self.y +=self.dy
        self.dy += self.gravity
        self.z+=self.dz
        self.rotation+=self.dr
        
        if self.z<-1.1:#+self.z*500: # dy > 600, y=600
            #self.y=300
            self.dz=0
            self.dx=0
            self.dr=0
            self.dy=0
        self.zoom = max(0.09, self.z)
        #if self.zoom<0.00000000000001:
        #    self.zoom=0.00000000000001
        
        
        if self.burntime<self.maxburntime and self.burntime >0:
            if random.randint(1,6)==1:
                Smoke(self.x, self.y, self.z)
            
            
        if self.burntime>random.random():
            self.i+=1
            self.burntime+=0
            if self.i >= len (Flugobjekt.images):
                self.i=0
        
        self.image= pygame.transform.rotozoom(Flugobjekt.images[self.i], self.rotation , self.zoom)
        self.rect = self.image.get_rect()
        self.rect.centerx=self.x + x
        self.rect.centery=self.y + y
        
        
    

class Smoke(pygame.sprite.Sprite):
    images=[]
    #images.append(pygame.image.load("smokebomb.png"))
    images.append(pygame.image.load("Nebel1.png"))
    images.append(pygame.image.load("Nebel2.png"))
    images.append(pygame.image.load("Nebel3.png"))
    images.append(pygame.image.load("Nebel4.png"))
    images.append(pygame.image.load("Nebel5.png"))
    
    def __init__(self, x, y, z):
        """Fliegende Fackel"""
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.z = z
        #Wind
        self.dx= 2+random.random()*0.4-0.2
        self.dy= -0.9+random.random()*0.4-0.2
        self.dz= 0.0 #  -0.007*random.random()
        self.gravity=0.0
        self.i=0
        self.divisor=8.0
        self.zoom = self.z/self.divisor   
        self.rotation = random.randint(1,360)
        self.dr = -5 + 10*random.random()
        self.image1 = pygame.transform.rotozoom(Smoke.images[self.i], self.rotation , self.zoom)
        self.image = self.image1
        self.rect = self.image.get_rect()
        self.rect.centerx=self.x + x
        self.rect.centery=self.y + y
        self.minimalzoom=0.09 #Minimal Rauchwolke
        
        self.maxburntime=random.randint(10,15)
        self.burntime=0
        #self.noburntime=random.randint(0,160)
        #self.maxnoburntime=10
       # self.burn=False
       
    def update (self, seconds, x, y):
        self.burntime+=seconds
        # flug
        self.x += self.dx
        self.y += self.dy
        self.z += self.dz
        self.rotation+=self.dr
        
        
        self.zoom = max(self.minimalzoom, self.z/self.divisor)
        
        
        
       
            
        if self.burntime>self.maxburntime:
            self.kill()    
            
        if self.burntime>random.random():
            self.i+=1
            self.burntime+=0
            if self.i >= len (Smoke.images):
                self.i=0
        
        self.image= pygame.transform.rotozoom(Smoke.images[self.i], self.rotation , self.zoom)
        self.rect = self.image.get_rect()
        self.rect.centerx=self.x + x
        self.rect.centery=self.y + y
    






class PygView(object):
    bildschirmbreite = 600 #300 #600
    bildschirmhoehe = 400  #300 #400
  
    def __init__(self, width=0, height=0, fps=30):
        """Initialize pygame, window, background, font,...
           default arguments 
        """
        if width == 0:
            self.width = PygView.bildschirmbreite
        else:
            self.width=width
        if height==0:
            self.height= PygView.bildschirmhoehe
        else:
            self.height=height
        pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        #self.width = width
        #self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        #self.background = pygame.Surface(self.screen.get_size()).convert()  
        #self.background.fill((255,255,255)) # fill background white
        self.background=pygame.image.load('stadionbildfertif.png')
        self.background.convert()
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0
        self.font = pygame.font.SysFont('mono', 24, bold=True)
        pygame.mixer.music.load(os.path.join('data', 'rapidgesang1.mp3'))#load music
        pygame.mixer.music.play(-1)
        self.allgroup = pygame.sprite.Group()
        self.armgroup = pygame.sprite.Group()
        self.fangroup = pygame.sprite.Group()
        self.fluggroup = pygame.sprite.Group()
        Fan.groups = self.allgroup,self.fangroup
        Flugobjekt.groups = self.allgroup
        Arm.groups = self.armgroup
        Smoke.groups = self.allgroup


    def paint(self):
        """painting on the surface"""
        #------- try out some pygame draw functions --------
        # pygame.draw.rect(Surface, color, Rect, width=0): return Rect
        #pygame.draw.rect(self.background, (0,255,0), (50,50,100,25)) # rect: (x1, y1, width, height)
        # pygame.draw.circle(Surface, color, pos, radius, width=0): return Rect
        #pygame.draw.circle(self.background, (0,200,0), (200,50), 35)
        # pygame.draw.polygon(Surface, color, pointlist, width=0): return Rect
       #pygame.draw.polygon(self.background, (0,180,0), ((250,100),(300,0),(350,50)))
        # pygame.draw.arc(Surface, color, Rect, start_angle, stop_angle, width=1): return Rect
        #pygame.draw.arc(self.background, (0,150,0),(400,10,150,100), 0, 3.14) # radiant instead of grad
        # ------------------- blitting a Ball --------------
        #myball = Ball() # creating the Ball object
        #myball.blit(self.background) # blitting it
        #Fan(60,400, 0.5).blit(self.background)
       # Fan(90,400, 0.3).blit(self.background)
        #Fan(80,400,0.4).blit(self.background)
        #Fan(85,400,2.0).blit(self.background)
        
        self.arm1=Arm(220,200)
        
        for y in range (4):
                 
            for x in range(20):
                if x % 4 == 0 and y == 0:
                    i=random.randint(1,7)
                else:
                    i=0
                #bad #Fan(140+x*35,450+y*50-2*x,0.5,i).blit(self.background)
                #Fan(140+x*35,500+y*55-2*x,0.5,i)#.blit(self.background) 
        
        
        
    def run(self):
        """The mainloop
        """
        self.paint() 
        running = True
        offsetx = -1700
        offsety = -400
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_RETURN:
                        Flugobjekt(150-offsetx,150-offsety)
            
            pressedkeys = pygame.key.get_pressed()
            print(offsetx, offsety)
            if pressedkeys[pygame.K_DOWN]:
                if offsety < 0:
                    offsety += 5   #1
                #print(offsety)
            if pressedkeys[pygame.K_UP]:
                if offsety >-600:  #-450 #-600
                    offsety -= 5 #1
                    
            if pressedkeys[pygame.K_LEFT]:
                if offsetx <0:
                    offsetx += 5 #1
                
                    
            if pressedkeys[pygame.K_RIGHT]:
                if offsetx >-3100:  #-450 #-1300
                    offsetx -= 3 #1
                    
            
                    
            #if offsety != 0 or offsetx != 0:
                
                
                 #turnfactor += 1
            milliseconds = self.clock.tick(self.fps)
            self.seconds=milliseconds/1000.0
            self.playtime += milliseconds / 1000.0
            #self.draw_text("FPS: %6.3f%sPLAYTIME: %6.3f SECONDS" %
                           #(self.clock.get_fps(), " "*5, self.playtime))
            #self.paint()
            pygame.display.flip()
            self.screen.blit(self.background, (offsetx, offsety))
            self.allgroup.update(self.seconds, offsetx, offsety)
            self.allgroup.draw(self.screen)
            if pygame.mouse.get_pressed()[2]:
                self.arm1.handwechsel()
                
            if pygame.mouse.get_pressed()[0]:
                self.armgroup.update(self.seconds,pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
                self.armgroup.draw(self.screen)
            
            
        pygame.quit()


    def draw_text(self, text):
        """Center text in window
        """
        fw, fh = self.font.size(text)
        surface = self.font.render(text, True, (0, 0, 0))
        self.screen.blit(surface, (50,150))




class Fan(pygame.sprite.Sprite):
    """this is not a native pygame sprite but instead a pygame surface"""
    images=[]
    images.append(pygame.image.load("fan2.png"))
    #images.append(pygame.image.load("fan3.png"))
    images.append(pygame.image.load("fan4.png"))
    images.append(pygame.image.load("fan5.png"))
    images.append(pygame.image.load("fan6.png"))
    images.append(pygame.image.load("fan7.png"))
    images.append(pygame.image.load("fan8.png"))
    images.append(pygame.image.load("fan9.png"))
    images.append(pygame.image.load("fan10.png"))
    #images.append(pygame.image.load("fan2.png"))
    #image.convert_alpha()
    
    def __init__(self, x, y, zoom, image_index=1):
        """create a (black) surface and paint,a blue ball on it"""
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.i=image_index
        self.zoom = zoom     
        self.image1 = pygame.transform.rotozoom(Fan.images[self.i], 0 , zoom)
        self.image = self.image1
        self.rect = self.image.get_rect()
        self.rect.centerx=x
        self.rect.centery=y
        self.burntime=0
        self.maxburntime=10
        self.noburntime=random.randint(0,160)
        self.maxnoburntime=10
        self.burn=False

        
    def blit(self, background):
        """blit the Ball on the background"""
        background.blit(self.image1, ( self.x, self.y))
        
    def update (self, seconds, x, y):
        if self.burn:
            self.burntime+=seconds
            self.i=random.randint(3,7)
            if self.burntime>self.maxburntime:
                self.burn=False
                self.burntime=0
                self.noburntime=0
        else:
            self.noburntime+=seconds
            self.i=0
            if self.noburntime>self.maxnoburntime:
                self.burn=True
                self.burntime=0
                self.noburntime=0
        self.image= pygame.transform.rotozoom(Fan.images[self.i], 0 , self.zoom)
        self.rect = self.image.get_rect()
        self.rect.centerx=self.x + x
        self.rect.centery=self.y + y
        
        



    
####

if __name__ == '__main__':

    # call with width of window and fps
    #PygView().paint()
    PygView().run()
