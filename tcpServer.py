import socket
import threading

IP='0.0.0.0'
PORT=8090

def main():
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((IP,PORT))
    server.listen(5)
    print(f"Server is listening on {IP}:{PORT}")
    
    while True:
        client,address=server.accept()
        print(f'[+] Accepted connection from {address[0]}:{address[1]}')
        client_handler=threading.Thread(target=handle_client,args=(client,))
        client_handler.start()
        
def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f"[+] Received: {request.decode("utf-8")}")
        sock.send(b'meowwwwwwwwwwww')
        
if __name__ == "__main__":
    main()
#the main() function is executed only when the script is run directly, and not when it is imported as a module.
