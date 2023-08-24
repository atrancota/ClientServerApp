import socket
import os
import json
import threading
import hashlib
import time
import psutil

HOST = '127.0.0.1'
PORT = 555

server = socket.create_server((HOST, PORT))
server.listen()
print(f"Serverul asculta pe {HOST}:{PORT}")


def procesare_fisier(path_fisier):

    detalii_fisier = dict()
    detalii_fisier['Nume_fisier'] = os.path.basename(path_fisier)
    dimensiune_kb = os.path.getsize(path_fisier) / 1024
    detalii_fisier['Size_fisier'] = str(dimensiune_kb) + " KB"
    detalii_fisier['Data_ultimei_modificari'] = time.ctime(os.path.getmtime(path_fisier))
    detalii_fisier['Data_crearii'] = time.ctime(os.path.getctime(path_fisier))

    with open(path_fisier, 'rb') as f:
        content = f.read()
        md5_hash = hashlib.md5(content).hexdigest()
        detalii_fisier['Hash_MD5'] = md5_hash

    return detalii_fisier


def gestionare_date_client(client_socket):

    start_time = time.time()

    date_client = client_socket.recv(4096).decode()
    client_socket.send("OK".encode())
    lista_fisiere = json.loads(date_client)
    lista_finala_json = []
    for element in lista_fisiere:
        json_info = procesare_fisier(path_fisier=element)
        lista_finala_json.append(json_info)
    for json_dict in lista_finala_json:
        print(json.dumps(json_dict, indent=4))
    client_socket.close()

    end_time = time.time()
    total_time = end_time - start_time

    proces = psutil.Process(os.getpid())
    utilizare_cpu = proces.cpu_percent()
    utilizare_memorie = proces.memory_percent()

    print(f"Timp total de procesare: {total_time * 1000:.2f} ms")
    print(f"Utilizare CPU: {utilizare_cpu:.50f}%")
    print(f"Utilizare memorie: {utilizare_memorie}%")


client_socket, _ = server.accept()
print("Clientul s-a conectat la server, detalii client:", client_socket.getpeername())
client_handler = threading.Thread(target=gestionare_date_client, args=(client_socket,))
client_handler.start()
