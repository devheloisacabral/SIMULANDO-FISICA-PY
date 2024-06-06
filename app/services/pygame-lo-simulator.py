import math
import pygame

# pygame setup
pygame.init()
largura, altura = 1900, 1300
win = pygame.display.set_mode((largura, altura))
font = pygame.font.SysFont(None, 36)
block_size = 50
clock = pygame.time.Clock()
running = True
global angle_input, force_input, active_input
angle_input = ""
force_input = ""
active_input = None


class Bola(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def desenhar_bola(self, win):
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), self.radius)
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius - 1)

    @staticmethod
    def caminho_da_bola(startx, starty, power, angle, time):
        velx = math.cos(angle) * power
        vely = math.sin(angle) * power
        dist_x = velx * time
        dist_y = (vely * time) + ((-9.8 * (time**2)) / 2)
        new_x = round(dist_x + startx)
        new_y = round(starty - dist_y)
        return (new_x, new_y)


def carregar_informacoes():
    text_surface1 = font.render(f"Velocidade: {power}m/s", True, (255, 255, 255))
    text_surface2 = font.render(f"Angulo: {math.degrees(angle)}º", True, (255, 255, 255))
    text_surface4 = font.render(f"Distancia: {bola.x-100}", True, (255, 255, 255))
    win.blit(text_surface1, (1000, 10))
    win.blit(text_surface2, (1000, 50))
    win.blit(text_surface4, (1000, 130))


def desenhar_grade():
    numeros_verticais = []
    numeros_horizontais = []
    for i in range(100, 1800, 100):
        numeros_horizontais.append((font.render(str(i-100), True, (255, 255, 255)), (i, 1050)))
    for i in numeros_horizontais:
        win.blit(i[0], i[1])
    for i in range(50, 1100, 100):
        numeros_verticais.append((font.render(str((i-1050)*-1), True, (255, 255, 255)), (100, i)))
    for i in numeros_verticais:
        win.blit(i[0], i[1])
    pygame.draw.line(win, (255, 255, 255), (100, 1050), (100, 0), 2)
    pygame.draw.line(win, (255, 255, 255), (100, 1050), (1800, 1050), 2)


def draw_inputs():
    angle_rect = pygame.Rect(790, 50, 200, 30)
    force_rect = pygame.Rect(790, 10, 200, 30)

    pygame.draw.rect(win, (255, 255, 255), angle_rect, 2)
    pygame.draw.rect(win, (255, 255, 255), force_rect, 2)

    angle_surface = font.render(angle_input, True, (255, 255, 255))
    force_surface = font.render(force_input, True, (255, 255, 255))

    win.blit(angle_surface, (angle_rect.x + 5, angle_rect.y + 5))
    win.blit(font.render("Digite o angulo", True, (255, 255, 255)), (500, 50))
    win.blit(force_surface, (force_rect.x + 5, force_rect.y + 5))
    win.blit(font.render("Digite a velocidade", True, (255, 255, 255)), (500, 10))


def redrawWindow():
    win.fill((0, 0, 0))
    bola.desenhar_bola(win)
    # pygame.draw.line(win, ("white"), linha[0], linha[1])
    desenhar_grade()
    draw_inputs()
    carregar_informacoes()
    pygame.display.update()


bola = Bola(100, 1050, 10, ("red"))
x = 0
y = 0
time = 0
power = 100
angle = math.radians(45)
shoot = False
final = False
lista_traços = []

while running:
    if shoot:
        if bola.y < 1051 and bola.y > 0 and bola.x < 1801 and bola.x > 99:
            time += 0.05
            po = bola.caminho_da_bola(x, y, power, angle, time)
            # print(po[0], po[1])
            lista_traços.append((po[0], po[1]))
            bola.x = po[0]
            bola.y = po[1]
            if bola.y >= 1051 or bola.y <= 0 or bola.x >= 1801 or bola.x <= 99:
                final = True
                shoot = False
            print(final)
        else:
            final = False
            shoot = False
            bola.x = 100
            bola.y = 1050
            lista_traços = []
    angle_rect = pygame.Rect(790, 50, 200, 30)
    force_rect = pygame.Rect(790, 10, 200, 30)
    mouse_pos = pygame.mouse.get_pos()
    linha = [(bola.x, bola.y), mouse_pos]
    redrawWindow()
    # print(lista_traços)
    for traco in lista_traços:
        xT, yT = traco
        pygame.draw.circle(win, (255, 255, 255), (xT, yT), 2)
        # print(f"x = {traco[0]} | y = {traco[1]}")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if shoot == True:
                active_input = None
                pass
            else:
                if angle_rect.collidepoint(event.pos):
                    active_input = "angle"
                elif force_rect.collidepoint(event.pos):
                    active_input = "force"
                elif final == True:
                    shoot = True
                elif shoot == False:
                    shoot = True
                    x = bola.x
                    y = bola.y
                    time = 0
                    active_input = None
        elif event.type == pygame.KEYDOWN:
            if active_input:
                if event.key == pygame.K_RETURN:
                    if active_input == "angle":
                        print("Ângulo digitado:", angle_input)
                        angle = math.radians(float(angle_input))
                    elif active_input == "force":
                        print("Força digitada:", force_input)
                        power = float(force_input)
                    angle_input = ""
                    force_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    if active_input == "angle":
                        angle_input = angle_input[:-1]
                    elif active_input == "force":
                        force_input = force_input[:-1]
                else:
                    if active_input == "angle":
                        angle_input += event.unicode
                    elif active_input == "force":
                        force_input += event.unicode

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()