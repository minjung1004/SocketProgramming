# socket(): Creates a new socket.
# bind(): Associates the socket to a specific address and port.
# listen(): Starts listening for incoming connections on the socket.
# accept(): Accepts a connection from a client and returns a new socket for communication.
# connect(): Establishes a connection to a remote server.
# send(): Sends data through the socket.
# recv(): Receives data from the socket.
# close(): Closes the socket connection.
import socket

def run_server():
    # create a socket object
    # AF_INET specifies the IP address family for IPv4
    # SOCK_STREAM specifies using a TCP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # binding server socket to IP address and port
    server_ip = "127.0.0.1"
    port = 8000
    server.bind((server_ip, port))
    
    # listening for incoming connections
    server.listen(0) 
    print(f"Listening on {server_ip}:{port}")
    
    # accepting incoming connections
    client_socket, client_address = server.accept()
    print(f"Accepted connection form {client_address[0]}:{client_address[1]}")
    
    # creating communication loop
    # recieve data from the client
    while True:
            request = client_socket.recv(1024)
            request = request.decode("utf-8") # convert bytes to string
            # if we recieve 'close' from the client, the we break out of 
            # the loop and close the connection
            if request.lower() == "close":
                # send reponse to the client which acknowledges that the 
                # connection should be closed and break out of the loop
                client_socket.send("closed".encode("utf-8"))
                break
            print(f"Received: {request}")
            
    # sending reponse back to client
    response = "accepted".encode("utf-8") # convert string to bytes
   
    # convert and sne daccepte reponse to the client
    client_socket.send(response)
    
    # close the connecttion socket with the client
    client_socket.close()
    print("Connection to client closed")
    # close server socket
    server.close()
    
run_server()
    