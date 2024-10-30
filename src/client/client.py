import socket

def run_client():
    # create a scoket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # connecting to server socket
    server_ip = "127.0.0.1" # replace with the server's IP  address
    server_port = 8000
    
    # establish connection with server
    client.connect((server_ip, server_port))
    
    # creating communication loop
    while True:
        # input msg and send it to the server
        msg = input("Enter message: ")
        client.send(msg.encode("utf-8")[:1024]) # trime to be 1024 bytes at max
        
        # recieve msg from the server
        response = client.recv(1024)
        response - response.decode("utf-8")
        
        # if server sent us "closed" in the payload, we break out of the loop 
        # and close out socket
        if response.lower() == "closed":
            break
        
        print(f"Received: {response}")
        
    # freeing the resources        
    # close client socket (connection to the server)
    client.close()
    print("Connection to server closed")
        
run_client()