# OverSploit

🚀 A lightweight, modular exploitation and recon framework written in Python — inspired by Metasploit, built from scratch by [black45-boop](https://github.com/black45-boop).

> 💡 For educational and authorized penetration testing only.

---

## 🧩 Features

- Modular system (`exploit/`, `payloads/`, `post/`)
- Reverse shell listeners
- Port scanners & banner grabbers
- HTTPS login brute-force
- Network activity monitor (detect Nmap, ARP poisoning)
- Hash identifier & cracker
- Fake ransomware simulator (safe)

---

## 📦 Requirements

### Python 3.8 or later  
Required Python libraries:

```txt
colorama
requests
scapy

LINUX 

git clone https://github.com/black45-boop/overst.git
cd overst/oversploit

# Optional: use a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run OverSploit (some modules need root)
sudo python3 oversploit.py

```txt
WINDOWS

git clone https://github.com/black45-boop/overst.git
cd overst\oversploit

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
python oversploit.py
