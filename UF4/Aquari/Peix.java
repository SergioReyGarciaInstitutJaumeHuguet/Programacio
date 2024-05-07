package UF4.Aquari;

public class Peix extends Organisme{
	private String procedencia;
	private char dieta;
	private double longitud;
	
	public Peix(String nom, String familia, char llum, double tempMax, double tempMin, double phMax, double phMin,
			String procedencia, char dieta, double longitud) {
		super(nom, familia, llum, tempMax, tempMin, phMax, phMin);
		this.procedencia = procedencia;
		this.dieta = dieta;
		this.longitud = longitud;
	}
	
	public String dadesMostrar() {
		return "Nom: " + this.nom + "\n" + "Acidesa: " + acidesa() + "\n" + "Temperatura: " + temperatura() + "\n" + "Llum: " + tipusLlum() + "\n" + "Longitud: " + this.longitud + "\n" + "Procedencia: " + this.procedencia + "\n" + "Dieta: " + dieta() + "\n" + "__________________________________";
	}
	
	public String dieta() {
		String dieta="";
		switch(this.dieta) {
		case 'A': dieta="Algues"; break;
		case 'O': dieta="Omnívor";break;
		case 'F': dieta="Fulles";break;
		}
		return dieta;
	}
	
	public String toString() {
		return dadesMostrar();
	}
	
}
