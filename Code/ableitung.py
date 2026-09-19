# Code/ableitung.py
from sympy import Symbol, SympifyError, diff, simplify, sympify


def ableiten(funktion: str, variable: str = "x", ordnung: int = 1) -> str:
    # Schritt 2: Eingabe prüfen
    if ordnung not in (1, 2):
        raise ValueError("Ordnung muss 1 oder 2 sein.")

    # Schritt 3: Strings in SymPy-Objekte umwandeln
    var = Symbol(variable)
    try:
        ausdruck = sympify(funktion)
    except (SympifyError, SyntaxError, TypeError):
        raise ValueError(f"Ungültige Funktion: {funktion}")

    # Schritt 4: Ableitung berechnen
    ableitung = diff(ausdruck, var, ordnung)

    # Schritt 5: Vereinfachen und als String zurückgeben
    return str(simplify(ableitung))


if __name__ == "__main__":
    print(ableiten("x**2 * sin(x)"))            # 1. Ableitung
    print(ableiten("x**3", ordnung=2))          # 2. Ableitung
    print(ableiten("x**2 * y", variable="y"))   # partielle Ableitung nach y

    try:
        ableiten("x**2 +")                      # fehlerhafte Eingabe
    except ValueError as e:
        print("Fehler:", e)