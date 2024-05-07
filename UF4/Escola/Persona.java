package UF4.Escola;

public class Persona {

	protected String nom, adreca;

	public String getNom() {
		return nom;
	}

	public void setNom(String nom) {
		this.nom = nom;
	}

	public String getAdreca() {
		return adreca;
	}

	public void setAdreca(String adreca) {
		this.adreca = adreca;
	}

	public Persona(String nom, String adreca) {
		super();
		this.nom = nom;
		this.adreca = adreca;
	}
	
}
