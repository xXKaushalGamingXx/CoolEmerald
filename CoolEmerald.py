from pygame import *
window = display.set_mode((700, 500))
display.set_caption("Cool Emnerald")
#class
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w]:
            self.rect.y -= 3
        if keys_pressed[K_s]:
            self.rect.y += 3
        if keys_pressed[K_a]:
            self.rect.x -= 3
        if keys_pressed[K_d]:
            self.rect.x += 3
class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, x1, x2):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.x1 = x1
        self.x2 = x2
        self.direction = "left"
    def updatee(self):
        if self.direction == "left":
            self.rect.x -= 3
        if self.rect.x <= self.x1:
            self.direction = "right"
        if self.direction == "right":
            self.rect.x += 3
        if self.rect.x >= self.x2:
            self.direction = "left"
class Wall(sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        self.color = color
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.image = Surface((self.width, self.height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#objects creation
background = transform.scale(image.load("background.jpg"), (700, 500))
hero = Player("MarioButBetter.png", 30, 410, 2)
shell = Enemy("shell.png", 500, 250, 5, 470, 615)
treasure = GameSprite("MinecraftEmerald.png", 500, 320, 2)
w1 = Wall((2, 48, 32), 100, 20 , 450, 10)
w2 = Wall((2, 48, 32), 100, 480, 350, 10)
w3 = Wall((2, 48, 32), 100, 20 , 10, 380)
w4 = Wall((2, 48, 32), 200, 130, 10, 350)
w5 = Wall((2, 48, 32), 450, 130, 10, 360)
w6 = Wall((2, 48, 32), 300, 20, 10, 350)
w7 = Wall((2, 48, 32), 390, 120, 130, 10)
walls = [w1, w2, w3, w4, w5, w6, w7]

#fps controls
clock = time.Clock()
FPS = 60
#gameloop
game = True
end = False
while game:
    keys_pressed = key.get_pressed()
    window.blit(background,(0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not end:
        hero.reset()
        hero.update()
        shell.reset()
        shell.updatee()
        treasure.reset()
        for wall in walls:
            wall.draw_wall()
            if sprite.collide_rect(hero, wall):
                end = True
        if sprite.collide_rect(hero, shell):
            end = True
        if sprite.collide_rect(hero,treasure):
            end = True
        
    clock.tick(FPS)
    display.update()





#fps controls
clock = time.Clock()
FPS = 60
#gameloop
game = True
end = False
while game:
    keys_pressed = key.get_pressed()
    window.blit(background,(0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    clock.tick(FPS)
    display.update()
