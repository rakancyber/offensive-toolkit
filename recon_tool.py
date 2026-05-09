import socket
import whois
import dns.resolver
import json
from datetime import datetime

# Reconnaissance script to grab basic target info
def perform_recon(target_ip, target_domain):
    print(f"\n--- Starting Reconnaissance on {target_domain} ({target_ip}) ---")
    data = {"target_ip": target_ip, "target_domain": target_domain, "dns": [], "whois": {}, "banners": {}}
    
    # 1. WHOIS Automation
    try:
        w = whois.whois(target_domain)
        data["whois"] = {"registrar": w.registrar, "creation_date": str(w.creation_date)}
        print("[+] WHOIS Data Extracted successfully.")
    except Exception:
        print("[-] WHOIS failed")

    # 2. DNS Enumeration
    try:
        for record in ['A', 'MX', 'TXT']:
            try:
                answers = dns.resolver.resolve(target_domain, record)
                for rdata in answers:
                    data["dns"].append(f"{record}: {rdata.to_text()}")
            except:
                pass
        print("[+] DNS Enumeration Complete.")
    except Exception:
        print("[-] DNS failed")

    # 3. Banner Grabbing (Port 80)
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((target_ip, 80))
        s.send(b"HEAD / HTTP/1.1\r\nHost: localhost\r\n\r\n")
        banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
        data["banners"][80] = banner[:100] 
        print(f"[+] Banner grabbed from port 80")
        s.close()
    except:
        print("[-] Could not grab banner (Port 80 might be closed).")
            
    # Save the structured report
    filename = f"recon_report_{target_ip}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"\n[+] Structured report saved to {filename}")

if __name__ == "__main__":
    # Testing locally per academic policy
    perform_recon("127.0.0.1", "google.com")
