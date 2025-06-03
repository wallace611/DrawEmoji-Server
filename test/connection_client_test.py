import socket

class TCPClient:
    def __init__(self, host: str, port: int):
        self._host = host
        self._port = port
        self._client_socket = None

    def connect(self):
        """Connect to the server."""
        self._client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._client_socket.connect((self._host, self._port))
        print(f"Connected to server at {self._host}:{self._port}")

    def send_message(self, message: str):
        """Send a message to the server and receive a response."""
        if self._client_socket is None:
            raise RuntimeError("Client not connected. Call connect() first.")
        self._client_socket.sendall(message.encode())
        response = self._client_socket.recv(1024)
        print(f"Received from server: {response.decode()}")

    def close(self):
        """Close the connection."""
        if self._client_socket:
            self._client_socket.close()
            print("Connection closed.")

if __name__ == "__main__":
    client = TCPClient(host="localhost", port=12345)
    try:
        client.connect()
        while True:
            message = input("Enter message to send (or 'exit' to quit): ")
            if message.lower() == 'exit':
                break
            client.send_message(message)
    finally:
        client.close()