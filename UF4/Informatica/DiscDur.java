package UF4.Informatica;

public class DiscDur extends Articles{

	private int capacitat;
	private float preuTotal;

	public DiscDur(String codi, String descripcio, int unitats, float preuBase, int capacitat) {
		super(codi, descripcio, unitats, preuBase);
		this.capacitat = capacitat;
		this.preuTotal = (preuBase * capacitat)/10;
	}

	public float preuTotal() {
		return preuTotal;
	}
	
	@Override
	public String toString() {
		return codi + "	" + descripcio + "	" + unitats + "	" + capacitat + " " + "GB" + "		" + preuTotal;
	}
	
	
}
