# XMAP

XMAP is a CLI-based AI-powered Nmap automation tool built using an MCP-style architecture.  
It allows you to chat with an AI and run Nmap scans automatically.

---

## What This Tool Does

- Run Nmap scans using natural language
- Use AI to decide which scan to run
- Execute scans automatically
- Show results in terminal
- Ask follow-up questions like open ports

---

## Folder Structure

xmap_mcp/
├── ai_client.py  
├── mcp_server.py  
├── tools.py  
├── api.env  
└── .gitignore  

---

## Requirements

- Python 3+
- Nmap installed
- OpenRouter API key

---

## Setup

### 1. Clone Project

git clone https://github.com/yourname/xmap_mcp.git  
cd xmap_mcp  

### 2. Install Python Library

pip install requests  


### 4. Protect API Key

Create file:

.gitignore  

Add:

api.env  
__pycache__/  

---

## Run Tool

python ai_client.py  

---

## Example Commands

scan scanme.nmap.org  
fast scan scanme.nmap.org  
full scan scanme.nmap.org  
service scan scanme.nmap.org  
detect os of scanme.nmap.org  
ping google.com  
get open ports  
hello  

---

## Available Tools

scan  
fast_scan  
full_scan  
service_scan  
os_detect  
ping_host  
get_open_ports  
chat  

## ⚠ Disclaimer

This project is for educational and ethical security testing only.  
Do NOT scan targets without permission.

---

## 👨‍💻 Author

Vignesh  
Cybersecurity | AI Agents | DevOps | Automation  
