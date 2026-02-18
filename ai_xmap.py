import requests
import subprocess
import json

# Load API Key
def load_api_key():
    with open("api.env") as f:
        return f.read().strip()

API_KEY = load_api_key()

last_scan_output = ""

def ask_ai(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": """You are an assistant for an nmap tool.
Return ONLY JSON.

For scan request:
{"action":"scan","target":"example.com"}

For questions about result:
{"action":"analyze","question":"how many open ports"}
"""
            },
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]

def run_xmap(target):
    global last_scan_output
    print(f"\n[+] Running XMAP on {target}\n")
    result = subprocess.run(
        ["nmap", "-F", target],
        capture_output=True,
        text=True
    )
    last_scan_output = result.stdout
    print(last_scan_output)

def analyze_result(question):
    if not last_scan_output:
        print("[-] No scan results yet")
        return

    ai_prompt = f"""
Here is nmap output:

{last_scan_output}

Answer this question:
{question}
"""

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": ai_prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    answer = response.json()["choices"][0]["message"]["content"]
    print("\n[AI]", answer)

def main():
    print("=== XMAP CHAT MODE ===")
    while True:
        user_input = input("XMAP> ")

        if user_input.lower() in ["exit", "quit"]:
            break

        ai_reply = ask_ai(user_input)

        try:
            data = json.loads(ai_reply)

            if data["action"] == "scan":
                run_xmap(data["target"])

            elif data["action"] == "analyze":
                analyze_result(data["question"])

            else:
                print("[-] Unknown action")

        except:
            print("[-] AI response error")

if __name__ == "__main__":
    main()
