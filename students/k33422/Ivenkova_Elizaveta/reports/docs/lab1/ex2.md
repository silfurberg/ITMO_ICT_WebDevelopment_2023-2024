# Упражнение 2



## Код

### Клиента
```python
import socket
import pickle

def main():
    server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_connection.connect(('127.0.0.1', 14900))
    base = int(input('Base:'))
    height = int(input('Height:'))
    parallelogram_data = (base, height)
    encoded_parallelogram_data = pickle.dumps(parallelogram_data)
    server_connection.send(encoded_parallelogram_data)
    server_response_enc = server_connection.recv(12000)
    server_response_dec = server_response_enc.decode('utf-8')
    print(f'Parallelogram area: {server_response_dec}')
    server_connection.close()


if __name__ == '__main__':
    main()
```

### Сервера

```python
import socket
import pickle


def main():
   server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   server_connection.bind(('127.0.0.1', 14900))
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
```
