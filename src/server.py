from utils import init_map, send_data, recv_data
from Entities.Player import Player
from Entities.Stone import Stone
from Entities.Bomb import Bomb
import socket, threading, pickle, struct

IP_ADDRESS = "localhost"
PORT = 9999
player_locations = [(32, 32),(992, 32)]

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP_ADDRESS, PORT))
server.listen()
connections = []
players = []
minimap = []
obstacles = []
init_map(minimap, obstacles, "map.txt")

def recv_send_players(client):
    while True:
        index = connections.index(client)
        data = recv_data(client)
        if not data:
            client.close()
            break
        players[index] = pickle.loads(data)
        send_data(client, players)

def accept_connections():
    while True:
        if not len(connections) < 2:
            continue
        client, addr = server.accept()

        client.send(str(len(players)).encode("unicode_escape"))
        player = Player(player_locations[len(players)][0], player_locations[len(players)][1])
        players.append(player)

        # Sending the players, minimap and obstacles to the client
        send_data(client, minimap)
        data = recv_data(client)
        if not data:
            print("No data returned after minimap had sent!")
            client.close()
            break

        send_data(client, obstacles)
        data = recv_data(client)
        if not data:
            print("No data returned after obstacles had sent!")
            client.close()
            break

        send_data(client, players)
        data = recv_data(client)
        if not data:
            print("No data returned after players had sent!")
            client.close()
            break

        connections.append(client)
        threading.Thread(target=recv_send_players, args=(client, )).start()

accept_connections()

server.close()
print("Bye")