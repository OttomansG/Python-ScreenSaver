import pygame

pygame.init()

boyut = (800, 500)

pencere = pygame.display.set_mode(boyut)

font = pygame.font.SysFont("Monotype Corsiva", 8)

x = 0
y = 0
c = 0
v = 0
t = 0

xYON = 1
yYON = 1
vYON = 1
tYON = 1

clock = pygame.time.Clock()


a = 0
b = 0
sayac1 = 0
sayac2 = 0

sayac = 0

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()


    yazi = font.render(".", 1, (255, 0, 0), (a, c, b))

    if x > 800 - yazi.get_width() or x < 0:
        xYON *= -1

    if y > 500 - yazi.get_height() or y < 0:
        yYON *= -1

    x +=  2 * xYON
    y -=  2 * yYON

    if sayac1 < 255:
        sayac1 += 1
        a += 1
    elif a > 10:
        a -= 1
    else:
        sayac1 = a

    if sayac2 < 255:
        sayac2 += 3
        b += 3
        sayac += 2
    elif b > 10:
        b -= 3
    else:
        sayac2 = b

    c = abs(a - b)



    if sayac > 355:
        clock.tick(180)
        sayac -= 1

        yazi1 = font.render(".", 1, (0, 0, 0), (b, a, c))
        if v > 800 - yazi.get_width() or v < 0:
            vYON *= -1

        if t > 500 - yazi.get_height() or t < 0:
            tYON *= -1

        v += 2 * vYON
        t -= 2 * tYON
        #yazi.fill((c, a, b))
        pencere.blit(yazi1, (v, t))
        pygame.display.update()

    pencere.blit(yazi, (x, y))
    pygame.display.update()




