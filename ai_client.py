import requests, subprocess, json

def load_api_key():
    with open("api.env") as f:
        return f.read().strip()

API_KEY = load_api_key()

SYSTEM_PROMPT = (
    "You are an MCP client.\n"
    "Return ONLY JSON.\n"
    "NEVER invent your own JSON keys.\n"
    "ALWAYS use one of the tools below.\n\n"

    "TOOLS:\n"
    "scan -> {\"tool\":\"scan\",\"args\":{\"target\":\"example.com\"}}\n"
    "fast_scan -> {\"tool\":\"fast_scan\",\"args\":{\"target\":\"example.com\"}}\n"
    "full_scan -> {\"tool\":\"full_scan\",\"args\":{\"target\":\"example.com\"}}\n"
    "service_scan -> {\"tool\":\"service_scan\",\"args\":{\"target\":\"example.com\"}}\n"
    "os_detect -> {\"tool\":\"os_detect\",\"args\":{\"target\":\"example.com\"}}\n"
    "ping_host -> {\"tool\":\"ping_host\",\"args\":{\"target\":\"example.com\"}}\n"
    "get_open_ports -> {\"tool\":\"get_open_ports\"}\n"
    "chat -> {\"tool\":\"chat\",\"args\":{\"message\":\"hello\"}}\n\n"

    "RULES:\n"
    "- If user asks to scan -> use scan\n"
    "- If user asks about open ports or port count -> use get_open_ports\n"
    "- If user chats -> use chat\n"
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
