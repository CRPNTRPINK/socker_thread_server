import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('localhost', 7777))
server.listen(5)
user_addr = {}
user_ignore = {}


def connect():
    while True:
        data, addr = server.accept()
        user_addr.setdefault(addr, data)
        threading.Thread(target=client_connect, args=[data, addr]).start()


def client_connect(data, addr):
    while True:
        try:
            information = data.recv(1024)
            if information:
                print(information)
                print(user_addr)
                for i in user_addr:
                    if user_ignore.get(i, False) is False:
                        user_addr[i].send(information)
            else:
                raise Exception('Client disconnected')
        except Exception:
            for i in user_addr:
                if i == addr:
                    user_ignore.setdefault(i, data)
            data.close()
            break

t2 = threading.Thread(target=connect)
t2.start()