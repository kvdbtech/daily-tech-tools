# Daily Tech Tools 🛠️
**Door Kevin Van den Brande** – Field Technician | Python | Hardware | AI

> **Handige scripts die ik dagelijks gebruik** – voor beveiliging, opruiming, automatisering en meer.

---

## Wat zit erin?

| Tool | Wat doet het? |
|------|---------------|
| `password_gen.py` | Genereert veilige, unieke wachtwoorden |
| `clean_downloads.py` | Ruimt oude bestanden op (Downloads, Desktop) |
| `price_alert.py` | Checkt webshops op prijsdaling (bijv. Coolblue) |
| `wifi_scanner.py` | Toont beschikbare WiFi-netwerken + signaalsterkte |

---

## Installatie & Gebruik

```bash
# Clone de repo
git clone https://github.com/kvdbtech/daily-tech-tools.git
cd daily-tech-tools

# Voorbeeld: wachtwoord genereren
python password_gen.py 16

# Voorbeeld: Downloads opruimen (ouder dan 30 dagen)
python clean_downloads.py --days 30
