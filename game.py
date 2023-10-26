import pyxel as px
import music

CHAO_Y = 50
TAMANHO_TELA_X = 200
TAMANHO_TELA_Y = 100

# Posição da camera do jogo
camera_x = 0

# Variaveis para o mario
direita = [32, 60, 0, 32]
quadro = 2
estado = 'direita'

#variavei do mario
y = CHAO_Y
x = 50

# variaveis para o pulo do Mario
pulando = False
pulo_inicial_y = 0
pulo_duracao = 25
pulo_tempo = 2
gravidade = 5

obstaculos = [
    # coluna 1
    (200, CHAO_Y - 8, 8, 8),
    (208, CHAO_Y - 8, 8, 8),
    (216, CHAO_Y - 8, 8, 8),

    # coluna 2
    (300, CHAO_Y - 8, 8, 8),
    (308, CHAO_Y - 8, 8, 8),
    (316, CHAO_Y - 8, 8, 8),

    # coluna 3
    (376, CHAO_Y - 8, 8, 8),
    (384, CHAO_Y - 8, 8, 8),
    (392, CHAO_Y - 8, 8, 8),
    (400, CHAO_Y - 8, 8, 8),
    (408, CHAO_Y - 8, 8, 8),
    (416, CHAO_Y - 8, 8, 8),
    (424, CHAO_Y - 8, 8, 8),

    # escada
    (484, 64, 8, 8),
    (492, 56, 8, 8),
    (500, 48, 8, 8),
    (508, 40, 8, 8),
    
    # saltos
    (560, 40, 8, 8),
    (620, 40, 8, 8),
    (670, 40, 8, 8),
    
    (710, 40, 8, 8),
    (720, 15, 8, 8),
    
    #plataforma oculta
    (730, -15, 8, 8),
    (738, -15, 8, 8),
    (746, -15, 8, 8),
    (754, -15, 8, 8),
    (762, -15, 8, 8),
    (770, -15, 8, 8),
    (778, -15, 8, 8),
    (786, -15, 8, 8),
    
    #escada
    (768, 40, 8, 8),
    (776, 48, 8, 8),
    (784, 56, 8, 8),
    
    #alto
    (856, 20, 8, 8),
    (864, 20, 8, 8),
    (872, 20, 8, 8),
    (880, 20, 8, 8),
    (888, 20, 8, 8),
    (896, 20, 8, 8),
    (904, 20, 8, 8),
    (912, 20, 8, 8),
    (920, 20, 8, 8),
    (928, 20, 8, 8),
    (936, 20, 8, 8),
    (944, 20, 8, 8),
    (952, 20, 8, 8),
    (960, 20, 8, 8),
    (968, 20, 8, 8),
    (976, 20, 8, 8),
    (984, 20, 8, 8),
    (992, 20, 8, 8),
    (1000, 20, 8, 8),
    (1008, 20, 8, 8),
    (1016, 20, 8, 8),
    (1024, 20, 8, 8),
    (1032, 20, 8, 8),
    (1040, 20, 8, 8),
    (1048, 20, 8, 8),
    (1056, 20, 8, 8),
    (1064, 20, 8, 8),
    (1072, 20, 8, 8),
    (1080, 20, 8, 8),
    (1088, 20, 8, 8),
    (1096, 20, 8, 8),
    (1104, 20, 8, 8),
    (1112, 20, 8, 8),
    (1120, 20, 8, 8),
    (1128, 20, 8, 8),
    (1136, 20, 8, 8),
    (1144, 20, 8, 8),
    (1152, 20, 8, 8),
    (1160, 20, 8, 8),
    (1168, 20, 8, 8),
    (1176, 20, 8, 8),
    (1184, 20, 8, 8),
    (1192, 20, 8, 8),
    (1200, 20, 8, 8),
    
    #plataforma
    (1208, 44, 8, 8),
    (1216, 44, 8, 8),
    (1224, 44, 8, 8),
    (1232, 44, 8, 8),
    (1240, 44, 8, 8),
    (1248, 44, 8, 8),
    
    (1300, 38, 8, 8),
    (1308, 38, 8, 8),
    (1316, 38, 8, 8),
    
    (1348, 34, 8, 8),
    (1356, 34, 8, 8),
    (1364, 34, 8, 8),
    (1372, 34, 8, 8),
    (1380, 34, 8, 8),
    
    (1458, 30, 8, 8),
    (1466, 30, 8, 8),
    (1474, 30, 8, 8),
    (1482, 30, 8, 8),
    (1490, 30, 8, 8),
    
    #fim
    (1800, 30, 8, 8),
    (1800, 22, 8, 8),
]

# Animação da fogueira
frame1 = [8, 24, 8, 8]
frame2 = [0, 24, 8, 8]
current_frame = 1  # começa com frame 1

retangulos = [(0, CHAO_Y + 15, TAMANHO_TELA_X, 50)]  # Retangulo do chão.

# "Fogueira"
fogueiras = [
    (412, 60, 8, 8),
    (420, 60, 8, 8),
    (526, 60, 8, 8),
    (532, 60, 8, 8),
    (540, 60, 8, 8),
    (548, 60, 8, 8),
    (556, 60, 8, 8),
    (564, 60, 8, 8),
    (572, 60, 8, 8),
    (580, 60, 8, 8),
    (588, 60, 8, 8),
    (596, 60, 8, 8),
    (604, 60, 8, 8),
    (612, 60, 8, 8),
    (620, 60, 8, 8),
    (628, 60, 8, 8),
    (636, 60, 8, 8),
    (644, 60, 8, 8),
    (652, 60, 8, 8),
    (660, 60, 8, 8),
    (668, 60, 8, 8),
    (676, 60, 8, 8),
    (684, 60, 8, 8),
    (692, 60, 8, 8),
    (700, 60, 8, 8),
    (708, 60, 8, 8),
    (716, 60, 8, 8),
    (724, 60, 8, 8),
    (732, 60, 8, 8),
    (740, 60, 8, 8),
    (748, 60, 8, 8),
    (756, 60, 8, 8),
    (764, 60, 8, 8),
    
    (1300, 60, 8, 8),
    (1340, 60, 8, 8),
    (1380, 60, 8, 8),
    (1420, 60, 8, 8),
    (1460, 60, 8, 8),
]


# Enemy class
class Enemy:
    def __init__(self, x, y, speed, sprite_coords):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = 1
        self.distance_walked = 0
        self.frame = 0
        self.sprite_coords = sprite_coords
        self.stone_cooldown = 0  # Cooldown for stone throwing

    def move(self):
        self.x += self.speed * self.direction
        self.distance_walked += abs(self.speed)

        if self.distance_walked >= 50:
            self.direction *= -1
            self.distance_walked = 0

    def update_frame(self):
        if px.frame_count % 5 == 0:
            self.frame = (self.frame + 1) % len(self.sprite_coords)

    def get_sprite_params(self):
        if self.direction == -1:
            return (
                self.x - camera_x,  # ajustado em funcao da camerax
                self.y,
                0,
                self.sprite_coords[self.frame],
                36,  # Y coordinate of the sprite when moving left
                14,  # Width of the sprite
                18,  # Height of the sprite
                7,  # Palette color
            )
        else:
            return (
                self.x - camera_x,  # Adjust for camera_x
                self.y,
                0,
                self.sprite_coords[self.frame],
                54,  # Y coordinate of the sprite when moving right
                14,  # Width of the sprite
                18,  # Height of the sprite
                7,  # Palette color
            )

    def throw_stone(self):
        if self.stone_cooldown == 0:
            new_stone = Stone(self.x - camera_x, self.y + 10, -1, [80])  # Adjust the speed to -1 for leftward motion
            new_stone.thrown = True
            stones.append(new_stone)
            self.stone_cooldown = 60  # Set a cooldown of 60 frames (adjust as needed)
        else:
            self.stone_cooldown -= 1
    
    def collides_with_player(self, player_x, player_y, camera_x):
        if (
            (self.x - camera_x + 14 > player_x and self.x - camera_x < player_x + 20 and self.y + 14 > player_y and self.y < player_y + 16)
        ):
            return True
        return False

class Stone:
    def __init__(self, x, y, speed, sprite_coords):
        self.x = x
        self.y = y
        self.speed = -2.5
        self.sprite_coords = sprite_coords
        self.thrown = False

    def move(self):
        # Limit stone movement to the left to 200 pixels
        if self.x - camera_x < enemy.x - 200:
            self.x += self.speed
        else:
            # Remove the stone when it reaches the limit
            stones.remove(self)

enemies = [] # Criei uma lista para lidar com a lógica de um geito mais prático
# Criar inimigos
enemy = Enemy(376, CHAO_Y - 25, 1, [42, 28, 14, 0])
enemy33 = Enemy(1200, CHAO_Y - 22, 0.5, [42, 28, 14, 0])
enemies.append(enemy)
enemies.append(enemy33)

stones = []

class Enemy2:
    def __init__(self, x2, y2, speed2, sprite_coords2):
        self.x2 = x2
        self.y2 = y2
        self.speed2 = speed2
        self.direction = 1
        self.distance_walked = 0
        self.frame = 0
        self.sprite_coords = sprite_coords2

    def move(self):
        self.x2 -= self.speed2 * self.direction
        self.distance_walked += abs(self.speed2)

    def update_frame(self):
        if px.frame_count % 5 == 0:
            self.frame = (self.frame + 1) % len(self.sprite_coords)

    def get_sprite_params(self):
        y_coord = 0  # Changed to y = 0
        return (
            self.x2 - camera_x, self.y2, 0, self.sprite_coords[self.frame],
            y_coord, 14, 18, 7
        )
    
    def collides_with_player(self, player_x, player_y, camera_x):
        if (
            (self.x2 - camera_x + 14 > player_x and self.x2 - camera_x < player_x + 20 and self.y2 + 14 > player_y and self.y2 < player_y + 16)
        ):
            return True
        return False

class Enemy3:
    def __init__(self, x3, y3, speed3, sprite_coords3):
        self.x3 = x3
        self.y3 = y3
        self.speed3 = speed3
        self.direction = 1
        self.distance_walked = 0
        self.frame = 0
        self.sprite_coords = sprite_coords3

    def move(self):
        self.x3 -= self.speed3 * self.direction
        self.distance_walked += abs(self.speed3)

    def update_frame(self):
        if px.frame_count % 5 == 0:
            self.frame = (self.frame + 1) % len(self.sprite_coords)

    def get_sprite_params(self):
        y_coord = 0  
        return (
            self.x3 - camera_x, self.y3, 1, self.sprite_coords[self.frame],
            y_coord, -50, 120, 7
        )
    
chefao = None
    
#criar chefao
def criar_chefao():
    global chefao
    if camera_x >= 1700 and chefao is None:
        chefao = Enemy3(1900, CHAO_Y -15, 1, [100, 0, 50, 0])

enemies2 = []
# Ciar inimigos2013
enemy22 = Enemy2(180, 50, 1, [42, 28, 14, 0])
enemy23 = Enemy2(380, 50, 1, [42, 28, 14, 0])
enemies2.append(enemy22)
enemies2.append(enemy23)

enemy5 = None
enemy6 = None

def criarInimigos():
    global enemy5, enemy6
    if camera_x >= 700 and enemy5 is None:
        enemy5 = Enemy2(1000, 50, 1, [42, 28, 14, 0])
        enemy6 = Enemy2(1200, 50, 1, [42, 28, 14, 0])
        enemies.append(enemy5)
        enemies2.append(enemy6)



class Princess:
    def __init__(self, x4, y4):
        self.x4 = x4
        self.y4 = y4
        self.frame = 0

    def update(self):
        # Alterne entre os frames para criar uma animação
        self.frame = (self.frame + 1) % 8

    def draw(self):
        # Desenhe o frame atual da princesa
        px.blt(self.x4 - camera_x, self.y4, 2, 64 + self.frame * 8, 17, 8, 8, 0)

# Crie uma instância da princesa
princess = Princess(1900, 58)

# Frame for fogueira
frame_fogueira = 1

vidas = 3

em_contato_com_obstaculo = False

#Criei uma variavel para saber se o Mario está em cima da plataforma
altura_no_obstaculo = None

def verificar_colisao():
    global x, y, pulando, vidas, altura_no_obstaculo
    
    # Verifique colisão com obstáculos e plataformas
    for obstaculo in obstaculos:
        if (
            x + 18 > obstaculo[0] - camera_x and
            8+x < obstaculo[0] + obstaculo[2] - camera_x and
            y + 18.6 > obstaculo[1] and
            y < obstaculo[1] + obstaculo[3]
        ):
            # Verifique a colisão pela parte superior do obstáculo
            if y + 18.6 <= obstaculo[1] + gravidade:
                y = obstaculo[1] - 18.6
                altura_no_obstaculo = y
                pulando = False

    # Colisão com inimigo1
    for enemy in enemies:
        if enemy.collides_with_player(x, y, camera_x):
            vidas -= 1
            if vidas == 0:
                estado = 'game_over'
            else:
                x = 50
                y = CHAO_Y

    # Colisão com inimigo2
    for enemy2 in enemies2:
        if enemy2.collides_with_player(x, y, camera_x):
            vidas -= 1
            if vidas == 0:
                estado = 'game_over'
            else:
                x = 50
                y = CHAO_Y
            
    # Colisão com chefao
    if chefao != None:
        if (
            (x + 8 > chefao.x3 - camera_x and x < chefao.x3 + 8 - camera_x and y + 12 > chefao.y3 and y < chefao.x3 + 10)
        ):
            vidas = 0
            if vidas == 0:
                estado = 'game_over'
            else:
                x = 50
                y = CHAO_Y

    # Colisão com pedras do inimigo
    for stone in stones:
        if (
            x + 25 > stone.x and
            x < stone.x + 8 and
            y + 17 > stone.y and
            y < stone.y + 8
        ):
            # se foi atingido remove a pedra
            stones.remove(stone)
            # Mario perde uma vida
            vidas -= 1
            if vidas == 0:
                estado = 'game_over'
            else:
                x = 50
                y = CHAO_Y
                
     # colisão com fogueiras
    for fogueira in fogueiras:
        if (
            x + 20 > fogueira[0] - camera_x and
            x < fogueira[0] + fogueira[2] - camera_x-5 and
            y + 17 > fogueira[1] and
            y < fogueira[1] + fogueira[3]
        ):
            # se colide
            vidas = 0  

    if camera_x == 1826:
        vidas = 4

def atualizar():
    global estado, quadro, x, y, pulando, pulo_inicial_y, pulo_tempo
    global camera_x, pontuacao
    global em_contato_com_obstaculo, pode_pular
    global current_frame, frame_fogueira
    
    princess.update()

    verificar_colisao()
    criarInimigos()
    criar_chefao()
    # Muda os frames da fogueira a cada 10 frames
    if px.frame_count % 5 == 0:
        frame_fogueira = 2 if frame_fogueira == 1 else 1

    # Primeiro mago logica
    enemy.move()
    enemy.update_frame()
    enemy.throw_stone()

   
    # Andarilho
    enemy22.move()
    enemy22.update_frame()
    
    # Andarilho2
    enemy23.move()
    enemy23.update_frame()
    
    if enemy5 != None:
        # Andarilho3
        enemy5.move()
        enemy5.update_frame()
    if enemy6 != None:
        # Andarilho4
        enemy6.move()
        enemy6.update_frame()
        
    #mago2
    enemy33.move()
    enemy33.update_frame()
    enemy33.throw_stone() 
    
    #chefao
    if chefao != None:
        chefao.move()
        chefao.update_frame()
    
    # logica para mover as pedras
    for stone in stones:
        stone.move()
        if stone.x < -camera_x:
            stones.remove(stone)

    if px.btnp(px.KEY_ESCAPE):
        px.quit()

    if px.btn(px.KEY_SPACE) and not pulando and ((y == altura_no_obstaculo) or (y == CHAO_Y)):
        
        pulando = True
        pulo_tempo = pulo_duracao
        pulo_inicial_y = y

    if pulando:
        y = pulo_inicial_y - int(pulo_tempo / pulo_duracao * 40)
        pulo_tempo -= 1
        if pulo_tempo == 0:
            pulando = False

    if y < CHAO_Y:
        y += gravidade
    else:
        y = CHAO_Y
        pode_pular = True

    #Mover Mario
    if px.btn(px.KEY_RIGHT):
        estado = 'direita'
        x += 2
        quadro = (quadro + 1) % 4
        if x > TAMANHO_TELA_X - 150:
            x = TAMANHO_TELA_X - 150
            camera_x += 2
        elif x > 50:
            camera_x += 2

    if px.btn(px.KEY_LEFT):
        estado = 'esquerda'
        x -= 2
        quadro = (quadro + 1) % 4
        if x < 0:
            x = 0
        elif x < 50:
            camera_x -= 2

def desenhar():
    global camera_x, estado

    px.cls(6)  # Limpar tela
    
    princess.draw()
    
    px.blt(1880 - camera_x, 58, 2, 16, 24, 8, 8, 0)#chave

    # cadeia
    px.blt(1908 - camera_x, 58 , 2, 80, 24, 8, 8, 7)
    px.blt(1908 - camera_x, 50 , 2, 80, 24, 8, 8, 7)
    px.blt(1900 - camera_x, 50 , 2, 80, 24, 8, 8, 7)
    px.blt(1892 - camera_x, 50 , 2, 80, 24, 8, 8, 7)
    px.blt(1892 - camera_x, 58 , 2, 80, 24, 8, 8, 7)
    px.blt(1916 - camera_x, 58, 2, 64, 24, 8, 8, 0)
    px.blt(1900 - camera_x, 58, 2, 72, 24, 8, 8, 0)    #grades
   
   #Aqui é a logica principal do jogo 
    if vidas == 1 or vidas == 2 or vidas == 3:
        
        for retangulo in retangulos: #chão
            px.rect(retangulo[0], retangulo[1], retangulo[2], retangulo[3], 11)

        # Obstaculos
        for obstaculo in obstaculos:
            px.blt(obstaculo[0] - camera_x, obstaculo[1], 2, 64, 112, obstaculo[2], obstaculo[3], 7)
            
        # Desenhar Mario
        if estado == 'direita':
            if pulando:
                px.blt(x, y, 2, 154, 0, 32, 16, 15)
            else:
                px.blt(x, y, 2, direita[quadro], 0, 25, 17, 15)
        elif estado == 'esquerda':
            if pulando:
                px.blt(x-10 , y, 2, 154, 0, -32, 16, 15)
            else:
                px.blt(x, y, 2, direita[quadro], 0, -25, 17, 15)
                
        # Desenhar corações
        for i in range(vidas):
            px.blt(8 + i * 10, 4, 2, 104, 88, 8, 8, 0) 
        
        # Desenhar "fogueiras" alternando entre os frames
        for fogueira in fogueiras:
            if frame_fogueira == 1:
                px.blt(fogueira[0] - camera_x, fogueira[1], 2, *frame1, 0)
            else:
                px.blt(fogueira[0] - camera_x, fogueira[1], 2, *frame2, 0)

        # Inimigos
        px.blt(*enemy33.get_sprite_params())
        px.blt(*enemy23.get_sprite_params())
        
        #condicoes para criar os inimigos
        if enemy.x - camera_x >= 0:
            px.blt(*enemy.get_sprite_params())
        if enemy22.x2 - camera_x >= 0:
            px.blt(*enemy22.get_sprite_params())
        if enemy5 != None:
            px.blt(*enemy5.get_sprite_params())
        if enemy6 != None:
            px.blt(*enemy6.get_sprite_params())
        if chefao != None:
            px.blt(*chefao.get_sprite_params())

        # Desenhar pedras
        for stone in stones:
            px.blt(
                stone.x, stone.y, 2, 16, 32, 8, 8, 0)

        #Cano de salto
        px.blt(1800 - camera_x, 30, 2, 0, 120, 8, 8, 0)
        px.blt(1800 - camera_x, 22, 2, 0, 104, 8, 8, 0)
        
    elif vidas == 4:
            px.cls(7)  
            px.text(85,45,"VOCE VENCEU",10)
            
    else:
        px.cls(0)        
        px.text(85,45,"GAME OVER",12)
        
        
# Inicialização
px.init(TAMANHO_TELA_X, TAMANHO_TELA_Y, title='Mario Game', fps=30)
px.load("PYXEL_RESOURCE_FILE.pyxres")

px.run(atualizar, desenhar)
