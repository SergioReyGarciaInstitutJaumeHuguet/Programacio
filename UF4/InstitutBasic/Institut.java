package UF4.InstitutBasic;
public class Institut {
	
	private String nom;
	private Alumne[] llistaAlumnes;
	private int num;
	
	public String getInstitut() {
		return "Este Instituto se llama " + nom + ", y alberga " + llistaAlumnes + " alumnos";
	}
	
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
	
	public void afegirAlumne(Alumne a) {
		this.llistaAlumnes[num] = a;
		this.num++;
	}
	
	public void verAlumne() {
		for (int i = 0; i < llistaAlumnes.length; i++) {
			if(llistaAlumnes[i] != null){
				System.out.println(llistaAlumnes[i]);
			}
		}
	}
}
