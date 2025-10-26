#!/usr/bin/env python3
"""
Automatisch Opruimen – Kevin Van den Brande
Verwijdert bestanden ouder dan X dagen uit Downloads/Desktop.
"""

import os
import shutil
import time
import argparse
from pathlib import Path

def clean_folder(folder, days=30, dry_run=True):
    cutoff = time.time() - (days * 86400)
    removed = 0
    for path in Path(folder).iterdir():
        if path.is_file() and path.stat().st_mtime < cutoff:
            print(f"🗑️  {path.name}")
            if not dry_run:
                path.unlink()
            removed += 1
    return removed

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--days", type=int, default=30, help="Ouder dan X dagen")
    parser.add_argument("--run", action="store_true", help="Echt verwijderen")
    args = parser.parse_args()

    folders = [
        os.path.expanduser("~/Downloads"),
        os.path.expanduser("~/Desktop")
    ]

    print(f"🧹 Opruimen bestanden ouder dan {args.days} dagen...\n")
    total = 0
    for folder in folders:
        if os.path.exists(folder):
            print(f"{folder}:")
            removed = clean_folder(folder, args.days, not args.run)
            total += removed
            print(f"   → {removed} bestanden\n")
        else:
            print(f"   ⚠️  Map niet gevonden\n")

    if args.run:
        print(f"✅ {total} bestanden verwijderd.")
    else:
        print(f"🔍 {total} bestanden gevonden. Gebruik --run om te verwijderen.")
