import socket


def server_program():
    host = "192.168.0.104"
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))

    while True:
        data = input(' -> ')
        conn.send(data.encode())
        if data == 'bye':
            break

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
