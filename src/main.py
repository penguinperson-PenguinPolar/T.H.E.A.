import pygame, sys, math
from random import randint

window = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

def sigmoid(x):
    return 1/(1+math.exp(-x)) 

def Neron(inputs, weights, bias):
    total = 0
    for i in range(len(inputs)):
        total += inputs[i]*weights[i]
    return hex(sigmoid(total+bias))

x, y = 30, 560
Lbias = randint(0, 100)
Lweights = [randint(0, 100), randint(0, 100)]
Rbias = randint(0, 100)
Rweights = [randint(0, 100), randint(0, 100)]
Ubias = randint(0, 100)
Uweights = [randint(0, 100), randint(0, 100)]
Dbias = randint(0, 100)
Dweights = [randint(0, 100), randint(0, 100)]

while True:
    window.fill((255, 255, 255))
    clock.tick(0)
    pygame.draw.rect(window, (0, 0, 0), pygame.rect.Rect(x, y, 20, 20))
    pygame.draw.rect(window, (0, 0, 0), pygame.rect.Rect(60, 60, 680, 480))
    if pygame.Rect.colliderect(pygame.rect.Rect(x, y, 20, 20), pygame.rect.Rect(60, 60, 680, 480)) or x<=0 or y<=0 or x>=780 or y>=580 or pygame.mouse.get_pressed()[0] == True:
        x, y = 30, 560
        Lbias = randint(0, 100)
        Lweights = [randint(0, 100), randint(0, 100)]
        Rbias = randint(0, 100)
        Rweights = [randint(0, 100), randint(0, 100)]
        Ubias = randint(0, 100)
        Uweights = [randint(0, 100), randint(0, 100)]
        Dbias = randint(0, 100)
        Dweights = [randint(0, 100), randint(0, 100)]
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x-=1
    if keys[pygame.K_RIGHT]:
        x+=1
    if keys[pygame.K_UP]:
        y-=1
    if keys[pygame.K_DOWN]:
        y+=1
    L = Neron([x, y], Lweights, Lbias)
    R = Neron([x, y], Rweights, Rbias)
    U = Neron([x, y], Uweights, Ubias)
    D = Neron([x, y], Dweights, Dbias)
    if L>R and L>U and L>D:
        x -= 1
    if R>L and R>U and R>D:
        x += 1
    if U>L and U>R and U>D:
        y -= 1
    if D>L and D>R and D>U:
        y += 1
    if pygame.mouse.get_pressed()[1] == True:
        print(f"Left:\nBias: {Lbias}, Weights: {Lweights}")
        print(f"Right:\nBias: {Rbias}, Weights: {Rweights}")
        print(f"Up:\nBias: {Ubias}, Weights: {Uweights}")
        print(f"Down:\nBias: {Dbias}, Weights: {Dweights}")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
