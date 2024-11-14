from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('Vampiresurvivor/images/player/down/0.png').convert_alpha()
        self.rect = self.image.get_rect(center = pos)

        self.direction = pygame.math.Vector2(0,0)
        self.speed = 5

    def input(self):
        keys = pygame.key.get_pressed()

        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        #self.direction = self.direction.normalize()
    def move(self, dt):
        self.rect.center = self.direction * self.speed * dt

    def update(self, dt):
        self.input()
        self.move(dt)
