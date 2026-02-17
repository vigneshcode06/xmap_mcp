# 🛰️ XMAP — MCP Powered AI Nmap Agent

XMAP is an AI-powered Nmap automation tool built using a custom  
Model Context Protocol (MCP) architecture.

It allows you to chat in natural language and let an AI agent run Nmap scans,
analyze results, and answer questions — all through a CLI interface.

Think of XMAP as:

ChatGPT + Nmap + MCP + Automation

---

## 🚀 Features

- Natural language scanning  
- AI-controlled tool execution  
- MCP-based client/server architecture  
- Multiple scan types  
- Ask questions about previous scans  
- Chat mode  
- API key stored safely in env file  

---

## 🧠 Architecture

User  
↓  
AI Client (ai_client.py)  
↓  
MCP Server (mcp_server.py)  
↓  
Tools (tools.py)  
↓  
Nmap / OS Commands  

AI decides WHAT to do  
MCP decides HOW to call tools  
Tools execute the real commands  

---

## 📁 Project Structure

xmap_mcp/  
├── ai_client.py  
├── mcp_server.py  
├── tools.py  
├── api.env  
└── .gitignore  

---

## 🛠 Requirements

- Python 3.8+  
- Nmap installed  
- OpenRouter API Key  

---

## 🔧 Installation

### Clone Repo

git clone https://github.com/vigneshcode06/xmap_mcp  
cd xmap_mcp  

### Install Dependencies

pip install requests  

### Install Nmap

Windows:  
https://nmap.org/download.html  

Linux:

sudo apt install nmap  

---

## 🔐 Create API Key File

Create file:

api.env  

Put inside:

YOUR_OPENROUTER_API_KEY  

---

## 🛡 Protect API Key

Create file:

.gitignore  

Add:

api.env  
__pycache__/  

---

## ▶ Run XMAP

python ai_client.py  

---

## 🧪 Example Commands

scan scanme.nmap.org  
fast scan scanme.nmap.org  
full scan scanme.nmap.org  
service scan scanme.nmap.org  
detect os of scanme.nmap.org  
ping google.com  
get open ports  
hello bro  

---

## 🔧 Available Tools

scan           - Basic scan  
fast_scan      - Quick scan  
full_scan      - All ports  
service_scan   - Service detection  
os_detect      - OS fingerprinting  
ping_host      - Ping host  
get_open_ports - List open ports  
chat           - Normal chat  

---

## 🧠 Why MCP?

Before MCP:

- Different AI models had different tool formats  
- Large if/else logic  
- Hard to scale  

With MCP:

- One standard protocol  
- Clean routing  
- Easy to add tools  
- Model independent  

---

## 🏗 Roadmap

- Vulnerability scan module  
- Exploit integration  
- Report generator  
- Web UI  
- Local LLM support  

---

## ⚠ Disclaimer

This project is for educational and ethical security testing only.  
Do NOT scan targets without permission.

---

## 👨‍💻 Author

Vignesh  
Cybersecurity | AI Agents | DevOps | Automation  

---

## ⭐ Support

If you like this project:

- Star the repo  
- Fork it  
- Build on it  

