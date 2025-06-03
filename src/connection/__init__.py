from queue import Queue
from threading import Thread
import socket
import time

class TCPServer:
    def __init__(self, host: str, port: int, receive_callback=None):
        self._host = host
        self._port = port
        if receive_callback is not None:
            self._receive_callback = receive_callback
        else:
            self._receive_callback = lambda x: print(x.decode('utf-8').strip('\0'))
        self._server_socket = None
        self._message_queue = Queue()

    def start_server(self):
        """Start the TCP server and listen for incoming connections."""
        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._server_socket.bind((self._host, self._port))
        self._server_socket.listen(1)
        print(f"Server started, listening on {self._host}:{self._port}")
        self._serve_forever()

    def start_server_nowait(self):
        """Start the server in a separate thread without blocking."""
        server_thread = Thread(target=self.start_server)
        server_thread.daemon = True
        server_thread.start()
        return server_thread

    def _handle_client(self, conn, addr):
        print(f"Connection established with {addr}")
        while True:
            try:
                reply = ""
                reply = conn.recv(2048)
                if not reply:
                    print("Client disconnected.")
                    break
                
                time.sleep(1)
                self._receive_callback(reply)
                message = self._message_queue.get()
                if message is None:
                    print("No message to send")
                    continue

                print(f"Sending message to client: {message}")

                conn.send(message)
                
            except Exception as e:
                print(e)
                break
        conn.close()
        print("Connection closed.")

    def _serve_forever(self):
        if self._server_socket is None:
            raise RuntimeError("Server not started. Call start_server() first.")
        try:
            while True:
                conn, addr = self._server_socket.accept()
                self._handle_client(conn, addr)
                time.sleep(1)
        except Exception as e:
            print(e)
        finally:
            self._server_socket.close()
            
    def send_message(self, message: bytes):
        """Send a message to the client."""
        self._message_queue.put(message)