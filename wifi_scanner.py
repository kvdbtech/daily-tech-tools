#!/usr/bin/env python3
"""
WiFi Scanner – Kevin Van den Brande
Toont beschikbare netwerken + signaalsterkte (Windows/Linux).
"""

import subprocess
import re
import platform

def scan_wifi():
    system = platform.system()
    if system == "Windows":
        result = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True, text=True)
        profiles = re.findall(r"All User Profile\s+:\s(.+)", result.stdout)
        networks = []
        for profile in profiles:
            res = subprocess.run(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'], capture_output=True, text=True)
            ssid = profile
            signal = re.search(r"Signal\s+:\s(\d+)%", res.stdout)
            strength = signal.group(1) if signal else "?"
            networks.append({"SSID": ssid, "Signal": strength})
        return networks
    else:
        print("ℹ️  Linux/macOS: gebruik 'nmcli' of 'iwlist'")
        return []

if __name__ == "__main__":
    print("📡 Beschikbare WiFi-netwerken:\n")
    networks = scan_wifi()
    for net in networks:
        bars = "█" * (int(net["Signal"]) // 20) if net["Signal"].isdigit() else "?"
        print(f"  {net['SSID']:25} | {bars} {net['Signal']}%")
