package UF4.Aquari;

public class Planta extends Organisme{
	private char tipus;

	public Planta(String nom, String familia, char llum, double tempMax, double tempMin, double phMax, double phMin,
			char tipus) {
		super(nom, familia, llum, tempMax, tempMin, phMax, phMin);
		this.tipus = tipus;
	}
	
	public String dadesMostrar() {
		return "Nom: " + this.nom + "\n" + "Acidesa: " + acidesa() + "\n"+ "Temperatura: " + temperatura() + "\n" + "Llum: " + tipusLlum() + "\n" + "Tipus: " + tipus() + "\n" + "__________________________________";
	}
	
	public String tipus() {
		String tipus = "";
		switch(this.tipus) {
		case 'T': tipus = "Tija"; break;
		case 'B': tipus = "Bulb"; break;
		case 'A': tipus = "Arrels"; break;
		}
		return tipus;
	}

	@Override
	public String toString() {
		return dadesMostrar();
	}

	
}
