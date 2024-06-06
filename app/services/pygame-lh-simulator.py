import math
import pygame

def reiniciar_jogo():
    global bola, power, angle, shoot, final, lista_traços
    bola = Bola(100, 1050, 10, ("red"))
    power = 100
    angle = math.radians(90)
    bola.resetar_altura_maxima()
    bola.resetar_tempo_subida()
    bola.resetar_tempo_descida()
    shoot = False
    final = False
    lista_traços = []

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
        self.altura_maxima = self.y
        self.tempo_subida = 0
        self.tempo_descida = 0
        self.tempo_subida_ativo = True

    def desenhar_bola(self, win):
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), self.radius)
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius - 1)

    def resetar_altura_maxima(self):
        self.altura_maxima = self.y

    def resetar_tempo_subida(self):
        self.tempo_subida = 0
        self.tempo_subida_ativo = True

    def resetar_tempo_descida(self):
        self.tempo_descida = 0

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
    text_surface2 = font.render(f"Altura Máxima: {abs(bola.altura_maxima - 1050)}", True, (255, 255, 255))
    text_surface3 = font.render(f"Tempo: {bola.tempo_subida:.2f}s", True, (255, 255, 255))
    text_surface6 = font.render(f"Distancia: {abs(bola.altura_maxima - 1050)*2}", True, (255, 255, 255))
    win.blit(text_surface1, (1000, 10))
    win.blit(text_surface2, (1000, 100))
    win.blit(text_surface3, (1000, 150))
    win.blit(text_surface6, (1000, 200))

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
    force_rect = pygame.Rect(790, 10, 200, 30)
    pygame.draw.rect(win, (255, 255, 255), force_rect, 2)
    force_surface = font.render(force_input, True, (255, 255, 255))
    win.blit(force_surface, (force_rect.x + 5, force_rect.y + 5))
    win.blit(font.render("Digite a velocidade", True, (255, 255, 255)), (500, 10))

def redrawWindow():
    win.fill((0, 0, 0))
    bola.desenhar_bola(win)
    desenhar_grade()
    draw_inputs()
    carregar_informacoes()
    pygame.display.update()

bola = Bola(100, 1050, 10, ("red"))
x = 0
y = 0
time = 0
power = 100
angle = math.radians(90)
shoot = False
final = False
lista_traços = []

while running:
    if shoot:
        if bola.y < 1051 and bola.y > 0 and bola.x < 1801 and bola.x > 99:
            time += 0.05
            po = bola.caminho_da_bola(x, y, power, angle, time)
            lista_traços.append((po[0], po[1]))
            bola.x = po[0]
            bola.y = po[1]
            if bola.y < bola.altura_maxima:
                bola.altura_maxima = bola.y
            if bola.y < 1050 and bola.tempo_subida_ativo:
                bola.tempo_subida += 0.05
            else:
                bola.tempo_subida_ativo = False
            if not bola.tempo_subida_ativo and bola.y > 1050:
                bola.tempo_descida += 0.05
            if bola.y <= 0:
                final = True
                shoot = False
        else:
            final = False
            shoot = False
            bola.x = 100
            bola.y = 1050
            lista_traços = []
    force_rect = pygame.Rect(790, 10, 200, 30)
    mouse_pos = pygame.mouse.get_pos()
    linha = [(bola.x, bola.y), mouse_pos]
    redrawWindow()
    for traco in lista_traços:
        xT, yT = traco
        pygame.draw.circle(win, (255, 255, 255), (xT, yT), 2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if shoot == True:
                active_input = None
                pass
            else:
                if force_rect.collidepoint(event.pos):
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
                    if active_input == "force":
                        print("Força digitada:", force_input)
                        power = float(force_input)
                        bola.resetar_altura_maxima()
                        bola.resetar_tempo_subida()
                        bola.resetar_tempo_descida()
                    force_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    if active_input == "force":
                        force_input = force_input[:-1]
                else:
                    if active_input == "force":
                        force_input += event.unicode
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            reiniciar_jogo()

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
