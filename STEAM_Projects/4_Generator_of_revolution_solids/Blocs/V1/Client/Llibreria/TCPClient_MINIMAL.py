import socket

class TCPClient:
    def __init__(self, host, port):
        print("Intentant connectar a", host, "port", port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(5)  # Espera màxima de 5 segons

        try:
            self.sock.connect((host, port))
            print("Connexió TCP establerta!")
        except Exception as e:
            print("Error de connexió:", e)
            raise e  # Torna a llençar l'error perquè el main.py el vegi

    def send_message(self, message):
        print("Enviant:", message)
        self.sock.send(message.encode())

    def close(self):
        print("Tancant connexió TCP")
        self.sock.close()
