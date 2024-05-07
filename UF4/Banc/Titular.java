package UF4.Banc;

public class Titular {

	private String dni, nom, cognom;
	
	public void Titular(String dni, String nom, String cognom) {
		this.dni = dni;
		this.nom = nom;
		this.cognom = cognom;
	}
	
	public String toString() {
		return "DNI: " + this.dni + "\nNom: " + this.nom + "\nCognom: " + this.cognom + "\n";
	}

	public String getDni() {
		return dni;
	}

	public void setDni(String dni) {
		this.dni = dni;
	}

	public String getNom() {
		return nom;
	}

	public void setNom(String nom) {
		this.nom = nom;
	}

	public String getCognom() {
		return cognom;
	}

	public void setCognom(String cognom) {
		this.cognom = cognom;
	}
	
	
}
