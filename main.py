import pygame, sys, pymunk


pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

# Created a universe
space = pymunk.Space()

# assgined gravity to the universe
space.gravity = (0.0, 500.0)

appleSurface = pygame.image.load("apple.png")

# created a physical body
def createObject(space, pos):
    # created an atom that cannot interact with other objects, only affected by gravity
    body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
    body.position = pos

    # provided a shape for the non interactive atom allowing it to interact with objects
    shape = pymunk.Circle(body, 65)
    space.add(body, shape)

    return shape


# gave a physical body an image
def drawObject(object):
    for obj in object:
        posX = int(obj.body.position.x)
        posY = int(obj.body.position.y)

        pygame.draw.circle(screen, (0, 0, 0), (posX, posY), 80)


# draw an appl e
def drawApple(object):
    for obj in object:
        posX = int(obj.body.position.x)
        posY = int(obj.body.position.y)

        appleRect = appleSurface.get_rect(center=(posX, posY))
        screen.blit(appleSurface, appleRect)


def createStaticObject(space, pos):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = pos

    shape = pymunk.Circle(body, 40)
    space.add(body, shape)

    return shape


def drawStaticObject(object):
    for obj in object:
        posX = int(obj.body.position.x)
        posY = int(obj.body.position.y)

        pygame.draw.circle(screen, (217, 98, 0), (posX, posY), 50)


object = []

balls = []

balls.append(createStaticObject(space, (400, 400)))
balls.append(createStaticObject(space, (250, 600)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            object.append(createObject(space, event.pos))

    screen.fill((217, 217, 217))
    drawObject(object)
    drawStaticObject(balls)
    space.step(1 / 50.0)
    pygame.display.update()
    clock.tick(120)
