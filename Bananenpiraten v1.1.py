# Version 1.1:

print("\n\n--- Version 1.1 ---")
# Variablen-Deklaration
piraten = ["Ray", "Tom", "Steve"]       # Piraten-Namensliste
pir_name = 0                            # Variable für die Ausgabe des Piraten-Namens aus der Liste, Startwert entspricht Index 0
pir_cnt = 3                             # hardcodierte Anzahl der Piraten zum Testen: bei 3 Piraten erhält morgens jeder 7 Bananen und es müssen zuvor 79 gesammelt werden
pir_cnt_alt = pir_cnt - 1               # Zwischenwert für die Restmengen nach Entnahme je Pirat (z.B. 2/3 Bananen bei 3 Piraten, 3/4 bei 4 ...)
banane_morgens = 0                      # Bananenstartwert, auch um die Schleife wahlweise später zu beginnen
teilmenge = 0                           # Die jeweilige Menge in den einzelnen Zwischenschritten
anteil = 0                              # der Anteil, den jeder Pirat für sich sichert
counter = 1

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

# Ausgabe-Bereich
print("Gesammelte Bananen:", counter)
menge = counter

for i in range(pir_cnt):
    anteil = (menge - 1) / pir_cnt
    print("Anteil, den ", piraten[pir_name], " versteckt: ", anteil, sep="")
    menge = anteil * pir_cnt_alt
    pir_name += 1
print("Menge, die alle morgens vorfinden:", menge, "Bananen")
restanteil = (menge - 1) / pir_cnt
print("=> Morgendlicher Anteil für jeden:", round(restanteil), "Bananen")
