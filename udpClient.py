import socket

target_ip = "127.0.0.1"  # Localhost (your own machine)
target_port = 80         # Port to send data to

# Create a UDP socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Data to send
message = "meow meow"

# Send the data to the target IP and port
client.sendto(message.encode(), (target_ip, target_port))

# Receive response from the server
data, addr = client.recvfrom(4096)  # 4096 is the buffer size

# Print the received data
print(f"Received from {addr}: {data.decode()}")
#print("Received from {}: {}".format(addr, data.decode()))  ->if not using f-string
# Close the socket
client.close()
