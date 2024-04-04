package UF4.Escola;

public class Estudiant extends Persona{
	
	protected String cicle;
	protected int curs;
	
	public String getCicle() {
		return cicle;
	}
	public void setCicle(String cicle) {
		this.cicle = cicle;
	}
	public int getCurs() {
		return curs;
	}
	public void setCurs(int curs) {
		this.curs = curs;
	}
	public Estudiant(String nom, String adreca, String cicle, int curs) {
		super(nom, adreca);
		this.cicle = cicle;
		this.curs = curs;
	}
	@Override
	public String toString() {
		return nom + " es un estudiant de " + cicle + " i cursa el " + curs + " any." + " Viu en " + adreca + ".";
	}
	

}
