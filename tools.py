import subprocess

last_scan_output = ""

def scan(target):
    global last_scan_output
    result = subprocess.run(
        ["nmap", "-F", target],
        capture_output=True,
        text=True
    )
    last_scan_output = result.stdout
    return result.stdout


def fast_scan(target):
    result = subprocess.run(
        ["nmap", "-F", target],
        capture_output=True,
        text=True
    )
    return result.stdout


def full_scan(target):
    result = subprocess.run(
        ["nmap", "-p-", target],
        capture_output=True,
        text=True
    )
    return result.stdout


def service_scan(target):
    result = subprocess.run(
        ["nmap", "-sV", target],
        capture_output=True,
        text=True
    )
    return result.stdout


def os_detect(target):
    result = subprocess.run(
        ["nmap", "-O", target],
        capture_output=True,
        text=True
    )
    return result.stdout


def ping_host(target):
    result = subprocess.run(
        ["ping", target],
        capture_output=True,
        text=True
    )
    return result.stdout


def get_open_ports():
    if not last_scan_output:
        return "No scan performed yet."

    ports = []
    for line in last_scan_output.splitlines():
        if "/tcp" in line and "open" in line:
            ports.append(line.split("/")[0])

    return "Open ports: " + ", ".join(ports)


def chat(message):
    return f"Chat: {message}"
