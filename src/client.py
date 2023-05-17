from utils import init_map, draw_pixels, send_data, recv_data
from Entities.Stone import Stone
from Entities.Player import Player
from Entities.Bomb import Bomb
import pygame, socket, threading, pickle, struct
pygame.init()

minimap = []
obstacles = []
players = []
init_map(minimap, obstacles, "map.txt")

run = True  # Game Loop
clock = pygame.time.Clock() # Game Clock
GREEN = (0,150,0)

# Multiplayer Socket
IP_ADDRESS = "localhost"
PORT = 9999
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP_ADDRESS, PORT))
# End Multiplayer Socket

player_id = int(client.recv(64).decode("unicode_escape"))

data = recv_data(client)
if not data: client.close()
else:
    players = pickle.loads(data)
    send_data(client, "SUCCESS")

def recv_bomb():
    while True:
        message = client.recv(1).decode('unicode_escape')
        if message == "B":
            data = recv_data(client)
            if not data:
                client.close()
                break

            row, column = pickle.loads(data)
            minimap[row][column] = Bomb(32 * column, 32 * row, row, column)
        else: continue

def send_recv_player(player):
    while True:
        send_data(client, player)
        data = recv_data(client)
        if not data:
            client.close()
            break
        else: 
            received_player_list = pickle.loads(data)
            if len(received_player_list) > len(players): players.append(received_player_list[len(received_player_list) - 1])
            else:
                for index, value in enumerate(received_player_list):
                    if index == player_id:
                        continue

                    players[index] = value

# Pygame Window Initialization
WIDTH, HEIGHT = 1056, 800           # Screen Resolution
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))       # Window Initialization
pygame.display.set_caption("Bomberman")
# End Pygame Window Initialization

threading.Thread(target=send_recv_player,args=(players[player_id],)).start()
# threading.Thread(target=recv_bomb).start()

while run:
    clock.tick(60) # Game FPS

    if players[player_id].bomb_timeout != 0:
        players[player_id].bomb_timeout += 1

    WINDOW.fill(GREEN)  # Draw window
    draw_pixels(WINDOW, minimap)
    change = players[player_id].deploy_bomb(minimap,obstacles)
    if change:
        send_data(client, change)

    players[player_id].move(obstacles)

    for pl in players:
        pl.draw(WINDOW)

    if players[player_id].bomb_timeout == 121:
        players[player_id].bomb_timeout = 0
    
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            client.close()
            run = False
            break

pygame.quit()