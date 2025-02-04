iimport socket

target_host = "www.google.com"
target_port = 80

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect the client
    client.connect((target_host, target_port))

    # Send an HTTP GET request
    request = "GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(target_host)
    client.send(request.encode())

    # Receive the server's response
    response = client.recv(4096)

    # Print the response
    print(response.decode())

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the client socket
    client.close()
