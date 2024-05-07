package UF4.Escola;

public class EstudiantInternacional extends Estudiant {

	protected String pais;

	public EstudiantInternacional(String nom, String adreca, String cicle, int curs, String pais) {
		super(nom, adreca, cicle, curs);
		this.pais = pais;
	}
	
	public String toString() {
		return nom + " es un estudiant de " + cicle + " i cursa el " + curs + " any." + " Viu en " + adreca + " i es de " + pais + ".";
	}
}
