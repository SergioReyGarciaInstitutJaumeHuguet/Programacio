package UF5.NotesAlumnes;

public class Alumne {

	private String nom;
	private float nota;
	
	public String getNom() {
		return nom;
	}


	public void setNom(String nom) {
		this.nom = nom;
	}


	public float getNota() {
		return nota;
	}


	public void setNota(float nota) {
		this.nota = nota;
	}


	public Alumne(String nom, float nota) {
		this.nom = nom;
		this.nota = nota;
	}

	
	@Override
	public String toString() {
		return "Alumne: " + nom + ", nota: " + nota;
	}
	
	
}
