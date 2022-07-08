#!/usr/bin/env python3

# Rechenansatz:
banane_morgens = 7                  # Variable für die Anzahl der Bananen, die jeder bekommen soll
restanteil = banane_morgens         # Anzahl der Bananen, die jeder am Ende bekommt
restmenge = 3 * restanteil + 1      # morgens bekommen 3 Piraten und ein Affe je eine Banane
steveanteil = restmenge / 2         # Steve hat zuvor sein Drittel entfernt, das halb so groß ist, wie der verbleibende Rest
stevemenge = 3 * steveanteil + 1    # Die Menge, die Steve vorfindet, ist also dreimal so groß wie sein Anteil + die übriggebliebene Banane
tomanteil = stevemenge / 2          #
tommenge = 3 * tomanteil + 1        #
rayanteil = tommenge / 2            #
gesamtmenge = 3 * rayanteil + 1     #

print("Vortags gesammelte Mindestmenge:", gesamtmenge, "Bananen\n")
print("Menge, die Ray vorfindet:", gesamtmenge, "Bananen")
print("Rays Anteil:", rayanteil, "Bananen")
print("Menge, die Tom vorfindet:", tommenge, "Bananen")
print("Toms Anteil:", tomanteil, "Bananen")
print("Menge, die Steve vorfindet:", stevemenge, "Bananen")
print("Steves Anteil:", steveanteil, "Bananen\n")
print("Morgendliche Restmenge:", restmenge, "Bananen")
print("Anteil für jeden:", restanteil, "Bananen")

# Testschleife für gesamtmenge bis zum ganzzahligen Wert
gesamtmenge = 3.5

while gesamtmenge % 1 != 0:
    gesamtmenge += 0.125
    print(gesamtmenge)
print(round(gesamtmenge), "Bananen")
