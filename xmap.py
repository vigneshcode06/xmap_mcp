import sys
import subprocess

def run_xmap(target):
    print(f"[+] Starting XMAP scan on {target}...\n")

    try:
        result = subprocess.run(
            ["nmap", "-F", target],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print("[+] Scan Completed Successfully\n")
            print(result.stdout)
        else:
            print("[-] Error Running Nmap")
            print(result.stderr)

    except FileNotFoundError:
        print("[-] Nmap not found. Please install nmap and try again.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python xmap.py <target>")
        sys.exit(1)

    target = sys.argv[1]
    run_xmap(target)
