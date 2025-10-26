#!/usr/bin/env python3
"""
Prijs Alert – Kevin Van den Brande
Checkt webshop op prijsdaling (bijv. Coolblue).
"""

import requests
from bs4 import BeautifulSoup
import json
import time

def check_price(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        price = soup.find("span", {"class": "sales-price__current"})
        if price:
            return float(price.text.replace("€", "").replace(",", "").strip())
    except:
        return None

# Voorbeeld URL (vervang door echte)
URL = "https://www.coolblue.be/product/123456/laptop.html"
TARGET = 599.00

if __name__ == "__main__":
    current = check_price(URL)
    if current:
        print(f"💰 Huidige prijs: €{current}")
        if current <= TARGET:
            print(f"🎉 DOEL BEREIKT! Koop nu!")
        else:
            print(f"⏳ Wacht... nog €{current - TARGET:.2f} te gaan.")
    else:
        print("❌ Kon prijs niet ophalen.")
