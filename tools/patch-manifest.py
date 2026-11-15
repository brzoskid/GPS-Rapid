#!/usr/bin/env python3
"""Idempotentne uprawnienia Bluetooth, telefonu i lokalizacji dla RAPID OBD."""
from pathlib import Path
import re

p = Path("android/app/src/main/AndroidManifest.xml")
s = p.read_text(encoding="utf-8")

permissions = [
    '    <uses-permission android:name="android.permission.BLUETOOTH" android:maxSdkVersion="30"/>',
    '    <uses-permission android:name="android.permission.BLUETOOTH_ADMIN" android:maxSdkVersion="30"/>',
    '    <uses-permission android:name="android.permission.BLUETOOTH_CONNECT"/>',
    '    <uses-permission android:name="android.permission.BLUETOOTH_SCAN" android:usesPermissionFlags="neverForLocation"/>',
    '    <uses-permission android:name="android.permission.CALL_PHONE"/>',
    '    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>',
    '    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>',
    '    <uses-feature android:name="android.hardware.telephony" android:required="false"/>',
]

missing = []
for line in permissions:
    match = re.search(r'(?:uses-permission|uses-feature) android:name="([^"]+)"', line)
    name = match.group(1)
    if f'android:name="{name}"' not in s:
        missing.append(line)

if missing:
    if "</manifest>" not in s:
        raise SystemExit("BŁĄD: nie znaleziono zamknięcia </manifest>")
    s = s.replace("</manifest>", "\n".join(missing) + "\n</manifest>")
    p.write_text(s, encoding="utf-8")

print("OK: manifest zawiera uprawnienia Bluetooth, telefonu i dokładnej/przybliżonej lokalizacji.")
