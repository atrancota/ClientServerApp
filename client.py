import socket
import json
import os

SERVER_IP = '127.0.0.1'
SERVER_PORT = 555


def itereaza_si_trimite_path_fisiere(path):

    lista_fisiere = []
    for rootpath, subdirector, fisiere in os.walk(path):
        for fisier in fisiere:
            path_fisier = os.path.join(rootpath, fisier)
            lista_fisiere.append(path_fisier)

    server_socket = socket.create_connection((SERVER_IP, SERVER_PORT))

    lista_fisiere_json = json.dumps(lista_fisiere)
    server_socket.sendall(lista_fisiere_json.encode())
    raspuns_confirmare = server_socket.recv(4096).decode()
    if raspuns_confirmare == "OK":
        print("Lista ce contine path-ul fiecarui fisier s-a trimis cu succes!")


if __name__ == "__main__":
    iterare_path = "C:/Users/andre/Desktop/test/"  # ex: "C:/Users/at/Desktop/test/"
    itereaza_si_trimite_path_fisiere(iterare_path)
