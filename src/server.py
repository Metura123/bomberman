from utils import init_map
from Entities.Player import Player
from Entities.Stone import Stone
from Entities.Bomb import Bomb
import socket, threading, pickle, struct
IP_ADDRESS = "localhost"
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP_ADDRESS, PORT))
server.listen()
connections = []
players = []
minimap = []
obstacles = []
init_map(minimap, obstacles, "map.txt")

def accept_connections():
    while True:
        if not len(connections) < 2:
            continue
        client, addr = server.accept()

        # Receiving the player object of the created player
        player = pickle.loads(client.recv(4096))
        if not player:
            print("An unexpected error occured!")
            client.close()
            break
        else:
            print("Player has added successfully!")
            players.append(player)

        # Sending the minimap and obstacles to the client
        to_send = pickle.dumps(minimap)
        client.send(struct.pack("I",len(to_send)))
        client.send(to_send)
        print("OK!")
        data = client.recv(128).decode('unicode_escape')
        if not data:
            print("No data returned after minimap had sent!")
            client.close()
            break
        
        to_send = pickle.dumps(obstacles)
        client.send(struct.pack("I",len(to_send)))
        client.send(to_send)
        data = client.recv(128).decode('unicode_escape')
        if not data:
            print("No data returned after obstacles had sent!")
            client.close()
            break

        connections.append(client)

def broadcast(item):
    for client in connections:
        to_send = pickle.dumps(item)
        client.send(struct.pack("I",len(to_send)))
        client.send(to_send)

accept_connections()

server.close()
print("Bye")