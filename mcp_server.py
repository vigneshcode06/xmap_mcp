import json
from tools import (
    scan,
    fast_scan,
    full_scan,
    service_scan,
    os_detect,
    ping_host,
    get_open_ports,
    chat
)

TOOLS = {
    "scan": scan,
    "fast_scan": fast_scan,
    "full_scan": full_scan,
    "service_scan": service_scan,
    "os_detect": os_detect,
    "ping_host": ping_host,
    "get_open_ports": get_open_ports,
    "chat": chat
}

while True:
    try:
        msg = input()
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
