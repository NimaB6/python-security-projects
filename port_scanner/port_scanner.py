import socket
target= input ("Enter IP address : ")
print("Scanning started...")
ports = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS"
}
found_open = False
for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        result = s.connect_ex((target, port))
    
        if result == 0:
            print(f"Port {port} ({ports[port]}) is open")
            found_open = True
    except:
        print("Error connecting...")
if not found_open:
    print("No open ports found")
print("Scan finished")