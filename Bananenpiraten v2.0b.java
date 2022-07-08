package bananenpiraten;

public class Code
{
	public static void main(String[] args)
	{
		String[] piratenliste = new String[3];  // erweiterbare Piraten-Namensliste
		
		piratenliste[0] = "Ray";
		piratenliste[1] = "Tom";
		piratenliste[2] = "Steve";
		
		int pir_name = 0;  // Variable für die Ausgabe des Piraten-Namens aus der Liste, Startwert entspricht Index 0
		int pir_cnt = piratenliste.length;  // Anzahl der Piraten zum Testen: bei 3 Piraten erhält morgens jeder 7 Bananen und es müssen zuvor 79 gesammelt werden
		int pir_cnt_alt = pir_cnt - 1;  //Zwischenwert für die Restmengen nach Entnahme je Pirat (z.B. 2/3 Bananen bei 3 Piraten, 3/4 bei 4 ...)
		double teilmenge = 0;  // Die jeweilige Menge in den einzelnen Zwischenschritten
		double anteil = 0;  // der Anteil, den jeder Pirat für sich sichert
		int counter = 1;
		
		while(true)
		{
			teilmenge = 0;
			teilmenge += counter;
//			System.out.println(teilmenge + " Menge");  // Testausgabe
			for(int i=1; i<=pir_cnt+1; i++)  // Schleifendurchlauf = Anzahl der Piraten + Teilen am nächsten Morgen
			{
				anteil = (teilmenge - 1) / pir_cnt;
//				System.out.println(anteil + " Anteil");  // Testausgabe
				teilmenge = anteil * pir_cnt_alt;
			}
			if(anteil%1==0)
			{
				break;
			}
			counter += 1;
		}
		System.out.println("Am Abend gesammelte Bananen: " + counter);
		int menge = counter;
		
		for(int i=0; i<pir_cnt;i++)
		{
			anteil = (menge - 1) / pir_cnt;
			System.out.println("\nMenge, die " + piratenliste[pir_name] + " vorfindet: " + menge);
			System.out.println("Anteil, den " + piratenliste[pir_name] + " versteckt: " + (int) anteil);
			menge = (int) anteil * pir_cnt_alt;
			pir_name++;
		}
		System.out.println("\nMenge, die alle morgens vorfinden: " + (int) menge + " Bananen");
		double restanteil = (menge - 1) / pir_cnt;
		System.out.println("=> Morgendlicher Anteil für jeden: " + (int) restanteil + " Bananen");
	}	
}
