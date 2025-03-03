package UF5.examen;
public class Main {

	public static void main(String[] args) {
		Port tarragona = new Port("Tarragona");
		VaixellSenseMotor vaixell1 = new VaixellSenseMotor("487584T",10.8,1995);
		Velers vaixell2 = new Velers("64875M",35,2004,2);
		VaixellAmbMotor vaixell3 = new VaixellAmbMotor("48759K",48,2005,48);
		IotLuxe vaixell4 = new IotLuxe("487597K",102,2018,56,3);
		
		Lloguer lloguer1 = new Lloguer("77794857P","05/08/2020","10/08/2020");
		lloguer1.setVaixell(vaixell1);
		tarragona.afegirLloguer(lloguer1);
		Lloguer lloguer2 = new Lloguer("77794827P","26/02/2013","22/10/2014");
		lloguer2.setVaixell(vaixell2);
		tarragona.afegirLloguer(lloguer2);
		Lloguer lloguer3 = new Lloguer("77794157P","02/12/2021","28/02/2022");
		lloguer3.setVaixell(vaixell3);
		tarragona.afegirLloguer(lloguer3);
		Lloguer lloguer4 = new Lloguer("77794854P","14/05/2023","16/07/2023");
		lloguer4.setVaixell(vaixell4);
		tarragona.afegirLloguer(lloguer4);
		
		tarragona.informe();
		System.out.println("Diners obtinguts desde que he creat el Port: " + tarragona.calcularImportTotal() + "€");
		System.out.println("Diners obtinguts el mes que has posat: " + tarragona.calcularImportMes(8, 2020) + "€");
	}

}
