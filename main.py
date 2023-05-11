import pygame, random


pygame.init()

screen = pygame.display.set_mode((1000, 800))
timer = pygame.time.Clock()

screen.fill((0,0,0))
pygame.display.set_caption("Apple Game")

icon = pygame.image.load("C:/Users/mariu/Desktop/CCC/pygames/redApple.png")
icon = pygame.transform.scale(icon, (32,32))
pygame.display.set_icon(icon)

score_font = pygame.font.Font('freesansbold.ttf', 50)
animation_font = pygame.font.Font('freesansbold.ttf', 30)

animations = {}
toDelete =[]

class cursor_hitbox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1,1))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.newPos = False

    def setPos(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.newPos = True

    def update(self):
        if self.newPos == False:
            self.rect.x = pygame.mouse.get_pos()[0]
            self.rect.y = pygame.mouse.get_pos()[1]
        else:
            self.newPos = False



class goldApple(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('C:/Users/mariu/Desktop/CCC/pygames/goldApple.png')
        self.image.convert()
        self.image = pygame.transform.scale(self.image, (50,50))

        self.rect = self.image.get_rect()

        self.value = +5

    def scoreAnimate(self):
        #self.text = font.render("+"+str(self.value), True, (255,255,255))
        #self.counter = 0
        animations[counter] = {"counter":0,"value":self.value, "pos":[self.rect.x+5, self.rect.y+10], "color":[255,255,255], "angle":20}


class redApple(pygame.sprite.Sprite):
    def __init__(self, pos_x=0, pos_y=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('C:/Users/mariu/Desktop/CCC/pygames/redApple.png')
        self.image.convert()
        self.image = pygame.transform.scale(self.image, (50,50))

        self.rect = self.image.get_rect()

        self.rect.x = pos_x
        self.rect.y = pos_y
        self.value = +1


    def scoreAnimate(self):
        #self.text = font.render("+"+str(self.value), True, (255,255,255))
        #self.counter = 0
        animations[counter] = {"counter":0,"value":self.value, "pos":[self.rect.x+5, self.rect.y+10], "color":[255,255,255], "angle":20}



class bomb(pygame.sprite.Sprite):
    def __init__(self, pos_x=0, pos_y=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('C:/Users/mariu/Desktop/CCC/pygames/bomb0.png')
        self.image.convert()
        self.image = pygame.transform.scale(self.image, (50,50))

        self.rect = self.image.get_rect()

        self.rect.x = pos_x
        self.rect.y = pos_y
        self.value = -3
        self.counter = counter
        self.tempCounter = 0
        self.exploCounter = 500
        self.angle = 20

    def scoreAnimate(self):
        #self.text = font.render("+"+str(self.value), True, (255,255,255))
        #self.counter = 0
        animations[self.counter] = {"counter":0,"value":self.value, "pos":[self.rect.x+5, self.rect.y+10], "color":[255,255,255], "angle":20}

    def update(self):
        if self.exploCounter <= 1:
            cursor.setPos(self.rect.x, self.rect.y)
        
        self.exploCounter -= 1


# initalizes cursor
cursorGroup = pygame.sprite.Group()
cursor = cursor_hitbox()
cursor.add(cursorGroup)



score = 0
 
#fontRender = font.render("Score: 0", True, (255,255,255))


counter=600
apples = pygame.sprite.Group()


#asd = bomb()
#asd.rect.x = 500
#asd.rect.y = 500
#asd.add(apples)





#score = 900



while True:
    #print(score)
    #print(counter)
   # print(animations)

        
    #pygame.display.set_caption("Counter: " + str(counter))

    if counter % (800) == 0: # generates apples
        pos = (random.randint(25,975), random.randint(25,775))
        rand = random.random()
        if rand < 0.1:
            object_ = bomb()
            object_.rect.center = pos
            apples.add(object_)
        
        elif rand > 0.7:
            object_ = goldApple()
            object_.rect.center = pos
            apples.add(object_)
        else:
            object_ = redApple()
            object_.rect.center = pos
            apples.add(object_)
        #counter = 0
    

    #print(cursor.rect.x, cursor.rect.y)

    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            
            pygame.quit()
            quit()


    # checks if cursor is touching an apple
    blocks_hit_list = pygame.sprite.spritecollide(cursor, apples, True)
    
    if blocks_hit_list != []:
        #print(blocks_hit_list[0])
        for i in blocks_hit_list:
            #print(i.value)
            i.scoreAnimate()
            score += i.value


    screen.fill((0,0,0))

    apples.update()
    apples.draw(screen)

    #cursorGroup.draw(screen)
    cursorGroup.update()
    cursorGroup.draw(screen)

    fontRender = score_font.render("Score: "+str(score), True, (255,255,255))
    screen.blit(fontRender, (0,0))


    for i in animations:
        animations[i]["counter"] += 1
        if animations[i]["value"] > 0: 
            text = animation_font.render("+"+str(animations[i]["value"]), True, (animations[i]["color"][0], animations[i]["color"][1], animations[i]["color"][2]))
        else:
            text = animation_font.render(str(animations[i]["value"]), True, (animations[i]["color"][0], animations[i]["color"][1], animations[i]["color"][2]))

        
        
        text = pygame.transform.rotate(text, animations[i]["angle"]-counter)

        if counter % 3 == 0:
            animations[i]["pos"][1] = animations[i]["pos"][1] - 1

        if counter % 7 == 0:
            animations[i]["pos"][0] = animations[i]["pos"][0] + 1

        screen.blit(text, (animations[i]["pos"][0], animations[i]["pos"][1]))
        for x in range(0,3):
            animations[i]["color"][x] = animations[i]["color"][x] - 1.5 
        if animations[i]["counter"] >= 170:
            toDelete.append(i)


    #try:
    #    animations[i]["explodingCounter"]
    #    print("bomb")
    #except:
    #    print("applæe")
    #else:
    #    animations[i]["explodingCounter"] -= 1
    #    print(animations[i]["explodingCounter"])

    for i in toDelete:
        animations.pop(i)
        
    toDelete.clear()    


    pygame.display.update()
    timer.tick(244)
    #print(timer)
    counter += 1