import socket

class TCPServer:
    def __init__(self, port):
        print("Inicialitzant servidor TCP al port", port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(('', port))
        self.sock.listen(1)
        print("Servidor escoltant al port", port)

    def run_server(self):
        while True:
            print("Esperant connexió entrant...")
            conn, addr = self.sock.accept()
            print("Connexió acceptada des de", addr)

            try:
                data = conn.recv(1024)
                if data:
                    message = data.decode()
                    print("Missatge rebut:", message)
            except Exception as e:
                print("Error en rebre:", e)

            print("Tancant connexió")
            conn.close()
