import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 55555

# List to store connected clients
clients = []

def handle_client(client_socket, username):
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"{username}: {message}")
            broadcast(f"{username}: {message}", client_socket)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        clients.remove((username, client_socket))
        broadcast(f"{username} has left the chat.", client_socket)

def broadcast(message, sender_socket):
    for username, client_socket in clients:
        if client_socket != sender_socket:
            try:
                client_socket.send(message.encode('utf-8'))
            except Exception as e:
                print(f"Error broadcasting message to {username}: {e}")
                client_socket.close()
                clients.remove((username, client_socket))

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Server is listening on {HOST}:{PORT}")

    try:
        while True:
            client_socket, address = server.accept()
            username = client_socket.recv(1024).decode('utf-8')
            clients.append((username, client_socket))
            print(f"{username} has joined the chat.")
            broadcast(f"{username} has joined the chat.", client_socket)

            client_handler = threading.Thread(target=handle_client, args=(client_socket, username))
            client_handler.start()

    except KeyboardInterrupt:
        print("Server is shutting down.")
    finally:
        server.close()

if __name__ == "__main__":
    start_server()
