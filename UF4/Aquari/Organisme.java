package UF4.Aquari;

public abstract class Organisme {

	protected String nom, familia;
	protected char llum;
	protected double tempMax, tempMin, phMax, phMin;
	
	public Organisme(String nom, String familia, char llum, double tempMax, double tempMin, double phMax,
			double phMin) {
		super();
		this.nom = nom;
		this.familia = familia;
		this.llum = llum;
		this.tempMax = tempMax;
		this.tempMin = tempMin;
		this.phMax = phMax;
		this.phMin = phMin;
	}
	public abstract String dadesMostrar();
	
	public String acidesa() {
		return this.phMin + "-" + this.phMax;
	}
	public String temperatura() {
		return this.tempMin + "-" + this.tempMax;
	}
	public String tipusLlum() {
		String tipus="";
		switch(llum) {
		case 'A': tipus="Alta"; break;
		case 'B': tipus="Mitjana";break;
		case 'M': tipus="Baixa";break;
		}
		return tipus;
	}
}
