import os
import requests

BASE_URL = os.getenv("API_URL", "https://ableitung.onrender.com")

faelle = [
    ({"funktion": "x**2 * sin(x)"}, 200),
    ({"funktion": "x**3", "ordnung": 2}, 200),
    ({"funktion": "x**2 +"}, 400),
    ({"funktion": "x**2", "ordnung": 3}, 400),
]

for body, erwartet in faelle:
    resp = requests.post(f"{BASE_URL}/ableitung", json=body, timeout=90)
    status = "OK" if resp.status_code == erwartet else "FEHLER"
    print(f"[{status}] {body} -> {resp.status_code} {resp.json()}")