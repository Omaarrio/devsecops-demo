import re, os

secret_patterns = [
    r"AKIA[0-9A-Z]{16}",
    r"password\s*=\s*['\"].+['\"]",
    r"token\s*=\s*['\"].+['\"]"
]

def scan_file(path):
    content = open(path, "r", errors="ignore").read()
    for pattern in secret_patterns:
        if re.search(pattern, content):
            print(f"[!] Potential secret in {path}")
            return True
    return False

for root, _, files in os.walk("."):
    for f in files:
        if scan_file(os.path.join(root, f)):
            pass
