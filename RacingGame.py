import pygame, sys, random, time, math
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Racing Game")

screen = pygame.display.set_mode((1700,800))

Player_1 = pygame.image.load("Black viper.png").convert_alpha()
Player_2 = pygame.image.load("Audi.png").convert_alpha()
Homepage = pygame.image.load("Intro screen.jpg")
P1wins = pygame.image.load("Player 1 wins screen.jpg")
P2wins = pygame.image.load("Player 2 wins screen.jpg")

White = (255, 255, 255)
Green = (124, 252, 0)
Black = (0, 0 ,0)
Blue = (0, 191, 225)

class Intro:
    def __init__(self):
        self.x = 0
        self.y = 0

    def draw(self):
        screen.blit(Homepage, (self.x, self.y))

class Player1_wins:
    def __init__(self):
        self.x = 0
        self.y = 0

    def draw(self):
        screen.blit(P1wins, (self.x, self.y))

class Player2_wins:
    def __init__(self):
        self.x = 0
        self.y = 0

    def draw(self):
        screen.blit(P2wins, (self.x, self.y))


class Player_one:
    def __init__(self):
        self.x = 200
        self.y = 675
        self.rot = 0.0
        self.spd = 0.0

    def draw(self):
        Car_1 = pygame.transform.rotate(Player_1, self.rot - 90) # Due to a rotation problem, the image i use needs to be rotated by 90 degrees when it is loaded in so that it correctly roatates and moves around
        Car_1X, Car_1Y = Car_1.get_size() # This gets the size of the image itself and also let me use it later when changing the rotation point of the image, also it means I dont need to manually put in the precise size of the image myself unless i want to
        screen.blit(Car_1, (self.x - (Car_1X /2), self.y - (Car_1Y /2))) # This sets the rotation point of the image at its centre rather than the top left because that made it rotate akwardly

    def update(self):
        if pressed_keys[K_RIGHT]:
            self.rot -= 1 # This is how fast the car will rotate
            self.rot %= 360 # This allows the car to rotate a full 360 degrees and also tells us that 360 degrees is equal to 0 degrees and it can keep rotating

        if pressed_keys[K_LEFT]:
            self.rot += 1
            self.rot %= 360

        if pressed_keys[K_UP] and self.x<1700 and self.x>0 and self.y<800 and self.y>0: # This keeps the car inside the screen
            self.spd = 2 #This is the cars speed
        else:
            self.spd *= -1 # This allows the car to drive again after hitting the border

        if pressed_keys[K_DOWN] and self.x<1700 and self.x>0 and self.y<800 and self.y>0:
            self.spd = -2
        else:
            self.spd *= +1

        # After many attempts on figuring out collsion and running into so, so many problems, I ended up using this very primitive way of collison with the walls, I am truly sorry mariza for causing so many problems and giving up in the end, but I had 2 days left to submit and I was panicking becausing I kept running into so many problems
        # When you collide with a wall you need to reverse first and then carry on driving or the car will just reverse even though you are driving forward until you get away from the wall, also there is no collision if you reverse through a wall, this is because when i tried to do it the car
        # would just start driving backwards if you weren't driving forward, however the game doesnt recognise a checkpoint being driven over if you drive backwards over it, so this helps prevent cheating a little
        if self.spd > 0 and self.x>200 and self.x<230 and self.y>200 and self.y<600:
            self.spd = 0
            #self.x -= 2    ## This was an attempt at making teh car
        else:
            self.spd *= +1

        if self.spd > 0 and self.x>200 and self.x<1450 and self.y>600 and self.y<630:
            self.spd = -1
        else:
            self.spd *= +1

        if self.spd > 0 and self.x>1450 and self.x<1480 and self.y>250 and self.y<630:
            self.spd = -1
        else:
            self.spd *= +1

        if self.spd > 0 and self.x>1200 and self.x<1230 and self.y>0 and self.y<425:
            self.spd = -1
        else:
            self.spd *= +1

        if self.spd > 0 and self.x>820 and self.x<1230 and self.y>425 and self.y<455:
            self.spd = -1
        else:
            self.spd *= +1

        if self.spd > 0 and self.x>600 and self.x<630 and self.y>200 and self.y<600:
            self.spd = -1
        else:
            self.spd *= +1

        if self.spd > 0 and self.x>600 and self.x<975 and self.y>200 and self.y<230:
            self.spd = -1
        else:
            self.spd *= +1

        if self.spd > 0 and self.x>385 and self.x<415 and self.y>0 and self.y<350:
            self.spd = -1
        else:
            self.spd *= +1

    def move(self): #This takes care of rotating my car
        self.x += math.cos(self.rot / 57.2958) * self.spd # Pygame apparently doesn't measure in degrees, when rotating an object, it measures in radians, so to compensate I put in 57.2958 degrees which is equal to one radian and lets the car rotate properly
        self.y -= math.sin(self.rot / 57.2958) * self.spd

    def points(self): #To prevet cheating I have added in checkpoints which the player must drive over before finishing a lap
        global P1lap # I print the variable every time it goes over the checkpoints for play testing purposes

        if pressed_keys[K_UP] and self.x>1000 and self.x<1020 and self.y>450 and self.y<600:
            if P1lap == 0:
                P1lap = 1
                print(P1lap)

        if pressed_keys[K_UP] and self.x>800 and self.x<820 and self.y>0 and self.y<200:
            if P1lap == 1:
                P1lap = 2
                print(P1lap)

        if pressed_keys[K_UP] and self.x>0 and self.x<200 and self.y>600 and self.y<620:
            if P1lap == 2:
                P1lap = 3
                print(P1lap)

class Player_two:
    def __init__(self):
        self.x = 200
        self.y = 725
        self.rot = 0.0
        self.spd = 0.0

    def draw(self):
        Car_2 = pygame.transform.rotate(Player_2, self.rot - 90)
        Car_2X, Car_2Y = Car_2.get_size()
        screen.blit(Car_2, (self.x - (Car_2X /2), self.y - (Car_2Y /2)))

    def update(self):
        if pressed_keys[K_d]:
            self.rot -= 1
            self.rot %= 360

        if pressed_keys[K_a]:
            self.rot += 1
            self.rot %= 360

        if pressed_keys[K_w] and self.x<1700 and self.x>0 and self.y<800 and self.y>0:
            self.spd = 2
        else:
            self.spd *= -1

        if pressed_keys[K_s] and self.x<1700 and self.x>0 and self.y<800 and self.y>0:
            self.spd = -2
        else:
            self.spd *= +1

        if self.spd > 0 and self.x>200 and self.x<230 and self.y>200 and self.y<600:
            self.spd = 0
        else:
            self.spd *= +1

        if self.spd > 0 and self.x>200 and self.x<1450 and self.y>600 and self.y<630:
            self.spd = -1
        else:
            self.spd *= +1

        if self.spd > 0 and self.x>1450 and self.x<1480 and self.y>250 and self.y<630:
            self.spd = -1
        else:
            self.spd *= +1

        if self.spd > 0 and self.x>1200 and self.x<1230 and self.y>0 and self.y<425:
            self.spd = -1
        else:
            self.spd *= +1

        if self.spd > 0 and self.x>820 and self.x<1230 and self.y>425 and self.y<455:
            self.spd = -1
        else:
            self.spd *= +1

        if self.spd > 0 and self.x>600 and self.x<630 and self.y>200 and self.y<600:
            self.spd = -1
        else:
            self.spd *= +1

        if self.spd > 0 and self.x>600 and self.x<975 and self.y>200 and self.y<230:
            self.spd = -1
        else:
            self.spd *= +1

        if self.spd > 0 and self.x>385 and self.x<415 and self.y>0 and self.y<350:
            self.spd = -1
        else:
            self.spd *= +1

    def move(self):
        self.x += math.cos(self.rot / 57.2958) * self.spd
        self.y -= math.sin(self.rot / 57.2958) * self.spd

    def points(self):
        global P2lap

        if pressed_keys[K_w] and self.x>1000 and self.x<1020 and self.y>450 and self.y<600:
            if P2lap == 0:
                P2lap = 1
                print(P2lap)

        if pressed_keys[K_w] and self.x>800 and self.x<820 and self.y>0 and self.y<200:
            if P2lap == 1:
                P2lap = 2
                print(P2lap)

        if pressed_keys[K_w] and self.x>0 and self.x<200 and self.y>600 and self.y<620:
            if P2lap == 2:
                P2lap = 3
                print(P2lap)


Car1 = Player_one()
Car2 = Player_two()

font = pygame.font.SysFont ('comicsans', 30, False)

lap1 = 0
P1lap = 0

lap2 = 0
P2lap = 0

Menu = Intro()

P1_wins = Player1_wins()

P2_wins = Player2_wins()

loop = 1

pressed_keys = pygame.key.get_pressed()

while True:

    while loop == 1:
        pressed_keys = pygame.key.get_pressed()
        Menu.draw()
        if pressed_keys[K_RETURN]:
            loop = 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()

    while loop == 2:
        pressed_keys = pygame.key.get_pressed()
        screen.fill(White)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if P1lap == 3:
            lap1 += 1
            P1lap = 0

        if P2lap == 3:
            lap2 += 1
            P2lap = 0

        P1 = font.render("Player One Laps: " + str(lap1) + "/3", 1, (Black))
        screen.blit(P1, ( 40, 10))
        P2 = font.render("Player Two Laps: " + str(lap2) + "/3", 1, (Black))
        screen.blit(P2, ( 40, 30))

        if lap1 == 3: #Resetting the points
            loop = 3
            lap1 = 0
            P1lap = 0
            lap2 = 0
            P2lap = 0

        if lap2 == 3:
            loop = 4
            lap1 = 0
            P1lap = 0
            lap2 = 0
            P2lap = 0

        pygame.draw.rect(screen, (Black), [1000, 450, 20, 150])
        pygame.draw.rect(screen, (Black), [800, 0, 20, 200])
        pygame.draw.rect(screen, (Blue), [0, 600, 200, 20])

        Car1.update()
        Car1.move()
        Car1.draw()
        Car1.points()

        Car2.update()
        Car2.move()
        Car2.draw()
        Car2.points()

        #These are my walls
        pygame.draw.rect(screen, (Green), [200, 200, 30, 400])
        pygame.draw.rect(screen, (Green), [200, 600, 1250, 30])
        pygame.draw.rect(screen, (Green), [1450, 250, 30, 380])
        pygame.draw.rect(screen, (Green), [1200, 0, 30, 425])
        pygame.draw.rect(screen, (Green), [820, 425, 410, 30])
        pygame.draw.rect(screen, (Green), [600, 200, 30, 400])
        pygame.draw.rect(screen, (Green), [600, 200, 375, 30])
        pygame.draw.rect(screen, (Green), [385, 0, 30, 350])

        pygame.display.update()

    while loop == 3:
        pressed_keys = pygame.key.get_pressed()
        P1_wins.draw()
        if pressed_keys[K_RETURN]:
            loop = 2
            ResPos1 = True
            Car1.__init__()#Resets the positions
            Car2.__init__()

        if pressed_keys[K_ESCAPE]:
            exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()

    while loop == 4:
        pressed_keys = pygame.key.get_pressed()
        P2_wins.draw()
        if pressed_keys[K_RETURN]:
            loop = 2
            Car1.__init__()
            Car2.__init__()

        if pressed_keys[K_ESCAPE]:
            exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        sys.exit()
pressed_keys = pygame.key.get_pressed()

pygame.display.update()
