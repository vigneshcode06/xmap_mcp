import json
from tools import scan, get_open_ports

from tools import scan, get_open_ports, chat

TOOLS = {
    "scan": scan,
    "get_open_ports": get_open_ports,
    "chat": chat
}


while True:
    msg = input()

    try:
        data = json.loads(msg)
        tool = data["tool"]
        args = data.get("args", {})

        if tool in TOOLS:
            result = TOOLS[tool](**args)
            print(json.dumps({"result": result}), flush=True)
        else:
            print(json.dumps({"error": "Unknown tool"}), flush=True)

    except Exception as e:
        print(json.dumps({"error": str(e)}), flush=True)


