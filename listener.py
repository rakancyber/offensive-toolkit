import socket

def start_listener():
    host = "127.0.0.1"
    port = 4444

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    
    print(f"[*] Starting educational listener on {host}:{port}...")
    s.bind((host, port))
    s.listen(1)
    
    print(f"[*] Listening for incoming sandbox connections...")
    conn, addr = s.accept()
    print(f"[+] Connection established from {addr}")
    
    while True:
        try:
            data = conn.recv(4096).decode("utf-8")
            if not data:
                break
            print(data, end="")
            
            cmd = input("Sandbox-Shell> ")
            if cmd.lower() in ['exit', 'quit']:
                conn.send(b"exit")
                break
            
            conn.send(cmd.encode("utf-8"))
            
        except KeyboardInterrupt:
            break
            
    print("\n[*] Closing connection.")
    conn.close()
    s.close()

if __name__ == "__main__":
    start_listener()