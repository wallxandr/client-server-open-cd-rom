import socket
import ctypes


def client_program():
    host = "192.168.0.104"
    port = 5000  # socket server port number

    # MessageBox = ctypes.windll.user32.MessageBoxW  # create error message window
    # MessageBox(None, 'Unknown error', 'Telegram', 0x10)

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    while True:
        data = client_socket.recv(1024).decode()  # receive response
        if data.lower().strip() == "openit":
            client_socket.send('Opening..'.encode())
            exec(
                "ctypes.windll.WINMM.mciSendStringW(u'set cdaudio door open', None, 0, None)")
        elif data.lower().strip() == "closeit":
            client_socket.send('Closing..'.encode())
            exec(
                "ctypes.windll.WINMM.mciSendStringW(u'set cdaudio door closed', None, 0, None)")
        elif data.lower().strip() == "bye":
            break
    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
