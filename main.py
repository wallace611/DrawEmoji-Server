from src.connection import TCPServer
from src.model import ImageToEmoji

server = None
model = None

def callback(result: bytes):
    print('Receive message: ' + result.decode('utf-8'))
    
    try:
        response = model.send_image(result.decode('utf-8'))
    except Exception as e:
        print(f"Error processing image: {e}")
        response = "Error processing image: " + str(e)
        
    server.send_message(response.encode('utf-8'))

if __name__ == '__main__':
    server = TCPServer(host='127.0.0.1', port=12345, receive_callback=callback, packet_size=2000000)
    server.start_server_nowait()
    
    model = ImageToEmoji()
    
    import time
    while True:
        time.sleep(1)
    
