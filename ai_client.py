import requests, json, subprocess

def load_api_key():
    with open("api.env") as f:
        return f.read().strip()

API_KEY = load_api_key()

def ask_ai(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    system_prompt = (
        "Return ONLY JSON.\n"
        "For scanning: {\"tool\":\"scan\",\"args\":{\"target\":\"example.com\"}}\n"
        "For open ports: {\"tool\":\"get_open_ports\"}\n"
        "For normal chat: {\"tool\":\"chat\",\"args\":{\"message\":\"hello\"}}"
    )

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": system_prompt},
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

    print("XMAP MCP CHAT MODE")

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
