package UF4.InstitutBasic;

public class Institut {
	
	private String nom;
	private int numAlumnes;
	
	public String getInstitut() {
		if (numAlumnes != 0){
			return "Este Instituto se llama " + nom + ", y alberga " + numAlumnes + " alumnos";
		} else { return "Este Instituto se llama " + nom + " y no se sabe la información de los alumnos que alberga";}
	}
	
	public void setInstitut(String insti) {
		this.nom = insti;
	}
	
	public void setInstitut(String insti, int numAlumnes) {
		this.nom = insti;
		this.numAlumnes = numAlumnes;
	}
	
	public void afegirAlumne() {
		System.out.println("No se como asignar los alumnos de la clase alumnos al un instituto");
	}
}
