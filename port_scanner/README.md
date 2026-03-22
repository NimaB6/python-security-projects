# 🔍 Port Scanner

A simple Python port scanner that checks common ports on a target IP address or hostname.

---

## 🚀 Features

- Scan important ports (21, 22, 80, 443)
- Detect open ports
- Show service names (FTP, SSH, HTTP, HTTPS)
- Handles connection errors safely
- Fast scanning using timeout

---

## 📌 Ports Included

| Port | Service |
|------|--------|
| 21   | FTP    |
| 22   | SSH    |
| 80   | HTTP   |
| 443  | HTTPS  |

---

## ⚙️ How It Works

The program asks the user for an IP address or domain, then tries to connect to each port.

- If connection is successful → port is **open**
- If connection fails → port is **closed**

---

## ▶️ Usage

Run the script:

```bash
python port_scanner.py
```

Then enter an IP or domain:

```
Enter IP address: scanme.nmap.org
```

---

## 🧪 Example Output

```
Scanning started...
Port 22 (SSH) is open
Port 80 (HTTP) is open
Scan finished
```

---

## 🛠 Technologies Used

- Python
- socket

---

## 👨‍💻 Author

Mohammadhosein(Nima) Bahrami