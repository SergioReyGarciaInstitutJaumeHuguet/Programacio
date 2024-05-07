package UF4.Hoteles;

public class Client {
	private String nom, dni;
	private int numTargeta;
	
	public void crearClient(String nom, String dni, int numT) {
		this.nom = nom;
		this.dni = dni;
		this.numTargeta = numT;
	}
	
	public String toString() {
		return "El cliente " + this.nom + " tiene este dni: " + this.dni;
	}
	
	public String getNom() {
		return nom;
	}
	public void setNom(String nom) {
		this.nom = nom;
	}
	public String getDni() {
		return dni;
	}
	public void setDni(String dni) {
		this.dni = dni;
	}
	public int getNumTargeta() {
		return numTargeta;
	}
	public void setNumTargeta(int numTargeta) {
		this.numTargeta = numTargeta;
	}
	
	

}
