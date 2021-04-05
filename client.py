import socket
import threading
from port_scanner import scanner
from auth import auth

ask_scan = input('Сканирова да/нет? ')
hostname = input('Введите имя хоста: ')
if ask_scan.lower() == 'да':
    hostname = scanner(socket, hostname)

port = int(input('Введите порт: '))
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = client.connect((hostname, port))

while True:
    name = input('Введите имя: ')
    password = input('Введите пароль: ')

    if auth(name, password):
        break


def client_send():
    while True:
        client.send(f'{name}: {input("")}'.encode())
        # recv = client.recv(1024)
        # print(recv.decode())

def client_recv():
    while True:
        recv = client.recv(1024)
        print(recv.decode())




# client_send()
t1 = threading.Thread(target=client_send)
t2 = threading.Thread(target=client_recv)
t1.start()
t2.start()
