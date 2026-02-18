
import json
from tools import scan, get_open_ports

TOOLS = {
    "scan": scan,
    "get_open_ports": get_open_ports
}

print("MCP Server Running...")

while True:
    msg = input()   # receives JSON from client

    try:
        data = json.loads(msg)
        tool = data["tool"]
        args = data.get("args", {})

        if tool in TOOLS:
            result = TOOLS[tool](**args)
            print(json.dumps({"result": result}))
        else:
            print(json.dumps({"error": "Unknown tool"}))

    except Exception as e:
        print(json.dumps({"error": str(e)}))
