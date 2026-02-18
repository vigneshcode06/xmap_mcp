import requests, subprocess, json

def load_api_key():
    with open("api.env") as f:
        return f.read().strip()

API_KEY = load_api_key()

SYSTEM_PROMPT = (
    "You are an MCP client.\n"
    "Return ONLY JSON.\n"
    "Use ONLY these tools:\n"
    "scan, fast_scan, full_scan, service_scan, os_detect, ping_host, get_open_ports, chat\n\n"

    "Examples:\n"
    "{\"tool\":\"scan\",\"args\":{\"target\":\"example.com\"}}\n"
    "{\"tool\":\"fast_scan\",\"args\":{\"target\":\"example.com\"}}\n"
    "{\"tool\":\"get_open_ports\"}\n"
    "{\"tool\":\"chat\",\"args\":{\"message\":\"hello\"}}"
)

def ask_ai(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
    }

    r = requests.post(url, headers=headers, json=data)
    return r.json()["choices"][0]["message"]["content"]

def main():
    server = subprocess.Popen(
        ["python", "mcp_server.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )

    print("\n🔥 XMAP MCP CHAT MODE 🔥\n")

    while True:
        user = input("XMAP> ")

        ai_reply = ask_ai(user)
        print("[AI]", ai_reply)

        server.stdin.write(ai_reply + "\n")
        server.stdin.flush()

        result = server.stdout.readline()
        print("[MCP]", result)

if __name__ == "__main__":
    main()
