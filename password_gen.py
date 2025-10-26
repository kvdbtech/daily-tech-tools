### 2. `password_gen.py`

```python
#!/usr/bin/env python3
"""
Veilige Wachtwoord Generator – Kevin Van den Brande
Genereert sterke, unieke wachtwoorden.
"""

import secrets
import string
import sys

def generate_password(length=16):
    if length < 8:
        print("❌ Minimaal 8 tekens.")
        return None
    
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        length = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    except:
        length = 16
    
    pwd = generate_password(length)
    if pwd:
        print(f"🔐 Je wachtwoord ({length} tekens):\n")
        print(f"   {pwd}\n")
        print("   (Kopieer nu – wordt niet opgeslagen!)")
