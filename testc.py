import socket
import threading

def receive_messages(client_socket):
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
    except Exception as e:
        print(f"Error receiving message: {e}")
    finally:
        client_socket.close()

def send_messages(client_socket, username):
    try:
        while True:
            message = input()
            client_socket.send(message.encode('utf-8'))
    except Exception as e:
        print(f"Error sending message: {e}")
    finally:
        client_socket.close()

def start_client():
    # Hardcoded server IP and port
    host = '127.0.0.1'
    port = 55555

    username = input("Enter your username: ")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Send username to the server
    client_socket.send(username.encode('utf-8'))

    # Create threads for sending and receiving messages
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    send_thread = threading.Thread(target=send_messages, args=(client_socket, username))

    # Start the threads
    receive_thread.start()
    send_thread.start()

if __name__ == "__main__":
    start_client()
