package UF4.InstitutBasic;
public class Institut {
	
	// Creo los objetos de la clase Institut
	private String nom; // Nombre del instituto
	private Alumne[] llistaAlumnes; // Lista de alumnos
	private int num; // Numero de alumnos que hay en cada instituto
	
	// Muestro el nombre y alumnos del instituto
	public String getInstitut() {
		return "Este Instituto se llama " + nom + ", y alberga " + num + " alumnos";
	}
	
	// Creo los institutos
	public void setInstitut(String insti) {
		this.nom = insti;
		this.llistaAlumnes = new Alumne[100];
		this.num=0;
	}
	
	public void setInstitut(String insti, int max) {
		this.nom = insti;
		this.llistaAlumnes = new Alumne[max];
		this.num=0;
	}
	
	// Añado al alumno a la tabla
	public void afegirAlumne(Alumne a) {
		this.llistaAlumnes[num] = a;
		this.num++;
	}
	
	// Muestro a los alumnos
	public void verAlumne() {
		for (int i = 0; i < llistaAlumnes.length; i++) {
			if(llistaAlumnes[i] != null){
				System.out.println();
				System.out.print(llistaAlumnes[i]);
				System.out.println(" Institut: " + this.nom);
			}
		}
	}
}
