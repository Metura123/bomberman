from utils import init_map
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

def broadcast(item):
    for client in connections:
        to_send = pickle.dumps(item)
        client.send(struct.pack("I",len(to_send)))
        client.send(to_send)

def receive_and_send_players(client):
    while True:
        to_recv = struct.unpack("I", client.recv(4))
        data = client.recv(to_recv[0])
        if not data:
            index = connections.index(client)
            players.pop(index)
            connections.pop(index)
            client.close()
            break
        else:
            to_send = pickle.dumps(players)
            client.send(struct.pack("I",len(to_send)))
            client.send(to_send)

def receive_and_send_minimap(client):
    while True:
        to_recv = struct.unpack("I", client.recv(4))
        data = client.recv(to_recv[0])
        if not data:
            index = connections.index(client)
            players.pop(index)
            connections.pop(index)
            client.close()
            break
        else:
            to_send = pickle.dumps(minimap)
            client.send(struct.pack("I",len(to_send)))
            client.send(to_send)

def accept_connections():
    while True:
        if not len(connections) < 2:
            continue
        client, addr = server.accept()

        client.send(str(len(players)).encode('unicode_escape')) 
        # Receiving the player object of the created player
        player = Player(player_locations[len(players)][0],player_locations[len(players)][1])
        print(player)
        players.append(player)

        # Sending the players, minimap and obstacles to the client
        to_send = pickle.dumps(players)
        client.send(struct.pack("I",len(to_send)))
        client.send(to_send)
        data = client.recv(128).decode('unicode_escape')
        if not data:
            print("No data returned after players had sent!")
            client.close()
            break

        to_send = pickle.dumps(minimap)
        client.send(struct.pack("I",len(to_send)))
        client.send(to_send)
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

        threading.Thread(target=receive_and_send_players,args=(client, )).start()
        threading.Thread(target=receive_and_send_minimap,args=(client, )).start()
        connections.append(client)

accept_connections()



server.close()
print("Bye")