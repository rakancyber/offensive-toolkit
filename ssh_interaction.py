import paramiko
import time

def ssh_interaction(ip, username, password):
    print(f"\n--- Testing SSH on {ip} ---")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # Simple rate limiting to avoid triggering brute-force alerts
    print("[*] Applying rate-limiting (2-second delay) done")
    time.sleep(2) 
    
    try:
        print(f"[*] Attempting login as '{username}' ...")
        client.connect(ip, username=username, password=password, timeout=5)
        print("[+] SSH Login Successful!")
        
        # Run a quick remote command
        stdin, stdout, stderr = client.exec_command('whoami')
        print(f"[+] Command output (whoami): {stdout.read().decode().strip()}")
        
        # Test file upload via SFTP
        print("# Opening SFTP channel ...")
        print("# Writing local_test.txt -> uploading to remote_test.txt")
        sftp = client.open_sftp()
        with open("local_test.txt", "w") as f:
            f.write("SFTP Transfer Test")
        sftp.put("local_test.txt", "remote_test.txt")
        print("[+] SFTP File Transfer successful")
        sftp.close()
        
    except Exception as e:
        print(f"[-] SSH Interaction failed: {e}")
    finally:
        print("# Connection closed cleanly via client.close()")
        client.close()

if __name__ == "__main__":
    ssh_interaction("127.0.0.1", "testuser", "testpassword")
