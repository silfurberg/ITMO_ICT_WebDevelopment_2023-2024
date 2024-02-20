# Упражнение 3

## Код

### Сервер 
```python
import socket


def get_webpage_response():
    response_type = 'HTTP/1.0 200 OK\n'
    headers = 'Content-Type: text/html\n\n'
    with open('index.html') as f:
        content = "".join(f.readlines())

    response_raw = response_type + headers + content
    response_encoded = response_raw.encode('utf-8')
    return response_encoded


def main():
    server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_connection.bind(('127.0.0.1', 14900))
    server_connection.listen(10)
    print(f'Переходи по адресу: 127.0.0.1:14900')

    while True:
        try:
            client_connection, address = server_connection.accept()

            print(client_connection)
            webpage_response = get_webpage_response()
            client_connection.send(webpage_response)
        except KeyboardInterrupt:
            break
    server_connection.close()


if __name__ == '__main__':
    main()
```
### index.html
```html
<!DOCTYPE html>
<html>
<head>
  <title>The best website ever existed</title>
</head>
<body>
Lorem Ipsum Dolor Sit O Met
</body>
</html>
```