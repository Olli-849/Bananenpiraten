
# Version 1.0:
print("\n--- Version 1.0 ---")
# Variablen-Deklaration
banane_morgens = 1
gesamtmenge = 3 * ((3 * ((3 * ((3 * banane_morgens + 1) / 2) + 1) / 2) + 1) / 2) + 1
print(gesamtmenge, "- Testwert")

while gesamtmenge % 1 != 0:
    banane_morgens += 1
    gesamtmenge = 3 * ((3 * ((3 * ((3 * banane_morgens + 1) / 2) + 1) / 2) + 1) / 2) + 1
    print(gesamtmenge)  # Ausgabe der Zwischenergebnisse zur Kontrolle
print(round(gesamtmenge), "Bananen")

print("\nRückwärtsrechnung:")
print("Gesammelte Bananen:", gesamtmenge)
rayanteil = (gesamtmenge - 1) / 3
print("Anteil, den Ray versteckt:", rayanteil)
tommenge = rayanteil * 2
print("Menge, die Tom vorfindet:", tommenge)
tomanteil = (tommenge - 1) / 3
print("Anteil, den Tom versteckt:", tomanteil)
stevemenge = tomanteil * 2
print("Menge, die Steve vorfindet:", stevemenge)
steveanteil = (stevemenge - 1) / 3
print("Anteil, den Steve versteckt:", steveanteil)
restmenge = steveanteil * 2
print("Menge, die alle morgens vorfinden:", restmenge, "Bananen")
restanteil = (restmenge - 1) / 3
print("Morgendlicher Anteil für jeden:", round(restanteil), "Bananen")
