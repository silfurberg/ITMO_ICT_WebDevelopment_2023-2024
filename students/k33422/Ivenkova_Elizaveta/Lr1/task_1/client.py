import socket

def main():
    client_connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_connection.connect(('127.0.0.1', 14900))
    client_connection.send(b'Hello, server')
    server_msg = client_connection.recv(12000).decode('utf-8')
    print(server_msg)
    client_connection.close()



if __name__ == '__main__':
    main()