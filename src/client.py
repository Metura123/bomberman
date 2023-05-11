from utils import init_map, draw_pixels
from Entities.Stone import Stone
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

player_id = int(client.recv(64).decode('unicode_escape'))

# Receiving players, minimap and obstacle
to_recv = struct.unpack("I", client.recv(4))
data = client.recv(to_recv[0])
if not data: client.close()
else: players = pickle.loads(data)
if len(players) != 0: client.send("SUCCESS".encode('unicode_escape'))
else: client.close()

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

def send_and_receive_players(players):
    while True:
        to_send = pickle.dumps(players)
        client.send(struct.pack("I",len(to_send)))
        client.send(to_send)

        to_recv = struct.unpack("I", client.recv(4))
        data = client.recv(to_recv[0])

        if not data: client.close()
        else: players[:] = data

def send_and_receive_minimap(minimap):
    while True:
        to_send = pickle.dumps(minimap)
        client.send(struct.pack("I",len(to_send)))
        client.send(to_send)

        to_recv = struct.unpack("I", client.recv(4))
        data = client.recv(to_recv[0])

        if not data: client.close()
        else: minimap[:] = data

while run: 
    clock.tick(60) # Game FPS

    send_and_receive_players(players)
    send_and_receive_minimap(minimap)

    if players[player_id].bomb_timeout != 0:
        players[player_id].bomb_timeout += 1

    WINDOW.fill(GREEN)  # Draw window
    draw_pixels(WINDOW, minimap)
    players[player_id].deploy_bomb(minimap,obstacles)
    players[player_id].move(obstacles)
    for pl in players:
        pl.draw(WINDOW)

    if players[player_id].bomb_timeout == 241:
        players[player_id].bomb_timeout = 0
    
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            client.close()
            run = False
            break

pygame.quit()