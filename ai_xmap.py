import requests
import subprocess
import json
import os

# Load API Key
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

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "Return ONLY JSON like {\"action\":\"scan\",\"target\":\"example.com\"}"},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]

def run_xmap(target):
    print(f"\n[+] Running XMAP on {target}\n")
    subprocess.run(["nmap", "-F", target])

def main():
    user_input = input("XMAP-AI> ")

    ai_reply = ask_ai(user_input)
    print("[AI RAW RESPONSE]", ai_reply)

    try:
        data = json.loads(ai_reply)
        if data["action"] == "scan":
            run_xmap(data["target"])
        else:
            print("[-] Unknown action")

    except Exception as e:
        print("[-] Failed to parse AI response")

if __name__ == "__main__":
    main()
