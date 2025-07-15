
import socket

class TCPServer:
    def __init__(self, port: int = 5000):
        self.port = port
        self.sock = None
        self.conn = None
        self.addr = None
        self.last_message = ""

    def start_server(self, port: int = 5000):
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('', self.port))
        self.sock.listen(1)
        print('Esperant connexió al port', self.port, '...')
        self.conn, self.addr = self.sock.accept()
        print('Connexió establerta amb:', self.addr)

    def send_message(self, message: str = 'Hello'):
        if self.conn:
            self.conn.send(message.encode('utf-8'))

    def has_new_message(self) -> bool:
        if self.conn:
            self.conn.setblocking(False)
            try:
                data = self.conn.recv(1024)
                if data:
                    self.last_message = data.decode('utf-8')
                    return True
                else:
                    return False
            except:
                return False
        return False

    def get_message(self) -> str:
        return self.last_message
