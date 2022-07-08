# Bananen-Piraterie
# Version 2.0b:

# Deklaration der Variablen
piraten = ["Ray", "Tom", "Steve", "Bill", "Ted"]  # Liste erweiterbar, um die Anzahl der Piraten zu erhöhen
pir_name = 0                            # Variable für die Ausgabe des Piraten-Namens aus der Liste, Startwert entspricht Index 0
pir_cnt = len(piraten)                  # Anzahl der Piraten laut Liste in die Variable pir_cnt
# pir_cnt = 3                             # hardcodierte Anzahl der Piraten zum Testen: bei 3 Piraten erhält morgens jeder 7 Bananen und es müssen zuvor 79 gesammelt werden
pir_cnt_alt = pir_cnt - 1               # Zwischenwert für die Restmengen nach Entnahme je Pirat (z.B. 2/3 Bananen bei 3 Piraten, 3/4 bei 4 ...)
banane_morgens = 1                      # Bananenstartwert, auch um die Schleife wahlweise später zu beginnen
teilmenge = 0                           # Die jeweilige Menge in den einzelnen Zwischenschritten
anteil = 0                              # der Anteil, den jeder Pirat für sich sichert

piraten.reverse()                       # Namensliste wird umgekehrt für korrekte Indizierung
while True:
    teilmenge = pir_cnt * banane_morgens + 1
    print("Bananen:", banane_morgens)
    pir_name = 0  # Variable für die Ausgabe des Piraten-Namens aus der Liste, Startwert entspricht Index 0
    for i in range(pir_cnt):
        anteil = teilmenge / pir_cnt_alt
        teilmenge = pir_cnt * anteil + 1
        print(anteil, " ", piraten[pir_name], "s Anteil", sep="")
        print(teilmenge, "- Zwischenmenge")
        pir_name += 1
    print(teilmenge, "- Testwert")
    if teilmenge % 1 == 0:
        break
    banane_morgens += 1

teilmenge = round(teilmenge)
print("\n", teilmenge, " Bananen müssen mindestens am Vortag gesammelt werden", sep="")
print("Testausgabe: ", banane_morgens, "Bananen erhält jeder am Morgen")

print("\nRückwärtsrechnung:")
piraten.reverse()                       # Namensliste wird wieder umgekehrt für korrekte Indizierung
print("Gesammelte Bananen:", teilmenge)
menge = teilmenge
anteil = 0
pir_name = 0
for i in range(pir_cnt):
    anteil = (menge - 1) / pir_cnt
    print("Anteil, den ", piraten[pir_name], " versteckt: ", anteil, sep="")
    menge = anteil * pir_cnt_alt
    pir_name += 1
print("Menge, die alle morgens vorfinden:", menge, "Bananen")
restanteil = (menge - 1) / pir_cnt
print("=> Morgendlicher Anteil für jeden:", round(restanteil), "Bananen")

# Vorwärtsversion:
# Deklaration der Variablen
piraten = ["Ray", "Tom", "Steve", "Bill", "Ted"]  # Liste erweiterbar, um die Anzahl der Piraten zu erhöhen
pir_name = 0                            # Variable für die Ausgabe des Piraten-Namens aus der Liste, Startwert entspricht Index 0
pir_cnt = len(piraten)                  # Anzahl der Piraten laut Liste in die Variable pir_cnt
# pir_cnt = 3                             # hardcodierte Anzahl der Piraten zum Testen: bei 3 Piraten erhält morgens jeder 7 Bananen und es müssen zuvor 79 gesammelt werden
pir_cnt_alt = pir_cnt - 1               # Zwischenwert für die Restmengen nach Entnahme je Pirat (z.B. 2/3 Bananen bei 3 Piraten, 3/4 bei 4 ...)
banane_morgens = 0                      # Bananenstartwert, auch um die Schleife wahlweise später zu beginnen
teilmenge = 0                           # Die jeweilige Menge in den einzelnen Zwischenschritten
anteil = 0                              # der Anteil, den jeder Pirat für sich sichert
counter = 1

print("\n\n--- Vorwärtsversion ---")
while True:
    teilmenge = 0
    teilmenge += counter
    # print(teilmenge, "Menge")     # Testausgabe
    for i in range(pir_cnt + 1):    # Schleifendurchlauf = Anzahl der Piraten + Teilen am nächsten Morgen
        anteil = (teilmenge - 1) / pir_cnt
        # print(anteil, "Anteil")   # Testausgabe
        teilmenge = pir_cnt_alt * anteil
    if anteil % 1 == 0:
        break
    counter += 1
gesamtmenge = (pir_cnt * anteil) + 1

print("Gesammelte Bananen:", counter)
print("Menge, die alle morgens vorfinden:", gesamtmenge, "Bananen")
print("=> Morgendlicher Anteil für jeden:", round(anteil), "Bananen")
