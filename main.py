import socket
import argparse

def start_server(HOST, PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen()
        print("server is listening..")
        conn, addr = sock.accept()
        handle_client(conn, addr)

def handle_client(conn, addr):
    print(f"connected from {addr}: ")

def main():
    parser = argparse.ArgumentParser(prog="spyll", description="basic http sever")
    parser.add_argument('--host', type=str, default="192.168.1.53")
    parser.add_argument('--port', type=int, default=8888)

    args = parser.parse_args()

    start_server(args.host, int(args.port))

if __name__ == "__main__":
    main()
