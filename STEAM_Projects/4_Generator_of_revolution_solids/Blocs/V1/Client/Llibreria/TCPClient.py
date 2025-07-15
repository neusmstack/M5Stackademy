

import socket

class TCPClient:
    """
    note:
        en: ''
    details:
        color: '#0fb1d2'
        link: https://github.com/neusmstack
        image: ''
        category: Custom
    example: ''
    """
    def __init__(self, host: str = '192.168.1.100', port: int = 5000):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))

    def connect_to_server(self, ip: str = '192.168.1.100', port: int = 5000):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((ip, port))

    def send_message(self, send_message: str = 'Hello'):
        if self.client_socket:
            self.client_socket.send(send_message.encode())

    def receive_message(self) -> str:
        if self.client_socket:
            try:
                data = self.client_socket.recv(1024)
                return data.decode()
            except:
                return "Error receiving"
        else:
            return "No connection"

