from utils import init_map, draw_pixels
from Entities.Stone import Stone
from Entities.Bomb import Bomb
from Entities.Player import Player
import pygame, socket, threading, pickle, struct
pygame.init()

minimap = []
obstacles = []
players = []
run = True  # Game Loop
clock = pygame.time.Clock() # Game Clock
GREEN = (0,150,0)

# Multiplayer Socket
IP_ADDRESS = "localhost"
PORT = 9999
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP_ADDRESS, PORT))
# End Multiplayer Socket

player = Player(32, 32)
players.append(player)
client.send(pickle.dumps(player)) # Send player to server

# Receiving minimap and obstacle
to_recv = struct.unpack("I", client.recv(4))
data = client.recv(to_recv[0])
if not data: client.close()
else: minimap = pickle.loads(data)
if len(minimap) != 0: client.send("SUCCESS".encode('unicode_escape'))
else: client.close()

to_recv = struct.unpack("I", client.recv(4))
data = client.recv(to_recv[0])
if not data: client.close()
else: obstacles = pickle.loads(data) 
if len(obstacles) != 0: client.send("SUCCESS".encode('unicode_escape'))
else: client.close()

# Pygame Window Initialization
WIDTH, HEIGHT = 1056, 800           # Screen Resolution
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))       # Window Initialization
pygame.display.set_caption("Bomberman")
# End Pygame Window Initialization

while run: 
    clock.tick(60) # Game FPS
    WINDOW.fill(GREEN)  # Draw window
    draw_pixels(WINDOW, minimap)
    player.move(obstacles)
    for pl in players:
        pl.draw(WINDOW)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            client.close()
            run = False
            break

pygame.quit()