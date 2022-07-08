# Version 2.0 - 4 Piraten:

piraten = ["Ray", "Tom", "Steve", "Bill"]
pir_cnt = len(piraten)                  # Anzahl der Piraten laut Liste
# pir_cnt = 3                             # hardcodierte Test-Anzahl der Piraten
pir_cnt_alt = pir_cnt - 1               # Zwischenwert für die Restmengen nach Entnahme je Pirat
banane_morgens = 1                      # Bananenstartwert, auch um die Schleife wahlweise später zu beginnen

gesamtmenge = pir_cnt * ((pir_cnt * ((pir_cnt * ((pir_cnt * ((pir_cnt * banane_morgens + 1) / pir_cnt_alt) + 1) / pir_cnt_alt) + 1) / pir_cnt_alt) + 1) / pir_cnt_alt) + 1
print(gesamtmenge, "- 1. Testwert")

while gesamtmenge % 1 != 0:
    banane_morgens += 1
    gesamtmenge = pir_cnt * ((pir_cnt * ((pir_cnt * ((pir_cnt * ((pir_cnt * banane_morgens + 1) / pir_cnt_alt) + 1) / pir_cnt_alt) + 1) / pir_cnt_alt) + 1) / pir_cnt_alt) + 1
    print(gesamtmenge)  # Ausgabe der Zwischenergebnisse zur Kontrolle
gesamtmenge = round(gesamtmenge)
print(gesamtmenge, "Bananen müssen mindestens am Vortag gesammelt werden")
print("Testausgabe: ", banane_morgens, "Bananen erhält jeder am Morgen")

print("\nRückwärtsrechnung:")
print("Gesammelte Bananen:", gesamtmenge)
rayanteil = (gesamtmenge - 1) / pir_cnt
print("Anteil, den Ray versteckt:", rayanteil)
tommenge = rayanteil * pir_cnt_alt
print("Menge, die Tom vorfindet:", tommenge)
tomanteil = (tommenge - 1) / pir_cnt
print("Anteil, den Tom versteckt:", tomanteil)
stevemenge = tomanteil * pir_cnt_alt
print("Menge, die Steve vorfindet:", stevemenge)
steveanteil = (stevemenge - 1) / pir_cnt
print("Anteil, den Steve versteckt:", steveanteil)
billmenge = steveanteil * pir_cnt_alt
print("Menge, die Bill vorfindet:", billmenge)
billanteil = (billmenge - 1) / pir_cnt
print("Anteil, den Bill versteckt:", billanteil)
restmenge = billanteil * pir_cnt_alt
print("Menge, die alle morgens vorfinden:", restmenge, "Bananen")
restanteil = (restmenge - 1) / pir_cnt
print("=> Morgendlicher Anteil für jeden:", round(restanteil), "Bananen")
