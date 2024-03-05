import socket
import pickle


def main():
   server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   server_connection.bind(('127.0.0.1', 14900))
   server_connection.listen(10)
   client_connection, address = server_connection.accept()
   encoded_data = client_connection.recv(12000)
   base, height = pickle.loads(encoded_data)
   area = base * height
   area = round(area, 2)
   area_encoded = str(area).encode('utf-8')
   client_connection.send(area_encoded)
   server_connection.close()

if __name__ == '__main__':
    main()