import threading
import socket
import threading#handling many threads at a go

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())#get ip address auto
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!CONNNECT'

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected')
    
    connected=True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f'[{addr}] {msg}')
            conn.send('Msg received')
        

def main():
    server.listen()
    print(f'[LISTENING] Server is listening on {SERVER}')
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.active_count()-1}')


if __name__=='__main__':
    print("...Starting server...")
    main()