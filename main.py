from src.connection import TCPServer
from src.model import ImageToEmoji

server = None
model = None

def callback(result):
    print('Receive message: ' + result.decode('utf-8'))
    response = model.send_image(result.decode('utf-8'))
    server.send_message(response.encode('utf-8'))

if __name__ == '__main__':
    server = TCPServer('127.0.0.1', 12345, callback)
    server.start_server_nowait()
    
    model = ImageToEmoji()
    
    import time
    while True:
        time.sleep(1)
    
