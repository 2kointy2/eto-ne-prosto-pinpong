from pygame import *


window = display.set_mode((500, 500))
bg = image.load('background.jpg')
bg = transform.scale(bg, (500, 500))
window.blit(bg, (0, 0))
clock = time.Clock()


class GameSprite(sprite.Sprite):
    def __init__(self, filename, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(filename), (65, 65))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Enemy(GameSprite):
    def update(self):
        self.rect.x += self.speed

        if self.rect.x > 450 or self.rect.x < 300:
            self.speed *= -1


class Wall(sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.color = color
        self.height = height
        self.width = width

        self.image = Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        Wall.add(self)

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        

class Player(GameSprite):
    def update(self):
        pressed = key.get_pressed()
        if pressed[K_d]:
            player.rect.x += player.speed
        elif pressed[K_a]:
            player.rect.x -= player.speed

        if pressed[K_s]:
            player.rect.y += player.speed
        elif pressed[K_w]:
            player.rect.y -= player.speed
player = Player('hero.png', 100, 100, 4)

wall1 = Wall(100, 100, 100, 20, (200, 255, 255))

hero = Player('hero.png', 20, 20, 5)
wall1 = Wall(100, 100, 100, 20, (200, 255, 255))
wall2 = Wall(200, 200, 100, 20, (200, 255, 255))
wall3 = Wall(300, 300, 100, 20, (200, 255, 255))
enemy1 = Enemy('cyborg.png', 400, 100, 3)

treasure = GameSprite('treasure.png', 400, 400, 0)

game = True
while game:
    window.blit(bg, (0, 0))

    wall1.draw(window)

    treasure.reset()

    player.reset()
    player.update()
    if sprite.collide_rect(hero, treasure):
        print('You win')
        game = False

    if sprite.spritecollide(hero, wall1, False):
        print('You lose')
        game = False

    enemy1.reset()
    enemy1.update()

    wall1.reset()

    for e in event.get():
        if e.type == QUIT:
            quit()

    display.update()
    clock.tick(40)
    