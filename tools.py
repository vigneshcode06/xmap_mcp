import subprocess

last_scan_output = ""

def scan(target):
    global last_scan_output
    print(f"\n[+] Running XMAP on {target}\n")

    result = subprocess.run(
        ["nmap", "-F", target],
        capture_output=True,
        text=True
    )

    last_scan_output = result.stdout
    return last_scan_output

def get_open_ports():
    if not last_scan_output:
        return "No scan performed yet."

    ports = []
    for line in last_scan_output.splitlines():
        if "/tcp" in line and "open" in line:
            ports.append(line.split("/")[0])

    return f"Open ports: {', '.join(ports)}"
