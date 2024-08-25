import socket
import argparse

def start_server(HOST, PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen()
        print(f"server is listening on ip: {HOST} port: {PORT}")
        conn, addr = sock.accept()
        handle_client(conn, addr)
        sock.close()

def handle_client(conn, addr):
    print(f"connected from {addr}: ")
    request = conn.recv(4096)
    print(request)
    http_response = b'HTTP/1.1 200 OK\n\nHello World!'
    conn.sendall(http_response)
    conn.close()

def main():
    parser = argparse.ArgumentParser(prog="spyll", description="basic http sever")
    parser.add_argument('--host', type=str, default="127.0.0.1")
    parser.add_argument('--port', type=int, default=8888)

    args = parser.parse_args()

    start_server(args.host, int(args.port))

if __name__ == "__main__":
    main()
